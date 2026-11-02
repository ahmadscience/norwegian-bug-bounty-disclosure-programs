#!/usr/bin/env python3
"""Look for Norwegian organisations with a vulnerability reporting channel that
programs.yaml does not list yet.

Sources, all primary data:
  1. Enhetsregisteret (Brønnøysundregistrene): every entity with at least
     --min-employees employees, plus every municipality, county and state body,
     that has a registered website. Each website is checked for a security.txt
     (RFC 9116).
  2. disclose.io's diodb program list: entries on a .no domain, with a .no
     contact address, or with Norwegian as a preferred language.

The output is a list of leads, not entries. Every lead still has to be checked
by a person and meet the criteria in CONTRIBUTING.md before it goes into
programs.yaml.

Writes discovery.md (report) and discovery.csv (every swept organisation).

Usage: discover.py [--min-employees N] [--max-orgs N] [--no-public-sector] [--no-diodb]
"""

import argparse
import csv
import json
import os
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import securitytxt  # noqa: E402

BRREG = "https://data.brreg.no/enhetsregisteret/api/enheter"
DIODB = "https://raw.githubusercontent.com/disclose/diodb/master/program-list.json"
# Kommune, fylkeskommune, staten, statsforetak, organisasjonsledd, kommunalt foretak,
# interkommunalt selskap, særlig lovbestemt foretak (e.g. Norsk Tipping, helseforetak).
PUBLIC_FORMS = ["KOMM", "FYLK", "STAT", "SF", "ORGL", "KF", "FKF", "IKS", "SÆR"]
BRREG_MAX = 10000  # page * size may not exceed this


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": securitytxt.UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def host_of(url):
    if "://" not in url:
        url = "https://" + url
    host = urllib.parse.urlsplit(url).netloc.lower().split(":")[0]
    return host[4:] if host.startswith("www.") else host


def brreg_query(params, limit):
    out, page, size = [], 0, 100
    while len(out) < limit and (page + 1) * size <= BRREG_MAX:
        q = urllib.parse.urlencode({**params, "size": size, "page": page})
        data = get_json(f"{BRREG}?{q}")
        rows = data.get("_embedded", {}).get("enheter", [])
        out.extend(rows)
        if page + 1 >= data.get("page", {}).get("totalPages", 0):
            break
        page += 1
    return out[:limit]


def brreg_orgs(min_employees, max_orgs, public_sector):
    rows = brreg_query({"fraAntallAnsatte": min_employees, "sort": "antallAnsatte,DESC"}, max_orgs)
    if public_sector:
        rows += brreg_query({"organisasjonsform": ",".join(PUBLIC_FORMS)}, BRREG_MAX)
    orgs = {}
    for r in rows:
        site = r.get("hjemmeside")
        if not site or r.get("konkurs") or r.get("underAvvikling"):
            continue
        orgs.setdefault(host_of(site), {
            "source": "brreg",
            "name": r.get("navn", ""),
            "orgnr": r.get("organisasjonsnummer", ""),
            "form": r.get("organisasjonsform", {}).get("kode", ""),
            "employees": r.get("antallAnsatte", ""),
        })
    return orgs


def diodb_leads():
    leads = []
    for p in get_json(DIODB):
        hay = " ".join(str(p.get(k) or "") for k in ("policy_url", "securitytxt_url", "contact_email"))
        langs = str(p.get("preferred_languages") or "").lower()
        hosts = [host_of(u) for u in hay.split() if "://" in u]
        mail = str(p.get("contact_email") or "").lower()
        if any(h.endswith(".no") for h in hosts) or mail.endswith(".no") or any(
                code in langs.replace(",", " ").split() for code in ("no", "nb", "nn")):
            leads.append({"name": p.get("program_name", ""), "policy": p.get("policy_url") or "",
                          "bounty": p.get("offers_bounty") or "", "hosts": hosts})
    return leads


PLATFORM_HOSTS = {"hackerone.com", "app.intigriti.com", "intigriti.com", "bugcrowd.com",
                  "yeswehack.com", "synack.com", "openbugbounty.org"}


def known_hosts():
    """Hosts of the organisations already listed (platform hosts excluded)."""
    programs = yaml.safe_load((ROOT / "programs.yaml").read_text(encoding="utf-8"))
    hosts = set()
    for p in programs:
        for key in ("url", "unit_url", "program_url", "security_txt"):
            if key in p:
                hosts.add(host_of(p[key]))
    return hosts - PLATFORM_HOSTS


def is_known(host, known):
    """True if host, or a parent domain of it, is listed (info.nrk.no matches nrk.no)."""
    parts = host.split(".")
    return any(".".join(parts[i:]) in known for i in range(len(parts) - 1))


def chapman(n1, n2, m):
    """Chapman's bias-corrected Lincoln-Petersen estimate of population size."""
    return (n1 + 1) * (n2 + 1) / (m + 1) - 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-employees", type=int, default=200)
    ap.add_argument("--max-orgs", type=int, default=5000)
    ap.add_argument("--no-public-sector", action="store_true")
    ap.add_argument("--no-diodb", action="store_true")
    args = ap.parse_args()

    known = known_hosts()
    orgs = brreg_orgs(args.min_employees, args.max_orgs, not args.no_public_sector)
    print(f"Sweeping {len(orgs)} websites from Enhetsregisteret ...", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=24) as pool:
        hits = dict(zip(orgs, pool.map(securitytxt.discover, orgs)))

    rows = []
    for host, org in orgs.items():
        hit = hits[host]
        row = {**org, "domain": host, "known": is_known(host, known), "security_txt": "", "contact": "",
               "policy": "", "acknowledgments": "", "expires": "", "signed": "", "problems": ""}
        if hit:
            url, parsed = hit
            f = parsed["fields"]
            row.update(security_txt=url, contact=" ".join(f.get("contact", [])),
                       policy=" ".join(f.get("policy", [])),
                       acknowledgments=" ".join(f.get("acknowledgments", [])),
                       expires=(f.get("expires") or [""])[0], signed=parsed["signed"],
                       problems="; ".join(securitytxt.problems(parsed)))
        rows.append(row)

    with open(ROOT / "discovery.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]) if rows else ["domain"])
        w.writeheader()
        w.writerows(rows)

    found = [r for r in rows if r["security_txt"]]
    new = [r for r in found if not r["known"]]
    # Capture-recapture inside the swept population: source 1 = the curated list,
    # source 2 = this sweep. The two are not fully independent (the list was partly
    # built from security.txt discovery), so treat the estimate as a lower bound.
    n1 = sum(1 for r in rows if r["known"])
    n2, m = len(found), sum(1 for r in found if r["known"])
    est = chapman(n1, n2, m)

    out = ["## Discovery sweep", "",
           f"- Organisations swept (Enhetsregisteret, website registered): **{len(rows)}**",
           f"- With a security.txt: **{n2}** ({n2 / max(len(rows), 1):.1%})",
           f"- Already in programs.yaml: **{n1}** of the swept, **{m}** of them found by the sweep",
           f"- New leads: **{len(new)}**",
           f"- Chapman estimate of swept organisations with a reporting channel: **{est:.0f}** "
           f"(list covers {n1 / max(est, 1):.0%}; lower bound, sources not independent)", "",
           "### New leads (security.txt, not in programs.yaml)", "",
           "| Organisation | Org.nr | Form | Ansatte | security.txt | Policy | Problems |",
           "|---|---|---|---|---|---|---|"]
    for r in sorted(new, key=lambda r: -(r["employees"] or 0)):
        out.append(f"| {r['name']} | {r['orgnr']} | {r['form']} | {r['employees']} | {r['security_txt']} | "
                   f"{r['policy'] or '-'} | {r['problems'] or '-'} |")

    if not args.no_diodb:
        leads = [d for d in diodb_leads() if not any(is_known(h, known) for h in d["hosts"])]
        out += ["", "### disclose.io diodb leads not in programs.yaml", ""]
        out += [f"- {d['name']}: {d['policy'] or '-'} (bounty: {d['bounty'] or '?'})" for d in leads] or ["- none"]

    report = "\n".join(out)
    (ROOT / "discovery.md").write_text(report + "\n", encoding="utf-8")
    print(report)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
            fh.write(report + "\n")


if __name__ == "__main__":
    main()
