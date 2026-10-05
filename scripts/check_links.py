#!/usr/bin/env python3
"""Check every URL in programs.yaml and report dead links.

A link counts as dead on 404/410, or when the host doesn't resolve or refuses
the connection. 401/403/429/5xx are reported as "blocked" only, since many
sites reject automated requests from CI runners.

Usage: check_links.py [--strict]   (--strict exits non-zero on dead links)
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
    if "--strict" in sys.argv and counts["dead"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
