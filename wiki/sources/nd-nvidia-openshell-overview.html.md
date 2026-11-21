# NVIDIA: Overview of OpenShell

> OpenShell’s four protection layers and the mechanisms behind them; no assurance claim. report, full text.

Source · LLM reviewed · updated 2026-11-21 · https://silentzero.ooo/wiki/sources/nd-nvidia-openshell-overview.html

NVIDIA. "Overview of OpenShell", a page of the OpenShell documentation, version v0.1.9 ("Latest"), undated, read on 21 November 2026. [Page](https://docs.nvidia.com/openshell/latest/about/overview). Read in full; it is short. A vendor's documentation.

## What it shows

- **What OpenShell is.** "An open-source runtime for executing fleets of autonomous AI agents in sandboxed environments with kernel-level isolation". It combines "sandbox runtime controls and a declarative YAML policy" so that agents run "without giving them unrestricted access to local files, credentials, and external networks".
- **Four protection layers.** Filesystem (reads and writes outside allowed paths are prevented; locked when the sandbox is created), network (unauthorised outbound connections are blocked; the policy can be reloaded at run time), process (privilege escalation and dangerous system calls are blocked; locked at creation) and provider credentials. For the last, the page says OpenShell "resolves opaque credential placeholders only at profile-authorized endpoints"; attachment, rotation and revocation of credentials take effect at run time, while a new environment variable needs a new process.
- **The mechanisms named.** Landlock for filesystem confinement, seccomp and an unprivileged process identity against privilege escalation, network policies that allow "only approved destinations; other outbound traffic is denied", and provider profiles that "restrict model traffic to approved endpoints and binaries".
- **Uses.** Running Claude Code, OpenCode, Codex or GitHub Copilot CLI "with constrained file and network access", and treating the policy file as "version-controlled security controls that can be reviewed and audited".

## How

A documentation overview: a table of four threats (exfiltration, credential theft, unauthorised API use, privilege escalation) with the control against each, a table of the layers, and links to pages on the architecture, the sandbox policies and the default policy, which were not read.

## Limits

The page describes mechanisms and makes no claim of assurance: no proof, test, audit or measurement is named, and it says OpenShell "mitigates" the failure modes; its "audit" use case concerns reviewing the policy file. It does not say what the policy grants are bound to beyond endpoints and binaries, and it does not mention the licence. It says nothing about the Linux kernel's own flaws or about timing.

## Against the wiki

- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md): **extends** with a runtime that uses the module for filesystem confinement beside seccomp ([OpenShell](https://silentzero.ooo/wiki/systems/openshell.html.md)).
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md): **extends** with a sandbox for agents that rests on a conventional Linux kernel and a policy engine.
- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): **extends** with default-deny outbound traffic and credential placeholders, which the wiki's table on what exists did not have. Our reading: the grants named on this page are by endpoint and binary and not by task, recipient or data.

## For Silent Zero

The paper's Section 6 says the hardened-Linux alternative leaves out the authority an agent holds over credentials and over what it sends out. Our reading: this page shows a Linux runtime that limits both by policy, so the clause is narrower than written; it does not show a grant that is bound to recipients, data and parameters of each call, which the paper asks of the broker. The paper does not name OpenShell. See [OpenShell](https://silentzero.ooo/wiki/systems/openshell.html.md), [Microsoft Execution Containers (MXC)](https://silentzero.ooo/wiki/systems/mxc.html.md).

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Agent operating systems](https://silentzero.ooo/wiki/concepts/agent-operating-systems.html.md)
- [Landlock](https://silentzero.ooo/wiki/systems/landlock.html.md)
- [Microsoft Execution Containers (MXC)](https://silentzero.ooo/wiki/systems/mxc.html.md)
- [OpenShell](https://silentzero.ooo/wiki/systems/openshell.html.md)
