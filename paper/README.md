# The paper's source

`src.md` is the paper. Everything else here turns it into the PDF and the landing page.

```
./build.sh      # needs Python 3 and pdfLaTeX; writes ../index.html, ../zos-zero-os.pdf and ../versions/
```

- `src.md`: the text, in Markdown. Edit this, nothing generated.
- `build_paper.py`: Markdown to LaTeX (two-column A4); `build.sh` runs pdfLaTeX twice on the result.
- `build_site.py`, `site.css`: the landing page. The revisions list lives in `build_site.py`; a new version gets a new entry at the top, and its number (`YYYY-MM-DD-vX.Y`) also goes into the header and title block in `build_paper.py`.
- `glossary.md`: the glossary, one entry per term; `glossary.py` turns it into the appendix and the term links on the page.
- `figs.py`: draws Figures 1 and 2 as SVG and HTML; `figshot.py` turns the HTML into the PNGs in `figs/` (needs Playwright). The PNGs are committed, so `build.sh` does not need either.

Every published version is kept as `../versions/zos-zero-os-YYYY-MM-DD-vX.Y.pdf`; `../zos-zero-os.pdf` is always the newest.

Licence: the build scripts are BSD-2-Clause. The text and figures: [CC BY 4.0](../LICENSE-CC-BY-4.0.txt).
