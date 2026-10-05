#!/usr/bin/env python3
"""Check every URL in programs.yaml and report dead links.

A link counts as dead on 404/410, or when the host doesn't resolve or refuses
the connection. 401/403/429/5xx are reported as "blocked" only, since many
sites reject automated requests from CI runners.

Usage: check_links.py [--strict] [--discover]
  --strict    exit non-zero on dead links
  --discover  also look for /.well-known/security.txt on entries without one
"""

import os
import socket
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from render import URL_FIELDS  # noqa: E402

UA = "Mozilla/5.0 (compatible; norwegian-disclosure-programs link check; +https://github.com/ahmadscience/norwegian-bug-bounty-disclosure-programs)"
DEAD_CODES = {404, 410}


def check(url):
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                return "ok", resp.status
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (400, 403, 404, 405, 501):
                continue  # some servers mishandle HEAD
            return ("dead" if e.code in DEAD_CODES else "blocked"), e.code
        except (urllib.error.URLError, socket.timeout, ConnectionError, OSError) as e:
            reason = getattr(e, "reason", e)
            if method == "HEAD":
                continue
            return "dead", str(reason)[:80]
    return "dead", "unreachable"


def find_security_txt(url):
    """Return the security.txt URL for a site if it serves a valid-looking one."""
    base = "/".join(url.split("/")[:3])
    candidate = f"{base}/.well-known/security.txt"
    req = urllib.request.Request(candidate, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read(65536).decode("utf-8", "replace")
            final = resp.geturl()
    except (urllib.error.URLError, socket.timeout, ConnectionError, OSError, ValueError):
        return None
    if "contact:" not in body.lower() or "<html" in body.lower():
        return None
    return final if final.startswith("https://") else candidate


def discover(programs):
    todo = [p for p in programs if "url" in p and "security_txt" not in p]
    with ThreadPoolExecutor(max_workers=16) as pool:
        found = list(pool.map(lambda p: find_security_txt(p["url"]), todo))
    lines = [f"- {p['name']}{' / ' + p['unit'] if 'unit' in p else ''}: {u}" for p, u in zip(todo, found) if u]
    out = f"\nsecurity.txt found for {len(lines)} of {len(todo)} entries without one:\n" + "\n".join(lines)
    print(out)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write(out + "\n")


def main():
    programs = yaml.safe_load((ROOT / "programs.yaml").read_text(encoding="utf-8"))
    owners = {}
    for p in programs:
        for key in URL_FIELDS:
            if key in p:
                owners.setdefault(p[key], []).append(f"{p.get('name', '(undisclosed)')}.{key}")
    urls = sorted(owners)
    with ThreadPoolExecutor(max_workers=16) as pool:
        results = dict(zip(urls, pool.map(check, urls)))

    lines = ["| Status | Code | URL | Used by |", "|---|---|---|---|"]
    counts = {"ok": 0, "blocked": 0, "dead": 0}
    for url in urls:
        state, code = results[url]
        counts[state] += 1
        if state != "ok":
            lines.append(f"| {state} | {code} | {url} | {', '.join(owners[url])} |")
    summary = (f"Checked {len(urls)} URLs: {counts['ok']} ok, {counts['blocked']} blocked, "
               f"{counts['dead']} dead\n\n" + "\n".join(lines))
    print(summary)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write(summary + "\n")
    if "--discover" in sys.argv:
        discover(programs)
    if "--strict" in sys.argv and counts["dead"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
