<!--
title: Proof obligations PO-01..PO-16
id: QL-20261121-01/01/proof_obligations
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: specification v1; LATTICE review flags pending corrections
internal-source: WitnessLab/01_PROBLEM_FORMALIZATION/proof_obligations.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
> **Public-archive note (2026-11-21):** LATTICE review 2026-11-21 flags PO-11/PO-12 sector and β-convention issues (defects 8, 9); corrections pending in v2. The body below is unchanged.

# Proof obligations for T★ — dependency map v1 (QL-20261121-01)

Author: QUASAR, 2026-11-21. Status vocabulary: **established** (published, peer-reviewed theorem, or elementary with proof given here), **partial**, **claimed** (asserted by a third party, not independently verified by WITNESS LAB), **open**. Citations marked (opened) were read this session. Citations marked (unopened) are standard references not yet read; their status is provisional (OI-01). Nothing here is a proof.

Route assumed: Wilson lattice → fixed-volume continuum limit on T⁴ → infinite volume → OS reconstruction. Other routes (stochastic quantization, Hamiltonian, continuum regularization [JW p.12]) get their own maps in WS07/WS08/WS09.

## The central obstacles, verbatim (anchors for PO-05, PO-06, PO-11–PO-13)
- [JW p.6 §5] "In addition the existence of a uniform gap for finite-volume approximations may play a fundamental role in the proof of existence of the infinite-volume limit."
- [JW p.7 §6] "Yet, even if this were accomplished, no present ideas point the direction to establish the existence of a mass gap that is uniform in the volume. Nor do present methods suggest how to obtain the existence of the infinite volume limit T4 → R4 ."
- [JW p.7 §6.1] "Establishing uniform a priori estimates is central to CQFT …"
- [JW p.12 §6.5] "New ideas are needed to prove the existence of a mass gap that is uniform in the volume of space-time. Such a result presumably would enable the study of the limit as T4 → R4 ."
- [JW p.12 fn 2] "We specifically exclude weak-existence (compactness) as the solution to the existence part … unless one also uses other techniques to establish properties of the limit (such as the existence of a mass gap and the axioms)."

## Obligations

**PO-01 Regulated theory.** For every G ∈ 𝒢, a ∈ (0,1], L ∈ aℕ: the Wilson measure μ_{a,L,β} on G^{links of (aℤ/Lℤ)⁴} is a well-defined, gauge-invariant probability measure, reflection positive with respect to lattice hyperplanes, with a positive transfer matrix T_{a,L}.
Depends on: —. Status: **established**. Wilson 1974 [JW ref 48] (unopened); reflection positivity: Osterwalder–Seiler, Ann. Phys. 110 (1978) 440–471, DOI 10.1016/0003-4916(78)90039-8 (Crossref-verified; text unopened; cited for this fact by [JW p.11], opened).

**PO-02 Fixed-volume UV limit.** At fixed L, along a renormalization trajectory β(a), correlation functions of suitably renormalized gauge-invariant local lattice observables converge as a → 0 (at least at non-coincident points) to the Schwinger functions of a theory on T⁴_L.
Depends on: PO-01, PO-03. Status: **partial (literature) / claimed (2026)**. Balaban: effective actions and UV stability, uniform in the spacing, on the torus (3D: CMP 102 (1985) 255–275, DOI 10.1007/BF01229380; 4D: CMP 109 (1987) 249–301, DOI 10.1007/BF01215223, both Crossref-verified, texts unopened). [JW p.11] (opened): "These results need to be extended to the study of expectations of gauge-invariant functions of the fields." 2026 OpenAI Lean submission: **claimed** along a construction-chosen spacing sequence (assessment Thm 4.1, p.6; see audit report).
Known obstacle location: [JW p.11–12]. Gauge-invariant expectations, and independence from the spacing sequence (no universality; assessment p.6).

**PO-03 Local field content.** Renormalized lattice representatives I_{a}(v,x) exist for each label v in the quotient of the gauge-invariant polynomials in F, DF of dimension ≤ d by their relations, with limits matching [JW p.6] and fn 1.
Depends on: PO-02. Status: **open (literature) / claimed (2026)** (assessment §3–4, p.4–6).

**PO-04 Short-distance structure.** Agreement with asymptotic freedom and perturbative renormalization: β-function running, stress tensor, OPE with the prescribed singularities [JW p.6].
Depends on: PO-02, PO-03. Status: **open / partially claimed (2026)**. The assessment (p.3, item 3) says the construction gives an OPE with error bounds "but does not show that it matches the predictions of a perturbative expansion". The public Lean spec requires β_N/log(1/a_N) → *some* positive slope (`WilsonRegularity.running`). The assessment's eq. (7) states the value 11C_g/(24π²) for the detailed construction. We have not located that value in the public statement (audit item 3).

**PO-05 Volume-uniform a priori bounds.** Bounds on renormalized correlations on compact sets of non-coincident configurations, uniform in L (and in a after PO-02).
Depends on: PO-02. Status: **open (literature) / claimed (2026)**: local boundedness and equicontinuity uniform in volume, via reflection positivity, chessboard estimates, transfer operator, Cauchy estimates (assessment p.7, eq. (11)).

**PO-06 Infinite-volume limit: existence of the full limit, and uniqueness.** Convergence as L → ∞ (not only along subsequences), independent of the subsequence and of boundary conditions.
Depends on: PO-05; plausibly PO-11 ([JW p.6]: a uniform gap "may play a fundamental role"). Status: **open**. 2026 construction: subsequential only, via Arzelà–Ascoli. "This limit is not proven to be unique" (assessment p.1, p.7; Open Question 1, p.13).
Known obstacle location: [JW p.7]; [JW p.12] fn 2.

**PO-07 OS axioms for the limit.** OS0 (+ growth), OS1 including restoration of full SO(4), OS2, OS3 for the limiting Schwinger functions, including contact terms at coincident points.
Depends on: PO-02, PO-05, PO-06. Status: **open (literature) / claimed (2026)**, for each component of a phase decomposition (assessment §6, p.7–8). Coincident points are handled by "an extension for the constructed prescription"; "uniqueness over other contact prescriptions … outside the claim" (repo README).

**PO-08 Reconstruction.** OS ⇒ Wightman: ℋ, U, Ω, H ≥ 0, local fields.
Depends on: PO-07, PO-09. Status: **established as a theorem** (Osterwalder–Schrader 1975, with the growth condition; DOI 10.1007/BF01608978, Crossref-verified; text unopened). Claimed re-proved formally in Lean in the 2026 submission (assessment p.8, Thm 6.1).

**PO-09 Vacuum uniqueness / clustering / phase structure.** The limit (or each chosen phase) clusters, so Ω is unique. The selected phase is identified, and phases agree or the choice is canonical.
Depends on: PO-06, PO-07. Status: **open (literature) / partially claimed (2026)**. Each component of a Gelfand / Riesz–Markov decomposition satisfies clustering. "Uniqueness across volume subsequences and agreement of the component theories are also unresolved" (assessment p.1).

**PO-10 Non-triviality.** The constructed theory is not a (generalized) free field (D7).
Depends on: PO-07/08, PO-04. Status: **open (literature) / claimed (2026)**. The trace-test short-distance law r⁸ log²(1/r)·S₂(Θ) → 3 dim 𝔤/π⁴ excludes finite sums of mass-shell Wick profiles. This is weaker than D7 as stated, but the log² law itself is not a free-field behavior [QUASAR, unreviewed]. Audit item 8.

**PO-11 Uniform finite-volume (lattice) gap.** Lower bound E_gap(a,L) = log(λ0/λ1) ≥ c(a) > 0 on the gauge-invariant sector, **uniform in L**, with c(a)/a bounded below along the renormalization trajectory (Δ_phys(a,L) ≥ ∆ > 0).
Depends on: PO-01; must be compatible with PO-02. Status: **open** in the continuum-relevant regime (β → ∞).
- Established only in other regimes: strong coupling (small β), at fixed a. Osterwalder–Seiler 1978 (unopened; standard attribution) and Shen–Zhu–Zhu 2023 (cited as [SZZ23] in the abstract of arXiv:2510.22788 (opened): "mass gap … for SU(N) and SO(N) lattice Yang–Mills theories … mixing of the associated Langevin dynamics … Bakry–Émery criterion").
- 't Hooft regime, U(N): Nissim, arXiv:2510.22788 (opened abstract: "We establish a mass gap, prove the existence of a unique infinite volume limit … for U(N) lattice Yang–Mills theory in the 't Hooft regime"). That is lattice and fixed coupling regime, not continuum.
Known obstacle location: [JW p.7], [JW p.12]: "New ideas are needed to prove the existence of a mass gap that is uniform in the volume." **← mission's first investigation targets PO-11 → PO-13.**

**PO-12 Continuum survival of the gap (UV side).** liminf_{a→0} a⁻¹ log(λ0/λ1)(a,L) ≥ ∆ > 0 along the PO-02 trajectory, uniformly in L ≥ L₀. Equivalently, dimensional transmutation yields a non-collapsing physical scale (mission §16).
Depends on: PO-02, PO-04, PO-11. Status: **open**. Obstacle: strong-coupling methods have c(a) at a fixed lattice scale. Asymptotic freedom gives a = Λ⁻¹ exp(−β/(2b₀))·(…) → 0, so a fixed lattice-unit gap gives a gap of order Λ only if the gap in lattice units scales like aΛ exactly. That is a statement about the IR (strong-coupling) end of the RG flow, which no current method controls.

**PO-13 Transfer of the gap to the reconstructed H.** σ(H) ∩ (0,∆) = ∅ for the H of PO-08.
Depends on: PO-08, PO-11, PO-12, PO-06/09.
- Status: the implication "uniform Euclidean decay with a common rate ∆ on a dense set ⇒ gap" is **established (elementary)** (`mass_gap_definition.md` E3, our proof, unreviewed).
- Status of the input: **open**. One needs uniform-in-(a,L) control of the decay constants on approximating vectors (E5). Spectral gaps are not stable under weak limits without it.

**PO-14 Group generality.** PO-01…PO-13 for every G ∈ 𝒢 (group_scope.md), with group-dependent constants tracked.
Depends on: all. Status: existence-type obligations **claimed (2026)** for all closed matrix groups with simple 𝔤. Gap: **open** for every G.

**PO-15 m < ∞.** σ(H) ≠ {0}.
Depends on: PO-08, PO-10. Status: **expected elementary**. To be written (mass_gap_definition.md).

**PO-16 Footnote-2 compliance (meta-obligation).** If existence uses compactness, the properties of the limit (axioms; and per fn 2's example "the existence of a mass gap") must be established by other techniques.
Status: for the 2026 construction, the axioms are claimed for each phase and no gap is claimed. Whether fn 2's parenthetical makes the gap part of *existence* is an interpretive question (ambiguity A1). Logged for LATTICE.

## Dependency graph (edges "needs")
```
PO-01 ─► PO-02 ◄─► PO-03 ─► PO-04
PO-02 ─► PO-05 ─► PO-06 ─► PO-07 ─► PO-08
PO-06,PO-07 ─► PO-09 ─► PO-08
PO-04,PO-08 ─► PO-10 ─► PO-15
PO-01 ─► PO-11 ─► PO-12 ─► PO-13 ◄─ PO-08, PO-06/09
PO-11 ┄┄► PO-06 (JW p.6: uniform gap "may play a fundamental role")
all ─► PO-14 ; PO-06 ─► PO-16
```
**Critical path for the Commander's first investigation:** PO-11 → PO-12 → PO-13, with the coupling to PO-06 (uniform gap ⇒ infinite-volume uniqueness/clustering).
