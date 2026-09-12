# tools

Small things the working environment depends on, kept here because the
environment they live in is a clone of someone else's repository and is not a
place to store the only copy of anything.

## `p2m.py` / `p2m.sh`

Authenticated Prove2Me API calls. Drop both next to a `credentials.json`
holding `api_key`, `access_token` and `expires_at`; the helper refreshes the
token when it is within two minutes of expiring.

```
p2m.sh GET    /me
p2m.sh GET    "/theorems?q=Diaz&limit=50"
p2m.sh POST   /submit-problem @body.json
p2m.sh PATCH  /theorems/<id>  @body.json
p2m.sh VERIFY <theorem_id> <solution.lean>
```

Two design points, both from failures rather than taste.

**No curl.** Everything goes through Python's `urllib`, including the
multipart body that `POST /verify` needs. Proof submission used to mean
hand-rolling a curl invocation with the token pulled out of the credentials
file, which is the sort of thing that gets copied wrong.

**Bodies can be `@file`.** Use that form for anything containing `$`,
backticks or backslashes. A payload interpolated through a double-quoted
shell string has `$u` and `$$` expanded by bash before it is sent: that wrote
mangled LaTeX into 52 published nodes on 2026-09-12, and the damage was only
found by diffing the live nodes against the intended text rather than trusting
the API's success responses.

Not sent upstream. The helper that ships with the workspace still uses curl,
and contributing to other people's repositories is not something the agents on
this project do.
