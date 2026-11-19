# SPDX-License-Identifier: BSD-2-Clause
"""The activity band on the landing page: what the wiki did lately, drawn from wiki/log.md and the pages themselves.

Nothing is written for it. A day counts when the log has an entry for it; the newest days list the sources worked in,
linked to their pages. The window ends on the newest log date, not on the day of the build, so the build stays
reproducible: the same repository gives the same band."""
import datetime as dt
import html
import re
from pathlib import Path

DAYS = 28      # the strip
LISTED = 4     # days listed below it
TITLES = 3     # titles shown per day before "+ n more"
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def _day(d):
    return f"{d.day} {MONTHS[d.month - 1]}"


def _title(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            t = line[2:].strip()
            m = re.match(r"^[^:]{2,60}\b(?:19|20)\d\d[a-z]?:\s+(.*)$", t)   # "Li et al. 2026: ToolFence" -> "ToolFence"
            return m.group(1) if m else t
    return path.stem


def entries(root):
    """The log's entries as (date, kind, ids), oldest first."""
    out = []
    for m in re.finditer(r"^## \[(\d{4}-\d\d-\d\d)\] (\w+)(?: \| (.*))?$", (Path(root) / "wiki" / "log.md").read_text(encoding="utf-8"), re.M):
        out.append((dt.date.fromisoformat(m.group(1)), m.group(2), [x.strip() for x in (m.group(3) or "").split(",") if x.strip()]))
    return out


def hint(root):
    """One line in the header, above the fold, that links down to the band. The date is ISO, like the paper's version,
    so that it needs no translation in the header's five languages."""
    log = entries(Path(root))
    if not log:
        return ""
    last = max(d for d, _, _ in log).isoformat()
    return (f'<p class="pulse-hint"><a href="#activity" aria-label="Wiki last updated {last}: see the recent activity">'
            f'<span class="dot" aria-hidden="true"></span>Wiki \u00b7 {last}</a></p>')


def band(root):
    root = Path(root)
    log = entries(root)
    if not log:
        return ""
    last = max(d for d, _, _ in log)
    first = last - dt.timedelta(days=DAYS - 1)
    count = {}
    for d, _, _ in log:
        count[d] = count.get(d, 0) + 1
    active = sum(1 for i in range(DAYS) if first + dt.timedelta(days=i) in count)
    pages = sum(1 for f in (root / "wiki").glob("*/*.md") if not f.name.endswith(".html.md"))

    cells = []
    for i in range(DAYS):
        d = first + dt.timedelta(days=i)
        n = count.get(d, 0)
        cls = "on" if n else ""
        if d == last:
            cls += " last"
        label = f"{_day(d)}: " + (f"{n} wiki update{'s' if n > 1 else ''}" if n else "no update")
        cells.append(f'<i class="{cls.strip()}" title="{label}"></i>')
    strip_label = f"Wiki updates on {active} of the {DAYS} days from {_day(first)} to {_day(last)}"

    # the newest days with sources worked in or a lint pass, newest first
    by_day = {}
    for d, kind, ids in log:
        if kind in ("ingest", "lint"):
            by_day.setdefault(d, []).append((kind, ids))
    items = []
    for d in sorted(by_day, reverse=True)[:LISTED]:
        links, lint = [], False
        for kind, ids in by_day[d]:
            if kind == "lint":
                lint = True
            for i in ids:
                p = root / "wiki" / "sources" / f"{i}.md"
                if p.exists():
                    links.append((i, _title(p)))
        shown = [f'<a href="wiki/sources/{i}.html">{html.escape(t)}</a>' for i, t in links[:TITLES]]
        if len(links) > TITLES:
            shown.append(f"{len(links) - TITLES} more")
        if lint:
            shown.append("lint pass")
        if shown:
            items.append(f'<li><time datetime="{d.isoformat()}">{_day(d)}</time><span>{" · ".join(shown)}</span></li>')

    return f"""<section class="pulse" id="activity" aria-label="Recent wiki activity"><div>
<div class="pulse-now">
<p class="pulse-title"><span class="dot" aria-hidden="true"></span><span><a href="wiki/">Wiki</a> · updated</span></p>
<p class="pulse-date"><time datetime="{last.isoformat()}">{_day(last)} {last.year}</time></p>
<p class="pulse-meta">{active} of {DAYS} days with updates · {pages} pages</p>
<div class="strip" role="img" aria-label="{strip_label}">{"".join(cells)}</div>
</div>
<ul class="pulse-list">{"".join(items)}</ul>
</div></section>
"""
