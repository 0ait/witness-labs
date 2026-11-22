<!--
title: Route 1 phase 1 (R1-P1): the 4D U(1) go/no-go filter — index
id: QL-20261121-01/07/README
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.2.0 (part 1, QUASAR; release pending)
status: published (QUASAR part of v0.2.0); v1 as reviewed
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# 07 — Route 1 phase 1 (R1-P1): RG to the crossover, tested against 4D U(1)

**Authorized by the principal** 2026-11-21 18:56 CT ("begin route 1"); work 18:57–19:20 CT; submitted to LATTICE 19:21 CT; publication of this batch approved 19:45 CT. **No mass gap is claimed. The Yang–Mills problem remains open.**

## What this phase did
Route 1 proposes: Balaban's renormalization group carries the lattice theory from weak bare coupling up to a crossover scale where the running coupling reaches a fixed γ, after which strong-coupling (cluster-expansion-type) methods would prove clustering. Phase 1 wrote the route as ten steps S0–S9 and asked, step by step, whether each would also "work" for 4D U(1), which is known to lose its mass gap at weak coupling (go/no-go filter). It then ran three checks: Balaban's bounds and their volume dependence; whether block averaging respects reflection positivity; whether cluster expansions reach the coupling the RG delivers.

## Outcome (QUASAR v1)
- **Filter: GO, with qualification.** Two steps fail for U(1): S4 (crossover attainment; no asymptotic freedom, as expected) and S6 (strong-coupling clustering at the crossover, which needs a non-perturbative input that U(1) lacks; conditional on hypothesis (M)).
- Balaban's bounds stop just before the crossover and are proved on finite periodic lattices only (R1-H01).
- Block maps and time reflection: R1-D02, R1-E03.
- Cluster-expansion threshold versus the RG exit: a large gap remains (R1-D04, R1-FP01).
- **Net:** Route 1 reduces to one open question, H-Gap (uniform clustering of effective actions in a fixed weak-coupling class), at least as hard as the open fixed-β lattice gap.

## Independent review: LATTICE verdict **REQUIRES CORRECTION (moderate)**
LATTICE's review v1 (published separately by LATTICE in `../05-lattice-independent-review/`) found nine defects. The route was not killed; the main reductions stand under stated conditions.

| Defect | Summary | Type |
|---|---|---|
| D-R1P1-1 | "Corner block map fails θ" overgeneralizes one (space-first) contour family; time-first contours or the centre map intertwine θ exactly on gauge-invariant data (LATTICE CE-005) | Scope of R1-D02 Prop. 4 |
| D-R1P1-2 | Hypothesis (M) is block-map dependent and concerns coarse observables; not established (UNRESOLVED) | Conditional S6 verdict |
| D-R1P1-3 | Driver 1987 does not support masslessness (it holds at arbitrary coupling) | Citation |
| D-R1P1-4 | "β_eff ≈ 40, ≈480×": 2× normalization ambiguity (240× vs 480×), lower bound growing like 1/γ; SZZ is a Bakry–Émery threshold | Numbers / naming |
| D-R1P1-5 | Guth's g² < 0.168 is a deconfinement bound, not a masslessness interval | Wording |
| D-R1P1-6 | E01 measured plaquettes and Creutz ratios, not masslessness | Wording |
| D-R1P1-7 | E01 error bars underestimated in/near the Coulomb phase (τ_int ≈ 72 sweeps at β=1.00) | E01 errors |
| D-R1P1-8 | S4 rests on Balaban's coupling-sequence theorem, stated as unpublished in 1989 | S4 status |
| D-R1P1-9 | "H-Gap ≥ fixed-β gap" holds in one direction only; a membership-free reduction exists | Wording |

**The files below are v1, published as reviewed, unchanged in technical content.** A corrected **v2 will be published later as an addendum**; nothing here will be deleted or overwritten (see [`/VERSIONING.md`](../../../VERSIONING.md)).

## Files
| Path | Contents |
|---|---|
| [`R1-P1_report.md`](R1-P1_report.md) | Phase report: skeleton, U(1) filter, checks 1–4, experiments, next steps |
| [`derivations/`](derivations/) | R1-D01 (skeleton and U(1) filter), R1-D02 (block maps and reflection), R1-D03 (X vs ME1; fixed-coupling reduction), R1-D04 (cluster-expansion threshold) |
| [`experiments/`](experiments/) | R1-E01 (4D U(1) vs SU(2) Monte Carlo, numerical evidence only), R1-E02 (running-coupling bookkeeping), R1-E03 (block map vs θ): code, `ENV.txt`, `RUN.md` with "How to reproduce", outputs with sha256 |
| [`hypotheses/`](hypotheses/) | R1-H01–H03 |
| [`proof-attempts/`](proof-attempts/) | R1-PA01 (abelian obstruction lemma) |
| [`failed-approaches/`](failed-approaches/) | R1-FP01 (failed proof), R1-FE01 (degenerate experiment), R1-LL01 (lessons learned) |
| [`submission-packet-R1-P1-v1.md`](submission-packet-R1-P1-v1.md) | The packet as submitted to LATTICE |
| [`sources_S-129_S-135.csv`](sources_S-129_S-135.csv) | New sources S-129…S-135: URLs/DOIs only (no third-party PDFs; `local_path` replaced by `internal_archive_copy`) |

Experiment metadata: [`/experiments/REGISTRY.md`](../../../experiments/REGISTRY.md). Redactions: [`/REDACTIONS.md`](../../../REDACTIONS.md) (in this section only the principal's former role title was changed, plus the source-register column).

## Next steps (all gated by the principal)
- (B) pin down Balaban's effective-action class from accessible texts; (C) a numerical SU(2)-vs-U(1) discriminator at equal weak coupling — **not started**.
- R1-P1 v2 corrections — **not started**, not yet authorized.

```
Witness Labs
Agentic Swarm
0ait
```

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
