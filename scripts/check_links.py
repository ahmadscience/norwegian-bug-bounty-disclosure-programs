#!/usr/bin/env python3
"""Check every URL in programs.yaml and report dead links.

A link counts as dead on 404/410, or when the host doesn't resolve or refuses
the connection. 401/403/429/5xx are reported as "blocked" only, since many
sites reject automated requests from CI runners.

Listed security.txt files are also parsed (RFC 9116) and reported if they lack a
Contact or their Expires date has passed. That is reported, never fatal.

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
import securitytxt  # noqa: E402
from render import URL_FIELDS  # noqa: E402

UA = securitytxt.UA
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
    hit = securitytxt.fetch("/".join(url.split("/")[:3]) + "/.well-known/security.txt", timeout=20)
    return hit[0] if hit and hit[0].startswith("https://") else None


def security_txt_problems(programs):
    """Parse every listed security.txt and report RFC 9116 problems (expired, no Contact)."""
    urls = sorted({p["security_txt"] for p in programs if "security_txt" in p})
    with ThreadPoolExecutor(max_workers=16) as pool:
        bodies = dict(zip(urls, pool.map(lambda u: securitytxt.fetch(u, timeout=20), urls)))
    lines = []
    for url in urls:
        hit = bodies[url]
        issues = securitytxt.problems(securitytxt.parse(hit[1])) if hit else ["not a security.txt (or unreachable)"]
        if issues:
            lines.append(f"- {url}: {', '.join(issues)}")
    out = f"\nsecurity.txt problems in {len(lines)} of {len(urls)} listed files:\n" + "\n".join(lines)
    print(out)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write(out + "\n")


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
    owners, active = {}, set()
    for p in programs:
        for key in URL_FIELDS:
            if key in p:
                owners.setdefault(p[key], []).append(f"{p.get('name', '(undisclosed)')}.{key}")
                if p.get("status", "active") == "active":
                    active.add(p[key])
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
    security_txt_problems(programs)
    if "--discover" in sys.argv:
        discover(programs)
    # Entries already marked unknown/closed are listed but don't fail the run.
    if "--strict" in sys.argv and any(results[u][0] == "dead" for u in active):
        sys.exit(1)


if __name__ == "__main__":
    main()
