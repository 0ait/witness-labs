<!--
title: Failed approach R1-FP01_strong_coupling_expansion_at_balaban_exit
id: QL-20261121-01/R1-P1/FP01
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: failed / refuted (kept per charter)
internal-source: WitnessLab/11_FAILED_APPROACHES/failed_proofs/R1-FP01_strong_coupling_expansion_at_balaban_exit.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# R1-FP01: "Balaban RG to the crossover, then an off-the-shelf strong-coupling cluster expansion" (refuted in its literal form)
- **Label:** Refuted strategy (as stated). The *route* R1 survives only in the reformulated form R1-D03 Prop. 2.
- **Attempted idea** (INV-001 report §6 R1; H03): run Balaban's RG until the effective coupling first exceeds γ, then prove clustering of the effective measure with an OS78/Seiler/SZZ-type strong-coupling (high-temperature) expansion, extended to non-local actions.
- **Why it fails** (R1-D04):
  - The expansions need the effective plaquette coupling below the strong-coupling threshold (SU(2): Wilson β_eff < 1/12, i.e. g² > 48, SZZ converted) and near-Haar link marginals.
  - Balaban's control ends at coupling ≈ γ ≪ 1, i.e. β_eff ≈ 2N/γ ≈ 40 (γ=0.1): a mismatch of ≈480×, with link marginals concentrated near 1.
  - No controlled flow connects the two. The perturbative flow reaches its pole first (R1-E02).
  - By the U(1) filter (R1-D01 Lemma A), no abelian-blind argument can bridge the window.
- **Lesson.** The crossover step must be posed at the *weak-coupling* exit scale (H-Gap at coupling γ), where it is a non-perturbative, non-abelian lattice mass-gap statement. It is not a strong-coupling statement.
- **Date:** 2026-11-21, Route 1 phase 1 (QUASAR).
