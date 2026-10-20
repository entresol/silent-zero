#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""Boot the loader in QEMU (RISC-V virt) with a good and with a tampered kernel image.

For each run: wait for the serial verdict, take a screenshot of the ram framebuffer through the
QEMU monitor, convert it to PNG, and check what happened (kernel reached or not)."""
import os, socket, subprocess, sys, time

REJECTED = ["halt: image rejected"]
NOT_STARTED = ["jump", "kernel stub reached"]
CASES = [  # tag, byte offset whose lowest bit is flipped (None = untouched), must appear on serial, must not appear
    ("good",        None, ["header: ok", "sha256: ", "jump", "kernel stub reached"], ["halt"]),
    ("bad-payload", 70,   ["header: ok", "sha256: "] + REJECTED, NOT_STARTED),
    ("bad-hash",    30,   ["header: ok", "sha256: "] + REJECTED, NOT_STARTED),
    ("bad-entry",   16,   ["header: ok", "sha256: "] + REJECTED, NOT_STARTED),   # header fields are covered by the hash
    ("bad-length",  8,    ["header: ok", "sha256: "] + REJECTED, NOT_STARTED),
    ("bad-magic",   0,    ["header: bad"] + REJECTED, NOT_STARTED + ["sha256: "]),   # never hashes what it cannot parse
]


def run(tag, flip, must, mustnot):
    data = bytearray(open("kernel.zimg", "rb").read())
    if flip is not None:
        data[flip] ^= 1
    image = f"{tag}.zimg"
    open(image, "wb").write(data)
    for f in (f"{tag}.log", f"{tag}.ppm", f"{tag}.sock"):
        if os.path.exists(f):
            os.remove(f)
    q = subprocess.Popen(
        ["qemu-system-riscv64", "-machine", "virt", "-m", "128M", "-bios", "none", "-kernel", "loader.elf",
         "-device", f"loader,file={image},addr=0x80400000,force-raw=on", "-device", "ramfb",
         "-display", "none", "-serial", f"file:{tag}.log", "-monitor", f"unix:{tag}.sock,server,nowait",
         "-no-shutdown"], stderr=subprocess.PIPE)
    try:
        done = ("kernel stub reached", "halt: image rejected")
        for _ in range(100):
            time.sleep(0.2)
            log = open(f"{tag}.log").read() if os.path.exists(f"{tag}.log") else ""
            if any(d in log for d in done):
                break
        time.sleep(0.5)
        s = socket.socket(socket.AF_UNIX)
        s.connect(f"{tag}.sock")
        s.settimeout(5)
        s.recv(4096)
        s.send(f"screendump {os.path.abspath(tag + '.ppm')}\n".encode())
        for _ in range(50):
            time.sleep(0.2)
            if os.path.exists(f"{tag}.ppm") and os.path.getsize(f"{tag}.ppm") > 1000:
                break
        time.sleep(0.3)
        s.send(b"quit\n")
    finally:
        try:
            q.wait(timeout=5)
        except subprocess.TimeoutExpired:
            q.kill()
    log = open(f"{tag}.log").read()
    problems = [f"missing on serial: {m!r}" for m in must if m not in log]
    problems += [f"unexpected on serial: {m!r}" for m in mustnot if m in log]
    shot = "no screenshot"
    if os.path.exists(f"{tag}.ppm"):
        from PIL import Image
        im = Image.open(f"{tag}.ppm")
        im.save(f"{tag}.png")
        shades = sorted(set(im.convert("RGB").tobytes()[::3]))
        shot = f"{im.size[0]}x{im.size[1]}, shades {shades}"
        if shades != [0, 85, 170, 255]:
            problems.append("screenshot does not hold exactly the four grey shades")
    else:
        problems.append("no screenshot taken")
    print(f"[{tag}] {'OK' if not problems else 'FAILED'}  screen: {shot}")
    print("  serial:", " | ".join(log.strip().splitlines()))
    for p in problems:
        print("  ", p)
    return not problems


sys.exit(0 if all([run(*c) for c in CASES]) else 1)
