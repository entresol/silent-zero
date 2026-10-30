# The zOS wiki – the schema

This file tells Claude Code how to build and keep the zOS wiki. Read it before any work in this directory. People read the wiki; Claude writes it and keeps it in order. The pattern follows Karpathy's "LLM Wiki" (gist, 4 April 2026). The sources stay unchanged, the wiki is a set of linked Markdown pages, and this file holds the rules. When a rule turns out wrong, change it here and say why in `log.md`.

## Where it lives

The wiki is public. It lives in `wiki/` of the public repository and becomes the section `/wiki/` of the project page. It moved here from the team's private research repository on 2026-10-30; the sources it is written from stay there.

So the rules of this repository apply to every page:

- Every claim cites a public source. The reader must be able to find it without access to the private repository.
- Nothing from `naming/`, `notes/`, `audit/` or `digests/` of the private repository, and nothing about people the team is in contact with, appears here. Notes may tell you where to look in a source; the page is written from the source itself.
- No long quotations. Quote a phrase when the exact words matter, and otherwise say it in your own words.
- English, written to the rules in "Writing the paper" in `CONTRIBUTING.md` of the public repository.

## The name

Write the project's name as `zOS`. It is the team's working name; the build of the page replaces it with the public name, today Silent Zero, so a change of name touches one line instead of every page. Quotations keep their own wording.

## Sources

The sources live in the private research repository, usually cloned next to this one as `../silent-zero-research` (from this directory: `../../silent-zero-research`).

- Its `pool.json` is the list of sources and the source of truth for authors, year, title and link. A wiki source page carries the pool id and nothing contradicts the pool.
- The texts are its `papers/<id>.pdf` and `sources/web/<id>--<date>.html`. They never change. Extract text with `pdftotext -layout`; the result goes to `.cache/text/<id>.txt`, which is not committed.
- A source we can read only in part (abstract, a talk's slides, a press release) can have a page, and the page says so.

## Pages

| Directory | One page per | Holds |
| --- | --- | --- |
| `sources/` | pool entry | what the source shows, how, and its limits |
| `concepts/` | idea | e.g. mixed criticality, WCET, confused deputy, Simplex |
| `systems/` | piece of existing work | e.g. seL4, LionsOS, Microkit, OpenTitan, CHERI, agentOS |
| `design/` | part of the zOS design | which sources carry it, and how well |

Plus `index.md` (the catalogue, read first for every question) and `log.md` (what happened, newest last). The build (`paper/build_wiki.py`, run by `paper/build.sh` and by the workflow *Build page*) renders every page as HTML next to its Markdown; never edit the HTML.

File names are lower case with hyphens. A source page is named by its pool id. Links between pages are `[[name]]` or `[[name|text]]`, so the wiki works in Obsidian and the build of the page can translate them.

Every page starts with front matter:

```yaml
---
type: source | concept | system | design
status: drafted | reviewed | doublechecked
sources: [pool ids this page relies on]
updated: YYYY-MM-DD
---
```

A source page adds `id`, `read: full | partial` and `kind`, which says what kind of evidence the source gives: `proof`, `measurement`, `test`, `progress` (work under way, with a method and results that are not final), `design` (an architecture without results), `survey`, `position` or `report` (news, project pages, vendor statements).

`status` says who has looked at a page, and the page shows it to the reader.

- `drafted`: Claude wrote the page and ran the checks below.
- `reviewed`: a second, independent pass found nothing open. Every figure and every quotation was found in its source, and the page's claims, hedges and inferences were read against the sources. Claude sets it; this is the normal state of a published page, because the team cannot check every page by hand.
- `doublechecked`: a person has also compared the page with its sources. Only a person sets it.

A page is held back as `drafted` only for a reason: a claim stronger than its source that cannot be fixed, a page that rests on the unread part of a source read only in part, or an open team decision. Do not use "verified" for any of these, because in this project that word means formal verification.

### A source page

1. **What it shows.** The claims, each with its figure and where in the source it stands (section, table, page). Separate what the authors measured or proved from what they expect.
2. **How.** Method and setting, in a few sentences: what was built, on which hardware, against what.
3. **Limits.** First what the authors say themselves, then what a careful reader adds, marked as such.
4. **Against the wiki.** For each existing page it touches: does it confirm, extend, contradict or replace what the page says? Link the page.
5. **For zOS.** Which `design/` pages it bears on, and whether it changes their state.

### A concept or system page

What it is in two or three sentences, its state with a date, and the sources that say so. A system page also names its licence and where its code lives. Open questions go at the end.

### A design page

One per part of the design: root of trust, bootloader, kernel, static system, drivers, broker, agents, real-time loops, safety path. Each says what the part must do, what exists, what is proven, tested or assumed and on which sources that rests, and what is still open. When a source contradicts the paper, the page says so and links both.

## Ingest: working in a new source

1. Read the whole text. A source read only in part gets `read: partial`.
2. Write the source page.
3. Compare it with the wiki. This is the point of the exercise. Go through `index.md`, open every page the source touches, and update it: new facts, a newer date, a contradiction stated openly. Do not overwrite an existing claim quietly. If the new source replaces it, say which source is newer and what changed.
4. Create a concept or system page when the source needs one and it does not exist.
   A source the text relies on but the pool lacks goes into `log.md` as a candidate for the pool; the page names it and says it is not yet in the pool.
5. Check facts (below), then style (below).
6. Update `index.md` and append to `log.md`.

## Checking facts

Style and truth are separate checks. A fluent sentence can be wrong, and fluency makes it more believable.

- After writing, check every figure and every claim on the changed pages against the source text once more, from the text and not from memory. A claim without a place in the source is removed or marked as an inference.
- Keep the source's hedges. Summaries drift stronger than their sources: "much" becomes "most", "there is hope" becomes "the way", a result "on RISC-V" loses its platform, and of two alternatives the authors name only one survives. The first fact check of this wiki found all four.
- Every inference is marked as such ("Our reading", "A careful reader adds"), also when it sits in a section about the source.
- A detail taken from another source (a venue, a date) names that source.
- Compare the changed pages with their previous version. No source, figure or link may get lost.
- When the ingest runs without a person, a second agent with fresh context does this check. It gets only the source text and the changed pages, so the draft's reasoning cannot lead it.

## Checking style

Run `slop_lint.py` and `vorfeld.py` from `paper/tools/` of the public repository on every changed page, and the Textwerkstatt skill where it is available. `vorfeld.py` needs spaCy; run it with the `uv run` command in its docstring, which needs no installation. It reports the words before the main verb; sentences joined by semicolons and list items merged by the extraction give false hits, so read its worst list and fix the real ones, mostly sentences without a verb. Strip the front matter first; `slop_lint.py` reads its `key: value` lines as colon turns. Colons that introduce a list or a table row are fine; a bold label with a colon at the start of every item is the pattern to avoid. Write a changed page anew from its facts; do not patch it sentence by sentence.

## When to stop and ask

Some decisions are not Claude's alone. Do not decide them; stop, leave the page as `drafted` without the change in question, and put the question to the team: in the session if a person is there, otherwise in the pull request under the heading **Needs a decision**.

- A source contradicts a claim in the paper, or changes the state of a `design/` page from proven to tested or assumed, or the other way round.
- Two sources contradict each other and neither is clearly newer or better.
- A source's standing is unclear: withdrawn, disputed, or only the vendor's own word on a figure that matters.
- Whether a source belongs in the wiki at all, when it touches the project's scope or a sensitive field (weapons, surveillance, named people).
- A page would describe the intent of a person or group, beyond what they published.
- Anything else where you notice you are about to choose a position for the project.

## The daily run

The routine "Silent Zero research pool – daily" works the wiki in two ways. Each source it adds to the pool is worked in on the same day, following "Ingest" above. Then it takes up to three sources from the backlog in `rings.md`, in the order of the rings, top to bottom, and marks them done there. Its wiki changes come as a pull request to this repository; pool entries and digests go to the private one. Each ingest gets the fact check by a second agent with fresh context. The pull request lists the pages it touched and every open question under **Needs a decision**. A pull request with open questions is never merged automatically. Whether the routine may merge the rest itself is decided by the team, and it is recorded here once it is.

## Rings

`rings.md` holds the order in which the pool is worked in: from the sources the design rests on outwards, in waves. The rings are a guide to the order, not a gate: when one ring is done, the work continues with the next. The team may reorder them at any time.

## log.md

One entry per ingest, query worth keeping or lint pass, with a fixed prefix so it can be searched:

```
## [YYYY-MM-DD] ingest | <pool id>
```

Then two or three lines: pages created, pages changed, questions raised.

## Lint

From time to time, and before the wiki moves: contradictions between pages, claims a newer source has replaced, pages nothing links to, concepts used on several pages without a page of their own, missing links, and `drafted` pages that are older than a month.
