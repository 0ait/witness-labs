<!--
title: Mass-gap definition
id: QL-20261121-01/01/mass_gap_definition
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: specification v1; LATTICE review flags pending corrections
internal-source: WitnessLab/01_PROBLEM_FORMALIZATION/mass_gap_definition.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
> **Public-archive note (2026-11-21):** LATTICE review 2026-11-21 flags PO-11/PO-12 sector and β-convention issues (defects 8, 9); corrections pending in v2. The body below is unchanged.

# Mass gap — definition and equivalent forms (QL-20261121-01)

## Official definition, verbatim [JW p.6]
> Since the vacuum vector Ω is Poincaré invariant, it is an eigenstate with zero energy, namely HΩ = 0. The positive energy axiom asserts that in any quantum field theory, the spectrum of H is supported in the region [0, ∞). A quantum field theory has a mass gap ∆ if H has no spectrum in the interval (0, ∆) for some ∆ > 0. The supremum of such ∆ is the mass m, and we require m < ∞.

Formally: ∃ ∆ > 0 such that σ(H) ∩ (0, ∆) = ∅, and m := sup{∆ : σ(H) ∩ (0,∆) = ∅} < ∞.
What is **not** required: that [∆, ∞) be filled; that an isolated one-particle state exists ("upper gap"); confinement. JW list these as "natural extensions" [JW p.6–7].

## Equivalent forms [QUASAR derivations; labels as stated; all unreviewed by LATTICE]
**E1 (projection form).** With E_H the spectral measure of H: E_H((0, ∆)) = 0. With a unique vacuum, ker H = ℂΩ. Then the gap is equivalent to H ≥ ∆ on {Ω}^⊥ ∩ D(H). *Label: elementary spectral theory.*

**E2 (Lorentz-invariant mass form).** Suppose the joint spectrum Σ ⊂ V̄₊ is invariant under SO⁺(1,3) (which follows from W0 and W2). Then inf σ(H|_{Ω^⊥}) = inf{√(p²) : p ∈ Σ \ {0}} if the second set contains no lightlike points. If Σ \ {0} contains any point with p² = 0 (massless states), then by boosts it contains points of arbitrarily small energy and there is no gap. So "mass gap ∆" ⇔ Σ ⊂ {0} ∪ {p : p⁰ ≥ 0, p² ≥ ∆²}, with {0} carried only by Ω. *Proof sketch:* each hyperboloid p² = μ², p⁰ > 0, contains the point (μ, 0⃗), whose energy is μ, and every point on it has p⁰ ≥ μ. The cone p² = 0 has inf p⁰ = 0 and contains no p = 0 point other than the vacuum's. *Label: elementary; to be checked by LATTICE.*

**E3 (Euclidean decay criterion, sufficient).** Let 𝒟 ⊂ {Ω}^⊥ be dense, for example D₀ := {OΩ − ⟨Ω,OΩ⟩Ω : O polynomial in time-zero-localized smeared fields}. Suppose that for every ψ ∈ 𝒟 there is C_ψ < ∞ with ⟨ψ, e^{−tH} ψ⟩ ≤ C_ψ e^{−∆t} for all t ≥ 0. Then σ(H|_{Ω^⊥}) ⊂ [∆, ∞).
*Proof:* let μ_ψ be the spectral measure of ψ and fix ∆' < ∆. Then e^{−t∆'} μ_ψ([0,∆')) ≤ ∫ e^{−tλ} dμ_ψ ≤ C_ψ e^{−∆t}, so μ_ψ([0,∆')) ≤ C_ψ e^{−(∆−∆')t} → 0. Hence E_H([0,∆))ψ = 0 on a dense set, so E_H([0,∆))|_{Ω^⊥} = 0. ∎ *Label: established (elementary); our proof, unreviewed.*
**Crucial point for the mission:** the rate ∆ must be the **same** for every ψ in a dense set. Decay of one correlator, or rates m(O) that depend on O with inf_O m(O) = 0, gives no gap. This is mission §17 / WS06 made precise. The constants C_ψ may depend on ψ.

**E4 (OS / transfer-matrix form).** In an OS-reconstructed theory, e^{−tH} is realized by Euclidean time translation on the OS Hilbert space. So E3 reads: for all positive-time-supported F in a dense class, the truncated Schwinger function S(ΘF̄ · τ_t F) − |S(F)|² ≤ C_F e^{−∆t}. On the lattice: T = e^{−aH_a} and E_gap = a·inf σ(H_a|_{Ω^⊥}) = log(λ0/λ1).

**E5 (physical vs lattice units).** Δ_phys(a,L) = a⁻¹ log(λ0(a,L)/λ1(a,L)). A uniform continuum gap requires liminf over the renormalization trajectory (a → 0, β(a) ~ 2b₀ log(1/a)) and L → ∞ of Δ_phys(a,L) ≥ ∆ > 0. **Even this does not suffice by itself:** one also needs that the lattice gap controls the gap of the limit theory. Spectral gaps are not continuous under weak convergence in general. This is lower semicontinuity in the wrong direction: new spectrum can appear in the limit. A gap passes to the limit if E3 holds **uniformly** (∆ and the bound on C_ψ uniform in (a,L) for the approximating vectors). This is the precise form of the "uniform estimate" bottleneck [JW p.7, p.12]. *Label: QUASAR analysis, unreviewed.* (b₀ = 11h∨/(48π²) in the normalization β = 1/g₀², h∨ = dual Coxeter number. Standard one-loop value; check the normalization against the source before use.)

## Finite mass m < ∞
m = ∞ would mean σ(H) = {0}, so H = 0 and U(time translations) = 1. With W0–W3 and a non-zero field this is impossible [QUASAR: expected elementary via the Wightman function of a non-constant field; to be written as PO-15].
