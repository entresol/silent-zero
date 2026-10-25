# zOS – notes for Claude Code

Read before working here: `README.md` (what zOS is), `CONTRIBUTING.md` (workflow, versions, changelog, writing rules), the top of `CHANGELOG.md` (where things stand) and, for the paper or the page, `paper/README.md`. They are the rules; this file only adds what a session needs on top.

## Before you start

- `git fetch` and work from an up-to-date `main`. Other people and sessions commit here too.
- This repository is public, and the page is live from `main`. Write nothing here you would not publish.
- The team's private repository `entresol/zero-os-research` usually sits next to this one (`../zero-os-research`). If it is there, read its `CLAUDE.md` for internal state: open questions, contacts, the name search, the daily research run. Nothing from it is copied into this repository, not even in commit messages or pull request descriptions.

## Working

- Branch and pull request for every change; never push to `main`, never merge your own pull request. When a pull request is ready, say so plainly, so nobody pulls a half-finished branch.
- Run `paper/build.sh` after any change to `paper/` or `CHANGELOG.md`, and commit `index.html` with the change. The workflow *Build page* (`.github/workflows/build-page.yml`) does the same on every such pull request and commits what is missing; pull before you continue on a branch it has touched. The build never rewrites a published PDF; if it warns that the paper differs from the published version, the change needs a new version in `CHANGELOG.md`.
- Before a version entry, check every new or changed claim against its source. Say "checked against the source" only when you did.
- Check page changes in a real browser, at 390 px and 1440 px, light and dark, and with JavaScript off when scripts are involved. Without a local Playwright install: `uv run --with playwright python script.py`, launching `chromium.launch(channel="chrome")` to use the installed Chrome.
- The loader and the splash have their own tests (`make test` in `loader/`); run them when you touch either.

Personal preferences, such as the language you talk to someone in, belong in that person's own `~/.claude/CLAUDE.md`, not here.
