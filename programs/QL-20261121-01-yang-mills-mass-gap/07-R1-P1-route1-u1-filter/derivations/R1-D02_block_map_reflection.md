<!--
title: R1-P1 derivation R1-D02
id: QL-20261121-01/R1-P1/D02
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: proposed by QUASAR; LATTICE review v1 (REQUIRES CORRECTION (moderate)) gives per-claim verdicts
internal-source: WitnessLab/06_QUASAR_RESEARCH/derivations/R1-D02_block_map_reflection.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# R1-D02: block maps, θ- and translation-intertwining, and reflection positivity after blocking (LATTICE check 2)

QL-20261121-01 · QUASAR · Route 1 phase 1 · 2026-11-21. These are elementary proofs by QUASAR, pending LATTICE verification. Computational checks are in R1-E03.
- **Depends on:** D08.2, D08.3; BIJ 1984 §2.3–2.4 (S-130, [P] opened).
- **Used by:** R1-D01 S7, R1-P1 report.

## Setting
Fine lattice Λ, with link reflection θ in a plane Π between two time slices, Λ = Λ₊ ⊔ Λ₋. 𝔄₊ is the set of bounded functions of links with both endpoints in Λ₊. Blocks of side b^k tile Λ, and **Π lies on block boundaries**. A coarse map B: Ω → Ω′ is measurable, and θ′ and 𝔄′₊ are the coarse analogues.

## Lemma 1 (what D08.3 actually needs; Proved here)
D08.3 uses three things:
- (i) θ′∘B = B∘θ;
- (ii) τ′∘B = B∘τ^{b^k};
- (iii) for each F′ ∈ 𝒮′, F′∘B is supported in a fine time slab of finite thickness s, together with **positivity of the fine transfer matrix T ≥ 0** (Lüscher).

It does **not** use reflection positivity of the coarse measure. Also, s need not be < b^k (correcting the "s_k < b^k" phrasing of D08.3): if s ≥ b^k, write nb^k − s = (n−q)b^k − s′ with q = ⌊s/b^k⌋ and 0 ≤ s′ < b^k. Then C e^{−m_* n} = (C e^{−m_* q}) e^{−m_*(n−q)}, and D08.1 applies unchanged (LATTICE defect 7 already noted that any fixed offset is absorbed).

## Lemma 2 (RP survives blocking; Proved here)
Assume (i) and the **locality condition (L)**: every coarse variable attached to a coarse site or link inside the coarse positive half is a function of fine links in Λ₊ only. If μ is RP with respect to θ, then μ′ = B_*μ is RP with respect to θ′.

*Proof.* For F′ ∈ 𝔄′₊, (L) gives F′∘B ∈ 𝔄₊, and (i) gives (θ′F̄′)∘B = θ(F̄′∘B). By D08.2, ⟨θ′F̄′·F′⟩_{μ′} = ⟨θ(F̄′∘B)·(F′∘B)⟩_μ ≥ 0. ∎

Condition (L) holds for BIJ-type averages when blocks do not straddle Π: a coarse link between two positive blocks uses contours inside those two blocks plus straight segments between them (BIJ Fig. 2 [P]). It fails for site reflections whose plane cuts through blocks. Choose link reflection at block boundaries.

## Lemma 3 (gauge-fixed averaging; Proved here)
Gauge fixing inside the fluctuation integral does not change μ′. BIJ §2.4 [P]: an axial gauge on a maximal tree in each block is inserted, and "the density ρ₁(v,ψ) is unchanged, as we take ∫du = 1". More generally, for gauge-invariant integrands, an exact Faddeev–Popov insertion (a tree gauge on a compact group: unique representative, Jacobian 1) leaves expectations unchanged. Hence:
- (a) **Intertwining is a property of the averaging map B alone, not of the gauge fixing.** The gauge fixing affects only the *representation* of the effective density, e.g. its polymer decomposition, which need not be termwise θ-symmetric.
- (b) If instead a block map is *defined* through a gauge condition (coarse variables read off in a fixed gauge), then (i)–(ii) need a θ- and τ-invariant gauge condition with a unique, measurable representative:
  - complete temporal-axial gauge needs a reference slice, which breaks either θ or τ^{b^k};
  - Landau-type gauges are θ-invariant conditions, but have Gribov copies at large fields, so the representative is not unique.
  - **Use gauge-covariant averaging, with no gauge fixing in B.** This is what Balaban/BIJ do: gauge fixing appears only in the fluctuation integral and only on small fields (S-114 [T]).

## Proposition 4 (the BIJ corner construction does not intertwine θ for non-abelian G; Computationally verified, R1-E03)
- Base points at block corners with one fixed contour pattern (BIJ §2.3, Fig. 1 [P]). θ maps the base corner of a block to the *opposite* corner of the reflected block, and reflects the contour pattern.
- **For U(1) small fields** the argument average is linear: V(y,y′) = φ(y) − φ(y′) + mean_x A(x→x+b e_μ), with φ(y) = mean_x A(Γ_{y,x}).
  - The contour and base-point dependence is a coarse gauge transformation.
  - Gauge-invariant coarse data are contour-independent, so (i) holds on gauge-invariant observables. (Proved here; E03: ≤2e−16)
- **For SU(2)** (projection-of-sum or exp-mean-log averaging), coarse ½Tr plaquettes of θ′B(U) and B(θU) differ by 6.8e−3, 1.0e−1 and 6.0e−1 at link spreads σ = 0.05, 0.15 and 0.3. This is the same order as 1−½Tr itself. So **(i) fails** for the corner construction. (Computationally verified counterexample)

## Proposition 5 (a θ-equivariant replacement; Proved here + Computationally verified)
- Take odd block side, base point at the block centre c, and a contour multiset invariant under the reflections of the block (all axis orderings of staircase paths). Use an averaging rule that is a **symmetric function of the multiset** and gauge-covariant, e.g. the projection Π_{SU(N)} of the sum, which is defined off a measure-zero degenerate set; use any measurable extension there.
- Then (i) and (ii) hold, (L) holds for link reflection at block boundaries, and coarse gauge invariance holds.
- E03: ≤7.2e−16 for SU(2).
- A *non-symmetric* rule (exp of mean log relative to the first transport) breaks (i) even with symmetric contours (E03: up to 1.06).

**What remains (Hypothesis R1-H03).** Balaban's estimates must hold for this θ-equivariant averaging. BIJ [P] remark that "almost any definition of average would do" in the large-field branch, and that "the choice of gauge fix is not very important". This is encouraging, but it is not a statement about S-113's estimates. The averaging lemma is abelian-blind (U(1) passes trivially), so it is not a filter-relevant step.
