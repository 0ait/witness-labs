<!--
title: INV-001 formulation (WS03)
id: QL-20261121-01/INV-001/formulation
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: internal record, copied
internal-source: WitnessLab/05_RESEARCH_WORKSTREAMS/WS03_continuum_limit/INV-001_formulation.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# INV-001 precise formulation: lattice objects, limits, and what a bridge theorem must assert (WS03/WS04)

QL-20261121-01 · QUASAR · 2026-11-21. These are definitions and statements of obligations only; nothing here is a claimed result. Proved lemmas are in `06_QUASAR_RESEARCH/derivations/INV001-D01…D07`.

## 1. Lattice objects
- **Group.** G is a compact simple Lie group with a faithful unitary representation of dimension N, and normalised Haar measure dU. Characters χ_r, dimensions d_r.
- **Lattice.** Λ_{L,N_t} = (ℤ/Lℤ)³ × (ℤ/N_tℤ) (periodic), or N_t=∞. Spacing a>0. Physical spatial size ℓ = La.
- **Wilson action.** For U:links→G, S_β(U) = β Σ_p (1 − (1/N)Re Tr U_p). The measure is dμ_{β,L} = Z^{−1}e^{−S_β}Π_l dU_l. For SU(N) the convention is β = 2N/g₀². SZZ use Nβ' Re Tr with β = Nβ'·… ('t Hooft scaling). Keep the normalisation explicit when quoting thresholds.
- **Lattice spacing a(β): a renormalisation trajectory.** a is not determined by β alone. A trajectory is fixed by a renormalisation condition μ_lat(β) = μ_phys·a(β) for a chosen lattice-unit scale μ_lat(β)→0 as β→∞. Possible choices are √σ_lat, 1/r₀, a gradient-flow scale, or a finite-volume running coupling ḡ²(L) held fixed at L = ℓ_ref/a. The last one does not presuppose an infrared property. *Heuristic expectation:* a(β)Λ ≈ (b₀g₀²)^{−b₁/2b₀²}e^{−1/(2b₀g₀²)} (D03.3). Choosing μ_lat := the gap itself makes the gap tautological (D03.3); the bridge must use an independent scale.
- **Transfer matrix (temporal gauge).** T_{β,L} acts on ℋ_L = L²(G^{E_s}). It is bounded, self-adjoint, positive (Lüscher 1977; OS78), has a strictly positive continuous kernel, and is trace class on a finite lattice. It commutes with the time-zero gauge group G^{V_s}, the spatial lattice symmetries and the centre (Polyakov-loop) symmetry.
  - Gauge-invariant sector ℋ_L^{inv}: vectors fixed by G^{V_s}. Physical states satisfy Gauss's law.
  - Local sector ℋ_L^{loc} ⊂ ℋ_L^{inv}: the smallest closed T-invariant subspace containing Ω_L and closed under multiplication by functions of contractible spatial Wilson loops (D02). It excludes centre-charged, torelon and electric-flux states.
  - λ₀ > λ₁ ≥ …: λ₀ is simple with Ω_L > 0 (Jentzsch).
- **Gaps in lattice units.**
  - m^{full}(β,L) = −log(λ₁^{full}/λ₀), where λ₁^{full} = sup σ(T|_{ℋ^{inv}⊖Ω}).
  - m^{loc}(β,L) = −log(λ₁^{loc}/λ₀), defined in the same way on ℋ^{loc}; m^{loc} ≥ m^{full}.
  - The quantity in the brief, m_lat(β,L) = −log(λ₁/λ₀), is m^{full} if λ₁ is taken on ℋ^{inv}. **The bridge needs m^{loc}** (D04, E02-B).
- **Physical gap.** Δ^{•}(a,L) := m^{•}(β(a),L)/a, i.e. the lattice Hamiltonian H_{a,L} = −a^{−1}log(T/λ₀) restricted to the sector.

## 2. Limits (which, in what order, along what)
Three admissible schemes:
- **(A) Infinite volume first.** L→∞ at fixed β, then β→∞ along a(β). Subsequential infinite-volume limits exist at every β by compactness (G compact implies tightness). Uniqueness of the limit is known only at strong coupling (OS78; SZZ Thm 1.2).
- **(B) Continuum first (Jaffe–Witten T⁴ route).** a→0 at fixed physical torus size ℓ, then ℓ→∞. Balaban's UV-stability regime is finite ℓ and small effective coupling (effectively small ℓΛ).
- **(C) Joint limit** along (β_k, L_k) with a(β_k)→0 and L_k a(β_k)→∞.

A bridge result should not depend on the order. The robust form requires estimates uniform in both regulators, i.e. valid for all β≥β₀ and all L≥L₀(β), stated in physical units.

## 3. Observables and convergence required
- **Family 𝒟.** Local gauge-invariant observables with lattice representatives F↦F_a: products of smeared Wilson loops of fixed physical size and shape, or plaquette fields smoothed at a fixed physical scale. They must be time-localised, so that θ and τ_t act. Raw plaquettes or Wilson loops need multiplicative or perimeter renormalisation (compare Chatterjee Problem 5.2, the c(β)(R+T) term). Proving the renormalisability of the chosen 𝒟 is part of the obligation.
- **Convergence (C1⁺).** For all n and F₁…F_n∈𝒟 at times t₁…t_n, the lattice Schwinger functions converge along the trajectory. The limit must satisfy:
  - OS0 (regularity/temperedness with a growth bound sufficient for OS75 reconstruction);
  - OS1 (Euclidean invariance; on the lattice only the hypercubic group is exact, so rotation invariance must be *proved* to be restored);
  - OS2 (reflection positivity; passes to the limit automatically);
  - OS3 (symmetry);
  - OS4 (clustering; implied by the gap).
- **Non-triviality.** The limit must not be Gaussian or free (for example, non-vanishing connected 4-point functions of 𝒟, or an area law of the continuum Wilson loops). D03.2 shows that a uniform lattice-unit gap forces triviality.
- **Field content / cyclicity (H1).** The reconstructed ℋ must be the physical Hilbert space of the Wightman theory whose local fields include the curvature composites (Jaffe–Witten: Tr F², and the stress tensor and OPE with asymptotic-freedom singularities). Cyclicity of 𝒟 is automatic only for the reconstruction from 𝒟 itself.

## 4. What a bridge theorem must assert
**Bridge Theorem (target form; Open problem as a whole).** For each compact simple G there exist a renormalisation trajectory β↦a(β)→0, a family 𝒟 as in §3, and constants Δ>0, β₀<∞, L₀(β)<∞ such that:
- (i) (C1⁺) the Schwinger functions of 𝒟 converge along every sequence (β_k,L_k) with β_k→∞ and L_ka(β_k)→∞, to a unique limit S, independent of the sequence, that satisfies OS0–OS3 and is non-trivial;
- (ii) (U) m^{loc}(β,L) ≥ Δ·a(β) for all β≥β₀ and L≥L₀(β); or the weaker family-wise (U′): |⟨F_a;F_a⟩_{n}| ≤ C(F)e^{−Δa(β)n} for all n, β≥β₀, L≥L₀(β), F∈𝒟;
- (iii) 𝒟 is cyclic for the physical Wightman Hilbert space.

**Conclusion** (proved conditional implication: D02(c) + D01): the reconstructed Hamiltonian H satisfies σ(H)∩(0,Δ)=∅ and ker H=ℂΩ.

**Necessity side** (proved: D03.2): if (i) holds non-trivially, then liminf m^{loc}/a < ∞. So any lattice-unit gap that is uniformly positive in β is incompatible with (i).

## 5. WS04 notes (infinite volume)
- A uniform-in-L lower bound on m^{loc} at fixed β gives exponential time-clustering of every subsequential infinite-volume limit, hence a unique vacuum in each such limit (D04.2). Uniqueness of the infinite-volume limit needs, in addition, convergence of the whole sequence.
- m^{full} need not be uniform in L, and need not even be relevant: torelon and electric-flux sectors (E02-B; 2D exact E01, where m^{full}=Lσ_lat and m^{loc}=∞).
- Tunnelling between degenerate finite-volume vacua forces m^{full}→0 exponentially in L without contradicting an infinite-volume pure-phase gap (D04 Example A; E03).
