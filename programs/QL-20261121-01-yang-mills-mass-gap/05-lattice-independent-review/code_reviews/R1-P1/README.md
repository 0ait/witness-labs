<!--
title: LATTICE record: code_reviews/R1-P1/README.md
id: QL-20261121-01/07/code_reviews/R1-P1/README.md
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: LATTICE (independent validator), Witness Labs, Agentic Swarm, 0ait
date: 2026-11-21
version: as committed in internal f5ccacd
status: LATTICE record, published v0.2.0 part 2
internal-source: WitnessLab/07_LATTICE_INDEPENDENT_REVIEW/code_reviews/R1-P1/README.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# LATTICE code for the R1-P1 review (QL-20261121-01)
Copies of `reviews/QL-20261121-01/R1-P1/code/`. Python 3 + numpy, sympy, mpmath. CPU: θ tests < 20 s; MC spot-check ≈ 101 s.
- `theta_intertwine.py`: 4D (and general-D) θ-intertwining test of gauge-covariant block averages (corner vs centre anchor; proj / logref / log averages; contour orders; raw and gauge-invariant metrics). Output: `theta_intertwine_output.txt`, `theta_intertwine_results.json`.
- `theta_2d_reproduce.py`: the same code in QUASAR's E03b geometry (2D 12×12, 3×3 blocks). Output: `theta_2d_reproduce_output.txt`, `theta_2d_reproduce_results.json`.
- `mc_spotcheck.py`: independent Metropolis spot-check of R1-E01 with τ_int. Output: `mc_spotcheck_output.txt`, `mc_spotcheck_results.json`.
- `conversions_check.py`: SZZ→Wilson threshold and R1-E02 bookkeeping, exact or 30 digits. Output: `conversions_check_output.txt`.
- `crossref_r1p1.py`: Crossref resolution of 19 DOIs. Output: `crossref_r1p1.out`.
Label: verification code. Results are Computationally verified finite results / Numerical evidence as stated in the review.
