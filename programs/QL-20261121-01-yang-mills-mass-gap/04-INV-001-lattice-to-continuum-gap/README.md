<!--
title: INV-001 — introduction for newcomers
id: QL-20261121-01/INV-001/README
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# INV-001 — From a lattice spectral gap to a continuum mass gap

**Question.** *What exactly is the bridge from a finite-lattice spectral gap to a uniform, strictly positive mass gap in the continuum, infinite-volume theory?*

## Why it matters
Lattice Yang–Mills theory is well defined, and a gap can be proved on the lattice in some regimes. The Clay problem asks about the continuum theory in infinite volume. Every route to a mass gap through the lattice has to cross this bridge, and most published "solutions" fail exactly here: they assume the crucial uniform estimate rather than prove it (see `../03-candidate-audits/`). Knowing precisely what must be proved, and what cannot work, tells future attempts where to aim.

## What was proved (QUASAR's proofs; checked by hand by LATTICE, none machine-checked)
- **The bridge itself is easy and standard (D01, D02).** If a family of gauge-invariant observables is rich enough to generate all states (cyclic) and all of its correlations decay in Euclidean time at **one common physical rate** Δ, then the Hamiltonian has no spectrum in (0, Δ) and the vacuum is unique. Conversely, a gap gives such decay (the converse also needs a unique vacuum, per LATTICE). On the lattice, contractible-loop observables decay at the lattice gap rate, and that bound passes to the limit if the gap scales correctly.
- **Why the obvious shortcuts fail (D03–D06, exact counterexamples).** A finite-box gap can close as the box grows (D04, E03). A free field has a positive lattice gap at every spacing yet none in the continuum (D05). One fast-decaying observable says nothing about the full gap (D06). If the lattice gap shrinks *slower* than the spacing, the continuum limit is trivial (D03), so a non-trivial limit must sit in the window Δ·a ≤ m_lat ≤ C·a. The spacing cannot be fixed using the gap itself (circular).
- **2D is exactly solvable (D07, E01).** Continuum string tension 1.5/β for SU(2), two methods agreeing to 50 digits; in 2D the local sector is trivial.
- **A conditional reduction (D08).** If the block-spin effective measure at a fixed physical scale clusters at a coupling-independent rate (hypothesis X), the uniform estimate ME1 follows.

## What was not proved
The open content is isolated in precise **missing estimates** (report §5):
- **ME1** — a uniform lower bound m^loc(β,L) ≥ Δ·a(β) at all weak couplings and large boxes. *Open.*
- **ME2** — convergence of the correlation functions to a unique, non-free limit with the OS properties and the right field content. *Open.*
- **ME2′** — a gap statement relative to the 2026 OpenAI construction: upgrade its polynomial bound M·s⁻² to exponential M·e^{−Δs}. *To be split (v2) into a "min" version, one selected phase, enough for Clay, and a "strong" version, all phases with one Δ.*
- **ME3, ME-R1, ME-R2** — upper window; crossover clustering; a β-uniform functional inequality.

No current tool reaches ME1/ME2 in 4D: strong-coupling results stop before the continuum region and work in lattice units; Balaban's RG works only while the coupling is small; finite-group results give gaps that grow with β (pointing to trivial limits); and any method that also works for 4D U(1) must fail, since that theory has a massless phase.

## LATTICE's verdict: REQUIRES CORRECTION (minor)
Full review: [`../05-lattice-independent-review/adversarial_reviews/QL-20261121-01-INV001-review_v1.md`](../05-lattice-independent-review/adversarial_reviews/QL-20261121-01-INV001-review_v1.md). The core reductions hold with conditions; there is no 4D gap content, as the report itself says. The ten defects, summarized:

| # | Defect | Effect |
|---|---|---|
| 1 | Sharp-time (t=0) observables of dimension 4 have divergent equal-time variance; restate the bridge with observables supported at strictly positive time | Scope (the bridge as written may not apply to the Jaffe–Witten fields) |
| 2 | Continuity at t=0 is unnecessary; injectivity of e^{−tH/2} suffices | Strengthening |
| 3 | ME3 is necessary only given ME2 (a unique limit) | Label |
| 4 | Split ME2′ into "min" and "strong"; specify the cyclic family | Target |
| 5 | Bound (B) does not follow from OS positivity alone; use sub-exponential growth | Wording |
| 6 | "Poincaré/LSI ⇒ decay" for non-local block measures is unproved; ME-R2 ⇒ ME-R1 is a hypothesis | Label |
| 7 | Precision fixes in hypothesis (X) (conjugation, positivity source, offsets, reflection alignment) | Wording |
| 8 | PO-11/PO-12 should ask for the local or pure-phase gap, not the full gauge-invariant sector (torelons) | Formalization |
| 9 | Two β conventions (1/g₀² and 2N/g₀²) must be unified | Convention |
| 10 | E01's Δ ≈ σℓ is an identity of the chosen trajectory, not a test | Label |

**Corrections are pending in v2, which has not been authorized yet.** The v1 files here are published as they were reviewed.

## Files
| Path | Contents |
|---|---|
| [`INV-001_report.md`](INV-001_report.md) | Main report: bridge theorem, proved items, experiments, literature, missing estimates, routes R1–R5, integrity notes |
| [`INV-001_formulation.md`](INV-001_formulation.md) · [`INV-001_ws04_pointer.md`](INV-001_ws04_pointer.md) | Lattice objects, limits and their order; infinite-volume pointer |
| [`derivations/`](derivations/) | D01–D08 |
| [`experiments/`](experiments/) | E01–E04: code, `ENV.txt`, `RUN.md` (with "How to reproduce"), outputs with sha256, failed runs |
| [`hypotheses/`](hypotheses/) | H01–H03 |
| [`failed-approaches/`](failed-approaches/) | FP01–FP02 (refuted proof strategies), CF01–CF02 (computational failures) |
| [`submission-packet-A-I-v1.md`](submission-packet-A-I-v1.md) | The A–I packet as submitted to LATTICE |

Literature baseline: [`../02-literature/INV-001_literature.md`](../02-literature/INV-001_literature.md). Experiment metadata: [`/experiments/REGISTRY.md`](../../../experiments/REGISTRY.md).

## Next steps (all gated by the Commander)
1. INV-001 v2 fixing the defects (wording and restatement; no new research); LATTICE re-verifies.
2. Lean formalization of the shared measure lemma behind D01/D08.1.
3. Only with explicit authorization: Route R1 (RG to the crossover + strong-coupling clustering), with a 4D U(1) go/no-go filter, before R2.

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
