# Contributing

How we work on zOS, for everyone who changes and commits here, people and AI assistants alike. This repository is public, and so is everything in it: the page is served straight from `main`.

## What lives where

- `paper/`: the paper's source (`src.md`), its glossary and the build for PDF and page. See [`paper/README.md`](paper/README.md).
- `CHANGELOG.md`: what changed in substance. The build reads the current paper version from it.
- `loader/`, `splash/`: the first code, a loader and its boot screen, with their own READMEs and tests.
- `review/`: reviews of earlier drafts.
- `assets/`: fonts and images for the page.
- Generated, never edited by hand: `index.html`, `zos-zero-os.pdf`, `versions/*.pdf`.

## Workflow

1. Branch from an up-to-date `main`, named by area: `paper/…`, `site/…`, `project/…`, `loader/…`.
2. One topic per pull request. `main` accepts changes only through pull requests; GitHub rejects direct pushes, for everyone, because every merge is published at once. The core group (the paper's authors) has write access and merges; everyone else works from a fork and opens a pull request from there.
3. A member of the core group may merge their own pull request for typos, wording in the changelog, links and formatting. Claims in the paper, a new version, changes to the build or the design, and anything that touches a source get a second pair of eyes first.
4. If the change touches `paper/` or `CHANGELOG.md`, the page has to be rebuilt. Run `paper/build.sh` and commit the regenerated `index.html` with it, or let the workflow *Build page* do it: it rebuilds every such pull request and commits the result into it, so a quick fix in GitHub's web editor arrives complete. Wait until it has run before merging. If it had something to add, its commit "Site: rebuild (automatic)" is the last one in the pull request; GitHub does not run checks on that commit again, so the green check sits on the commit before it. GitHub Pages serves exactly what is on `main`.
5. Commit messages in English. First line: area and what changed (`Site: contents menu on narrow screens`, `Version 2026-10-23-v0.11: a glossary of 38 terms`). Body: why, and how it was checked.

## Versions and the changelog

- **A change to the paper's text is a new paper version.** Add an entry `## YYYY-MM-DD-vX.Y · Paper` at the top of `CHANGELOG.md`; the build prints that version on the paper and the page and writes `versions/zos-zero-os-YYYY-MM-DD-vX.Y.pdf`.
- **A published version never changes.** Once a version's PDF is on `main`, the build leaves it as it is and warns if the paper it just built differs. That warning means: add a new version.
- **Changes without a new paper version** (the page, the project) get an entry with only their date: `## YYYY-MM-DD · Site` or `· Project`.
- **What goes in:** what a reader or contributor notices or needs to know. Typos, small layout fixes and build internals stay in the commit history.
- **Only the public project.** The changelog describes this repository and nothing else.

## Writing the paper

- English only, in plain words. The page around it may be translated later; the paper is not.
- Every factual claim has a source in References (author, year), and the source says what we cite it for. Check it before citing; prefer the primary source.
- Say how we know: *proven* only for a machine-checked proof, *tested* for what was shown under defined load or attack, *assumed* for what is simply trusted. Goals are named as goals.
- Dates are absolute ("the third quarter of 2028", not "in two years").
- A new technical term that a reader may not know gets an entry in `paper/glossary.md`.

## What never goes into this repository

Internal material stays in the team's private repository: research notes, papers we may not redistribute, contacts, and the search for the project's final name. "zOS" is a working title; the domain in `CNAME` stays as it is until the project has its name.

## Licences

Code, including the build scripts: BSD-2-Clause, with an `SPDX-License-Identifier` line at the top of each new file. Paper, texts and figures: CC BY 4.0. By contributing, you agree that your contribution is published under these licences.
