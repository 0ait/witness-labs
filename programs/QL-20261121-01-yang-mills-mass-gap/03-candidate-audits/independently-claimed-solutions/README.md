<!--
title: Independently claimed solution record: README
id: QL-20261121-01/T5/README
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: first-pass register entry
internal-source: WitnessLab/04_CANDIDATE_SOLUTIONS/independently_claimed_solutions/README.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Independently claimed solutions: first-pass register (Task 5, QL-20261121-01)

Scope: a bounded search (6 Tavily searches) for public claims of a *complete* solution, plus direct fetches. All verdicts are first-pass only. None of these is a proof, and this lab endorses none. Deeper items are marked PENDING.

| Slug | Claimant | Venue / date | Claims | Cond./Uncond. | First-pass verdict | Decisive defect |
|---|---|---|---|---|---|---|
| nye-2025-ijt-quantum-information | L. Nye (CMU) | Int. J. Topology, 2025-02-25, DOI 10.3390/ijt2010002 | Existence + gap, all G | Uncond. (self-described) | DEFECTIVE; §6 PENDING | Problem misstated (adds an exclusion); uniform-in-a decay with m>0 (eq. 36) asserted without proof, i.e. the bridge is assumed |
| jacobsen-2025-arxiv-2506.00284 | D. C. Jacobsen | arXiv, 2025-05-30; **withdrawn** 2025-06-13 | Existence + gap, SU(3) only | Uncond. | DEFECTIVE (scope); text PENDING | SU(3) only; convergent polymer expansion claimed uniform as a→0; arXiv admin withdrawal |
| umpolungfish-yang-mills-lean4 | GitHub "umpolungfish" | GitHub @97b840d, 2026-11-21 | Existence + gap, SU(N), "formally verified" | "Unconditional" | FALSE completeness claim | 21 `sorry`s supply the canonical OS/Wightman structures for `clay_yang_mills_strict`; proofs cover strong coupling only |
| croft-adams-medium-2026 | Croft Adams | Medium, 2026-02-20 | Gap, SU(3) | Uncond. | NOT A QFT STATEMENT | Classical energy functional; false by scaling E(tF)=t²E(F) |
| portela-moura-filho-academia | J. H. Portela Moura Filho | Academia.edu (3 pp) | Gap | Uncond. | INSUFFICIENT; PENDING | No construction; 3 pages, 3 refs; full text not opened |
| wilson-ssrn-4819820 | J. Wilson (unverified) | SSRN | unknown | unknown | INACCESSIBLE | 403 / timeout |

## Explicitly NOT complete-solution claims (recorded to prevent misclassification)
- **OpenAI 2026 construction** (yang-mills-group): existence as a scaling limit for all simple compact G. The assessment says it does **not** prove uniqueness or a mass gap. Audited in `candidate_audit_reports/openai_2026_existence_audit.md`.
- **Alpöge–Sussman** (submitted 2026-11-15 per the committee listing, "work in progress"): secondary sources say existence, not the gap. Primary text not opened. PENDING.
- **Eriksson Programme** (lluiseriksson/THE-ERIKSSON-PROGRAMME): the README says verbatim "No four-dimensional continuum mass gap is claimed." Its Balaban UV bound is a carried hypothesis.
- **Nissim, arXiv:2510.22788**: mass gap for U(N) **lattice** YM in the 't Hooft regime. Lattice only; not a Clay claim.

## Common failure pattern
Every complete-solution claim reviewed either:
- (a) asserts the uniform continuum and infinite-volume decay rate (PO-12/PO-13) without proof;
- (b) proves it only at strong coupling; or
- (c) never builds a quantum theory at all.

This matches the lab's first investigation target, the finite-lattice → continuum gap bridge.
