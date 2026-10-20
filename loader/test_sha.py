#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""Compare our SHA-256 with Python's hashlib on random data, with lengths around the block boundaries."""
import hashlib, os, subprocess, sys

bad = 0
for n in [0, 1, 3, 55, 56, 57, 63, 64, 65, 119, 120, 128, 1000, 100000]:
    data = os.urandom(n)
    open("t.bin", "wb").write(data)
    got = subprocess.check_output(["./test_sha", "t.bin"]).decode().strip()
    ok = got == hashlib.sha256(data).hexdigest()
    bad += not ok
    print(f"{n:>7} bytes: {'ok' if ok else 'MISMATCH'}")
os.remove("t.bin")
sys.exit(1 if bad else 0)
