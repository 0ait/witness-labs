<!--
title: Official definitions
id: QL-20261121-01/01/official_definitions
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: specification v1; LATTICE review flags pending corrections
internal-source: WitnessLab/01_PROBLEM_FORMALIZATION/official_definitions.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
> **Public-archive note (2026-11-21):** LATTICE review 2026-11-21 flags PO-11/PO-12 sector and β-convention issues (defects 8, 9); corrections pending in v2. The body below is unchanged.

# Official definitions — QL-20261121-01

Prepared by QUASAR, 2026-11-21. Every definition is tagged with its source:
- **[JW p.N]** = verbatim or near-verbatim from Jaffe–Witten (S-001), printed page N (see `../00_GOVERNANCE/official_problem_statement.md`).
- **[STD-unopened]** = standard textbook formulation, NOT read this session (Streater–Wightman 1964 is a print book; Osterwalder–Schrader CMP 31/42 could not be retrieved: Springer and Project Euclid returned HTML stubs to our client, and we did not try to get around that). These need verification against the primary text before they bear any weight. Open item OI-01.
- **[QUASAR]** = our own precise restatement or derivation. Status: unreviewed by LATTICE.

## D1. Gauge group
"compact gauge group G" with curvature F = dA + A ∧ A and Lagrangian L = (1/(4g²)) ∫ Tr F ∧ ∗F, "where Tr denotes an invariant quadratic form on the Lie algebra of G" [JW p.1–2]. The Millennium statement restricts to "compact simple" G [JW p.6]. JW give no further definition; see `group_scope.md` for our reading.

## D2. Quantum field / QFT "in the above sense"
"an operator-valued generalized function on space-time obeying certain axioms" [JW p.5]. Its data: a Hilbert space with a positive-energy Poincaré representation, self-adjoint generators H and P⃗, a Poincaré-invariant vacuum Ω that is unique up to phase, covariant gauge-invariant fields, and locality (commutation at spacelike separation) [JW p.5]. The precise axioms are those "cited in [45, 35]" [JW p.6], i.e. Gårding–Wightman (Streater–Wightman) or Osterwalder–Schrader. See `required_axioms.md`.

## D3. Yang–Mills local fields
"local quantum field operators in correspondence with the gauge-invariant local polynomials in the curvature F and its covariant derivatives, such as Tr F_ij F_kl(x)" [JW p.6]. Footnote 1 [JW p.6] says there is no natural 1–1 correspondence, because of renormalization. The expectation is only that the classical differential polynomials of dimension ≤ d correspond to the local quantum operators of dimension ≤ d.

## D4. Short-distance requirements
"Correlation functions of the quantum field operators should agree at short distances with the predictions of asymptotic freedom and perturbative renormalization theory, as described in textbooks. Those predictions include among other things the existence of a stress tensor and an operator product expansion, having prescribed local singularities predicted by asymptotic freedom." [JW p.6]

## D5. Vacuum, energy, positivity
HΩ = 0, and the positive energy axiom says that σ(H) ⊂ [0, ∞) [JW p.6].

## D6. Mass gap and mass
"A quantum field theory has a mass gap ∆ if H has no spectrum in the interval (0, ∆) for some ∆ > 0. The supremum of such ∆ is the mass m, and we require m < ∞." [JW p.6]. See `mass_gap_definition.md`.

## D7. Non-trivial
JW do not define this term explicitly. Contextually [JW p.7]: "we do not know any non-trivial relativistic field theory that satisfies the Wightman (or any other reasonable) axioms in four dimensions", which contrasts with free (Gaussian/generalized free) fields [JW p.8]: "The Gaussian measure … yields the free, mass-m0 field; but one requires non-Gaussian dµ to obtain nonlinear fields." **[QUASAR] working definition:** the theory is not unitarily equivalent to a (generalized) free field theory. Equivalently, some truncated n-point Wightman function with n ≥ 3, or the non-Gaussian part of the 4-point function, is nonzero. Any weaker test (for example, excluding only finitely many Wick profiles) must be flagged as weaker.

## D8. Existence via limits (exclusion of compactness)
"We specifically exclude weak-existence (compactness) as the solution to the existence part of the Millennium problem, unless one also uses other techniques to establish properties of the limit (such as the existence of a mass gap and the axioms)." [JW p.12, fn 2]

## D9. Clustering (a consequence of a gap, not a definition)
[JW p.6, eq. (2)]: for C < ∆, |⟨Ω, O(x⃗)O(y⃗)Ω⟩| ≤ exp(−C|x⃗ − y⃗|) for |x⃗ − y⃗| sufficiently large, when ⟨Ω, OΩ⟩ = 0.

## D10. Lattice and transfer-matrix quantities [QUASAR, standard]
Wilson action on Λ = (aZ/LZ)⁴: S = β Σ_□ (1 − (1/d_ρ) Re tr_ρ U_□), with Haar product measure [JW p.11 describes Wilson's approach; its reflection positivity is [JW p.11] citing Osterwalder–Seiler 1978, DOI 10.1016/0003-4916(78)90039-8 (Crossref-verified)]. Transfer matrix T_{a,L} > 0 acts on the gauge-invariant subspace of L²(G^{spatial links}). Its top eigenvalues are λ0 > λ1 ≥ …. Lattice gap: E_gap = log(λ0/λ1), in lattice units. Physical gap: Δ_phys(a,L) = a⁻¹ log(λ0/λ1). Sector, boundary condition, and the precise eigenvalue ordering must be fixed per formulation (mission order §14 WS03).
