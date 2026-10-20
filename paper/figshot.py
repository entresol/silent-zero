# SPDX-License-Identifier: BSD-2-Clause
"""Screenshots figs/fig1.html and figs/fig2.html into PNGs. Serve this folder first: python3 -m http.server 8766"""
import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1344,'height':1200}, device_scale_factor=1)
        for n in ['fig1','fig2']:
            await pg.goto(f'http://localhost:8766/figs/{n}.html'); await pg.wait_for_timeout(600)
            await pg.locator('svg').screenshot(path=f'figs/{n}.png')
        await b.close()
asyncio.run(main())
