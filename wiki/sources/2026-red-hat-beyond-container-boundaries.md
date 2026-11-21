---
type: source
id: 2026-red-hat-beyond-container-boundaries
status: reviewed
read: full
kind: report
sources: [2026-red-hat-beyond-container-boundaries]
updated: 2026-11-21
---

# Red Hat 2026: Kernel-level agent security in OpenShift AI 3.5

Mike Hepburn, Roberto Carratalá and Adel Zaalouk (Red Hat). "Beyond container boundaries: Kernel-level agent security in Red Hat OpenShift AI 3.5", blog post, 8 September 2026. [Page](https://www.redhat.com/en/blog/beyond-container-boundaries-kernel-level-agent-security-red-hat-openshift-ai-35). Read in full. A vendor's product post.

## What it shows

- **What ships.** Red Hat OpenShift AI 3.5 "ships OpenShell agent sandboxing as a Developer Preview", called "the 1st step" toward making kernel-enforced boundaries a standard feature of the platform.
- **Where OpenShell comes from.** "An open source industry collaboration backed by NVIDIA, Red Hat, Docker, GitHub, SAP, Google, and Dell", "vendor-neutral at the sandbox layer by design".
- **Mechanisms.** Three kernel layers (Landlock for the filesystem, seccomp for system calls, network namespaces), and an Open Policy Agent engine that decides at the TCP level (destination address and port) and at the HTTP level (URL path, method and headers). The post's example allows `GET /api/v1/public` and blocks `DELETE` on the same host. Policies are declarative YAML in version control, reloadable without a restart; "central IT sets a floor, teams extend within it". Every connection, file access, system call and HTTP request emits a structured event in the OCSF v1.7 format.
- **Default.** "Every sandbox starts with no outbound access." A denied call gets a structured 403 reply that names the host, port and binary and says what a valid proposal looks like.
- **Policy advisor.** The agent can submit an "addRule" proposal; a developer approves or rejects it from outside the sandbox, and a rejection reason goes back to the agent. For "low-risk expansions", an auto-approval mode "runs a formal prover" with four checks (reach to link-local or cloud-metadata addresses, an uninspectable protocol gaining reach to a credentialed host, a binary gaining credentialed reach to a new destination, a new HTTP method on an already credentialed target); if all four pass and no security note arises, the policy reloads by itself, and the event is logged as auto-approved. The post's words: "The governance machinery doesn't trust the model's judgment about whether its own access expansion is safe."
- **Credentials.** A requirement the post lists is to inject credentials "without exposing them to the agent's execution context". In its example the agent's key is set to "unused" and its base URL is `https://inference.local`; the post says the walkthroughs in its guides route inference traffic "without exposing credentials to the sandbox".
- **The rest of the stack.** NeMo Guardrails for content rules, Garak for red-team tests, signed base images and agent harness images for Codex, Goose, OpenClaw, OpenCode and Pi. "No single control is sufficient."
- **What comes next.** An operator, "SPIFFE-based agent identity", declarative deployment and deeper observability, with feedback shaping a Tech Preview in OpenShift AI 3.6.

## How

A product blog post with an example install (Helm, OpenShift 4.21 or later, command line version 0.0.85) and a sample of the event stream. It reports no measurement or evaluation.

## Limits

A vendor post for a Developer Preview. The claim that controls at the kernel layer "cannot" be bypassed is an assertion; the post does not discuss flaws in the Linux kernel itself. The "formal prover" is only named: the post lists four checks and does not say against which model they are proved or with what guarantee. It lists red-team testing with Garak as a layer and gives no results, and none against an adaptive attacker. The statistics in its opening and the later references to the EU AI Act and to IDC are the authors' and were not checked.

## Against the wiki

- [[agent-operating-systems]]: **extends** with a Linux sandbox that treats the agent as untrusted and keeps the check outside the model ([[openshell]]).
- [[broker]]: **extends**. Default-deny outbound traffic and, in the post's example, an agent that never holds the real key are in the broker's job; the policy advisor goes the other way from the paper, since the agent words the proposal and a person reviews it.
- [[landlock]]: **extends** (a use of the module).

## For zOS

Our reading: this is the closest product to the broker's flow of asking and granting, on Linux and without a verified kernel. Its grants name endpoints, binaries, methods and paths; the post does not say they are bound to a task or to the data of a call. The paper wants the broker to word every request a human sees, "so the agent never does"; here the agent drafts the request. For the question of refusals that leak, compare [[2026-chinaei-causality-laundering-denial]]: the 403 reply tells the agent what is missing. See [[openshell]].
