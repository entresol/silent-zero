# SPDX-License-Identifier: BSD-2-Clause
"""The band of latest changes on the landing page, and the date of the newest change for the header.

Nothing is written for it. Two files in the repository say what changed: CHANGELOG.md (paper, project and page) and
wiki/log.md (the wiki). A day counts when either has an entry for it. The band lists the newest change of each area:
the paper, the wiki, the project. The window ends on the newest date, not on the day of the build, so the build stays
reproducible: the same repository gives the same band."""
import datetime as dt
import html
import re
from pathlib import Path

import changelog

DAYS = 28      # the strip
TITLES = 2     # wiki sources named before "n more"
TITLE = 42     # characters of a source title
SENTENCE = 100 # characters of a changelog sentence
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
# a page-scope changelog entry that reports the wiki's daily work: the wiki's own log covers those
WIKI_ENTRY = re.compile(r"^(?:Wiki[:,]|The wiki (?:grew|checks)|\w+ (?:further )?sources? worked)")


def _day(d):
    return f"{d.day} {MONTHS[d.month - 1]}"


def _title(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            t = line[2:].strip()
            m = re.match(r"^[^:]{2,60}\b(?:19|20)\d\d[a-z]?:\s+(.*)$", t)   # "Li et al. 2026: ToolFence" -> "ToolFence"
            return m.group(1) if m else t
    return path.stem


def _short(title):
    return title if len(title) <= TITLE else title[:TITLE - 1].rsplit(" ", 1)[0].rstrip(",;:-") + "\u2026"


def _log(root):
    """The wiki log's entries as (date, kind, ids), oldest first."""
    text = (Path(root) / "wiki" / "log.md").read_text(encoding="utf-8")
    return [(dt.date.fromisoformat(m.group(1)), m.group(2), [x.strip() for x in (m.group(3) or "").split(",") if x.strip()])
            for m in re.finditer(r"^## \[(\d{4}-\d\d-\d\d)\] (\w+)(?: \| (.*))?$", text, re.M)]


def _changes(root):
    """The changelog's entries as (date, version, scope, text), newest first."""
    return [(dt.date.fromisoformat(v[:10]), v, s, t) for v, s, t in changelog.parse(Path(root) / "CHANGELOG.md")]


def last_date(root):
    """The date of the newest change of any kind, as an ISO string."""
    days = [d for d, _, _ in _log(root)] + [d for d, _, _, _ in _changes(root)]
    return max(days).isoformat()


def _sentence(text):
    """The first sentence of a changelog entry, as plain HTML: code spans kept, links reduced to their words."""
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    m = re.match(r"(.+?[.!?])(?:\s|$)", text)
    s = m.group(1) if m else text
    cut = re.match(r"(.{25,}?)[:;]\s", s)   # a long sentence stops at its first colon or semicolon
    if cut and len(s) > SENTENCE:
        s = cut.group(1)
    if len(s) > SENTENCE:
        s = s[:SENTENCE - 1].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", html.escape(s, quote=False))


def band(root):
    root = Path(root)
    log, changes = _log(root), _changes(root)
    last = dt.date.fromisoformat(last_date(root))
    first = last - dt.timedelta(days=DAYS - 1)
    count = {}
    for d in [d for d, _, _ in log] + [d for d, _, _, _ in changes]:
        count[d] = count.get(d, 0) + 1
    active = sum(1 for i in range(DAYS) if first + dt.timedelta(days=i) in count)

    cells = []
    for i in range(DAYS):
        d = first + dt.timedelta(days=i)
        cls = ("on" if d in count else "") + (" last" if d == last else "")
        cells.append(f'<i class="{cls.strip()}" title="{_day(d)}: {"change" if d in count else "no change"}"></i>')
    strip_label = f"Changes on {active} of the {DAYS} days from {_day(first)} to {_day(last)}"

    # the newest change of each area
    items = []   # (date, order, html)
    wiki = {}
    for d, kind, ids in log:
        if kind in ("ingest", "lint"):
            wiki.setdefault(d, []).append((kind, ids))
    if wiki:
        d = max(wiki)
        links, lint = [], False
        for kind, ids in wiki[d]:
            lint = lint or kind == "lint"
            links += [(i, _title(root / "wiki" / "sources" / f"{i}.md")) for i in ids if (root / "wiki" / "sources" / f"{i}.md").exists()]
        shown = [f'<a href="wiki/sources/{i}.html">{html.escape(_short(t))}</a>' for i, t in links[:TITLES]]
        if len(links) > TITLES:
            shown.append(f'<a href="#changes">{len(links) - TITLES} more</a>')
        if lint:
            shown.append("lint pass")
        items.append((d, 0, "Wiki", " · ".join(shown)))
    project = next(((d, v, t) for d, v, s, t in changes if s == "Project" or (s == "Site" and not WIKI_ENTRY.search(t))), None)
    if project:
        d, v, t = project
        items.append((d, 1, "Project", f'<a href="#changes">{_sentence(t)}</a>'))
    paper = next(((d, v, t) for d, v, s, t in changes if s == "Paper"), None)
    if paper:
        d, v, t = paper
        pdf = f' · <a href="versions/zos-zero-os-{v}.pdf">PDF</a>' if changelog.has_pdf(v) else ""
        items.append((d, 2, "Paper", f'<a href="#changes">{_sentence(t)}</a>{pdf}'))
    items.sort(key=lambda x: (-x[0].toordinal(), x[1]))
    rows = "".join(f'<li><span class="area">{a}</span><time datetime="{d.isoformat()}">{_day(d)}</time><span class="what">{h}</span></li>'
                   for d, _, a, h in items)

    return f"""<section class="pulse" id="activity" aria-label="Latest changes"><div>
<div class="pulse-now">
<p class="pulse-title"><span class="dot" aria-hidden="true"></span>Paper · Wiki · Project</p>
<p class="pulse-date"><time datetime="{last.isoformat()}">{_day(last)} {last.year}</time></p>
<p class="pulse-meta">{active} of {DAYS} days with changes · <a href="#changes">All changes</a></p>
<div class="strip" role="img" aria-label="{strip_label}">{"".join(cells)}</div>
</div>
<ul class="pulse-list">{rows}</ul>
</div></section>
"""
