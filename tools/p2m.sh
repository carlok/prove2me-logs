#!/bin/bash
# Helper: authenticated Prove2me API call. See p2m.py for usage.
exec python3 "$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)/p2m.py" "$@"
