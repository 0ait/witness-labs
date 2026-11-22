<!--
title: INV001-E04 run record
id: QL-20261121-01/INV-001/E04
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: experiment completed; see experiments/REGISTRY.md
internal-source: WitnessLab/06_QUASAR_RESEARCH/experiments/INV001-E04/RUN.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
## How to reproduce
1. Install the pinned stack in `ENV.txt` (Python 3.13.5, numpy 2.5.5, scipy 1.18.1, mpmath 1.3.0); full freeze in `/environment/`.
2. Copy this folder somewhere writable, `cd` into it, and run `python3 -u e04_single_link_poincare.py` (runtime ≈1 s on the original machine).
3. Outputs are written to `outputs/` (this overwrites the archived outputs, so work on a copy). Compare with the archived files and `outputs/SHA256SUMS.txt`.
4. Note: the `.py` files here carry one added attribution comment line, so their sha256 differs from the script hash recorded in `outputs/SHA256SUMS.txt` (which is the hash of the original, uncommented script). Code is otherwise identical.

---


# INV001-E04: single-link SU(2) Langevin Poincaré gap vs β, compared with the Bakry–Émery bound (route R2, first experiment)

**Question.** The strong-coupling mass-gap proofs of SZZ (S-106) go through a Bakry–Émery curvature condition (Ric + Hess S ≥ K_S > 0) that holds only for small |β|. On the smallest possible "lattice" (one link with measure ∝ e^{(β/2)Tr U}dU on SU(2) ≅ unit S³), how far is the true Poincaré constant from the BE bound and from the Holley–Stroock perturbation bound, as β→∞?

**Model.** V(θ) = −β cos θ, where θ is the geodesic distance to 1 on the unit S³ (Ric = 2g). The generator is L = Δ − ∇V·∇, self-adjoint in L²(e^{−V}dvol). Separating f = g(θ)Y_l(ω) reduces each l-sector to a weighted 1D Sturm–Liouville problem.
- Discretisation: P1 finite elements on a graded grid θ = π s², with 4-point Gauss quadrature, solved by shift-invert eigsh.
- Sector checks: l=0 (excluding the constant) and l=1. Higher l are larger by monotonicity of the l(l+1)/sin²θ term.

**Run.** `python3 -u e04_single_link_poincare.py` (≈1 s). Outputs: `outputs/e04_results.json` and `outputs/e04_stdout.txt`.

**Results.**

| β | gap (l=1) | gap (l=0, first non-const) | BE bound 2−β | Holley–Stroock 3e^{−2β} |
|---|---|---|---|---|
| 0 | 3.00000003 | 3.00000003 | 2 | 3 |
| 1 | 3.13226241 | 3.19966382 | 1 | 0.406 |
| 2 | 3.51637516 | 3.79447957 | 0 | 0.0549 |
| 8 | 8.60890557 | 13.69638371 | −6 (void) | 3.4e−7 |
| 64 | 64.51008380 | 125.97949898 | void | 7.7e−56 |
| 256 | 256.50246067 | 509.99513133 | void | 1.3e−222 |

- **Precision.** Relative change between n=4000 and n=8000 elements is ≤ 4.3e−7 at every β. The β=0 value matches the exact S³ value 3 (ℓ(ℓ+2), ℓ=1) to 1e−8.
- **Observations.**
  - (Numerically supported) The single-link gap is ≈ β + 1/2 for large β. It *grows* linearly, matching the Ornstein–Uhlenbeck (Gaussian) asymptote β. The l=0 sector is ≈ 2β − 2.
  - (Established, elementary) The BE bound K = Ric + inf Hess V = 2 − β becomes void at β = 2, because Hess V = β cos θ·g is negative near the antipode θ=π. The perturbative Holley–Stroock bound decays like e^{−2β}.

**What this does and does not show.**
- It is a one-link toy. It is NOT a statement about the lattice gauge theory's mass gap, and it is not 4D.
- The *dynamical* (Langevin) gap of a measure is a different object from the transfer-matrix gap. SZZ derive spatial decay from the dynamical gap plus uniform-in-volume LSI.
- The point for R2: at weak coupling the global BE curvature is destroyed by the non-convex region far from the identity. That region has measure ~e^{−2β}, yet BE is a worst-case pointwise condition. Moreover, by D03.2 a β-uniform lattice-unit gap is exactly what must NOT happen in the true 4D model. Any scale-uniform functional inequality must therefore be applied to *block-spin effective measures at a fixed physical scale*, not to the bare Wilson measure. This sharpens route R2 into the requirement stated as ME-R2 in the report.

**Cosmetic note.** In the stdout, the β=0 "gap/beta" column divides by 1e−300 and is meaningless; it is kept unedited.
