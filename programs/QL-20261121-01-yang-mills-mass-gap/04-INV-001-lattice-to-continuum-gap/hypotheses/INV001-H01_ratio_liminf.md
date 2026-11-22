<!--
title: Hypothesis INV001-H01_ratio_liminf
id: QL-20261121-01/INV-001/INV001-H0
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: Hypothesis (open)
internal-source: WitnessLab/06_QUASAR_RESEARCH/hypotheses/INV001-H01_ratio_liminf.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# INV001-H01: positive liminf of the local gap in units of an independent scale
- **Label:** Hypothesis (the analogue for 4D SU(N) is believed by physicists on numerical grounds; it is unproved).
- **Statement.** For 4D SU(N) Wilson LGT and μ_lat(β) := 1/r₀(β) or a gradient-flow scale (a non-gap scale): liminf_{β→∞} inf_{L ≥ L₀(β)} m^{loc}(β,L)/μ_lat(β) > 0, and limsup < ∞.
- **Role.** Equivalent to ME1 + ME3 for the trajectory a(β) := μ_lat(β)/μ_phys (report §5).
- **Evidence.** None proved. Lattice Monte Carlo literature (not reviewed in INV-001) is the physical motivation. Labelled for later WS02 numerics.
- **Falsifiers.** A proof that m^{loc}/μ_lat → 0 along some trajectory. Within INV-001 this is excluded only for trivial limits (D03.2 concerns the opposite direction).
- **Depends on:** D02, D03.
