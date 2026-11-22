<!--
title: INV001-E01 run record
id: QL-20261121-01/INV-001/E01
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: experiment completed; see experiments/REGISTRY.md
internal-source: WitnessLab/06_QUASAR_RESEARCH/experiments/INV001-E01/RUN.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
## How to reproduce
1. Install the pinned stack in `ENV.txt` (Python 3.13.5, numpy 2.5.5, scipy 1.18.1, mpmath 1.3.0); full freeze in `/environment/`.
2. Copy this folder somewhere writable, `cd` into it, and run `python3 -u e01_2d_wilson.py` (runtime ≈4 s on the original machine).
3. Outputs are written to `outputs/` (this overwrites the archived outputs, so work on a copy). Compare with the archived files and `outputs/SHA256SUMS.txt`.
4. Note: the `.py` files here carry one added attribution comment line, so their sha256 differs from the script hash recorded in `outputs/SHA256SUMS.txt` (which is the hash of the original, uncommented script). Code is otherwise identical.

---


# INV001-E01 — 2D Wilson lattice gauge theory (SU(2), U(1)): exact character expansion

**Question.** In 2D, where everything is exactly solvable, what are the transfer-matrix gap and the string tension in lattice units as functions of β; how must a(β) be chosen for a continuum limit; and what happens to the lattice-unit gap along that trajectory?

**Run.** `python3 -u e01_2d_wilson.py` (≈4 s). Outputs: `outputs/e01_results.json`, `outputs/e01_stdout.txt`. Env: `ENV.txt`. Failed run 1 kept in `failed_runs/`.

## Exact formulas used (derivation)
Weight per plaquette w(U)=exp((β/2)Re Tr U)=exp(β cos θ). Class functions on SU(2): Haar class density (2/π)sin²θ, χ_j=sin((2j+1)θ)/sin θ, orthonormal. Character expansion w=Σ_j ĉ_j χ_j with
ĉ_j=∫wχ_j dU=(1/π)∫_0^π e^{β cos θ}[cos 2jθ−cos(2j+2)θ]dθ=I_{2j}(β)−I_{2j+2}(β)=(2(2j+1)/β)I_{2j+1}(β).
Set a_j=ĉ_j/d_j (d_j=2j+1), t_j=a_j/a_0=I_{2j+1}(β)/I_1(β). Gluing rule ∫χ_j(XU)χ_k(U^{-1}Y)dU=δ_{jk}χ_j(XY)/d_j gives, for a closed surface with n plaquettes, E links, V vertices, Z=Σ_j d_j^{V−E+n} a_j^n; for the torus (Euler characteristic 0) Z=Σ_j a_j^n. With n=L·T, Z=Tr T^T where the transfer matrix on the L-link spatial circle acts on class functions of the spatial Polyakov loop with eigenvectors χ_j and eigenvalues λ_j=a_j^L. Hence the exact full-sector gap
  m_lat(β,L)=−log(λ_{1/2}/λ_0)=L·σ_lat(β),  σ_lat(β)=−log(I_2(β)/I_1(β)).
On the infinite plane (free boundary, axial gauge) the plaquette variables are i.i.d., ⟨W_C⟩=t_{1/2}^{Area(C)}; connected correlations of distinct plaquettes vanish identically. U(1): a_n=I_n(β), σ_lat=−log(I_1/I_0).

## Results (50-digit mpmath; all digits shown are exact to the printed precision)
| β | σ_lat SU(2) | β·σ_lat SU(2) | σ_lat U(1) | β·σ_lat U(1) |
|---|---|---|---|---|
| 1 | 1.426309498445 | 1.426309498445 | 0.806562345998 | 0.806562345998 |
| 4 | 0.418478515344 | 1.673914061376 | 0.146735196417 | 0.586940785669 |
| 16 | 0.096714835402 | 1.547437366438 | 0.032287934847 | 0.516606957558 |
| 64 | 0.023621285434 | 1.511762267831 | 0.007874428545 | 0.503963426931 |
| 256 | 0.005870830135 | 1.502932514567 | 0.001956953429 | 0.500980078068 |
| 4096 | 0.000366255643 | 1.500183116636 | 0.000122085216 | 0.500061048820 |
β·σ_lat → 3/2 (SU(2)) and 1/2 (U(1)), matching I_2/I_1=1−3/(2β)+O(β^{-2}), I_1/I_0=1−1/(2β)+O(β^{-2}).

**Continuum trajectory (2D).** Fixing σ_phys=1 forces a(β)=σ_lat(β)^{1/2} ≈ (3/(2β))^{1/2}, i.e. β a² → 3/2 = 4/g²·(3g²/8) (g the dimensionful 2D coupling, σ=g²C_F/2, C_F=3/4). On a spatial circle of physical length ℓ (L=round(ℓ/a)): ℓ=4, β=16384: a=0.00956846, L=418, m_lat=0.0382702 (lattice units), Δ=m_lat/a=3.99962=σ_phys·L·a. So the lattice-unit gap → 0 like a, the physical gap stays finite, and it equals σℓ, the energy of a flux loop wound around the circle, which grows linearly in ℓ. There are no local excitations. In infinite volume the 2D gauge-invariant local sector has no connected correlations, so ℋ_loc=ℂΩ.

**Exact 2D decimation (Migdal; exact in 2D).** Blocking b×b plaquettes maps t_j→t_j^{b²}. From β=64: t_{1/2}=0.97666 (block 1) → 0.68527 (4) → 0.22052 (8) → 2.36e-3 (16) → 3.13e-11 (32). The flow carries a weak-coupling action into the strong-coupling (small-t) regime in about log₂(1/a) steps. log t_1/log t_{1/2}=2.66638 is preserved exactly; it is ≈ C_2(1)/C_2(1/2)=8/3, the heat-kernel value.

## Cross-checks
1. ĉ_j by direct mpmath quadrature against the Bessel closed form for β∈{0.5,2,8,30}, j≤2: max relative error 7.5e-51.
2. A closed form for Tr(UVU⁻¹V⁻¹), checked against explicit 2×2 matrix products at 2000 random points: max error 1.1e-15.
3. The 1×1 torus Z=∫∫w(UVU⁻¹V⁻¹) by 3D `scipy.nquad` (epsrel 1e-11), compared with Σ_j a_j: β=0.5: 1.1704757999176094 vs 1.17047579991760926; β=1: 1.4522159507070371 vs …069; β=3: 5.068248112440882 vs 5.06824811244088122. Relative differences are ≤1.6e-16.

## What this can and cannot establish
- **Can:** it gives exact, computationally verified finite results for 2D (Computationally verified finite result / Established theorem for the closed forms). It illustrates the scale-obstruction lemma (D03): the lattice-unit gap must vanish ∝ a for a non-trivial limit. It also illustrates that a finite-volume full-sector gap may consist entirely of non-local, volume-dependent states (torelons).
- **Cannot:** 2D YM has no propagating local degrees of freedom and is super-renormalizable. Nothing here bears directly on 4D. In particular, an area law in 2D is not a mass gap of anything local.
