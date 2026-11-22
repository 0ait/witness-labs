<!--
title: Failed approach INV001-CF01_mpmath_3D_quadrature
id: QL-20261121-01/INV-001/INV001-CF0
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: failed / refuted (kept per charter)
internal-source: WitnessLab/11_FAILED_APPROACHES/computational_failures/INV001-CF01_mpmath_3D_quadrature.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# INV001-CF01 — 3D mpmath quadrature too slow (E01 run 1)
- **Attempted:** cross-checking the 1×1-torus SU(2) partition function by nested 3D `mpmath.quad` at 20 digits.
- **Expected:** to finish in a few minutes.
- **Happened:** no result after more than 11 minutes, so the run was killed. Output was also block-buffered through `tee`.
- **Failure type:** computational.
- **Repair:** used `scipy.integrate.nquad` with epsrel 1e-11; it finished in 2.3 s per β with agreement ≤1.6e-16. Use `python -u` for long runs.
- **Lesson:** use high-precision quadrature only in 1D; use double-precision adaptive cubature with an error estimate for d≥2. Evidence is kept in `06_QUASAR_RESEARCH/experiments/INV001-E01/failed_runs/`.
