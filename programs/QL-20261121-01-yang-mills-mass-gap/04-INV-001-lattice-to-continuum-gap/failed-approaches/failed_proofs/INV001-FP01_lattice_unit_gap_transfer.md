<!--
title: Failed approach INV001-FP01_lattice_unit_gap_transfer
id: QL-20261121-01/INV-001/INV001-FP0
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: failed / refuted (kept per charter)
internal-source: WitnessLab/11_FAILED_APPROACHES/failed_proofs/INV001-FP01_lattice_unit_gap_transfer.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# INV001-FP01: "transfer a lattice-unit gap that is uniform in β to the continuum" (refuted approach)
- **Label:** Refuted hypothesis (as a proof strategy).
- **Attempted idea.** Use a strong- or weak-coupling theorem that gives m_lat(β,L) ≥ c > 0 uniformly in β (e.g. Adhikari–Cao-type rates (β/2)Δ_G, or a Bakry–Émery constant), divide by a(β), and obtain Δ = c/a(β) → ∞ ≥ any Δ.
- **Why it fails.** D03.2: if m^{loc}/a → ∞ along a converging sequence, the limit is trivial (all of 𝒟 is a c-number). So a β-uniform lattice-unit gap is a *certificate of triviality*, not of a gap. The gap must vanish exactly like a(β) (window D03, ME1 + ME3).
- **Illustrations.**
  - E02: the single-plaquette gap → 4 as g→0.
  - E04: the single-link Langevin gap ≈ β+½.
  - S-111: finite-G rate grows with β; finite-group theories have no non-trivial continuum limit.
- **Lesson.** Every candidate estimate must be stated in units of an independent scale μ_lat(β) → 0 (H01).
