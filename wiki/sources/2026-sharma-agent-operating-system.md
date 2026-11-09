---
type: source
id: 2026-sharma-agent-operating-system
status: drafted
read: partial
kind: design
sources: [2026-sharma-agent-operating-system]
updated: 2026-11-09
---

# Sharma and Shah 2026: the AOS reference architecture

Ankur Sharma and Deep Shah. "The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems". [arXiv:2608.03214](https://arxiv.org/abs/2608.03214), version 1 of 4 August 2026; the document calls itself AOS-0001, Draft v0.8, in an "AOS Specification Series". It extends the authors' earlier paper [[2026-sharma-agent-operating-systems]]. Read in part: abstract, executive summary, problem statement, contributions, the delegation and scheduling parts of the mathematical model, the limitations and validation sections, section 16.8 and the table of contents. The long chapters on interfaces, deployment, reliability, the appendices and the reference list were searched for key terms only, and this page makes no claim about them. For that reason the page stays `drafted`.

## What it shows

- **The claim.** Current agent stacks are "execution-centric": frameworks, model servers, protocols and observability tools exist, but no implementation-independent operating architecture governs intent, authority and audit across them (abstract, §3.2). The paper proposes two logical planes: a Control and Governance Plane (intent, policy, trust, authority, confidence, audit, human oversight) and a Runtime and Coordination Plane (agent lifecycle, workflow, model and tool routing, memory, scheduling, assurance). Linux or Windows, container runtimes and hardware stay outside the boundary (abstract, §2).
- **Capabilities in a different sense.** A consumer asks for a named capability such as a case summary; the control plane first drops providers that break hard constraints (authorisation, data residency, minimum trust) and then ranks the rest (§2). Our reading: these are service names, not the unforgeable references of [[object-capabilities]].
- **Delegation.** A child delegation may not exceed its parent's permissions, scope, budget or validity interval, and the paper states this as four inequalities (§12.6). Revocation "may not be instantaneous" for a disconnected asynchronous task, so a delegation record carries an expiry and a maximum tolerated propagation delay (§12.6).
- **Enforcement below the plane.** Approved authority may be translated into process, filesystem, network, namespace, cgroup or syscall constraints; the paper names Linux cgroup v2 and seccomp as "enforcement substrates", not as the semantic control plane (§2).
- **Verification is future work.** Some invariants (non-expanding delegation, no execution without authorisation, revocation safety) "can be expressed" in TLA+ or temporal logic; the paper lists them as candidate properties, and none was checked in the parts read. Formal methods will not verify model reasoning but can check the deterministic boundary around it (§16.8).

## How

A reference architecture and research proposal. It defines objects, invariants, a mathematical model for feasibility, ranking, confidence, delegation and latency, deployment profiles and conformance profiles. It states that it does not claim benchmark superiority and that its quantitative examples are illustrations (§3.5). A reference implementation, aos-core, is described as evolving; it "validates selected architectural concepts but does not define the architecture" (document control); the nine follow-on specifications are planned and unpublished (§2, document control).

## Limits

What the authors say themselves: no large-scale empirical evaluation; the invariants depend on declared side effects of capabilities, so undeclared side effects fall to runtime assurance and lower-level enforcement, and high-assurance profiles should not rely on declaration alone; confidence aggregation is under-specified; federated policy conflicts and revocation consistency are open (§15.10).

A careful reader adds: the paper offers no proof and no measurement, and its enforcement relies on the host operating system, whose isolation it takes as given. In the parts read it names no actuator and no real-time deadline; "safety-critical" and "deadline" appear as scheduling classes borrowed from real-time practice (§12.9).

## Against the wiki

- [[2026-sharma-agent-operating-systems]]: extends it from an argument about agent control planes to a layered reference architecture, by the same authors; the two do not contradict each other.
- [[broker]]: same job, a different place. The monotone delegation inequalities and the admitted revocation delay are a more formal statement of attenuation than the broker page quotes from other sources. The paper's TLA+ remark is a proposal for future work, not a result.
- [[object-capabilities]]: see the reading above; our reading is that the authority model is policy over named services, with delegation grants carrying lineage and scope; the parts on delegation objects were not read in full.
- [[agentos]], [[2026-zou-agentkernel-trust-native]]: further agent-OS designs; this one sits above Linux or Windows and has no kernel of its own (§5.4, not read in full).

## For zOS

It bears on the *broker* page as one more design of the authority layer, with a clear statement of delegation attenuation and no proofs. It changes the state of no `design/` page. The paper (Section 5) does not cite it; whether to cite it is for the team.
