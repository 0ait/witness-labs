<!--
title: Failed approach INV001-FP02_full_sector_finite_volume_gap
id: QL-20261121-01/INV-001/INV001-FP0
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: failed / refuted (kept per charter)
internal-source: WitnessLab/11_FAILED_APPROACHES/failed_proofs/INV001-FP02_full_sector_finite_volume_gap.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# INV001-FP02: "a positive finite-volume transfer-matrix gap m^{full}(β,L) for all L gives the gap" (refuted approach)
- **Label:** Refuted hypothesis (as a proof strategy).
- **Why it fails.**
  - (i) *Not sufficient:* D04 Example B (m(L)>0 ∀L, limit 0) and D05 (m_lat>0 ∀a, continuum gap 0 if m₀(a)→0).
  - (ii) *Not necessary:* D04 Example A and E03 (tunnelling splitting 1.0e−10 at TFIM h=0.3, L=18, while the bulk gap is ≈2.83).
  - (iii) *Wrong sector:* m^{full} sees torelon/electric-flux states (E01: m^{full} = Lσ_lat in 2D with m^{loc} = ∞; E02-B torelon gap ∝ n).
  - (iv) A single correlator's decay is not enough (D06).
- **Correct object.** m^{loc}, uniform in L and in physical units, for a cyclic family (D02, ME1).
