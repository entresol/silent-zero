# SPDX-License-Identifier: BSD-2-Clause
"""Renders assets/favicon.svg into favicon.ico (16, 32, 48 px) and assets/apple-touch-icon.png (180 px, on white).
The .ico cannot follow dark mode like the SVG, so it sits on a light rounded tile that reads on dark tab bars too.
Run when the icon changes: uv run --with playwright --with pillow python paper/icons.py"""
import io
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
svg = (root / "assets" / "favicon.svg").read_text(encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    def shot(size, pad, bg, tile="none", radius=0):
        pg = b.new_page(viewport={"width": size, "height": size}, color_scheme="light")
        pg.set_content(f'<body style="margin:0;background:{bg}"><div style="width:{size}px;height:{size}px;padding:{pad}px;'
                       f'box-sizing:border-box;background:{tile};border-radius:{radius}px">{svg.replace("<svg ", "<svg width=\"100%\" height=\"100%\" ", 1)}</div></body>')
        png = pg.screenshot(omit_background=bg == "transparent")
        pg.close()
        return Image.open(io.BytesIO(png)).convert("RGBA")
    big = shot(256, 20, "transparent", "#ffffff", 56)
    big.save(root / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    shot(180, 22, "#ffffff").convert("RGB").save(root / "assets" / "apple-touch-icon.png")
    b.close()
