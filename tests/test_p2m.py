"""Smoke tests for tools/p2m.py. No network, no real credentials."""
import json
import pathlib
import sys
import time

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
import p2m  # noqa: E402


def test_body_arg_literal_is_encoded_verbatim():
    assert p2m.body_arg('{"a": "$u $$"}') == b'{"a": "$u $$"}'


def test_body_arg_at_file_reads_bytes(tmp_path):
    body = tmp_path / "body.json"
    body.write_bytes(b'{"tex": "\\\\frac{a}{b} $x$"}')
    assert p2m.body_arg(f"@{body}") == body.read_bytes()


def test_multipart_contains_fields_and_file(tmp_path):
    proof = tmp_path / "solution.lean"
    proof.write_text("theorem t : True := trivial\n")
    data, ctype = p2m.multipart({"theorem_id": "abc"}, proof)
    boundary = ctype.split("boundary=", 1)[1]
    assert ctype.startswith("multipart/form-data; boundary=")
    assert data.startswith(f"--{boundary}\r\n".encode())
    assert data.endswith(f"\r\n--{boundary}--\r\n".encode())
    assert b'name="theorem_id"\r\n\r\nabc\r\n' in data
    assert b'filename="solution.lean"' in data
    assert b"theorem t : True := trivial\n" in data


def test_main_without_arguments_prints_usage(capsys):
    assert p2m.main(["p2m.py"]) == 2
    assert "p2m.sh GET" in capsys.readouterr().out


def test_token_reuses_unexpired_access_token(tmp_path, monkeypatch):
    cred = tmp_path / "credentials.json"
    cred.write_text(json.dumps({
        "api_key": "dummy-key",
        "access_token": "dummy-token",
        "expires_at": int(time.time()) + 3600,
    }))
    monkeypatch.setattr(p2m, "CRED", cred)

    def no_network(*args, **kwargs):
        pytest.fail("token() must not call the API while the token is still valid")

    monkeypatch.setattr(p2m, "_req", no_network)
    assert p2m.token() == "dummy-token"
