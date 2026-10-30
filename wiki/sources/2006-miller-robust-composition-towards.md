---
type: source
id: 2006-miller-robust-composition-towards
status: reviewed
read: partial
kind: design
sources: [2006-miller-robust-composition-towards]
updated: 2026-10-29
---

# Miller 2006: Robust Composition

Mark S. Miller. PhD thesis, Johns Hopkins University, 2006. [PDF](http://www.erights.org/talks/thesis/markm-thesis.pdf). The wiki has read the chapters on the approach (1 to 3), on access rights, the object-capability model and confinement (8, 9 and 11) and the summary of access control (12), most of the thesis's access-control part; chapter 10 on the loader, on which confinement relies, and the chapters on the E language, concurrency, distribution and related work are not read.

## What it shows

- **Excess authority is the gateway to abuse.** Conventional systems give every program the user's full authority; the Principle of Least Authority (POLA) says to grant each program only what its job needs, and to grant it "just-in-time, not excess authority just-in-case" (§3.1).
- **Designation decides how much authority is needed.** `cp foo.txt bar.txt` receives names and needs the user's whole file system to resolve them; `cat < foo.txt > bar.txt` receives two open files and needs nothing more. Systems that pass names are "name-centric", systems that pass references "key-centric"; least authority needs the latter (§3.2).
- **Permission is not authority.** Permission is what a program may invoke directly; authority is every effect it can cause, including through others who act for it. A program can gain authority through a proxy without any new permission. Analyses that look only at the graph of permissions miss this and have "proven" capability systems unable to do things they do (§8, Table 8.1).
- **The object-capability model.** A reference indivisibly combines designation, permission and the means of access. A program can come to hold a reference only by initial conditions, by creating the object, by being created with it, or by being handed it by someone who holds it: "only connectivity begets connectivity" (§9.1, §9.2).
- **Attenuation and revocation are programs.** A reference gives full, perpetual access. To restrict it, one interposes an *access abstraction*: Redell's caretaker forwards messages until its gate is disabled, which makes a grant revocable; a membrane wraps every reference passing through it, so revocation holds even if the target tries to hand out direct access (§9.3, Figures 9.2 and 9.3).
- **Confinement and one-way channels.** A customer can run untrusted code in an environment she controls, and can give two such programs a *data diode* that carries data in one direction and capabilities in neither. This answers the claim that capabilities cannot enforce the *-properties (§11.1, §11.2).
- **Revocation across machines fails unsafe.** Between machines, a lost message that would grant authority fails safe, but a lost message that would *revoke* authority fails unsafe. The remedy is a dead man's switch: the revocation gate disables itself when contact is lost for longer than a timeout (§11.5.3).
- **Limits without a shared platform.** The model assumes a platform all parties rely on. Between machines that do not, only cryptography is left, and it cannot stop one party from handing all its secrets, and so its identity, to another (§11.5).
- **Security from simple programs.** Security emerges from primitive protection plus "security-enforcing programs" that are often simple, so the required analysis "should frequently prove tractable, provided these programs are built on effective primitives" (§12).

## How

A thesis: a computational model, design rules, and their embodiment in the language E and a desktop built in it. The access-control part argues from the model and from patterns used in existing capability systems; it ignores covert and side channels by its own choice (§8.1, footnote 1).

## Limits

The thesis states that it deals only with overt causation and leaves covert and side channels aside (§8.1).

A careful reader adds:

- **Partial reading.** The concurrency and distribution chapters, which are half of the thesis's contribution, are not covered here.
- **Patterns, not proofs.** The caretaker and membrane are shown as code and argued about informally; the thesis cites later tool work (SCOLL) for bounds on authority (§12).

## Against the wiki

- [[1988-hardy-confused-deputy-or]]: **extends** it. The thesis generalises Hardy's remedy into the name-centric versus key-centric distinction.
- [[functional-correctness]], [[sel4]]: seL4's authority-confinement proof bounds the capabilities a component can come to hold at the kernel level ([[2018-klein-formally-verified-software]], §3.2). Our reading: in Miller's terms that bounds permission; authority that flows through programs acting for others is what a kernel proof alone does not cover.
- [[object-capabilities]]: created with this source.

## For zOS

- [[broker]]: the paper (Section 2.4) cites this thesis, with Dennis and Van Horn, for "authority must be passed explicitly, as capabilities". Confirmed. The paper's broker grants capabilities that are "attenuated, time-limited and revocable" (Section 3); the caretaker and membrane are the established patterns for exactly that.
- Our reading: the dead man's switch is the pattern for the paper's "revocation for actions under way" (Section 5): authority held outside zOS, such as an external credential, must lapse by itself when the broker cannot reach it. Miller's permission-authority distinction states the paper's sentence in Section 1 precisely: "the kernel will enforce every boundary correctly while" a broker grants the wrong authority. The kernel bounds permissions; the broker's behaviour bounds authority.
