# Develop with Silent Zero

> For people who build, verify or just want to look inside. Everything here is open; the label says what works today.

## Get involved

We are looking for people who know firmware, formal verification or robots, and who want to test this argument before the architecture hardens around it.

- Discuss an idea or ask a question: [Discussions](https://github.com/entresol/silent-zero/discussions).
- See what the sources behind the paper show, page by page: the [wiki](https://silentzero.ooo/wiki/).
- Point out a flaw, a wrong claim or a missing source: [Issues](https://github.com/entresol/silent-zero/issues).
- Propose a change to the paper or the code: a pull request; [CONTRIBUTING.md](https://github.com/entresol/silent-zero/blob/main/CONTRIBUTING.md) says how we work.

## Start here

- **Architecture on one page** (available now): What the parts are and why nothing at the base is new. [The paper](https://silentzero.ooo/silent-zero.pdf)
- **What is proven, what is assumed** (available now): The kernel page lists the proof status per configuration: proven, not stated, tested, assumed. [Kernel](https://silentzero.ooo/wiki/design/kernel.html)
- **Read the code** (available now): The loader (under 8 KB on RISC-V), the splash renderer and the build scripts. [Code](https://github.com/entresol/silent-zero/tree/main/loader)
- **Run the loader in QEMU** (available now): Needs clang with the RISC-V target, ld.lld and QEMU; `make test` boots a good image and tampered ones. The steps are in the README; not yet checked on a clean machine. [README](https://github.com/entresol/silent-zero/blob/main/loader/README.md)
- **Where we are unsure and want help** (available now): Every wiki page ends with its open questions; the Issues collect what the team has to decide. [Wiki](https://silentzero.ooo/wiki/)
- **How AI helps with proofs** (available now): A model proposes, the proof checker judges. The wiki collects what is known. [Proof automation](https://silentzero.ooo/wiki/concepts/proof-automation.html)
- **The broker: how authority is handed out** (in progress): A design, no code yet, nothing proven. [Design](https://silentzero.ooo/wiki/design/broker.html)
- **Add a component on top of the kernel** (planned): A static system description with protection domains and channels. [Static system](https://silentzero.ooo/wiki/design/static-system.html)
- **Build the image yourself** (planned): A reproducible build from source.
- **Contribute** (available now): CONTRIBUTING.md says how we work: branches, pull requests, the changelog. [CONTRIBUTING.md](https://github.com/entresol/silent-zero/blob/main/CONTRIBUTING.md)
- **Follow along** (available now): The changelog says what changed in substance, the wiki log what was worked in each day. [Changelog](https://github.com/entresol/silent-zero/blob/main/CHANGELOG.md)

Looking for the other door? [Users](https://silentzero.ooo/use/index.html.md)
