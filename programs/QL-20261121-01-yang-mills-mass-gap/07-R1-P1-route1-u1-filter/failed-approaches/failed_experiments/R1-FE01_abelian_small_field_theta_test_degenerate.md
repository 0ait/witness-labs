<!--
title: Failed approach R1-FE01_abelian_small_field_theta_test_degenerate
id: QL-20261121-01/R1-P1/FE01
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: failed experiment (kept per charter)
internal-source: WitnessLab/11_FAILED_APPROACHES/failed_experiments/R1-FE01_abelian_small_field_theta_test_degenerate.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# R1-FE01: testing θ-intertwining of block averages with U(1) small fields is degenerate
- **Label:** Failed (uninformative) experiment, kept.
- **What was run.** R1-E03 first version (`r1e03_block_theta.py`): 2D U(1), BIJ corner averaging versus centre-symmetric averaging. Both intertwine θ to ≤2e−16.
- **Why it is uninformative.** The U(1) argument average is linear, so contour and base-point dependence reduce to a coarse gauge transformation (Proved here, R1-D02 Prop. 4). Any averaging passes on gauge-invariant data. The test cannot discriminate.
- **Fix.** The SU(2) test (`r1e03b_block_theta_su2.py`) discriminates: the corner rule fails (up to 0.6) and the centre-symmetric projection rule passes (≤7e−16).
- **Lesson.** Abelian controls can be *too easy* as well as *too hard* (cf. 3D U(1) confining, Göpfert–Mack). Pick the control by the structure being tested.
