<!--
title: INV001-E02 run record
id: QL-20261121-01/INV-001/E02
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: experiment completed; see experiments/REGISTRY.md
internal-source: WitnessLab/06_QUASAR_RESEARCH/experiments/INV001-E02/RUN.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
## How to reproduce
1. Install the pinned stack in `ENV.txt` (Python 3.13.5, numpy 2.5.5, scipy 1.18.1, mpmath 1.3.0); full freeze in `/environment/`.
2. Copy this folder somewhere writable, `cd` into it, and run `python3 -u e02_ks_hamiltonian.py && python3 -u e02b_ladder_weak.py` (runtime ≈35 s on the original machine).
3. Outputs are written to `outputs/` (this overwrites the archived outputs, so work on a copy). Compare with the archived files and `outputs/SHA256SUMS.txt`.
4. Note: the `.py` files here carry one added attribution comment line, so their sha256 differs from the script hash recorded in `outputs/SHA256SUMS.txt` (which is the hash of the original, uncommented script). Code is otherwise identical.

---


# INV001-E02 — exact diagonalisation of Kogut–Susskind Hamiltonians

**Run.** `python3 -u e02_ks_hamiltonian.py` (~30 s) and `python3 -u e02b_ladder_weak.py` (~5 s). Outputs are in `outputs/`.

## Part A: SU(2) single plaquette (lattice units)
H=(g²/2)Σ_{l=1}^4E_l²−(1/g²)(Tr U_p+Tr U_p†). Gauss's law at the four bivalent vertices forces all links into a common irrep j, so the gauge-invariant space is class functions of U_p with basis χ_j. In that basis H_{jj}=2g²j(j+1) and H_{j,j±1/2}=−2/g², since χ_{1/2}χ_j=χ_{j+1/2}+χ_{j−1/2}. Truncation j≤j_max.

Independent methods:
- (a) A sine-Galerkin solution (400 modes) of the radial equation −(g²/2)(u″+u)−(4/g²)cos θ·u=Eu, u(0)=u(π)=0.
- (b) Mathieu characteristic values: E_n=(g²/8)b_{2n+2}(16/g⁴)−g²/2.

| g² | gap (j_max=64) | Galerkin | Mathieu |
|---|---|---|---|
| 8 | 12.007288822406 | 12.007288822406 | 12.007288822406052 |
| 4 | 6.057972654204 | same | 6.057972654203661 |
| 2 | 3.426288565734 | same | 3.4262885657340387 |
| 1 | 3.269099185521 | same | 3.2690991855209104 |
| 0.5 | 3.663550052481 | same | 3.6635500524806863 |
| 0.1 | 3.936673438305 | same | 3.9366734383053483 |
| 0.05 | 3.968546650102 | same | **−45.56 (scipy `mathieu_b` failure at q=6400; logged in 11_FAILED_APPROACHES/computational_failures)** |

- Truncation convergence: see `gap_vs_jmax`. For g²≥0.05 the gap is stable to 12 digits by j_max=32.
- Strong coupling: gap≈(3/2)g². Weak coupling: gap→4 (the radial s-wave levels of a 3D oscillator with ω=2 are spaced 2ω=4).
- The minimum gap over g is about 3.27, near g²≈1.

**Reading:** the lattice-unit gap of this toy is bounded below uniformly in g. By D03 that is exactly the kind of bound that says nothing about a continuum limit. With one plaquette there is no volume and no continuum limit.

## Part B: Z₂ gauge theory on a periodic ladder of n plaquettes
H=hΣ_l(1−σ^x_l)−JΣ_pΠ_{l∈p}σ^z_l. The gauge-invariant space is the Z₂ cycle space (dimension 2^{n+1}). Sectors are labelled by the winding w∈{0,1}: w=0 is the local sector containing the vacuum, w=1 is the torelon sector.

Cross-check: for n=3,4, diagonalising the full 2^{3n}-dimensional Hilbert space with an explicit Gauss-law projector reproduces the gauge-invariant construction (physical dimensions 16 and 32 agree; eigenvalue differences ≤7.1e-15).

| J/h | local gap (n=16) | torelon gap n=4 → 16 | full gap n=16 |
|---|---|---|---|
| 0.25 | 7.984606366 | 7.967 → 31.874 | 7.9846 (local) |
| 1 | 7.801154402 | 7.271 → 29.585 | 7.8012 (local) |
| 4 | 8.674989917 | 2.876 → 11.522 | 8.675 (local, for n≥14) |
| 8 | 14.944574 | 1.2611 → 5.0453 | 5.0453 (torelon) |
| 16 | 30.354018 | 0.56515 → 2.26062 | 2.26062 (torelon) |

- The local gap converges in n exponentially fast; the J/h=1 values agree to 1e-12 by n=12.
- The torelon gap is linear in n, ≈σ(J)·n with σ≈0.1577 (J=8) and ≈0.0353 (J=16).
- So for every n computed at J/h≥8, the full finite-volume gap is a non-local, volume-dependent energy, far below the local gap.

## What this can and cannot establish
These are computationally verified finite results for toy Hamiltonians. They show:
1. Truncation control is easy for one plaquette.
2. The finite-volume full-sector gap and the local-sector gap are different objects, and finite-size data in the full sector can be dominated by flux/torelon states.
3. A uniform-in-coupling lattice-unit gap carries no continuum information.

They cannot say anything about SU(2) in 3+1 dimensions, the continuum limit, or infinite volume. The Z₂ ladder is quasi-one-dimensional and has no continuum limit of interest.
