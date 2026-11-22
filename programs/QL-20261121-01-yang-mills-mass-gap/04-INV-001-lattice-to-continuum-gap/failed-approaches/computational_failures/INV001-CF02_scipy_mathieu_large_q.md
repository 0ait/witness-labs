<!--
title: Failed approach INV001-CF02_scipy_mathieu_large_q
id: QL-20261121-01/INV-001/INV001-CF0
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: failed / refuted (kept per charter)
internal-source: WitnessLab/11_FAILED_APPROACHES/computational_failures/INV001-CF02_scipy_mathieu_large_q.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# INV001-CF02 — scipy.special.mathieu_b fails at large q (E02)
- **Attempted:** an independent check of the SU(2) single-plaquette spectrum using Mathieu characteristic values b_2(q), b_4(q) at q=16/g⁴.
- **Happened:** the values agree with the tridiagonal and Galerkin methods to ≤1e-12 for q≤1600 (g²≥0.1). At q=6400 (g²=0.05), `mathieu_b` returned a gap of −45.56, which is impossible because a gap must be positive. The other two methods agree with each other at 3.968546650102.
- **Failure type:** computational (library breakdown at large q).
- **Lesson:** never rely on a single special-function library in extreme parameter ranges; keep two independent discretisations. The result for g²=0.05 is labelled as two-method agreement, not three.
