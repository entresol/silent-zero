#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""Wrap a flat payload in the zOS kernel image header (see loader.c): mkimage.py payload.bin image.zimg [entry_offset]"""
import hashlib, struct, sys

payload = open(sys.argv[1], "rb").read()
entry = int(sys.argv[3], 0) if len(sys.argv) > 3 else 64            # payload starts right after the header
head = struct.pack("<IIQQ", 0x4B534F7A, 1, len(payload), entry)      # magic "zOSK", version, length, entry
digest = hashlib.sha256(head + payload).digest()
open(sys.argv[2], "wb").write(head + digest + bytes(8) + payload)
print(f"{sys.argv[2]}: {64 + len(payload)} bytes, sha256 {digest.hex()}")
