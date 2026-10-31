#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""Renders the two recordings of record_hifive.py as one video: the good image, then the same image tampered with.

Left the unedited serial console, right the loader's screen, both at the time they were recorded. The HiFive
model has no display: the screen is the framebuffer the loader drew into, copied out of guest memory each time it
finished a frame. QEMU pauses while a frame is copied, and the pauses are included in the timing. Nothing is added to
or removed from the console output. Uses the macOS system fonts Menlo and SF; writes recording/loader-sel4-boot.mp4."""
from bisect import bisect_right
import json, math, subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
W, H, FPS = 1920, 1080, 25
BG, PANEL, LINE, TEXT, DIM, OK, STOP = '#1c1e1f', '#26292b', '#3a3e41', '#eceeef', '#9aa1a6', '#7ad3a6', '#f08a7e'
ACCENT = '#fe9f04'
mono = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 14)
small = ImageFont.truetype('/System/Library/Fonts/SFNS.ttf', 17)
ui = ImageFont.truetype('/System/Library/Fonts/SFNS.ttf', 22)
big = ImageFont.truetype('/System/Library/Fonts/SFNS.ttf', 40)

SX, SY, SW, SH = 836, 128, 1050, 780                   # the loader's panel, enlarged 1.5 times
PANEL_BOX = (210, 157, 910, 677)                       # 700 x 520 of the 1120 x 832 screen around the 560 x 404 panel
CX, CY, CW, CH = 32, 128, 780, 782                     # console
PHASES = [  # name, what, serial line that starts it
    ('Firmware', 'OpenSBI v1.8.1', 'OpenSBI'),
    ('zOS loader', 'checks the image', 'zOS loader'),
    ('seL4 ELF loader', 'unpacks kernel and root task', 'ELF-loader started'),
    ('seL4 kernel', 'RISCV64_MCS_verified', 'Jumping to kernel-image'),
    ('Root task', 'user space, 5 heartbeats', 'USERSPACE:'),
]


def load(name):
    rec = json.loads((HERE / name / 'events.json').read_text())
    serial = [(t, s.replace('\r', '')) for kind, t, s in rec['events'] if kind == 'serial']
    text, prefixes = '', []
    for _, s in serial:
        text += s
        prefixes.append(text)
    frames = [(t, Image.open(HERE / name / f).convert('RGB').crop(PANEL_BOX).resize((SW, SH), Image.LANCZOS))
              for kind, t, f in rec['events'] if kind == 'frame']
    return dict(times=[t for t, _ in serial], prefixes=prefixes, frames=frames, end=rec['ended_at_seconds'],
                recorded=rec['recorded_seconds'])


def draw(run, t, title, note):
    clock = min(t, run['recorded'])
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle((32, 36, 37, 92), fill=ACCENT)
    d.text((56, 30), title, font=big, fill=TEXT)
    d.text((58, 80), note, font=small, fill=DIM)

    i = bisect_right(run['times'], clock) - 1
    text = run['prefixes'][i] if i >= 0 else ''
    d.rectangle((CX, CY, CX + CW, CY + CH), fill=PANEL, outline=LINE)
    d.text((CX + 16, CY - 26), 'Serial console, unedited QEMU output', font=small, fill=DIM)
    lines = text.split('\n')[-(CH - 24) // 18:]
    for n, line in enumerate(lines):
        colour = OK if line.startswith(('USERSPACE:', 'CAPABILITIES:', 'RUNNING:', 'BOOT SUCCESS:')) else \
                 STOP if line.startswith('halt:') else TEXT if line.startswith(('zOS', 'display', 'header', 'sha256', 'jump')) else DIM
        d.text((CX + 14, CY + 12 + n * 18), line[:90], font=mono, fill=colour)

    j = bisect_right([t for t, _ in run['frames']], clock) - 1
    d.text((SX, CY - 26), 'Loader screen, copied from guest memory (panel enlarged)', font=small, fill=DIM)
    if j >= 0:
        im.paste(run['frames'][j][1], (SX, SY))
    else:
        d.rectangle((SX, SY, SX + SW, SY + SH), fill='#000000', outline=LINE)
        d.text((SX + SW // 2, SY + SH // 2), 'No frame yet: the firmware is still running', font=ui, fill=DIM, anchor='mm')

    halted = 'halt: image rejected' in text
    reached = [p[2] in text for p in PHASES]
    x0, pw = 32, (W - 64) // len(PHASES)
    for k, (name, what, _) in enumerate(PHASES):
        x = x0 + k * pw
        current = reached[k] and not any(reached[k + 1:])
        state = (STOP if halted and k == 1 else OK if reached[k] and not current else ACCENT if current else LINE)
        d.rectangle((x, 940, x + pw - 12, 944), fill=state)
        d.text((x, 956), name, font=ui, fill=TEXT if reached[k] else DIM)
        sub = 'stopped: hash mismatch' if halted and k == 1 else 'not started' if halted and k > 1 else what
        d.text((x, 988), sub, font=small, fill=STOP if halted and k >= 1 else DIM)
    d.text((32, 1040), f'time since QEMU started: {clock:5.2f} s   ·   QEMU sifive_u (HiFive Unleashed model)   ·   '
           'QEMU pauses while each frame is copied; the pauses are included in the timing', font=small, fill=DIM)
    return im


def card(line1, line2, line3=''):
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle((W // 2 - 420, H // 2 - 62, W // 2 - 415, H // 2 + (88 if line3 else 50)), fill=ACCENT)
    d.text((W // 2 - 392, H // 2 - 64), line1, font=big, fill=TEXT)
    d.text((W // 2 - 390, H // 2 + 6), line2, font=ui, fill=DIM)
    d.text((W // 2 - 390, H // 2 + 46), line3, font=small, fill=DIM)
    return im


good, bad = load('recording'), load('recording-tampered')
scenes = [  # seconds, frame for a time within the scene, name of the still taken from its last frame
    (3.0, lambda t: card('Power-on to user space', 'OpenSBI, the zOS loader, seL4 16.0.0 (MCS, verified configuration)'), None),
    (good['end'] + 4.0, lambda t: draw(good, t, 'The image checks out',
                                       'the loader hashes the kernel image, shows the result and only then starts it'), 'still-good.png'),
    (3.0, lambda t: card('The same image, tampered with', 'one byte changed after the image was built and hashed',
                         'A hash stored with the image catches this, not an attacker who rewrites the hash too; signing the image comes next.'), None),
    (bad['end'] + 5.0, lambda t: draw(bad, t, 'Tampered image',
                                      'the hash no longer matches: the loader says so on screen and does not start the kernel'), 'still-tampered.png'),
]
out = HERE / 'recording' / 'loader-sel4-boot.mp4'
enc = subprocess.Popen(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pixel_format', 'rgb24',
                        '-video_size', f'{W}x{H}', '-framerate', str(FPS), '-i', '-', '-an', '-c:v', 'libx264',
                        '-preset', 'slow', '-crf', '24', '-tune', 'stillimage', '-pix_fmt', 'yuv420p',
                        '-movflags', '+faststart', str(out)], stdin=subprocess.PIPE)
total = 0.0
for seconds, frame, still in scenes:
    for n in range(math.ceil(seconds * FPS)):
        im = frame(n / FPS)
        enc.stdin.write(im.tobytes())
    total += seconds
    if still:
        im.save(HERE / 'recording' / still)
enc.stdin.close()
assert enc.wait() == 0
print(f'rendered {out.name}: {total:.1f} s, {out.stat().st_size / 1024:.0f} KiB')
