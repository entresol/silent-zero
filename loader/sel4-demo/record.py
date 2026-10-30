# SPDX-License-Identifier: BSD-2-Clause
"""Boots the image from build.sh in QEMU's HiFive Unleashed model and records the serial console with the time each
piece of output arrived. Writes recording/boot-serial.log (the output, unchanged) and recording/boot-events.json
(the timed pieces, the command, versions and hashes). Fails unless the root task reports five heartbeats."""
import hashlib
import json
import os
import selectors
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "recording"
OUT.mkdir(exist_ok=True)
IMAGE = HERE / "build" / "images" / "boot-demo-image-riscv-hifive"
KERNEL = HERE / "build" / "kernel.bin"
CMD = ["qemu-system-riscv64", "-M", "sifive_u", "-m", "8G", "-smp", "5",
       "-nographic", "-bios", "default", "-nic", "none", "-kernel", str(IMAGE)]
expected = json.loads((HERE / "expected.json").read_text())
kernel = KERNEL.read_bytes()
assert hashlib.sha256(kernel).hexdigest() == expected["kernel_sha256"], "run build.sh: the kernel is not the expected one"

start = time.monotonic()
qemu = subprocess.Popen(CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
sel = selectors.DefaultSelector()
sel.register(qemu.stdout, selectors.EVENT_READ)
events, raw, success_at = [], bytearray(), None
try:
    while time.monotonic() - start < 25:
        for key, _ in sel.select(timeout=0.1):
            data = os.read(key.fileobj.fileno(), 65536)
            if not data:
                break
            raw.extend(data)
            events.append([time.monotonic() - start, data.decode("utf-8", errors="replace")])
            print(data.decode(errors="replace"), end="", flush=True)
            if success_at is None and b"BOOT SUCCESS:" in raw:
                success_at = time.monotonic() - start
        if success_at is not None and time.monotonic() - start > success_at + 1:
            break
        if qemu.poll() is not None:
            break
finally:
    qemu.stdin.write(b"\x01x")   # Ctrl-A x quits QEMU
    qemu.stdin.flush()
    try:
        qemu.wait(timeout=3)
    except subprocess.TimeoutExpired:
        qemu.terminate()
        qemu.wait(timeout=3)
    sel.close()

(OUT / "boot-serial.log").write_bytes(raw)
meta = dict(command=[c if c != str(IMAGE) else "build/images/boot-demo-image-riscv-hifive" for c in CMD],
            events=events, success=success_at is not None, success_at_seconds=success_at,
            recorded_seconds=time.monotonic() - start,
            configuration="RISCV64_MCS_verified", kernel_bytes=len(kernel),
            kernel_sha256=hashlib.sha256(kernel).hexdigest(), image_bytes=IMAGE.stat().st_size,
            image_sha256=hashlib.sha256(IMAGE.read_bytes()).hexdigest(),
            qemu=subprocess.check_output(["qemu-system-riscv64", "--version"], text=True).splitlines()[0],
            sel4_commit=subprocess.check_output(["git", "-C", str(HERE / "deps" / "seL4"), "rev-parse", "HEAD"], text=True).strip())
(OUT / "boot-events.json").write_text(json.dumps(meta, indent=2) + "\n")
assert meta["success"], "QEMU did not reach the root task's success line"
assert raw.count(b"-- seL4_Yield returned") == 5
print(f"\nrecorded: success after {success_at:.3f} s")
