# SPDX-License-Identifier: BSD-2-Clause
"""The two doors of the page: Use (for the people who will run Silent Zero) and Devel (for developers and technically
interested visitors). Each is a real page, /use/ and /devel/, and the start page can lay it over itself as a sheet.

The contents are in sheets.json (English only for now): about a dozen points per door, each with a status. Everything
here only turns that data into HTML and Markdown; build_wiki.py writes the pages, build_site.py puts the tabs on the
start page. A point may only say "available now" if it points at something that exists today."""
import html as _h
import json
import re
from pathlib import Path

DATA = json.loads((Path(__file__).resolve().parent / "sheets.json").read_text(encoding="utf-8"))
NAMES = [k for k in DATA if not k.startswith("_")]
STATUS = {"now": "available now", "wip": "in progress", "plan": "planned", "open": "open question"}
SITE = "https://silentzero.ooo"


def _check():
    for name in NAMES:
        for it in DATA[name]["items"]:
            assert it[0] in STATUS, (name, it)
            assert it[0] != "now" or len(it) > 3, ("an item that is available now needs a link", it[1])


_check()


def _link(label, url):
    return f'<a href="{_h.escape(url)}">{_h.escape(label)}</a>'


def points(items):
    out = []
    for status, title, text, *link in items:
        more = " " + _link(*link[0]) if link else ""
        out.append(f'<li><span class="st st-{status}">{STATUS[status]}</span>'
                   f'<div><strong>{_h.escape(title)}</strong><p>{text}{more}</p></div></li>')
    return '<ul class="points">' + "".join(out) + "</ul>"


def head(name):
    d = DATA[name]
    return (f'    <div class="titleblock">\n      <h1 class="name">{_h.escape(d["title"])}</h1>\n'
            f'      <p class="sub">{_h.escape(d["lede"])}</p>\n    </div>')


def article(name):
    d = DATA[name]
    out = []
    inv = d.get("involved")
    if inv:
        bullets = "".join("<li>" + "".join(_link(*p) if isinstance(p, list) else p for p in b) + "</li>" for b in inv["bullets"])
        out.append(f'<h2 id="get-involved">{_h.escape(inv["heading"])}</h2>\n<p>{_h.escape(inv["text"])}</p>\n<ul>{bullets}</ul>')
        out.append(f'<h2 id="start-here">{_h.escape(d["start"])}</h2>')
    out.append(points(d["items"]))
    other = DATA[d["other"]]
    out.append(f'<p class="other">Looking for the other door? <a href="/{other["dir"]}/">{_h.escape(other["tab"])}</a></p>')
    return "\n".join(out)


def markdown(name):
    d = DATA[name]
    md = [f"# {d['title']}", "", f"> {d['lede']}", ""]
    inv = d.get("involved")
    if inv:
        md += [f"## {inv['heading']}", "", inv["text"], ""]
        for b in inv["bullets"]:
            md.append("- " + "".join(f"[{p[0]}]({p[1] if p[1].startswith('http') else SITE + p[1]})" if isinstance(p, list) else p for p in b))
        md += ["", f"## {d['start']}", ""]
    for status, title, text, *link in d["items"]:
        text = re.sub(r"<code>(.*?)</code>", r"`\1`", text)
        url = ""
        if link:
            u = link[0][1]
            url = f" [{link[0][0]}]({u if u.startswith('http') else SITE + u})"
        md.append(f"- **{title}** ({STATUS[status]}): {text}{url}")
    other = DATA[d["other"]]
    md += ["", f"Looking for the other door? [{other['tab']}]({SITE}/{other['dir']}/index.html.md)", ""]
    return "\n".join(md)


def doors():
    """The two tabs on the edges of the start page. Without JavaScript they are links to the pages."""
    sides = {NAMES[0]: "l", NAMES[1]: "r"}   # the first door lies on the left, the second on the right
    return "".join(f'<a class="sh-tab sh-tab-{sides[n]}" href="{DATA[n]["dir"]}/" data-sheet="{n}"><span>{_h.escape(DATA[n]["tab"])}</span></a>' for n in NAMES)
