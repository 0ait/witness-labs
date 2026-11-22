<!--
title: INV001-E01 failed_runs/RUN1_NOTE.md
id: QL-20261121-01/INV-001/E01/failed_runs/RUN1_NOTE.md
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: failure record (kept per charter)
internal-source: WitnessLab/06_QUASAR_RESEARCH/experiments/INV001-E01/failed_runs/RUN1_NOTE.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# INV001-E01 run 1 — killed (computational failure, kept per charter)
- Started 2026-11-21 17:40 CT; killed at ~17:52 CT after >11 min with no output.
- Cause: the 1x1-torus cross-check used a 3-dimensional `mpmath.quad` (tanh-sinh, 20 digits, split
  intervals) for three beta values; nested adaptive mpmath quadrature in 3D is far too slow.
  stdout was also block-buffered by `tee`, so no partial output was visible.
- Fix in run 2: torus cross-check done with `scipy.integrate.nquad` (double precision, epsrel 1e-11),
  main exact tables computed first, `python3 -u` for unbuffered output.
- Lesson: budget nested high-precision quadrature; use mpmath only in 1D, scipy for >=2D checks.
