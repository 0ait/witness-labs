<!--
title: R1-P1 derivation R1-D04
id: QL-20261121-01/R1-P1/D04
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: proposed by QUASAR; LATTICE review v1 (REQUIRES CORRECTION (moderate)) gives per-claim verdicts
internal-source: WitnessLab/06_QUASAR_RESEARCH/derivations/R1-D04_cluster_expansion_threshold.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# R1-D04: do OS78/Seiler-type polymer and cluster expansions accept Balaban's effective actions at the crossover? (LATTICE check 3)

QL-20261121-01 · QUASAR · Route 1 phase 1 · 2026-11-21. These are threshold comparisons. The general expansion criteria are cited at title level (texts not opened) and stated here in their standard form, labelled as such. The comparison arithmetic is exact (R1-E02).

## 1. What the expansions accept (standard form; label: Established in the literature, texts not opened [T])
- **High-temperature / Dobrushin-type criteria** (Gross 1979 S-134 [T], "Decay of correlations in classical lattice models at high temperature"):
  - For a Gibbs measure on a product of compact single-site spaces (here: coarse links with Haar a priori measure), with a possibly *infinite-range* interaction Φ = {Φ_X}, a smallness condition of the form Σ_{X∋0} (|X|−1)‖Φ_X‖_∞ e^{κ·diam X} < c_d gives uniqueness and exponential decay of correlations at a rate ~κ.
  - The criterion depends only on interaction norms, so it is **automatically uniform over any class** satisfying the norm bound. Non-locality is allowed provided the tails are summable with exponential weight.
- **Polymer expansions** (Kotecký–Preiss S-135 [T]): convergence if Σ_{Y≁X} |z(Y)| e^{a(Y)} ≤ a(X). For gauge theories (OS78 S-005, Seiler S-105 [T]), activities come from expanding e^{−S} − 1 around the Haar measure. For exponentially decaying non-local tails the criterion still applies, with polymer activities ≈ ‖Φ_X‖ — again uniform over a norm-bounded class.
- **Strong-coupling LGT thresholds actually proved:** SZZ S-106 [P in INV-001 (archived PDF); not re-read this session]: |β| < 1/(16(d−1)) in 't Hooft normalisation. Converted (R1-E02, normalisation assumption stated there), this is **g² > 48 for SU(2)** (Wilson β < 1/12) and g² > 32 for SU(3).

**Answer to the first half of check 3.** Yes: these methods accept non-local actions with exponentially decaying tails, uniformly in β, *provided* the whole interaction is small in a weighted norm, i.e. the a priori single-link measure is close to Haar and the effective plaquette coupling is ≲ the strong-coupling threshold. (Standard; [T])

## 2. What the RG supplies at the crossover (R1-D01 S3–S4; R1-E02)
At the last controlled scale k_*−1 the effective coupling is ≈ γ (within 0.7% for γ=0.1). The density is of Balaban form: (1/g²)Σ Re Tr(1−V_p) plus small corrections, small-field dominated, with large fields suppressed. So:
- the effective Wilson-type coefficient is β_eff ≈ 2N/γ, e.g. **≈ 40 for SU(2), γ=0.1** (and larger for smaller γ);
- the single-link marginals are concentrated near the identity, which is the *opposite* of a near-Haar measure.

## 3. The mismatch (Proved here, arithmetic; label of the inputs as above)
| | Strong-coupling expansion needs | RG gives at its exit scale |
|---|---|---|
| plaquette coupling (SU(2), Wilson β) | β_eff < 1/12 ≈ 0.083 (g² > 48) | β_eff ≈ 2N/γ = 40 (γ=0.1), 80 (γ=0.05) |
| ratio | — | **≈ 480× (γ=0.1)**, ≈ 960× (γ=0.05) in β; equivalently in g² |
| single-link law | ≈ Haar | concentrated near 1 at scale ~γ^{1/2} |
| model-flow steps to close the gap | — | undefined: the perturbative flow hits its pole first (152 steps from γ=0.1 to the pole, SU(2), 2-loop) |

**Conclusion (check 3).** The threshold at which polymer/cluster expansions accept non-local effective actions (interaction norm O(10⁻²) per plaquette, β_eff ≲ 0.08 for SU(2)) is **not met** by anything Balaban's RG can output. The RG output at its exit scale is a weak-coupling object, β_eff ≈ 2N/γ ≫ 1. Between them lies the crossover window. There, neither expansion has a small parameter, and by the U(1) filter (R1-D01 Lemma A) no abelian-blind argument can work. The plan "Balaban to the crossover, then an off-the-shelf strong-coupling cluster expansion" is therefore a **failed approach in its literal form** (logged as `11_FAILED_APPROACHES/failed_proofs/R1-FP01_*`). R1 survives only as the reformulation R1-D03 Prop. 2 (H-Gap at coupling γ), which is a different, harder statement than strong-coupling clustering.

**Not settled here.** Whether a *weak-coupling* cluster expansion around a non-trivial minimum could handle the coarse measure, Balaban-style but in infinite volume with a mass, is not settled. For U(1) such an expansion must produce a massless result. So again only a non-abelian mechanism could produce a gap, and none is known. (Heuristic)
