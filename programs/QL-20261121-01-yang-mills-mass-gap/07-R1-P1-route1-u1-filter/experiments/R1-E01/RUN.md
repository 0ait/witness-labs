<!--
title: R1-E01 run record
id: QL-20261121-01/R1-P1/E01
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: experiment completed; see experiments/REGISTRY.md
internal-source: WitnessLab/06_QUASAR_RESEARCH/experiments/R1-E01/RUN.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
## How to reproduce
1. Install the pinned stack in `ENV.txt` (Python 3.13.5, numpy 2.5.5, scipy 1.18.1, mpmath 1.3.0); full freeze in `/environment/`.
2. Copy this folder somewhere writable, `cd` into it, and run `export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1; for c in valid_u1 valid_su2 u1_L6 u1_L8 su2_L6 su2_L8; do python3 -u r1e01_u1_su2_4d.py $c; done; python3 -u r1e01_summary.py` (runtime ≈8.5 CPU-minutes single-threaded on the original machine).
3. Outputs are written to `outputs/` (this overwrites the archived outputs, so work on a copy). Compare with the archived files and `outputs/SHA256SUMS.txt`.
4. Note: the `.py` files here carry one added attribution comment line, so their sha256 differs from the script hash recorded in `outputs/SHA256SUMS.txt` and in the output JSONs (which is the hash of the original, uncommented script). Code is otherwise identical.

---


# R1-E01: 4D U(1) vs 4D SU(2) Wilson lattice gauge theory on small lattices (U(1) filter, numerical contrast)

QL-20261121-01 · WITNESS LAB · QUASAR · Route 1 phase 1 · run 2026-11-21 19:03–19:12 CT.
**Label: Numerical evidence only.** Small lattices, short runs. Nothing here is a proof, and nothing here bears directly on the continuum mass gap. The point is the qualitative contrast the U(1) filter relies on: 4D U(1) has a (weakly first-order) transition near β≈1.01 into a massless Coulomb phase, while 4D SU(2) has a smooth crossover.

## Method
- Script: `r1e01_u1_su2_4d.py` (sha256 `2e4ce2c9…e6b8`, full hash in `outputs/SHA256SUMS.txt`; each output JSON records the hash of the script that produced it, and it matches).
- Wilson action, periodic L⁴. Vectorised checkerboard heat-bath: per direction μ, the even and odd sublattices are updated in turn. Two μ-links in a common plaquette always have opposite parity.
  - U(1): an exact von Mises heat bath, θ ~ VM(−arg S, β|S|), with S the staple sum.
  - SU(2): Kennedy–Pendleton heat bath in quaternions, with reunitarisation each sweep.
- Observables:
  - mean plaquette P;
  - plaquette susceptibility χ_P = N_p(⟨P²⟩−⟨P⟩²), N_p = 6L⁴;
  - Wilson loops W(R,T) with R,T ≤ 2, averaged over all planes and orientations;
  - Creutz ratio χ(2,2) = −ln[W₂₂W₁₁/(W₂₁W₁₂)];
  - hot (random) and cold (identity) starts at every β.
- Errors: 10-block jackknife. Integrated autocorrelation times were **not** measured, so errors near the U(1) transition are underestimates.
- Seeds: 20261121 + 1000·i_β + i_start + 10L (+500000 for SU(2)). Single-threaded BLAS.
- Runs: `outputs/run_A_stdout.txt` (validation + U(1) L=6), `run_B` (U(1) L=8), `run_C` (SU(2) L=6, 8). JSONs per configuration; `r1e01_summary.py` → `outputs/summary_stdout.txt`.
- **CPU:** 488 s for the production runs, plus about 20 s for benchmark and validation.

## Validation (exact limits)
| check | measured | exact/expected |
|---|---|---|
| U(1) β=0.2, L=4 | P = 0.09882(109) | I₁(0.2)/I₀(0.2) = 0.09950 (strong coupling, leading) |
| SU(2) β=0.4, L=4 | P = 0.09946(73) | I₂(0.4)/I₁(0.4) = 0.09934 |
| U(1) β=3, L=4, 300 therm (side check, cold and hot) | 0.91287 / 0.91259 | 1 − 1/(4β) + 1/(32β²) ≈ 0.913 (Gaussian + quartic) |
| SU(2) β=2.5, L=6 | 0.65205(45)/0.65276(33) | ≈0.652 (standard literature value; not re-sourced here) |

**Kept discrepancy.** The logged `valid_u1` run at β=3 with only 100 thermalisation sweeps from a hot start gives 0.90033. This is **under-thermalised**, consistent with slowly relaxing monopole loops in the Coulomb phase. The 300-sweep side check above, run interactively and not in the logged JSON, gives 0.9129 for both starts. Production U(1) runs use 500 thermalisation sweeps.

## Results (summary_stdout.txt)
| | max dP/dβ (interval) | max χ_P | χ(2,2) across the steep interval | max |hot−cold|/σ |
|---|---|---|---|---|
| U(1), L=6 | 4.10 on [1.00,1.02] | 3.14 (β=1.00) | 0.359 → 0.147 | 4.05 (β=1.06) |
| U(1), L=8 | **6.87 on [1.00,1.01]** (P: 0.5856 → 0.6551) | 2.68 (β=1.00) | 0.353 → 0.166 | 1.72 |
| SU(2), L=6 | 0.356 on [2.1,2.2] | 0.364 | 0.509 → 0.392 | 1.88 |
| SU(2), L=8 | 0.334 on [2.2,2.3] | 0.393 | 0.405 → 0.319 | 1.86 |

## Observations
- (Numerical evidence) U(1) has a near-discontinuity in P between β=1.00 and 1.01 at L=8, with a slope about 20× the largest SU(2) slope. The Creutz ratio χ(2,2) halves across the same 0.01 in β. This is consistent with the literature location β_c≈1.01 of the Wilson-action U(1) transition (not re-sourced in this run).
- SU(2) is smooth over β∈[1.6,3.0]. Its χ_P is ≤0.39, with a broad, weak maximum near β≈2.1–2.3 (the known bulk-crossover region). There is no hot/cold separation beyond 1.9σ.
- **Not shown:** finite-size scaling. The U(1) χ_P peak does not grow from L=6 to L=8 at this β resolution. No robust hot/cold hysteresis appears at L=8; the one 4σ difference at L=6, β=1.06 is attributed to autocorrelation. These lattices are too small to establish first-order behaviour. We rely on the literature for the order of the transition, and on the rigorous Guth/Fröhlich–Spencer/Driver results (S-127, S-128, S-132) for the massless phase.
- **Relevance to R1 (R1-D01 §3).** At β just above 1.01 the bare U(1) coupling is g₀² = 1/β ≈ 1. That is far above any "sufficiently small" γ, yet the phase is non-confining. Numerically this supports the filter conclusion that "the effective coupling exceeds γ" does not by itself force strong-coupling behaviour.
