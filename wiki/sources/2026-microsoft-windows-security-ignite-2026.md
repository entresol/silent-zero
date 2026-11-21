---
type: source
id: 2026-microsoft-windows-security-ignite-2026
status: reviewed
read: full
kind: report
sources: [2026-microsoft-windows-security-ignite-2026]
updated: 2026-11-21
---

# Microsoft 2026: Windows security at Ignite

Dana Huang (Microsoft). "Windows security at Ignite 2026: Start secure, protect what matters, prepare for AI", Windows Experience Blog, 17 November 2026. [Page](https://blogs.windows.com/windowsexperience/2026/11/17/windows-security-at-ignite-2026-start-secure-protect-what-matters-prepare-for-ai/). Read in full; only its section on agents bears on the wiki. A vendor announcement.

## What it shows

- **The direction for agents.** Windows "is building that foundation through agent identity, containment, isolation, policy, observability, and governance". The post says Microsoft Execution Containers, "announced last month", "provide governed boundaries for agent execution", helping organisations "contain agent activity and maintain control over access to resources and tools".
- **The framing.** Agentic security "isn't just about securing the agents themselves", it is about "giving users the ability to trust and control the agents running on their devices"; people need confidence that "agents act only in ways they have authorized".
- **The rest of the post** covers the Windows endpoint security platform (generally available, to reduce reliance on kernel drivers), a baseline protection in preview, post-quantum TLS, passwordless sign-in and management features. None of it concerns agents.

## How

An announcement post with links to further posts, which were not read.

## Limits

It adds no technical detail on containment and refers back to the earlier announcement in general terms ([[2026-microsoft-execution-containers-policy-driven]]).

## Against the wiki

- [[agent-operating-systems]]: **confirms** the direction of platform vendors ([[mxc]]); it adds no new design.

## For zOS

Our reading: little beyond dating the claim; on 17 November 2026 the vendor presents agent containment as one part of a broader identity and management story. See [[mxc]].
