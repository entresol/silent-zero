#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""Boots OpenSBI, this loader, seL4's ELF loader and the seL4 kernel in QEMU's HiFive Unleashed model, and records it.

The model has no display, so the loader draws into memory only. A debugger stops QEMU each time the loader has finished
a picture (the empty function zos_frame_shown), copies the framebuffer out of guest memory and lets QEMU go on. The
serial console is recorded with the time each piece arrived. Writes recording/: serial.log, frame-NN.png and
events.json. Needs the xPack RISC-V GCC's gdb (riscv-none-elf-gdb) and Pillow; run `make hifive` first.

With --tamper the loader gets an image with one flipped payload bit and must stop before the ELF loader."""
import json, os, selectors, subprocess, sys, time
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
OUT = HERE / ("recording-tampered" if "--tamper" in sys.argv else "recording")
OUT.mkdir(exist_ok=True)
for f in OUT.glob("*"):
    f.unlink()
W, H, FB = 1120, 832, 0x81000000                       # as in loader.c
image = HERE / "hifive" / "sel4.zimg"
if "--tamper" in sys.argv:
    data = bytearray(image.read_bytes()); data[70] ^= 1
    image = OUT / "tampered.zimg"; image.write_bytes(data)
nm = subprocess.check_output(["riscv-none-elf-nm", str(HERE / "hifive" / "loader.elf")], text=True)
shown = next(l.split()[0] for l in nm.splitlines() if l.endswith(" zos_frame_shown"))

cmd = ["qemu-system-riscv64", "-M", "sifive_u", "-m", "8G", "-smp", "5", "-nographic", "-bios", "default", "-nic", "none",
       "-kernel", "hifive/loader.elf", "-device", f"loader,file={os.path.relpath(image, HERE)},addr=0x81ffffc0,force-raw=on",
       "-gdb", "tcp:127.0.0.1:12345", "-S"]
qemu = subprocess.Popen(cmd, cwd=HERE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
gdb_script = OUT / "capture.gdb"
# QEMU shows the model's harts as two processes, the E51 monitor core and the four U54 cores; the loader runs on a U54,
# so the debugger attaches to both and resumes them together.
gdb_script.write_text(f"""set pagination off
set confirm off
set architecture riscv:rv64
target extended-remote 127.0.0.1:12345
add-inferior
inferior 2
attach 2
set schedule-multiple on
set $n = 0
break *0x{shown}
commands
silent
set $n = $n + 1
eval "dump binary memory {OUT}/frame-%02d.raw {FB:#x} {FB + W * H * 4:#x}", $n
eval "shell echo %d >> {OUT}/frames.txt", $n
continue
end
continue
""")
time.sleep(0.5)
gdb = subprocess.Popen(["riscv-none-elf-gdb", "-batch", "-x", str(gdb_script)], stdin=subprocess.DEVNULL,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

start, events, raw, end_at = time.monotonic(), [], bytearray(), None
frames_seen = 0
sel = selectors.DefaultSelector(); sel.register(qemu.stdout, selectors.EVENT_READ)
marks = [b"BOOT SUCCESS:", b"halt: image rejected"]
try:
    while time.monotonic() - start < 40:
        for key, _ in sel.select(timeout=0.05):
            data = os.read(key.fileobj.fileno(), 65536)
            if data:
                raw.extend(data); events.append(["serial", time.monotonic() - start, data.decode("utf-8", "replace")])
                print(data.decode(errors="replace"), end="", flush=True)
        if (OUT / "frames.txt").exists():
            n = len((OUT / "frames.txt").read_text().split())
            for i in range(frames_seen + 1, n + 1):
                events.append(["frame", time.monotonic() - start, f"frame-{i:02d}.png"])
            frames_seen = n
        if end_at is None and any(m in raw for m in marks):
            end_at = time.monotonic() - start
        if end_at is not None and time.monotonic() - start > end_at + 1:
            break
finally:
    qemu.stdin.write(b"\x01x"); qemu.stdin.flush()
    for p in (qemu, gdb):
        try:
            p.wait(timeout=3)
        except subprocess.TimeoutExpired:
            p.kill()

for rawf in sorted(OUT.glob("frame-*.raw")):   # XRGB, little endian: bytes b, g, r, x
    Image.frombytes("RGBX", (W, H), rawf.read_bytes(), "raw", "BGRX").convert("RGB").save(rawf.with_suffix(".png"))
    rawf.unlink()
(OUT / "frames.txt").unlink(missing_ok=True); gdb_script.unlink()
(OUT / "serial.log").write_bytes(raw)
meta = dict(command=cmd, events=events, frames=frames_seen, ended_at_seconds=end_at, recorded_seconds=time.monotonic() - start,
            qemu=subprocess.check_output(["qemu-system-riscv64", "--version"], text=True).splitlines()[0])
(OUT / "events.json").write_text(json.dumps(meta, indent=2) + "\n")
log = raw.decode(errors="replace")
if "--tamper" in sys.argv:
    assert "halt: image rejected" in log and "ELF-loader" not in log, "the tampered image was not stopped"
    print(f"\nrecorded: tampered image stopped, {frames_seen} frames")
else:
    assert "BOOT SUCCESS:" in log and log.count("-- seL4_Yield returned") == 5 and frames_seen >= 3
    print(f"\nrecorded: boot to user space after {end_at:.2f} s, {frames_seen} frames")
