# zOS boot splash (prototype)

The first screen after power-on: a grey panel in four shades, bevelled edges, the name in Inter Thin under the title "zOS", crisp grey-scale type, and the boot report of what was loaded and what we know about each part.

![boot splash, final frame](preview.png)

Freestanding C: no libc, no heap, no floating point. `zos_splash(fb, w, h, step)` draws one boot step of the demonstration report into a framebuffer of one byte per pixel holding a shade 0..3. The loader (`../loader`) instead draws the frame once and fills the report with what it has measured: `zos_splash_frame`, `zos_splash_row`, `zos_splash_progress`, `zos_splash_footer`. Size of `splash.c` including its glyphs (text + data of the object file, `-Os -ffreestanding`, rv64imac): 5,582 bytes with GCC 15.2. The earlier clang figures (6,436 bytes for rv64gc, 8,696 for AArch64, with a large "zOS" in place of the name and run-length coded glyphs) have not been measured again.

- `gen_glyphs.py` rasterises the needed glyphs into 2-bit coverage as `glyphs.h`. Each byte is one drawn pixel: its shade and the number of background pixels before it; trailing background is left out. Type is mostly background, so this is about a quarter smaller than run lengths. The typography is the site's: Inter only as Thin and only large (the name), Nunito Sans for everything else. Both are licensed under the SIL Open Font License 1.1 (`../assets/fonts/`).
- `splash.c` draws panel, bevels, type and the boot report.
- `harness.c` renders every boot step to PGM files on an ordinary computer.

Build and render on a normal host:

```
python3 gen_glyphs.py        # needs Pillow and fontTools; only when the texts change
cc -O2 harness.c splash.c -o harness && ./harness
```

Where it lives: the first screen is now drawn by the loader (`../loader`), because that is the one place that knows, before the kernel starts, what it is about to start. The price is that the renderer is part of the trusted base. Its inputs are fixed: compiled-in texts and glyph tables, plus a hash; it parses nothing from outside. The rows for the parts after the kernel (proven, tested, untrusted) are still the hard-coded demonstration of `zos_splash`; in the real system they must come from the measured image and the system description, drawn by an isolated component that holds the framebuffer and nothing else.
