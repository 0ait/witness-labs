<!--
title: Experiment registry
id: WL/experiments/REGISTRY
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Experiment registry

Every experiment in the archive, with the task metadata required by the [publication protocol](../docs/publication-protocol.md). All experiments ran locally on 2026-11-21 (Linux x86_64, 8 cores; Python 3.13.5, numpy 2.5.5, scipy 1.18.1, mpmath 1.3.0; see [`/environment/`](../environment/)).

## INV001-E01 — 2D Wilson lattice gauge theory, exact character expansion
| Field | Value |
|---|---|
| Task ID | QL-20261121-01 / INV-001 / E01 |
| Date and time (CT) | 2026-11-21; run 1 started 17:40 (killed ~17:52 per RUN1_NOTE); run 2 outputs written 17:51; committed e9e455b 17:53 |
| Domain | Lattice gauge theory (2D, SU(2) and U(1)); exact computation |
| Objective | Exact transfer-matrix gap and string tension in lattice units vs β; the continuum trajectory a(β); behaviour of the lattice-unit gap along it |
| Route | Bridge analysis (WS01–WS03); 2D sanity check for D03, D07 and route R1 decimation |
| Contributing agents | QUASAR (experiment); LATTICE (independent second implementation: COMPUTATIONALLY REPRODUCED) |
| Intent | Test the bridge framework where everything is exactly solvable |
| Importance | Shows concretely that the lattice-unit gap → 0 along a continuum trajectory while the physical gap stays finite (D03); shows that the 2D local sector is trivial |
| Methodology | Peter–Weyl character expansion with Bessel coefficients at 50-digit mpmath precision; cross-check by direct quadrature (1×1 torus, scipy nquad); exact block decimation |
| Results | βσ_lat → 1.5 (SU(2)), 0.5 (U(1)); at β=4096, βσ = 1.500183116636. Bessel vs quadrature agree to 7.5e−51 relative; torus check ≤1.6e−16. Trajectory at ℓ=4, β=16384: L=418, m_lat=0.03827021087, Δ=m/a≈3.9996. Decimation t_{1/2}: 0.97666 → 3.13e−11 (b=32) |
| Outcome classification | Successful (computationally verified finite result) |
| Key findings | Continuum string tension 1.5/β for SU(2); gap on the 2D torus is torelon energy; m_lat → 0 in lattice units as required by D03 |
| Limitations | 2D only (no propagating gluons). LATTICE defect 10: Δ≈σℓ is an identity of the chosen trajectory, not an independent test |
| Next steps | Relabel Δ≈σℓ as bookkeeping in v2 (pending authorization) |
| Links | [`programs/QL-20261121-01-yang-mills-mass-gap/04-INV-001-lattice-to-continuum-gap/experiments/INV001-E01/`](../programs/QL-20261121-01-yang-mills-mass-gap/04-INV-001-lattice-to-continuum-gap/experiments/INV001-E01/) · D07, D03 · failed run: CF01 |

## INV001-E02 — Kogut–Susskind Hamiltonians: SU(2) plaquette (A) and Z₂ ladder (B, B-weak)
| Field | Value |
|---|---|
| Task ID | QL-20261121-01 / INV-001 / E02 (E02-A, E02-B, E02b) |
| Date and time (CT) | 2026-11-21; outputs written 17:51 (E02) and 17:52 (E02b); ENV recorded 17:52; committed e9e455b 17:53 |
| Domain | Hamiltonian lattice gauge theory; exact diagonalization |
| Objective | (A) single-plaquette SU(2) gap vs coupling, in lattice units; (B) local vs torelon (flux) sector gaps on a Z₂ ladder vs size and coupling |
| Route | Bridge analysis; illustration for D03, D04, FP02; route R3 (Hamiltonian coercivity) |
| Contributing agents | QUASAR; LATTICE reproduced E02-B independently (COMPUTATIONALLY REPRODUCED) and found the torelon sector to be an exactly solvable free-fermion (TFIM) chain |
| Intent | Show that a lattice-unit gap can stay O(1) at weak coupling, and that the full-sector gap is dominated by flux sectors |
| Importance | Motivates using m^loc rather than m^full (LATTICE defect 8) |
| Methodology | (A) Gauss-law reduction to class functions; tridiagonal matrix (j_max=64), sine-Galerkin (400 modes), Mathieu characteristic values. (B) exact diagonalization with Gauss projector; ladders n ≤ 16 |
| Results | (A) gap 12.0073 (g²=8), 3.2691 (g²=1), 3.96855 (g²=0.05) → 4 as g→0. (B) at n=16 local gap 7.98→7.59→8.67→14.94→30.35 for J/h=0.25…16; torelon gap ≈ σ(J)·n, growing linearly in n. Gauss-projector check ≤7.1e−15 |
| Outcome classification | Successful (computationally verified finite result); one method failed at extreme q (CF02) |
| Key findings | Lattice-unit gaps at weak coupling do not certify a continuum gap; full-sector gap is the wrong object |
| Limitations | Tiny systems; at g²=0.05 only two of three methods agree (scipy Mathieu breaks down) |
| Next steps | None pending; superseded in v2 only by labelling changes |
| Links | [`programs/QL-20261121-01-yang-mills-mass-gap/04-INV-001-lattice-to-continuum-gap/experiments/INV001-E02/`](../programs/QL-20261121-01-yang-mills-mass-gap/04-INV-001-lattice-to-continuum-gap/experiments/INV001-E02/) · D03, D04, FP02 · CF02 |

## INV001-E03 — finite-volume gap closing by tunnelling
| Field | Value |
|---|---|
| Task ID | QL-20261121-01 / INV-001 / E03 |
| Date and time (CT) | 2026-11-21; outputs written 17:52; committed e9e455b 17:53 |
| Domain | Statistical mechanics (Ising / transverse-field Ising chain); exact diagonalization and free fermions |
| Objective | Exhibit a finite-volume gap that closes as volume grows while the infinite-volume pure phase is gapped |
| Route | WS04 infinite volume; illustration of D04 |
| Contributing agents | QUASAR |
| Intent | Show that a finite-volume gap is neither necessary nor sufficient |
| Importance | Concrete counterexample to the shortcut "finite-box gap for all L ⇒ gap" (FP02) |
| Methodology | (1) rigid-column Ising toy, exact at 60 digits; (2) periodic TFIM, J=1, h∈{0.3,0.5,0.7}, L=4…18, ED in Z₂ sectors cross-checked against free-fermion NS/R energies |
| Results | Tunnelling splitting at L=18: 1.008e−10 (h=0.3), 9.09e−7 (0.5), 3.28e−4 (0.7); fitted log-slopes −1.247/−0.737/−0.403 vs −log(J/h) −1.204/−0.693/−0.357; bulk gap → 4(J−h); ED vs free fermion ≤5e−14 |
| Outcome classification | Successful (computationally verified finite result) |
| Key findings | Finite-box gap closes exponentially while the physical excitation gap stays open |
| Limitations | Toy models, not gauge theory; fitted slopes include power-law prefactor corrections |
| Next steps | None |
| Links | [`programs/QL-20261121-01-yang-mills-mass-gap/04-INV-001-lattice-to-continuum-gap/experiments/INV001-E03/`](../programs/QL-20261121-01-yang-mills-mass-gap/04-INV-001-lattice-to-continuum-gap/experiments/INV001-E03/) · D04, FP02 |

## INV001-E04 — single-link SU(2) Langevin Poincaré gap vs Bakry–Émery
| Field | Value |
|---|---|
| Task ID | QL-20261121-01 / INV-001 / E04 |
| Date and time (CT) | 2026-11-21; outputs written 18:01, ENV recorded 18:02; committed 832442d 18:03 |
| Domain | Functional inequalities; spectral theory on SU(2) ≅ S³; finite elements |
| Objective | Compare the true Poincaré gap of the single-link measure with the Bakry–Émery and Holley–Stroock bounds as β grows |
| Route | R2 (first experiment) |
| Contributing agents | QUASAR; LATTICE (independent implementation: COMPUTATIONALLY REPRODUCED; l=1 gap at β=256 = 256.5024606763; last 2–3 printed digits of QUASAR's l=0 values not significant) |
| Intent | Find where the standard curvature criterion stops working at weak coupling |
| Importance | Shows that route R2 must improve on curvature bounds for structural reasons |
| Methodology | Separation into l-sectors; weighted Sturm–Liouville problem; P1 finite elements on a graded grid θ=πs², 4-point Gauss quadrature, shift-invert eigsh; grid refinement n=4000→8000 |
| Results | Gap ≈ β+½ (β=256: 256.50246067; β=8: 8.60890557; β=0: exactly 3 to 1e−8). Grid change ≤4.3e−7. Bakry–Émery bound 2−β is void for β≥2; Holley–Stroock gives 3e^{−2β} |
| Outcome classification | Successful (numerically supported result) |
| Key findings | The curvature criterion fails at weak coupling although the true gap is large |
| Limitations | Single link only; not a lattice field theory; LATTICE notes the follow-up 2D decimated test proposed for R2 is degenerate (product measure) |
| Next steps | Only if R2 is authorized: a non-product-measure test |
| Links | [`programs/QL-20261121-01-yang-mills-mass-gap/04-INV-001-lattice-to-continuum-gap/experiments/INV001-E04/`](../programs/QL-20261121-01-yang-mills-mass-gap/04-INV-001-lattice-to-continuum-gap/experiments/INV001-E04/) · FP01, report §6 R2 |

## Computational failures (kept)
| ID | What failed | Lesson |
|---|---|---|
| CF01 | E01 run 1: nested 3D mpmath quadrature hung for >11 min and was killed | Use high-precision quadrature only in 1D; double-precision cubature with error estimates for d≥2; unbuffered output |
| CF02 | E02-A: `scipy.special.mathieu_b` returned an impossible negative gap (−45.56) at q=6400 | Never rely on one special-function library at extreme parameters; keep two independent methods |

## Public-tree re-run (v0.1.0 publication check, 2026-11-21 18:48 CT)
Purpose: confirm that adding the one-line attribution comment to each script did not change behaviour. E04 and E03 were copied from this public tree to a scratch directory and run with the pinned environment (Python 3.13.5, numpy 2.5.5, scipy 1.18.1, mpmath 1.3.0).
- Both exited with status 0.
- **E04:** all 88 numerical result fields agree with the archived `e04_results.json` to ≤1.2e−11 relative (eigensolver round-off); printed gaps identical to the archived stdout; only run-time and round-off-level diagnostic fields differ.
- **E03:** all 264 result fields agree; the largest relative difference, 3.5e−5, is in tunnelling splittings of size ~1e−10 obtained as differences of O(1) eigenvalues (absolute difference ~4e−15, i.e. double-precision round-off); printed values identical to 4 significant figures; ED-vs-free-fermion diagnostics differ only at the 1e−14 level.
- Archived outputs were **not** overwritten; the published outputs are the original runs.

## Route 1 phase 1 experiments (added in v0.2.0 part 1)
Run 2026-11-21 on the same machine and Python stack as above; R1-E01 ran single-threaded (`nproc 1`, BLAS threads = 1; see its `ENV.txt`).

## R1-E01 — 4D U(1) vs 4D SU(2) Wilson lattice gauge theory on small lattices
| Field | Value |
|---|---|
| Task ID | QL-20261121-01 / R1-P1 / E01 |
| Date and time (CT) | 2026-11-21; runs 19:03–19:12; committed a4d4959 19:17 |
| Domain | Lattice gauge theory (4D, U(1) and SU(2)); Monte Carlo |
| Objective | Numerical contrast behind the U(1) filter: U(1) transition near β≈1.01 vs smooth SU(2) crossover |
| Route | Route 1 phase 1 (U(1) go/no-go filter) |
| Contributing agents | QUASAR; LATTICE independent Metropolis spot-check (agrees within errors at SU(2) β=2.5, U(1) β=0.9) |
| Intent | Qualitative evidence only, for R1-D01 §3–4 |
| Importance | Supports "effective coupling above γ does not by itself force strong-coupling behaviour" (U(1) non-confining at g₀²≈1) |
| Methodology | Checkerboard heat bath (von Mises for U(1); Kennedy–Pendleton for SU(2)); L=6, 8; hot and cold starts; plaquette, susceptibility, Wilson loops, Creutz ratio χ(2,2); 10-block jackknife |
| Results | U(1) L=8: P 0.5856 → 0.6551 between β=1.00 and 1.01 (max dP/dβ 6.87), χ(2,2) 0.353 → 0.166; SU(2) smooth (max dP/dβ ≈0.36). CPU ≈8.5 min |
| Outcome classification | Successful (numerical evidence only) |
| Key findings | Sharp U(1) transition near β≈1.0; no comparable SU(2) feature |
| Limitations | Small lattices, no finite-size scaling, τ_int not measured. LATTICE D-R1P1-6/7: masslessness was not measured; errors are underestimated in/near the Coulomb phase |
| Next steps | Wording and error-bar corrections in v2 (pending authorization) |
| Links | [`R1-E01/`](../programs/QL-20261121-01-yang-mills-mass-gap/07-R1-P1-route1-u1-filter/experiments/R1-E01/) · R1-D01, R1-LL01 |

## R1-E02 — perturbative running-coupling bookkeeping
| Field | Value |
|---|---|
| Task ID | QL-20261121-01 / R1-P1 / E02 |
| Date and time (CT) | 2026-11-21 19:07; committed a4d4959 19:17 |
| Domain | Renormalization group; exact arithmetic (mpmath, 30 digits) |
| Objective | RG steps to reach the crossover coupling γ, and the window γ → pole |
| Route | Route 1 phase 1 (S4, check 4) |
| Contributing agents | QUASAR; LATTICE checked the bookkeeping (exact) |
| Intent | Quantify where asymptotic freedom enters (S4) |
| Importance | Shows k_*(β) is finite and linear in β for SU(2), infinite for U(1) |
| Methodology | 1- and 2-loop flow ODE, block factor b=2, Wilson normalization g₀² = 2N/β |
| Results | SU(2): 3.883 steps per unit β; γ→pole window 152 steps at γ=0.1 (illustrative). U(1): b₀=b₁=0 |
| Outcome classification | Successful (Heuristic model; exact arithmetic) |
| Key findings | Crossover attainment is exactly where asymptotic freedom is used |
| Limitations | Perturbative; γ illustrative; normalization ambiguity (D-R1P1-4) |
| Next steps | Fix one lab-wide effective-action normalization (v2) |
| Links | [`R1-E02/`](../programs/QL-20261121-01-yang-mills-mass-gap/07-R1-P1-route1-u1-filter/experiments/R1-E02/) · R1-D03, R1-D04 |

## R1-E03 — block-average maps and time reflection θ
| Field | Value |
|---|---|
| Task ID | QL-20261121-01 / R1-P1 / E03 (E03 U(1), E03b SU(2)) |
| Date and time (CT) | 2026-11-21 19:13–19:16; committed a4d4959 19:17 |
| Domain | Lattice gauge theory (2D, 12×12, 3×3 blocks); exact finite configurations |
| Objective | Does gauge-covariant block averaging intertwine θ (check 2)? |
| Route | Route 1 phase 1 (reflection positivity of the coarse measure) |
| Contributing agents | QUASAR; LATTICE second implementation (COMPUTATIONALLY REPRODUCED for QUASAR's contour family) |
| Intent | Test reflection-compatibility of the block map |
| Importance | Determines whether coarse measures inherit reflection positivity |
| Methodology | Corner (space-first contours) vs centre-symmetric averaging; U(1) and SU(2) random configurations at several spreads σ |
| Results | SU(2) corner map mismatch 6.8e−3 / 1.0e−1 / 6.0e−1 at σ = 0.05 / 0.15 / 0.3; centre map ≤ ~1e−15. U(1): both maps pass (abelian test degenerate; see R1-FE01) |
| Outcome classification | Successful (computationally verified finite result) |
| Key findings | Corner map with space-first contours fails θ; centre map passes |
| Limitations | LATTICE D-R1P1-1 (CE-005): with time-first contours the corner map also passes; the failure is a contour artifact, not general. 2D only |
| Next steps | Restate Prop. 4 in v2 (pending authorization) |
| Links | [`R1-E03/`](../programs/QL-20261121-01-yang-mills-mass-gap/07-R1-P1-route1-u1-filter/experiments/R1-E03/) · R1-D02, R1-H03 · failed experiment: R1-FE01 |

### Public-tree re-run (v0.2.0 part 1 publication check, 2026-11-21)
R1-E02 and R1-E03 (both scripts) were copied from this public tree to a scratch directory and run with the pinned environment: all exited 0; stdout identical to the archived stdout; every JSON result field identical except `script_sha256`, which differs as expected because of the added attribution line. R1-E01 (≈8.5 CPU-min) was not re-run. Archived outputs were not overwritten.

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
