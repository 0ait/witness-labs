<!--
title: Theorem specification T★
id: QL-20261121-01/01/theorem_specification
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: specification v1; LATTICE review flags pending corrections
internal-source: WitnessLab/01_PROBLEM_FORMALIZATION/theorem_specification.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
> **Public-archive note (2026-11-21):** LATTICE review 2026-11-21 flags PO-11/PO-12 sector and β-convention issues (defects 8, 9); corrections pending in v2. The body below is unchanged.

# Theorem specification — the official target T★ (QL-20261121-01)

Status: **specification** (not a claim). Author: QUASAR, 2026-11-21. Awaiting LATTICE's independent formulation (mission §20 item 2). LATTICE should formulate T★ blind from `../00_GOVERNANCE/official_problem_statement.md` before reading this file.

## T★ (official statement, verbatim [JW p.6])
"Prove that for any compact simple gauge group G, a non-trivial quantum Yang–Mills theory exists on R4 and has a mass gap ∆ > 0. Existence includes establishing axiomatic properties at least as strong as those cited in [45, 35]."

## T★ unpacked [QUASAR]. Each clause is tagged with its textual anchor.
For every G in the class 𝒢 of `group_scope.md`, there exist:

1. **(Hilbert space and symmetry)** A separable Hilbert space ℋ with a strongly continuous unitary representation U of the proper orthochronous Poincaré group (or its cover) that satisfies the spectrum condition (joint spectrum of (H, P⃗) in the closed forward cone), and a vacuum Ω that is U-invariant and unique up to phase. [JW p.5; STD-unopened]
2. **(Fields)** Operator-valued tempered distributions Φ_v(f), indexed by a label space 𝓥 = ⋃_d 𝓥_d. They have a common dense invariant domain D ∋ Ω, satisfy Poincaré covariance and locality, and Ω is cyclic. Equivalently, there are Schwinger functions satisfying OS0–OS4 together with the OS growth condition needed for reconstruction. [JW p.5–6 via [45, 35]]
3. **(Yang–Mills identification)** 𝓥_d is in correspondence with the gauge-invariant local polynomials of dimension ≤ d in F and its covariant derivatives. The correspondence is not required to be canonical (footnote 1). The theory must arise as Yang–Mills, which in practice means as a limit of a gauge-invariant regularization of the Lagrangian (1) [JW p.2, p.6, p.11]. **[QUASAR] interpretive gap:** JW do not specify a test that certifies "is Yang–Mills" beyond items 3–4. A construction-independent characterization is an open definitional issue (OI-02).
4. **(Short distance)** Correlation functions agree at short distances with asymptotic freedom and perturbative renormalization. This includes a stress tensor and an OPE with the singularities that asymptotic freedom predicts. [JW p.6]
5. **(Non-triviality)** The theory is not free (D7).
6. **(Existence standard)** If existence comes from a limit, compactness alone is excluded unless other techniques establish the properties of the limit [JW p.12 fn 2].
7. **(Mass gap)** There exists ∆ > 0 with σ(H) ∩ (0, ∆) = ∅, and m := sup{∆} < ∞ [JW p.6].

## Quantifier structure [QUASAR]
∀ G ∈ 𝒢 ∃ (ℋ, U, Ω, Φ) : [1 ∧ 2 ∧ 3 ∧ 4 ∧ 5 ∧ 6] ∧ ∃ ∆ > 0 : σ(H) ∩ (0,∆) = ∅ ∧ m < ∞.
The *same* theory must satisfy both the existence clauses and the gap. A gap proved for a different object (a lattice at fixed a, a finite volume, one phase of a non-unique limit, another subsequence) does not discharge clause 7.

## Ambiguities and our defensible readings (logged, not silently resolved)
| # | Ambiguity | Reading adopted | Why |
|---|---|---|---|
| A1 | Does "exists" require uniqueness of the infinite-volume limit? | Not literally stated. But by fn 2, a subsequential (compactness) limit must have its properties proved. If the limit is non-unique, T★ is plausibly met by *one* limit point having all properties, including the gap. Flag: reviewers may demand independence from the subsequence. | Literal text plus fn 2 |
| A2 | Wightman vs OS | Either, as long as the reconstruction is valid ("at least as strong as those cited in [45, 35]") | [JW p.6] |
| A3 | "compact simple" | Compact Lie group whose Lie algebra is simple and nonabelian. All global forms G̃/Z, Z ⊂ Z(G̃), are included. See `group_scope.md` | Standard usage; JW give no definition |
| A4 | Fermionic fields | Not required; this is pure Yang–Mills | [JW p.6] |
| A5 | Which quadratic form "Tr" | Any invariant form, since for simple 𝔤 it is unique up to scale and the scale is absorbed in g | Standard (Killing-form uniqueness) |
| A6 | Strength of the "non-trivial" test | D7 working definition | see `official_definitions.md` D7 |
