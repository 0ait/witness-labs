<!--
title: Gauge-group scope
id: QL-20261121-01/01/group_scope
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: specification v1; LATTICE review flags pending corrections
internal-source: WitnessLab/01_PROBLEM_FORMALIZATION/group_scope.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
> **Public-archive note (2026-11-21):** LATTICE review 2026-11-21 flags PO-11/PO-12 sector and β-convention issues (defects 8, 9); corrections pending in v2. The body below is unchanged.

# Group scope — "any compact simple gauge group G" (QL-20261121-01)

## Textual basis
"Prove that for any compact simple gauge group G …" [JW p.6]. JW define neither "compact" nor "simple". Elsewhere they say "compact gauge group G" [JW p.1] and use an "invariant quadratic form on the Lie algebra of G" [JW p.2]. **Reading adopted (A3 in theorem_specification.md):** "compact simple" is meant in JW's sense, i.e. the usage standard in gauge theory: a compact Lie group G whose Lie algebra 𝔤 is simple (nonabelian, no proper nonzero ideals). Under this reading:
- every global form G = G̃/Z with Z ⊂ Z(G̃) is included (e.g. SU(N) and SU(N)/ℤ_N; Spin(n) and SO(n));
- U(1), tori, and semisimple non-simple groups such as SU(2)×SU(2) are excluded;
- disconnected groups with simple identity component (e.g. O(n)) are not clearly in or out. Our reading treats the target as connected G, and records disconnected groups as an over-coverage when a proof includes them.
- "Simple" in the strict abstract-group sense (trivial center) would exclude SU(N). No physics reading uses that, and JW's own example SU(3) [JW p.3] has center ℤ₃. Rejected as a reading.

## Classification (compact, simply connected G̃; every compact connected G with simple 𝔤 is G̃/Z) [standard; QUASAR transcription. dim column cross-checked 2026-11-21 against SymPy 1.14 root systems (2·|Φ⁺| + rank) for A1,A2,A3,A7,B2,B3,B5,C3,C4,D4,D5,D6,G2,F4,E6,E7,E8: all agree. Centers and h∨ not yet machine-checked]
| Type | Rank range (no duplicates) | G̃ | dim 𝔤 | Z(G̃) | Other global forms | dual Coxeter h∨ |
|---|---|---|---|---|---|---|
| A_n | n ≥ 1 | SU(n+1) | n(n+2) | ℤ_{n+1} | SU(n+1)/ℤ_k for k ∣ n+1 | n+1 |
| B_n | n ≥ 2 | Spin(2n+1) | n(2n+1) | ℤ₂ | SO(2n+1) | 2n−1 |
| C_n | n ≥ 3 | Sp(n) | n(2n+1) | ℤ₂ | Sp(n)/ℤ₂ | n+1 |
| D_n | n ≥ 4 | Spin(2n) | n(2n−1) | ℤ₄ (n odd), ℤ₂×ℤ₂ (n even) | SO(2n), PSO(2n); for n even also the half-spin groups Ss(2n) (Ss(8) ≅ SO(8) by triality) | 2n−2 |
| G₂ | — | G₂ | 14 | 1 | — | 4 |
| F₄ | — | F₄ | 52 | 1 | — | 9 |
| E₆ | — | E₆ | 78 | ℤ₃ | E₆/ℤ₃ | 12 |
| E₇ | — | E₇ | 133 | ℤ₂ | E₇/ℤ₂ | 18 |
| E₈ | — | E₈ | 248 | 1 | — | 30 |
Low-rank coincidences (why the ranges start where they do): A₁ = B₁ = C₁ (SU(2) ≅ Spin(3) ≅ Sp(1)); B₂ = C₂ (Spin(5) ≅ Sp(2)); A₃ = D₃ (SU(4) ≅ Spin(6)); D₂ = A₁ × A₁ is not simple; D₁ is abelian.

## Where the global form (center) matters [QUASAR, to investigate in WS10]
- **Local gauge-invariant fields on R⁴** (polynomials in F, DF) depend only on 𝔤 at the classical level. Whether the quantum correlation functions of local fields depend on the global form is a WS10 question. On R⁴ we expect them not to; on T⁴ the global form affects the flux sectors.
- **On T⁴ and on the lattice** the global form enters: the Wilson action in a representation that is not faithful on Z(G̃) changes the configuration space. 't Hooft twisted boundary conditions and Z(G̃)-flux sectors exist. Center symmetry relates to confinement, which is *not* required by T★.
- **Line operators** (Wilson / 't Hooft loops) are sensitive to the global form. They are not required by T★.
- **Group-dependent constants** that any uniform proof must track: dim 𝔤, h∨ (enters b₀ = 11h∨/(48π²) in the β = 1/g₀² convention), the Casimir of the representation used in the Wilson action, and the curvature (Ricci) lower bound of G with its bi-invariant metric. The Ricci bound enters Bakry–Émery-type arguments; per the abstract of arXiv:2510.22788 (opened) its failure for U(N) is exactly what obstructs that method.

## Transfer between groups
No result we know reduces T★ for all G to finitely many G. Any proof for SU(N) only, or for classical groups only, must be supplemented. The exceptional groups G₂, F₄, E₆, E₇, E₈ can never be silently omitted (mission §14 WS10).

## Comparison: scope of the 2026 OpenAI construction (claimed)
`GaugeGroup` in its public spec is a closed subgroup of U(n+1) with a simple, nonabelian real Lie algebra (`PublicTheory.lean`, `GaugeGroup.IsSimple`). Every compact Lie group has a faithful finite-dimensional unitary representation (Peter–Weyl, standard), so the class covers every compact G with simple 𝔤, including disconnected ones. The Wilson action uses the trace in that chosen faithful representation, normalized by its dimension (`PublicWilson.lean`, `wilsonEnergy`). Coverage of 𝒢 is therefore claimed in full for *existence only*.
