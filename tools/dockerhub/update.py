#!/usr/bin/env python3
"""Set short description and overview of gcubeai Docker Hub repositories.

Run in your own terminal (the token is asked without echoing):
    python3 tools/dockerhub/render.py          # writes descriptions.json from the READMEs
    python3 tools/dockerhub/update.py [--dry-run] [repo ...]

The token needs the repository edit scope (an organization access token with
repository edit permission). The CI push token (DOCKERHUB_ORG_TOKEN) cannot edit
descriptions. Delete the token after use.
"""
import getpass, json, os, sys, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
NS = "gcubeai"
data = json.load(open(os.path.join(HERE, "descriptions.json"), encoding="utf-8"))
args = [a for a in sys.argv[1:] if not a.startswith("--")]
dry = "--dry-run" in sys.argv
repos = args or sorted(data)

def call(method, url, body=None, token=None):
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Content-Type": "application/json", **({"Authorization": f"Bearer {token}"} if token else {})})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(errors="replace")[:300]

user = input(f"Docker Hub username for the token [{NS}]: ").strip() or NS
secret = getpass.getpass("Access token (hidden): ").strip()
code, res = call("POST", "https://hub.docker.com/v2/auth/token", {"identifier": user, "secret": secret})
token = res.get("access_token") if isinstance(res, dict) else None
if not token:
    code, res = call("POST", "https://hub.docker.com/v2/users/login", {"username": user, "password": secret})
    token = res.get("token") if isinstance(res, dict) else None
if not token:
    sys.exit(f"login failed: HTTP {code} {res}")
print("login ok")

ok = fail = 0
for repo in repos:
    if repo not in data:
        print(f"skip {repo}: no description"); continue
    if dry:
        print(f"[dry-run] {repo}: {data[repo]['description']}"); continue
    code, res = call("PATCH", f"https://hub.docker.com/v2/namespaces/{NS}/repositories/{repo}", data[repo], token)
    if code == 404:  # older endpoint
        code, res = call("PATCH", f"https://hub.docker.com/v2/repositories/{NS}/{repo}/", data[repo], token)
    if code in (200, 201):
        ok += 1; print(f"ok   {repo}")
    else:
        fail += 1; print(f"FAIL {repo}: HTTP {code} {res}")
        if fail == 1 and code in (401, 403):
            sys.exit("permission denied: this token cannot edit repository descriptions")
print(f"done: ok={ok} fail={fail}")
