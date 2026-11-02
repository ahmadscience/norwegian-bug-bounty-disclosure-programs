"""Fetch and parse security.txt files (RFC 9116). Shared by check_links.py and discover.py."""

import datetime as dt
import socket
import urllib.error
import urllib.request

UA = ("Mozilla/5.0 (compatible; norwegian-disclosure-programs; "
      "+https://github.com/ahmadscience/norwegian-bug-bounty-disclosure-programs)")
MULTI = {"contact", "policy", "acknowledgments", "canonical", "encryption", "hiring", "csaf"}


def parse(body):
    """Return a dict of lowercased field -> list of values, plus 'signed' and 'expires_at'."""
    fields = {}
    signed = "-----BEGIN PGP SIGNED MESSAGE-----" in body
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().lower()
        if " " in key or not key:
            continue
        fields.setdefault(key, []).append(value.strip())
    expires_at = None
    if fields.get("expires"):
        value = fields["expires"][0].replace("Z", "+00:00")
        try:
            expires_at = dt.datetime.fromisoformat(value)
            if expires_at.tzinfo is None:
                expires_at = expires_at.replace(tzinfo=dt.timezone.utc)
        except ValueError:
            expires_at = None
    return {"fields": fields, "signed": signed, "expires_at": expires_at}


def problems(parsed, now=None):
    """List RFC 9116 problems: missing Contact, missing/invalid/expired Expires."""
    now = now or dt.datetime.now(dt.timezone.utc)
    out = []
    f = parsed["fields"]
    if not f.get("contact"):
        out.append("no Contact")
    if not f.get("expires"):
        out.append("no Expires")
    elif parsed["expires_at"] is None:
        out.append(f"unparseable Expires '{f['expires'][0]}'")
    elif parsed["expires_at"] < now:
        out.append(f"expired {parsed['expires_at'].date()}")
    return out


def fetch(url, timeout=15):
    """Return (final_url, body) if url serves something that looks like a security.txt, else None."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ctype = resp.headers.get("Content-Type", "")
            body = resp.read(65536).decode("utf-8", "replace")
            final = resp.geturl()
    except (urllib.error.URLError, socket.timeout, ConnectionError, OSError, ValueError):
        return None
    low = body.lower()
    if "contact:" not in low or "<html" in low or "html" in ctype.lower():
        return None
    return final, body


def discover(domain, timeout=15):
    """Try the RFC 9116 location on the domain and its www/apex twin. Returns (url, parsed) or None."""
    host = domain.lower().strip().strip("/")
    hosts = [host, host[4:]] if host.startswith("www.") else [host, "www." + host]
    for h in hosts:
        for path in ("/.well-known/security.txt", "/security.txt"):
            hit = fetch(f"https://{h}{path}", timeout)
            if hit:
                return hit[0], parse(hit[1])
    return None
