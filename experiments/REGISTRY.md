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

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
