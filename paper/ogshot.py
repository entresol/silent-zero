# SPDX-License-Identifier: BSD-2-Clause
"""Screenshots the page's header into assets/og.png, the preview that social media and chats show for a link.
Run after paper/build.sh: uv run --with playwright python paper/ogshot.py
The header is shown at its own size, as the page draws it in a 1200 px window on a 2x screen; nothing is scaled up.
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
      .hero { height: 630px; padding-block: 0; border: 0; display: flex; align-items: center; }
      .hero-inner { width: 100%; }
    """)
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(300)
    pg.screenshot(path=str(root / "assets" / "og.png"), clip={"x": 0, "y": 0, "width": 1200, "height": 630})
    b.close()
