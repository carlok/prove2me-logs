#!/usr/bin/env python3
"""Authenticated Prove2Me API calls, with no curl and no shell interpolation.

    p2m.sh GET    /me
    p2m.sh GET    "/theorems?q=Diaz&limit=50"
    p2m.sh POST   /submit-problem '<json>'
    p2m.sh POST   /submit-problem @body.json
    p2m.sh PATCH  /theorems/<id>  @body.json
    p2m.sh VERIFY <theorem_id> <solution.lean>

Pass bodies as @file whenever they contain LaTeX, backticks or `$`: a body
interpolated through a double-quoted shell string gets `$u` and `$$` expanded
by bash before it is sent, which once wrote mangled mathematics to 52 nodes.
"""
import json, sys, time, uuid, pathlib, urllib.request, urllib.error

BASE = "https://prove2.me/api/v1"
HERE = pathlib.Path(__file__).resolve().parent
CRED = HERE / "credentials.json"


def _req(method, url, data=None, headers=None):
    r = urllib.request.Request(url, data=data, method=method)
    for k, v in (headers or {}).items():
        r.add_header(k, v)
    try:
        with urllib.request.urlopen(r) as resp:
            return resp.read().decode()
    except urllib.error.HTTPError as e:
        return e.read().decode()


def token():
    c = json.loads(CRED.read_text())
    if int(c.get("expires_at") or 0) > time.time() + 120:
        return c["access_token"]
    body = json.dumps({"api_key": c["api_key"]}).encode()
    out = _req("POST", BASE + "/agent/refresh", body, {"Content-Type": "application/json"})
    d = json.loads(out)
    c["access_token"], c["expires_at"] = d["access_token"], d["expires_at"]
    CRED.write_text(json.dumps(c, indent=2))
    return c["access_token"]


def body_arg(a):
    """A literal JSON string, or @path to read it from a file."""
    if a.startswith("@"):
        return pathlib.Path(a[1:]).read_bytes()
    return a.encode()


def multipart(fields, filepath):
    b = "----p2m" + uuid.uuid4().hex
    out = b""
    for k, v in fields.items():
        out += f"--{b}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode()
    p = pathlib.Path(filepath)
    out += (f"--{b}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{p.name}\"\r\n"
            f"Content-Type: text/plain\r\n\r\n").encode()
    out += p.read_bytes() + f"\r\n--{b}--\r\n".encode()
    return out, "multipart/form-data; boundary=" + b


def main(argv):
    if len(argv) < 3:
        print(__doc__.strip()); return 2
    method, target = argv[1].upper(), argv[2]
    tok = token()
    if method == "VERIFY":
        if len(argv) < 4:
            print("usage: p2m.sh VERIFY <theorem_id> <solution.lean>"); return 2
        data, ctype = multipart({"theorem_id": target}, argv[3])
        print(_req("POST", BASE + "/verify", data,
                   {"Authorization": "Bearer " + tok, "Content-Type": ctype}))
        return 0
    h = {"Authorization": "Bearer " + tok}
    data = None
    if len(argv) > 3:
        data = body_arg(argv[3]); h["Content-Type"] = "application/json"
    print(_req(method, BASE + target, data, h))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
