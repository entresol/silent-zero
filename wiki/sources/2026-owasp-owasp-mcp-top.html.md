# the OWASP MCP Top 10

> A security vendor’s guide to the OWASP MCP Top 10 (version 0.1): ten risks, 30-plus CVEs in two months, figures without method. report, full text.

Source · Cycode 2026 · LLM reviewed · updated 2026-11-23 · https://silentzero.ooo/wiki/sources/2026-owasp-owasp-mcp-top.html

"OWASP MCP Top 10: Risks, CVEs & Defenses for 2026", a blog post by Cycode, a software-security company. [Post](https://cycode.com/blog/owasp-mcp-top-10/). The page carries no date of its own; its text speaks of January and February 2026, and its related posts run to October 2026. Read in full from a saved copy. It is a vendor's summary of an OWASP project, not the OWASP text, which the pool still lacks; its closing section and parts of the guidance promote Cycode's products.

## What it shows

- **The list.** The post calls the OWASP MCP Top 10 the first OWASP project on the Model Context Protocol and gives its ten risks as version 0.1 of 2025: token mismanagement and secret exposure; privilege escalation through scope creep; tool poisoning; supply-chain attacks; command injection; intent-flow subversion by prompt injection; insufficient authentication and authorization; lack of audit and telemetry; shadow MCP servers; context injection and over-sharing.
- **Figures it reports, with no method given.** More than 30 CVEs against MCP servers, clients and infrastructure in January and February 2026, of which 43 per cent were shell injection. A 78.3 per cent attack success rate with five MCP servers connected to one agent, attributed to Palo Alto Networks' Unit 42. Of 2,614 surveyed servers, 82 per cent exposed path traversal, 34 per cent command injection and 67 per cent code injection; the survey is not attributed. In Cycode's own 2026 report, 81 per cent of organisations lack full view of AI use in the software lifecycle.
- **Named incidents.** CVE-2025-6514 in mcp-remote, a command injection scored 9.6 in a package downloaded more than 437,000 times, found in July 2025. The first malicious MCP server in the wild, a backdoor that silently copied out its users' emails. A GitHub MCP attack in which a poisoned public issue and a broadly scoped personal access token let an agent pull private repository content into its context and expose it in a public pull request or comment.
- **Defences it recommends.** Short-lived scoped tokens and per-server audience validation; signed and pinned tools with an alert on description drift; sandboxed servers with outbound traffic denied by default; audit logs; an inventory of servers. For intent-flow subversion it calls human approval of sensitive actions "the most reliable defense".

## How

A guide that walks through the list one risk at a time, with a scenario, an incident or a CVE for most. It reports no experiment of its own.

## Limits

A careful reader adds:

- The post is secondary. Each figure is the vendor's, and the saved text shows no source for most of them, and none was checked here.
- The post's own description of the list as "first" and "2025" sits beside a headline for 2026; the OWASP original would show its status.
- The risks are mostly ordinary application-security flaws, as the post says itself ("classic web application vulnerabilities wearing new uniforms"). Our reading: the Unit 42 figure comes from a setting that the wiki's other MCP sources measure differently, so the numbers do not compare.

## Against the wiki

- [Model Context Protocol](https://silentzero.ooo/wiki/concepts/model-context-protocol.html.md): **extends**. Our reading: a practitioner's catalogue beside the preprints, with named CVEs and a supply-chain view that the preprints on the page do not give.
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md): **confirms** the picture of tool descriptions and retrieved text entering the context as instructions. It names human approval as the most reliable defence; the post gives no test of that.

## For Silent Zero

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md): the GitHub example is excessive access across a trust boundary, which the post says is "not just prompt injection". Our reading: this is the case a broker answers by granting no scope wider than the request, whatever the agent has read. The post names the missing piece as runtime policy enforcement; the control it lists is scopes that expire and are reviewed. Our reading: that is a convention, where the broker would issue each grant itself.
- Our reading: some of the post's controls (signing, sandboxing, deny-by-default egress) sit outside the agent, as the broker does; others, such as context isolation and human approval, work inside the agent's loop. None is described as enforced below a verified kernel.

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Model Context Protocol](https://silentzero.ooo/wiki/concepts/model-context-protocol.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
