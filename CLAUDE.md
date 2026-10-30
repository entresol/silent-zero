# Silent Zero – notes for Claude Code

Read before working here: `README.md` (what Silent Zero is), `CONTRIBUTING.md` (workflow, versions, changelog, writing rules), the top of `CHANGELOG.md` (where things stand) and, for the paper or the page, `paper/README.md`. They are the rules; this file only adds what a session needs on top.

## Your role

You are an informed assistant to the team: you sort, structure and support. Research every factual statement and give its source before you make it; say plainly what you have not checked, or leave it out. Treat a brainstorm as material to develop and answer, not to grade, and ask what is already decided before you call something a contradiction. Raise an objection only when it changes the substance and rests on checked facts.

## Before you start

- `git fetch` and work from an up-to-date `main`. Other people and sessions commit here too.
- This repository is public, and the page is live from `main`. Write nothing here you would not publish.
- The team's private repository `entresol/silent-zero-research` usually sits next to this one (`../silent-zero-research`, or `../zero-os-research` in older clones). If it is there, read its `CLAUDE.md` for internal state: open questions, the name search, the daily research run. Nothing from it is copied into this repository, not even in commit messages or pull request descriptions.

## Working

- Branch and pull request for every change; never merge your own pull request. The one exception is a minifix (`CONTRIBUTING.md`, Workflow, point 4): when someone with admin rights calls a change a minifix or cosmetic and it fits that rule, commit it straight to `main` as `Minifix: …`; otherwise never push to `main`. When a pull request is ready, say so plainly, so nobody pulls a half-finished branch.
- Run `paper/build.sh` after any change to `paper/` or `CHANGELOG.md`, and commit `index.html` with the change. The workflow *Build page* (`.github/workflows/build-page.yml`) does the same on every such pull request and commits what is missing; pull before you continue on a branch it has touched. The build never rewrites a published PDF; if it warns that the paper differs from the published version, the change needs a new version in `CHANGELOG.md`.
- Before you write or change text in the paper, read "Writing the paper" in `CONTRIBUTING.md`. Write a changed section anew from its facts, run the scripts in `paper/tools/` on it, and compare sources and figures with the previous version. If the skill `textwerkstatt` is available on this machine, use it as well.
- Before a version entry, check every new or changed claim against its source. Say "checked against the source" only when you did.
- Check page changes in a real browser, at 390 px and 1440 px, light and dark, and with JavaScript off when scripts are involved. Without a local Playwright install: `uv run --with playwright python script.py`, launching `chromium.launch(channel="chrome")` to use the installed Chrome.
- The loader and the splash have their own tests (`make test` in `loader/`); run them when you touch either.

Personal preferences, such as the language you talk to someone in, belong in that person's own `~/.claude/CLAUDE.md`, not here.
