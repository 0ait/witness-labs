<!--
title: Required axioms
id: QL-20261121-01/01/required_axioms
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: specification v1; LATTICE review flags pending corrections
internal-source: WitnessLab/01_PROBLEM_FORMALIZATION/required_axioms.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
> **Public-archive note (2026-11-21):** LATTICE review 2026-11-21 flags PO-11/PO-12 sector and β-convention issues (defects 8, 9); corrections pending in v2. The body below is unchanged.

# Required axioms — QL-20261121-01

Tags: [JW p.N] = Jaffe–Witten (opened). [STD-unopened] = standard formulation; the primary text was not opened this session (OI-01). [LEAN-OAI] = the encoding in the 2026 OpenAI submission's public spec (`../04_CANDIDATE_SOLUTIONS/openai_2026_existence/source/PublicTheory.lean`, commit 3456e5e7…), opened and read, and given only as a comparison point.

## What JW require (verbatim anchor)
"Existence includes establishing axiomatic properties at least as strong as those cited in [45, 35]" [JW p.6]. [45] = Streater–Wightman 1964. [35] = Osterwalder–Schrader, CMP 31 (1973) 83–112, DOI 10.1007/BF01645738, and CMP 42 (1975) 281–305, DOI 10.1007/BF01608978 (both DOIs Crossref-verified 2026-11-21). JW's own summary is at [JW p.5]; see `official_definitions.md` D2.

## Wightman axioms (W0–W3 numbering as in the common textbook presentation) [STD-unopened]
- **W0 Relativistic QM.** Separable Hilbert space ℋ. Continuous unitary representation U(a,Λ) of the covering of the proper orthochronous Poincaré group. Spectrum condition: the joint spectrum of P^μ lies in the closed forward cone V̄₊. There is a unique (up to phase) invariant vacuum Ω. [JW p.5 states all of these in words.]
- **W1 Fields.** Φ(f), f ∈ 𝒮(R⁴), operator-valued tempered distributions on a dense domain D ∋ Ω, with Φ(f)D ⊂ D and Φ(f)* ⊃ Φ(f̄)† (Hermitian structure on labels). Ω is cyclic for the polynomial algebra.
- **W2 Covariance.** U(a,Λ)Φ(f)U(a,Λ)⁻¹ = Φ(f_{(a,Λ)}) with the finite-dimensional representation acting on labels, and U D ⊂ D.
- **W3 Locality.** [Φ(f), Φ(g)] = 0 on D when supp f and supp g are spacelike separated (bosonic fields only here).
- [LEAN-OAI] encodes W0 as: a spectral representation of translations by a projection-valued energy–momentum measure, positive energy (projection of the complement of the closed forward cone = 0), and uniqueness of translation-invariant vectors. W1 as a common dense domain, cyclic vacuum, temperedness in the test function, and an adjoint identity. W2 as covariance under a group whose coordinates are homeomorphic to SO⁺(1,3) × R⁴. W3 as commutation for spacelike-separated supports. Observations: (i) the time coordinate is the last coordinate; (ii) translations are recovered by `charFun` with the Euclidean dot product instead of the Minkowski pairing. Since the spectrum is invariant under spatial reflection, we believe this only relabels P⃗ → −P⃗ [QUASAR, unreviewed]; (iii) only the restricted Lorentz group is required, not its covering. That is adequate for integer-spin (bosonic) gauge-invariant fields.

## Osterwalder–Schrader axioms [STD-unopened]
- **OS0 Regularity / temperedness**, plus the **linear growth condition** (E0′ in OS 1975). It is needed for the reconstruction to give tempered Wightman distributions. Its absence in the 1973 paper was corrected in 1975 (standard history; to verify against the text).
- **OS1 Euclidean covariance** (translations and SO(4) rotations).
- **OS2 Reflection positivity.** For Wilson lattice gauge theory this holds at finite spacing [JW p.11, citing Osterwalder–Seiler 1978, DOI 10.1016/0003-4916(78)90039-8].
- **OS3 Symmetry** under permutations.
- **OS4 Cluster property.** This corresponds to uniqueness of the vacuum. It is what the 2026 construction does **not** establish for the raw limit. It proves it only for each component of a phase decomposition (assessment p.7–8, see audit report).

## Requirements beyond the axioms (from [JW p.6])
- Local gauge-invariant fields matching the polynomials in F and D F (`official_definitions.md` D3).
- Short-distance agreement with asymptotic freedom: stress tensor, OPE with prescribed singularities (D4).
- JW (p.6, §3 end) note that existing axiom sets may need refinement "to incorporate properties considered important by physicists such as the existence of an operator product expansion or of a local stress-energy tensor". So the OPE and stress tensor are *not* part of [45, 35]; they are additional requirements stated in §4.

## Lattice-to-continuum axiom status table (proof-obligation cross-reference)
| Axiom | Holds at finite (a, L)? | Survives a → 0? | Survives L → ∞? | PO |
|---|---|---|---|---|
| OS2 reflection positivity | yes (Osterwalder–Seiler 1978) | preserved under weak limits of positive forms [QUASAR: elementary] | same | PO-07 |
| OS1 translation | lattice translations only | needs a → 0 | needs L → ∞ | PO-07 |
| OS1 rotation | hypercubic group only | **non-trivial (restoration of SO(4))** | — | PO-07 |
| OS0 + growth | trivial on a finite lattice | needs UV bounds uniform in a | needs bounds uniform in L | PO-02, PO-05 |
| OS4 clustering | finite systems: unique Gibbs state | — | **open in general** (non-unique limits, phase mixtures) | PO-09 |
