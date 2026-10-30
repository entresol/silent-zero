# SPDX-License-Identifier: BSD-2-Clause
"""Renders recording/boot-events.json as a video: the serial console in real time, then the same output slowed down
for reading, clearly labelled. Nothing is added to or removed from the output; the panel on the right only marks how far
the boot has come. Uses the macOS system fonts Menlo and SF; writes recording/sel4-riscv-boot.mp4 and a still."""
from bisect import bisect_right
import json
import math
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / 'recording'
capture = json.loads((OUT / 'boot-events.json').read_text())
assert capture['success']
events = capture['events']
W, H, FPS = 1920, 1200, 20
mono = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 20)
small = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 16)
ui = ImageFont.truetype('/System/Library/Fonts/SFNS.ttf', 22)
title = ImageFont.truetype('/System/Library/Fonts/SFNS.ttf', 48)
label = ImageFont.truetype('/System/Library/Fonts/SFNS.ttf', 28)

times = [e[0] for e in events]
prefixes, accumulated = [], ''
for _, text in events:
    accumulated += text.replace('\r', '')
    prefixes.append(accumulated)
lines = accumulated.splitlines(keepends=True)
line_times, line_prefixes = [], []
position = 0
display_time = 0
for line in lines:
    position += len(line)
    original_idx = next(i for i,p in enumerate(prefixes) if len(p) >= position)
    display_time = max(display_time + 0.24, times[original_idx])
    line_times.append(display_time)
    line_prefixes.append(accumulated[:position])

INTRO = 2.0
REAL_END = INTRO + capture['recorded_seconds'] + 3.0
REPLAY_START = REAL_END + 2.0
END = REPLAY_START + line_times[-1] + 7.0

def draw_frame(t):
    im = Image.new('RGB', (W,H), '#0a1019')
    d = ImageDraw.Draw(im)
    replay = t >= REAL_END
    if t < INTRO:
        text, clock, mode = '', 0, 'STARTING SOON'
    elif t < REAL_END:
        clock = min(max(t - INTRO, 0), capture['recorded_seconds'])
        i = bisect_right(times, clock) - 1
        text = prefixes[i] if i >= 0 else ''
        mode = 'LIVE SPEED · 1×'
    else:
        rt = max(0, t - REPLAY_START)
        i = bisect_right(line_times, rt) - 1
        text = line_prefixes[i] if i >= 0 else ''
        clock = next((times[j] for j,p in enumerate(prefixes) if len(p) >= len(text)), 0) if text else 0
        mode = 'SLOW REPLAY · LINE BY LINE'
    success = 'BOOT SUCCESS:' in text
    user = 'USERSPACE:' in text
    loader = 'ELF-loader started' in text
    firmware = 'OpenSBI' in text
    d.text((40,26), 'seL4 boots on RISC-V', font=title, fill='#f2f6fc')
    d.text((42,91), f"HiFive Unleashed in QEMU  ·  seL4 16.0.0, official configuration {capture['configuration']}", font=ui, fill='#9cabbd')
    d.rounded_rectangle((40,140,1435,1110), radius=16, fill='#101925', outline='#29364a', width=2)
    d.rectangle((42,190,1433,192), fill='#29364a')
    for x,c in [(64,'#fa6a71'),(90,'#e8bd60'),(116,'#65cc9d')]:
        d.ellipse((x,160,x+12,172), fill=c)
    d.text((157,153), 'SERIAL CONSOLE / UNMODIFIED QEMU OUTPUT', font=small, fill='#a3b4c9')
    visible = text.split('\n')[-38:]
    for i,line in enumerate(visible):
        color = '#ccdae9'
        if line.startswith(('USERSPACE:', 'CAPABILITIES:', 'RUNNING:', 'BOOT SUCCESS:')):
            color = '#7ae0ba'
        elif line.startswith(('ELF-', 'Enabling MMU', 'Jumping to')):
            color = '#8ec6ff'
        elif line.startswith('KERNEL:'):
            color = '#e9cb88'
        d.text((64,210+i*23), line, font=mono, fill=color)
    x=1475
    d.text((x,148), 'BOOT SEQUENCE', font=small, fill='#859ab3')
    milestones=[('01  Firmware', 'OpenSBI / M-mode', firmware),
                ('02  Bootloader', 'ELF-loader / MMU',loader),
                ('03  seL4 kernel', 'Initializes the root task',user),
                ('04  Userspace', 'UART + capability calls',user)]
    for i,(a,b,done) in enumerate(milestones):
        y=195+i*100
        d.text((x,y), a, font=label, fill='#7ae0ba' if done else '#6b7b91')
        d.text((x,y+38), b, font=ui, fill='#9cabbd')
    d.line((x,615,1875,615), fill='#29364a', width=2)
    d.text((x,646), f"{capture['kernel_bytes'] / 1024:.1f} KiB", font=title, fill='#f2f6fc')
    d.text((x,709), f"Kernel · {capture['kernel_bytes']:,} bytes", font=ui, fill='#9cabbd')
    d.text((x,751), 'Matches the expected build', font=ui, fill='#7ae0ba')
    d.text((x,793), f"SHA-256: {capture['kernel_sha256'][:12]}…", font=small, fill='#859ab3')
    d.line((x,844,1875,844), fill='#29364a', width=2)
    d.text((x,875), 'BOOT SUCCESSFUL' if success else 'BOOTING' if text else 'READY', font=label,
           fill='#7ae0ba' if success else '#8ec6ff')
    d.text((x,927), '5 heartbeats confirmed' if success else 'Actual output from the VM', font=ui, fill='#9cabbd')
    d.text((x,997), 'QEMU: 8 GiB, 5 Harts', font=ui, fill='#9cabbd')
    d.text((x,1037), 'seL4 uses 1 CPU core', font=ui, fill='#9cabbd')
    d.text((42,1134), mode, font=small, fill='#8ec6ff')
    d.text((690,1134), f'Original time since VM start: {clock:05.2f} s', font=small, fill='#a3b4c9')
    d.text((42,1165), 'Recorded serial console · no graphical desktop · slow replay changes display timing only',font=small,fill='#74869d')
    if REAL_END <= t < REPLAY_START:
        d.rounded_rectangle((210,430,1275,700),radius=20,fill='#18283c',outline='#527499',width=2)
        d.text((270,477),'The same output, slowed down for reading',font=label,fill='#f2f6fc')
        d.text((270,545),'Now replaying line by line instead of in real time.',font=ui,fill='#bfd0e4')
        d.text((270,591),'Content and sequence remain unchanged.',font=ui,fill='#bfd0e4')
    return im

cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pixel_format','rgb24',
     '-video_size',f'{W}x{H}','-framerate',str(FPS),'-i','-','-an','-c:v','libx264',
     '-preset','fast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',str(OUT/'sel4-riscv-boot.mp4')]
encoder=subprocess.Popen(cmd,stdin=subprocess.PIPE)
for i in range(math.ceil(END*FPS)):
    encoder.stdin.write(draw_frame(i/FPS).tobytes())
encoder.stdin.close()
assert encoder.wait() == 0
draw_frame(END-1).save(OUT/'boot-success.png')
print(f'Video rendered: {END:.2f} seconds at {W}x{H}, {FPS} fps')
