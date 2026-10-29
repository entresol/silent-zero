# SPDX-License-Identifier: BSD-2-Clause
"""Screenshots the page's header into assets/og.png, the preview that social media and chats show for a link.
Run after paper/build.sh: uv run --with playwright python paper/ogshot.py
The image leaves out the version, so it does not go stale with a new paper version."""
from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2, color_scheme="light")
    pg.goto((root / "index.html").as_uri())
    pg.add_style_tag(content="""
      .langs, button.menu, .ver, .status, .actions { display: none !important; }
      .hero { height: 630px; padding: 0 80px; border: 0; display: flex; align-items: center; }
      .hero-inner { margin: 0; max-width: none; }
      .hero h1 { font-size: 160px; margin-bottom: 28px; }
      .hero .lede { font-size: 28px; line-height: 1.45; max-width: 900px; margin-bottom: 40px; hyphens: none; }
      .titleblock { max-width: none; padding-left: 22px; }
      .titleblock .name { font-size: 68px; margin-bottom: 6px; }
      .titleblock .sub { font-size: 28px; line-height: 1.4; }
    """)
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(300)
    pg.screenshot(path=str(root / "assets" / "og.png"), clip={"x": 0, "y": 0, "width": 1200, "height": 630})
    b.close()
