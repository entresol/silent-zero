#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""Builds the wiki's pages (wiki/**/*.html) from its Markdown, in the style of the landing page.

The Markdown in wiki/ is the source; Claude writes it to the rules in wiki/CLAUDE.md. This script only renders it:
[[links]] become links, the working name zOS becomes the public name, and every page shows its status and the pages
that link to it. Pages without a type (the schema, the log, the rings) stay Markdown on GitHub."""
import hashlib
import html as _h
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lexicon

PUBLIC_NAME = "Silent Zero"           # the one place the wiki's working name zOS is translated
root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
# the same version as on the main page (build_site.py): a changed icon gets a new address, so browsers fetch it
iv = hashlib.sha256(b"".join((root / f).read_bytes() for f in ("favicon.ico", "assets/favicon.svg", "assets/apple-touch-icon.png"))).hexdigest()[:8]
wiki = root / "wiki"
REPO = "https://github.com/entresol/silent-zero"

GROUPS = [("design", "Design", "The parts of the design: what each must do, what exists, and what is proven, tested or assumed."),
          ("concept", "Concepts", "The ideas the design relies on."),
          ("system", "Systems", "Existing work the design builds on or draws from."),
          ("source", "Sources", "One page per source: what it shows, how, and its limits.")]
GROUP_NAME = {k: n for k, n, _ in GROUPS}
STATUS = {"drafted": "Draft", "reviewed": "LLM reviewed", "doublechecked": "Human curated"}

def front(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M)) if m else {}
    return meta, text[m.end():] if m else text

pages = {}
for f in sorted(wiki.rglob("*.md")):
    meta, body = front(f.read_text(encoding="utf-8"))
    if meta.get("type") not in GROUP_NAME and f.name != "index.md":
        continue
    name = f.stem
    url = "/wiki/" if f.name == "index.md" and f.parent == wiki else "/" + f.relative_to(root).with_suffix(".html").as_posix()
    srcs = re.findall(r"[\w.-]+", meta.get("sources", "").strip("[]"))
    title = re.search(r"^# (.+)$", body, re.M)
    t = title.group(1).strip() if title else name
    by = None
    m = re.match(r"^(.+? (?:\d{4}|\(n\.d\.\))): (.+)$", t) if meta.get("type") == "source" else None
    if m:   # "Klein et al. 2009: seL4, ..." shows the topic first; the authors go to the meta line
        by, t = m.group(1), m.group(2)
    pages[name] = {"file": f, "meta": meta, "body": body, "url": url, "n_sources": len(srcs), "srcs": srcs, "title": t, "by": by}

# the catalogue's one-line descriptions double as each page's subtitle
index_md = pages["index"]["body"]
desc = {m.group(1): m.group(2).strip() for m in re.finditer(r"^- \[\[([^\]|]+)\]\] · (.+)$", index_md, re.M)}
desc = {k: re.sub(r"\s*\d+ sources?\.$", "", v) for k, v in desc.items()}   # the count is in the meta line

def public(s):
    """The working name becomes the public name, in text only."""
    return re.sub(r"(?<![\w/-])zOS(?![\w-])", PUBLIC_NAME, s)

# every page's links, collected before any page is written, so each page knows who links to it
LINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
links_out = {n: {m.group(1).strip() for m in LINK.finditer(p["body"])} & set(pages) - {n, "index"}
             for n, p in pages.items() if n != "index"}
linked_from = {n: {m for m, out in links_out.items() if n in out} for n in pages}
def wikilinks(md, here):
    def rep(m):
        target, text = m.group(1).strip(), (m.group(2) or "").strip()
        p = pages.get(target)
        if not p:
            print(f"wiki: [[{target}]] in {here} has no page", file=sys.stderr)
            return text or target
        by = f" ({p['by']})" if here == "index" and not text and p["by"] else ""   # the catalogue keeps who wrote it
        return f"[{text or p['title']}]({p['url']}){by}"
    return LINK.sub(rep, md)

def to_html(md):
    out = subprocess.run(["pandoc", "-f", "markdown-yaml_metadata_block", "-t", "html5", "--wrap=none"],
                         input=md, capture_output=True, text=True, check=True).stdout
    out = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="noopener" target="_blank"', out)
    out = out.replace("<table>", '<div class="table-wrap wide"><table>').replace("</table>", "</table></div>")
    def label_table(m):   # phones show each row as a card; the cells carry their column's name
        t = m.group(0)
        heads = [re.sub("<[^>]+>", "", h).strip() for h in re.findall(r"<th[^>]*>(.*?)</th>", t, flags=re.S)]
        def lab_row(r):
            cells = iter(heads)
            return re.sub(r"<td([^>]*)>", lambda c: f'<td{c.group(1)} data-label="{_h.escape(next(cells, ""))}">', r.group(0))
        return re.sub(r"<tr.*?</tr>", lab_row, t, flags=re.S)
    out = re.sub(r"<table>.*?</table>", label_table, out, flags=re.S)
    segs = re.split(r"(<[^>]+>)", out)
    return "".join(s if s.startswith("<") else public(s) for s in segs)

def date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][int(m) - 1]} {y}"

css = (root / "paper" / "site.css").read_text(encoding="utf-8")
css = "\n".join(l for l in css.splitlines() if "SPDX-License-Identifier" not in l)
css = css.replace("url(assets/", "url(/assets/")

SCRIPT = """<script>
// narrow screens: the menu button opens the contents as a panel; while it is open the page behind it is inert
const menu = document.querySelector('button.menu'), toc = document.getElementById('toc');
const behind = document.querySelectorAll('header.hero, article, footer');
const isOpen = () => menu.getAttribute('aria-expanded') === 'true';
function setMenu(open) {
  menu.setAttribute('aria-expanded', open);
  document.documentElement.classList.toggle('menu-open', open);
  behind.forEach(el => el.inert = open);
  if (open) toc.querySelector('a').focus();
}
menu.hidden = false;   // without JavaScript the button stays hidden and the page works as before
menu.addEventListener('click', () => setMenu(!isOpen()));
toc.addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
document.addEventListener('click', e => { if (isOpen() && !toc.contains(e.target) && !menu.contains(e.target)) setMenu(false); });
document.addEventListener('keydown', e => { if (e.key === 'Escape' && isOpen()) { setMenu(false); menu.focus(); } });
matchMedia('(min-width: 76rem)').addEventListener('change', e => { if (e.matches) setMenu(false); });
// the contents mark the section being read: the last heading that has passed the upper fifth of the screen
const heads = [...document.querySelectorAll('article h2[id]')], links = new Map([...toc.querySelectorAll('a')].filter(a => a.hash).map(a => [a.hash.slice(1), a]));
let current = null, queued = false;
function mark() {
  queued = false;
  const h = heads.filter(h => h.getBoundingClientRect().top < innerHeight / 5).pop(), a = h ? links.get(h.id) : null;
  if (a === current) return;
  current?.removeAttribute('aria-current'); a?.setAttribute('aria-current', 'location'); current = a;
}
addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(mark); } }, { passive: true });
mark();
</script>"""

def page(title, head, body, crumb):
    back = '<li><a href="/">\u2190 The paper</a></li>' + ('' if title == "Wiki" else '<li><a href="/wiki/">\u2190 Wiki index</a></li>')
    toc = back.replace('<li>', '<li class="toc-back">') + '<li><a href="#top">↑ Top</a></li>' + "".join(
        f'<li><a href="#{i}">{re.sub("<[^>]+>", "", t)}</a></li>' for i, t in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{PUBLIC_NAME + " wiki" if title == "Wiki" else _h.escape(title) + " · " + PUBLIC_NAME + " wiki"}</title>
<link rel="icon" href="/favicon.ico?v={iv}" sizes="32x32">
<link rel="icon" href="/assets/favicon.svg?v={iv}" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png?v={iv}">
<style>
{css}
</style>
</head>
<body>
<header class="hero slim" id="top">
  <div class="hero-inner">
    <p class="crumbs">{crumb}</p>
{head}
  </div>
</header>
<button class="menu" type="button" aria-controls="toc" aria-expanded="false" aria-label="Contents" hidden><span></span></button>
<div class="layout">
  <nav class="toc" id="toc" aria-label="Contents"><p>Contents</p><ol>{toc}</ol></nav>
  <article>
{body}
  </article>
</div>
<footer><div><span class="about"><span>{PUBLIC_NAME} OS</span><span class="sep"> · </span><span>Wiki</span><span class="sep"> · </span><span>Text <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></span></span><span class="links"><a href="/">Paper</a> <a href="{REPO}/tree/main/wiki">GitHub</a> <a href="https://unwritten.studio/impressum">Imprint</a></span></div></footer>
{SCRIPT}
</body>
</html>
"""

CRUMB = f'<a href="/">{PUBLIC_NAME} OS</a> · <a href="/wiki/">Wiki</a>'
written = 0
for name, p in pages.items():
    if name == "index":
        continue
    meta = p["meta"]
    body = re.sub(r"^# .+\n", "", p["body"], count=1, flags=re.M)
    html_body = to_html(wikilinks(body, name))
    # two blocks at the end: what the page rests on, and every other page it is connected with, either way
    order = lambda n: ([k for k, *_ in GROUPS].index(pages[n]["meta"]["type"]), pages[n]["title"].lower())
    def item(n, kind=True):
        by = f' <span class="kind">{_h.escape(pages[n]["by"])}</span>' if pages[n]["by"] else ""
        kd = f' <span class="kind">{GROUP_NAME[pages[n]["meta"]["type"]][:-1] if pages[n]["meta"]["type"] != "design" else "Design"}</span>' if kind else ""
        return f'<li><a href="{pages[n]["url"]}">{_h.escape(public(pages[n]["title"]))}</a>{by if not kind else kd}</li>'
    rests = [s for s in p["srcs"] if s in pages and s != name]
    if rests:
        html_body += ('\n<h2 id="page-sources">Sources</h2>\n<p class="links-note">What this page rests on.</p>\n<ul class="linked-from">'
                      + "".join(item(s, kind=False) for s in sorted(rests, key=order)) + "</ul>")
    related = sorted((links_out[name] | linked_from[name]) - set(rests) - {name}, key=order)
    if related:
        html_body += ('\n<h2 id="related-pages">Related pages</h2>\n<p class="links-note">Pages this one links to, and pages that link here.</p>\n<ul class="linked-from">'
                      + "".join(item(r) for r in related) + "</ul>")
    status = meta.get("status", "drafted")
    bits = [GROUP_NAME[meta["type"]][:-1] if meta["type"] != "design" else "Design"]
    if p["by"]:
        bits.append(_h.escape(p["by"]))
    bits.append(f'<a href="/wiki/#how">{STATUS.get(status, status)}</a>')
    if meta.get("updated"):
        bits.append(f'updated {date(meta["updated"])}')
    if meta["type"] != "source" and p["n_sources"]:
        bits.append(f'{p["n_sources"]} source{"s" if p["n_sources"] != 1 else ""}')
    sub = desc.get(name, "")
    sub = to_html(wikilinks(sub, "index")).strip().removeprefix("<p>").removesuffix("</p>") if sub else ""
    head = (f'    <div class="titleblock">\n      <h1 class="name">{_h.escape(public(p["title"]))}</h1>\n'
            + (f'      <p class="sub">{sub}</p>\n' if sub else "")
            + f'      <p class="ver">{" · ".join(bits)}</p>\n    </div>')
    out = p["file"].with_suffix(".html")
    out.write_text(page(public(p["title"]), head, html_body, CRUMB), encoding="utf-8")
    written += 1

# the wiki's front page: what it is, how it is made, then the catalogue
cat = re.sub(r"^# .+\n+(?:The catalogue.*\n+)?", "", index_md, count=1, flags=re.M)
cat = re.sub(r"^## zOS$", "## Design", cat, flags=re.M)
nyc = re.search(r"^## Not yet covered\n.*?(?=^## |\Z)", cat, flags=re.M | re.S)
if nyc:   # it has no links, so it closes the catalogue instead of interrupting it
    cat = cat[:nyc.start()] + cat[nyc.end():].rstrip() + "\n\n" + nyc.group(0)
counts = {k: sum(1 for p in pages.values() if p["meta"].get("type") == k) for k, *_ in GROUPS}
intro = (f"This wiki gathers what the sources behind the paper show. It has a page for each source, each concept, each "
         f"system the paper builds on and each part of the design: {counts['source']} sources, {counts['concept']} concepts, "
         f"{counts['system']} systems and {counts['design']} parts of the design so far. Every page says what is proven, "
         f"tested or assumed, and on which source that rests.\n\n"
         f"## How this wiki is made {{#how}}\n\n"
         f"A language model writes the wiki and keeps it up to date from the sources in the project's research pool, after Andrej "
         f"Karpathy's idea of a wiki that a language model maintains. A daily run adds new sources and works older ones in.\n\n"
         f"- **Draft.** Written, not yet reviewed, or held back for a stated reason.\n"
         f"- **LLM reviewed.** A second, independent pass found every figure and every quotation in its source and read "
         f"the page's claims against the sources. This is the state of most pages.\n"
         f"- **Human curated.** Someone on the team has also compared the page with its sources.\n\n"
         f"A page can still be wrong or misleading in detail. If you find a mistake, please [open an issue]({REPO}/issues). "
         f"Wiki rules are noted [here]({REPO}/blob/main/wiki/CLAUDE.md), changes are followed [here]({REPO}/blob/main/wiki/log.md).\n\n")
index_body = to_html(intro + wikilinks(cat, "index"))
index_head = (f'    <div class="titleblock">\n      <h1 class="name">Wiki</h1>\n'
              f'      <p class="sub">What the sources behind the paper show, page by page.</p>\n'
              f'      <p class="ver">{len(pages) - 1} pages · updated {date(pages["index"]["meta"].get("updated", "2026-01-01"))} · <a href="#how">How this wiki is made</a></p>\n    </div>')
(wiki / "index.html").write_text(page("Wiki", index_head, index_body, f'<a href="/">{PUBLIC_NAME} OS</a>'), encoding="utf-8")
print(f"wiki: {written + 1} pages")

# the lexicon: one line per term, collected from glossary and wiki (lexicon.py); G and W lead to the longer texts
lx, lx_problems = lexicon.collect(root)
for msg in lx_problems:
    print("lexicon:", msg, file=sys.stderr)
lx_body = ['<div class="wide">', lexicon.az_bar(lx, ""), ""]
for c in sorted({lexicon.letter(e) for e in lx}):
    lx_body.append(f'<h2 class="lx-letter" id="{c.lower()}">{c}</h2>\n<dl class="lexicon">')
    for e in (e for e in lx if lexicon.letter(e) == c):
        refs = []
        if e["glossary"]:
            refs.append(f'<a href="/#{e["glossary"]}" aria-label="{_h.escape(e["term"])} in the glossary">G</a>')
        if e["wiki"]:
            refs.append(f'<a href="{e["wiki"]}" aria-label="{_h.escape(e["term"])} in the wiki">W</a>')
        head_words, _, last = _h.escape(public(e["short"])).rpartition(" ")   # the references stay with the last word
        lx_body.append(f'<div><dt>{_h.escape(public(e["term"]))}</dt><dd>{head_words} <span class="nw">{last}<sup class="refs">{"".join(refs)}</sup></span></dd></div>')
    lx_body.append("</dl>")
lx_body.append("</div>")
lx_head = (f'    <div class="titleblock">\n      <h1 class="name">Lexicon</h1>\n'
           f'      <p class="sub">Every term in one line. G leads to the glossary, W to the wiki.</p>\n    </div>')
(root / "lexicon").mkdir(exist_ok=True)
(root / "lexicon" / "index.html").write_text(page("Lexicon", lx_head, "\n".join(lx_body), f'<a href="/">{PUBLIC_NAME} OS</a>'), encoding="utf-8")
