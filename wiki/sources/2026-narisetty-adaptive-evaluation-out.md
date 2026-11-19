---
type: source
id: 2026-narisetty-adaptive-evaluation-out
status: reviewed
read: full
kind: test
sources: [2026-narisetty-adaptive-evaluation-out]
updated: 2026-11-05
---

# Narisetty et al. 2026: adaptive evaluation of out-of-band defenses

Praneeth Narisetty, Shiva Nagendra Babu Kore, Uday Kumar Reddy Kattamanchi and Jayaram Kumarapu (LaunchSafe Research). "Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents". [arXiv:2606.26479](https://arxiv.org/abs/2606.26479), version 1 of 25 June 2026. A preprint that calls its results preliminary and not peer-reviewed. Read in full.

## What it shows

- **A systematization.** Defences that enforce outside the model (CaMeL, FIDES, Progent, RTBAS, Conseca, FORGE) are read as reference monitors, integrity labels and least privilege, and compared on eight dimensions: primitive, whether the gate is deterministic, where the monitor sits, integrity and confidentiality coverage, implicit flows, reported cost and whether it fits an unmodified agent (§5, §6, Table 2). The authors say the lens is not new.
- **The gap.** Most of these defences report their headline security on a fixed benchmark, mostly AgentDojo; Progent's authors did analyse adaptive attacks on their own policy updater, which §11 repeats. Twelve in-band defences looked strong the same way until adaptive attacks broke them ([[2026-nasr-attacker-moves-second]]), and the out-of-band ones have not had that test across the board (§7).
- **Weak spots that remain even if the defences hold.** The authors name four. Provenance labels are the trusted base and are under-specified in every system surveyed. Tasks that must act on untrusted content need a person's endorsement, which an attacker can target and which breeds approval fatigue. Text-only harms go through, and side channels remain (§8).
- **A protocol.** What an adaptive evaluation of such a defence needs: an attacker who knows the policy, string optimization against the monitor, provenance spoofing, endorsement-targeting and side-channel probes, with attack success, utility, endorsement rate and overhead as metrics (§10).
- **One run of it.** Against Progent, on AgentDojo with a self-hosted Qwen2.5-7B agent, three runs, the first 8 user tasks per suite across banking, slack and workspace. Mean attack success fell from 25.8 % to 4.2 % with the defence, and was 2.6 % under the authors' hand-made adaptive attack (§11.2, Table 3). Mean task utility under attack fell from 45.2 % to 27.1 % with the defence, and the defended runs needed about fifteen times more model calls (§11.3, Table 4).

## How

AgentDojo's standard "important instructions" attack, against Progent with default settings, and an adaptive variant that disguises the malicious action as a benign, pre-authorized step to fool Progent's model-based policy updater. The policy model was the same 7B model; Progent's authors used GPT-4o (§11.1, §12).

## Limits

What the authors say. The test covers one defence, one weak open model and one attack template, with no white-box optimized attack and none confined to authorized tools. The travel suite was left out because its agent loops ran too long. The result "bounds these attacks, not all attacks"; it fits the idea that deterministic enforcement is a harder target than detection and does not establish it (§11.5, §12, abstract).

A careful reader adds:

- **The adaptive attack may be weak.** The authors suggest the disguise softened the instruction aimed at the agent and so lowered its compliance; the authors say the low number may reflect a weak attack as much as a strong defence (§11.3).
- **A reproduction of a setting.** It follows the setting of Progent's own adaptive analysis on a different model, with a small subsample; it does not reproduce Progent's figures; the authors say their 2 to 4 per cent lands in the band Progent's authors report for their own adaptive attacks, 0.5 to 4.2 per cent (§11.3).
- **Workspace says nothing.** Its attack success is zero even without the defence, so the comparison rests on banking and slack (§11.4).
- **Interest.** The authors state that the work guides their company's agent-security tooling (§14).

## Against the wiki

- [[prompt-injection]]: adds the first adaptive test in the wiki of a defence around the model, and a statement of what is still untested. It did not test CaMeL or FIDES.
- [[broker]]: no change of state. The paper states the premise the broker rests on (the gate must not be a model) and says it has not been shown to survive an adaptive attacker. Our reading: its list of weak spots matches the broker's open questions on provenance, endorsement and implicit flows.
- [[information-flow-control]]: names provenance assignment as the trusted base of every labelling scheme.

## For zOS

The paper does not cite this source. It bears on [[broker]] (state *tested* aimed for, *proven* as the target): a deterministic gate that holds against a hand-made adaptive attack on a weak model is a small data point, not evidence of the kind the broker's table calls for.
