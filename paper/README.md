# The paper's source

`src.md` is the paper. Everything else here turns it into the PDF and the landing page.

```
./build.sh      # needs Python 3 and pdfLaTeX; writes ../index.html, ../zos-zero-os.pdf and ../versions/
```

- `src.md`: the text, in Markdown. Edit this, nothing generated.
- `build_paper.py`: Markdown to LaTeX (two-column A4); `build.sh` runs pdfLaTeX twice on the result.
- `build_site.py`, `site.css`: the landing page. Navigation: on wide screens the contents stay in a sticky column; below 76rem a menu button at the top left opens them as a panel (a few lines of script; without JavaScript the button stays hidden). Both lead with a link back to the top. The list of changes at the end comes from `../CHANGELOG.md`.
- `changelog.py`: reads `../CHANGELOG.md`; the newest paper version in it is the one printed on the paper and the page, with its date.
- `glossary.md`: the glossary, one entry per term; `glossary.py` turns it into the appendix and the term links on the page.
- `tools/`: two scripts that measure a draft for machine prose (`slop_lint.py`, `vorfeld.py`); see "Writing the paper" in `../CONTRIBUTING.md`. The build does not use them.
- `figs.py`: draws Figures 1 and 2 as SVG and HTML; `figshot.py` turns the HTML into the PNGs in `figs/` (needs Playwright). The PNGs are committed, so `build.sh` does not need either.

Every published version is kept as `../versions/zos-zero-os-YYYY-MM-DD-vX.Y.pdf`; `../zos-zero-os.pdf` is always the newest. Once a version's PDF is on `origin/main`, the build keeps it unchanged and warns if the paper it built differs; a changed paper needs a new version in `../CHANGELOG.md`. The check needs `pdftotext` (Poppler, like `pdfinfo`).

Licence: the build scripts are BSD-2-Clause. The text and figures: [CC BY 4.0](../LICENSE-CC-BY-4.0.txt).
