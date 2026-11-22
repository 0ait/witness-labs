<!--
title: INV-001 A–I submission packet v1
id: QL-20261121-01/INV-001/packet-v1
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: submitted to LATTICE; review v1 returned REQUIRES CORRECTION (minor)
internal-source: WitnessLab/06_QUASAR_RESEARCH/submissions_to_lattice/QL-20261121-01-INV001-v1.md
body: copy of the internal record; only local absolute paths were redacted (see REDACTIONS.md)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
> **Status (added for publication): Submitted to LATTICE 2026-11-21 18:16 CT; review v1 returned REQUIRES CORRECTION (minor).** The "DRAFT. Not sent" line below is the original v1 header, preserved unchanged; it predates transmission.

# QUASAR Submission — QL-20261121-01 (INV-001) — submission v1

*DRAFT. Not sent. Transmission to LATTICE is the Commander's/parent's decision.*

## A. Identification
- Title: INV-001: the bridge from a finite-lattice spectral gap to a uniform, strictly positive continuum, infinite-volume mass gap
- ID: QL-20261121-01 / INV-001
- Version: v1
- Date (America/Chicago): 2026-11-21
- Status: draft for LATTICE review (not transmitted)
- Researcher: QUASAR (session S01-B)
- Validator: LATTICE
- Path: `WitnessLab/` (repo `<internal-lab-root>`). Primary report `05_RESEARCH_WORKSTREAMS/WS01_spectral_gap/INV-001_report.md`

## B. Original problem
- Original statement (as delegated): "What exactly is the bridge from a finite-lattice spectral gap to a uniform, strictly positive mass gap in the continuum, infinite-volume theory?" Context: the Clay Yang–Mills Existence and Mass Gap problem (Jaffe–Witten official description, archived in `03_LITERATURE_AND_SOURCE_ARCHIVE/official_sources/`).
- Desired result:
  - a precise statement of what a bridge theorem must assert (objects, limits and their order, trajectory, required convergence);
  - rigorous proofs of whatever parts of the bridge can be proved;
  - a literature baseline;
  - the precise missing estimates, stated as quantified inequalities;
  - ranked attack routes.
- Constraints:
  - every claim carries a constitution knowledge label;
  - lattice-unit gaps, strong-coupling gaps, area law, single-correlator decay and 2D results must not be presented as the 4D mass gap;
  - all computation is local;
  - website restrictions are not circumvented.
- Definitions and notation:
  - G compact simple, with a faithful unitary representation of dimension N;
  - Λ_L = (ℤ/Lℤ)³×ℤ with spacing a;
  - Wilson action S_β = βΣ_p(1−(1/N)Re Tr U_p);
  - transfer matrix T_{β,L} on L²(G^{spatial links});
  - m_lat = −log(λ₁/λ₀) and Δ = m_lat/a;
  - a(β) a lattice-spacing trajectory;
  - Schwinger functions S^{(n)} and OS reconstruction ⟨F̂,e^{−tH}Ĝ⟩ = S(θF̄·τ_tG).
- Assumptions (explicit): none beyond the definitions. Which sector λ₁ is taken over, and which renormalisation condition fixes a(β), are part of the question.
- Domain / boundary conditions: periodic spatial boundary conditions; time direction infinite or periodic.
- Type: theoretical, with supporting computation.
- Complete vs partial:
  - Complete: an unconditional proof that the needed uniform estimates hold for 4D Yang–Mills, which would solve the gap part of the Millennium problem.
  - Partial: an exact formulation, proofs of the implication and obstruction lemmas, and quantified missing estimates.

## C. Executive mathematical summary
- **Investigated.** The logical structure of the lattice→continuum gap transfer; the role of sectors, limits and renormalisation trajectories; and the reach of existing rigorous results.
- **Established, as proposed proofs pending LATTICE verification.**
  - (D01, Established-theorem level) A uniform-*rate* exponential time-clustering of a cyclic family in an OS-reconstructed theory is equivalent to σ(H)∩(0,Δ)=∅ with a unique vacuum. Prefactors may depend on the observable.
  - (D02) A lattice local-sector gap m^{loc} gives lattice clustering. The uniform physical bound m^{loc}(β,L) ≥ Δa(β) passes to the limit under Schwinger-function convergence, giving the lattice form of the bridge theorem.
  - (D03.2) If m^{loc}/a → ∞, the limit is trivial. Hence non-trivial limits force the window Δa ≤ m^{loc} ≤ Ca.
  - (D04/D05/D06, Established counterexamples) Finite-volume or full-sector gaps are neither sufficient nor necessary, and a single correlator's decay is insufficient.
  - (D07 + E01) Exact 2D spectrum.
  - (D08.1) Decay along an arithmetic progression suffices for a gap on the generated subspace.
  - (D08.3, conditional) β-uniform clustering of block-spin effective measures at a fixed physical scale implies the uniform physical gap.
- **Uncertain / open.** Every hypothesis of the bridge theorem for 4D non-abelian G: the uniform gap ME1, convergence and field content ME2, and the upper window ME3. These are Open problems. Nothing here proves a 4D mass gap.
- **Why it matters.** It isolates the gap problem into explicit inequalities. It shows which known results (strong coupling, Balaban, MRS, stochastic quantisation, finite groups) supply none of them, and why. It converts the bridge into checkable conditional statements, including one stated against the 2026 claimed existence construction (ME2′).

## D. Literature
Full baseline: `05_RESEARCH_WORKSTREAMS/WS01_spectral_gap/INV-001_literature.md` (register rows S-101…S-128; DOIs Crossref-checked).
- **Sources consulted (key).**
  - Lüscher 1977 (S-101, transfer matrix positivity) and OS78 (S-005): lattice objects.
  - Seiler LNP159 (S-105) and Shen–Zhu–Zhu CMP 400 (S-106: Thm 1.2 uniqueness, Thm 1.4 LSI, Cor 1.6 exponential decay for |β|<1/(16(d−1))): strong-coupling, lattice-unit gaps.
  - SZZ-YMH (S-107); Cao–Nissim–Sheffield (S-108/109): area law, not a gap.
  - Adhikari–Cao AoP 53 (S-111): finite G, weak coupling, rate (β/2)Δ_G in lattice units.
  - Balaban 1984–89 (S-006/7, S-112…S-119): UV stability on a torus, conditional on small effective couplings; no correlation functions or infinite volume.
  - Magnen–Rivasseau–Sénéor 1993 (S-121): SU(2) with an IR cutoff.
  - Chatterjee (S-122): Problems 5.1/5.2 open.
  - CCHS / Chevyrev–Shen (S-123…S-125): 2D/3D stochastic quantisation.
  - Guth 1980 / Fröhlich–Spencer 1982 (S-127/128): massless 4D U(1) phase.
- **Related results.** The OS reconstruction framework (S-003/4, S-126).
- **Competing approaches.**
  - Multiscale RG (Balaban, MRS); stochastic quantisation; functional inequalities (SZZ); finite-size criteria.
  - The 2026 claimed existence construction (parallel worker's audit; S-013/S-014): claimed existence of subsequential limits, no gap claimed.
- **Potential novelty (only potential until checked).**
  - The explicit packaging of D03.2 (a β-uniform lattice-unit gap certifies triviality) and of D08.3 (the conditional crossover reduction to hypothesis X).
  - The ME2′ formulation relative to the 2026 artifact.
  - All are elementary and very likely known in some form. No novelty search was done beyond the sources above.
- **Open questions.** ME1, ME2, ME3, ME-R1 and ME-R2 (Section E/I); Chatterjee Problems 5.1/5.2.
- **Not opened (paywall/bot-block; not circumvented).** Project Euclid full texts (Lüscher, OS78, Balaban, MRS) and Glimm–Jaffe. Statements from them are abstract-level, or come from verified excerpts as marked.

## E. Mathematical development
- **Dependency graph.**
  - D01 ← OS reconstruction.
  - D02 ← D01 + transfer-matrix properties (S-101, S-005).
  - D03 ← D01, D02.
  - D04 ← D01, D02.
  - D05 ← D01–D03.
  - D06 ← D01.
  - D07 ← Peter–Weyl/Schur orthogonality (checked by E01).
  - D08 ← D01, D02 (2D check: E01).
  - Report ← all.
- **Derivations and proofs.** `06_QUASAR_RESEARCH/derivations/INV001-D01.md` … `INV001-D08.md` (full proofs). Statements:
  - **D01.** Assume OS+, (T), (B). If {F̂: F∈𝒟} is dense and |C_{F,F}(t)| ≤ C(F)e^{−Δt} for t ≥ t_F, then E_H([0,Δ)) = |Ω⟩⟨Ω|. Conversely, a gap Δ gives |C_{F,G}(t)| ≤ ‖QF̂‖‖QĜ‖e^{−Δt}.
  - **D02.** (a) |⟨F;G⟩_n| ≤ ‖QFΩ_L‖‖QGΩ_L‖e^{−m^{loc}n} for contractible-loop observables. (b) (C1)+(U) ⇒ |S(F,G;t) − s̄(F)s(G)| ≤ c(F)c(G)e^{−Δt}. (c) Adding OS and cyclicity ⇒ gap ≥ Δ.
  - **D03.2.** (C1)+(T)+[m^{loc}(β_k,L_k)/a_k → ∞] ⇒ S(F,F;t) = |s(F)|² for all F∈𝒟 ⇒ ℋ = ℂΩ.
  - **D04.2.** At fixed spacing, uniform m^{loc}(L) ≥ m ⇒ time-clustering of the limit, a gap ≥ m for the reconstruction from 𝒟, and no non-trivial mixture of clustering states.
  - **D08.1.** For A ≥ 0 a self-adjoint contraction: ⟨ψ,A^{nb−s}ψ⟩ ≤ C_ψe^{−μn} for all ψ∈𝒮 ⇒ ‖A|_{𝒦₀}‖ ≤ e^{−μ/b}.
  - **D08.3.** (Conditional) Hypothesis (X), β-uniform clustering at rate m_* of the block-spin pushforward at physical scale a_*, implies m(T|_{𝒦_β}) ≥ (m_*/(b a_*))·a(β).
  - **Exact counterexamples.**
    - D04 Example A: m(L) = log coth(LK) → 0 with gapped pure phases.
    - D04 Example B: twisted massless field, m(L) > 0 ∀L, limit 0.
    - D05: m_lat = 2asinh(m₀a/2).
    - D06: Wick square decays at 2m, gap m.
    - D07: λ_r = a_r^L in 2D.
- **Alternative approaches considered.** Routes R1–R5 (report §6). Refuted strategies FP01 (transfer of a lattice-unit gap) and FP02 (full-sector finite-volume gap) are kept in `11_FAILED_APPROACHES/failed_proofs/`.
- **Formal statements offered.** None. No Lean statements are claimed for INV-001.

## F. Computational evidence
- **Environment and tool versions.** Python 3.13.5, numpy 2.5.5, scipy 1.18.1, mpmath 1.3.0, Linux x86_64, 8 cores (each experiment's ENV.txt).
- **Code.** `06_QUASAR_RESEARCH/experiments/INV001-E01…E04/` (scripts, RUN.md, outputs with SHA256SUMS, failed_runs).
- **Inputs, parameters, seeds.** Deterministic, with no random seeds. Parameters are listed in each RUN.md.
- **Precision and arithmetic mode.** E01 uses mpmath at 60 digits for Bessel/character data and double-precision scipy nquad for cross-checks. E02–E04 use double-precision dense/sparse eigensolvers.
- **Results.**
  - E01: βσ_lat → 3/2 (SU(2)), 1/2 (U(1)); at β=4096, βσ = 1.500183116636. Trajectory ℓ=4, β=16384: L=418, m_lat=0.0382702, Δ=3.99962 ≈ σℓ. Decimation t_{1/2}: 0.97666 → 3.13e−11 (b=32).
  - E02: SU(2) single-plaquette KS gap 12.0073 (g²=8), 3.2691 (g²=1), 3.96855 (g²=0.05). Z₂ ladder at n=16: local gap 7.98 (J/h=0.25) … 30.35 (16), with torelon gap ∝ n (J=8: 1.2611 at n=4 → 5.0453 at n=16).
  - E03: TFIM L=18 splitting 1.008e−10 / 9.09e−7 / 3.28e−4 (h = 0.3/0.5/0.7); bulk gap → 4(J−h).
  - E04: single-link SU(2) Langevin gap ≈ β+½ (256.50246067 at β=256), while the Bakry–Émery bound 2−β is void for β ≥ 2 and Holley–Stroock gives 3e^{−2β}.
- **Tests, reference cases, and second-method cross-checks.**
  - E01: Bessel vs quadrature 7.5e−51; 1×1 torus character sum vs nquad ≤1.6e−16.
  - E02: tridiagonal = Galerkin = Mathieu (except the documented scipy failure at q=6400, CF02); Gauss projector ≤7.1e−15.
  - E03: ED vs free fermions ≤5e−14.
  - E04: β=0 exact value 3 reproduced to 1e−8; n=4000 vs 8000 elements ≤4.3e−7.
- **Error, stability, and conditioning analysis.**
  - CF01: nested mpmath quadrature hung; replaced.
  - CF02: scipy Mathieu at large q is unreliable; two-method agreement used instead.
  - E04 rescales the weight by e^{−β} to avoid overflow and drops underflowed nodes.
- **What the experiments can and cannot establish.** They are finite, toy or 2D computations (Computationally verified finite results or Numerically supported results). They illustrate D03, D04 and D07 and the failure of bare Bakry–Émery. They say nothing about the 4D mechanism, and in particular nothing about a 4D mass gap.

## G. Adversarial considerations
- **Weaknesses.**
  - The proofs are QUASAR's own and unverified.
  - Transfer-matrix properties are taken from abstracts and secondary sources, because S-101 and S-005 were not opened.
  - D08.3's slab version of the OS vector representation is sketched, not written in full.
  - The definition of ℋ^{loc} via contractible loops needs checking for groups with trivial centre (G₂) and for disconnected G.
- **Fragile assumptions.**
  - Cyclicity (H1) of 𝒟 in the *full* physical Hilbert space (LATTICE baseline §11(a)).
  - The independence of a(β) from the gap.
  - The time-continuity (T) used in D03.2.
- **Potential counterexamples.**
  - U(1)₄ (S-127/128) shows that any argument that also applies to abelian G must fail.
  - Phase or subsequence dependence of limits (relevant to ME2′).
- **Edge cases unexamined.** Non-periodic boundary conditions; θ-terms; G with non-trivial π₀; the precise renormalisation of 𝒟 (Wilson-loop perimeter terms).
- **Possible contradictions.** None found. The D03 window is consistent with E01 (m_lat→0 while Δ stays finite) and with S-111 (a growing lattice-unit rate in a theory with a trivial continuum).

## H. Specific requests to LATTICE
- **Verify.** D01 (steps 2–4), D02(b), D03.2, D04.2, D08.1 and D08.3.
- **Redo.** E01 Δ = 3.99962 at ℓ=4, β=16384; E04 at β = 8 and 256; one E02 ladder value (n=16, J/h=8, local gap 14.944574).
- **Most vulnerable steps.**
  - D08.3: the slab transfer-matrix representation, and the claim that the coarse correlation is ≥ 0 by RP.
  - D03.2: interchange of limits at t>0.
  - ℋ^{loc} vs the cyclicity requirement.
- **Assumptions to attack.**
  - Whether (U′) (family-wise) really suffices without cyclicity in the full ℋ.
  - Whether ME2′ is the right formulation of the gap relative to the 2026 artifact (quantifiers over phases and subsequences).
- **Alternatives to explore.** LATTICE's L-04 (3D/4D small-volume Hamiltonian enclosures) and L-02/L-11 (crossover LSI constants), aligned with routes R3 and R2.
- **Where stuck.** The crossover window between Balaban's small-coupling regime (S-119: effective couplings ≤ γ) and strong-coupling thresholds (S-106: |β| < 1/(16(d−1))). No known tool controls effective measures there, and that is exactly ME-R1.

## I. Current conclusion
- [ ] Established result
- [ ] Proposed proof requiring independent verification
- [ ] Computationally supported result
- [ ] Strong conjecture
- [ ] Preliminary hypothesis
- [ ] Unresolved question
- [ ] Refuted hypothesis
- [x] Partially solved problem

**Justification.**
- The sub-question "what exactly is the bridge" has been answered in a precise conditional form, with proposed proofs pending verification: D01–D04.2, D08.
  - The bridge implication itself is soft (Established-theorem level).
  - The whole content is the uniform physical-unit estimate ME1 together with ME2 (convergence, OS, non-triviality, cyclicity) and the window ME3.
- The constituent claims are labelled in Section E. The counterexamples are Established. The experiments are Computationally verified finite results or Numerically supported results.
- The 4D mass gap itself remains an **Open problem**. Nothing here advances it beyond the conditional reductions stated.

**Recommended next investigation.**
1. R1: specify the β-uniform class of effective actions for which a strong-coupling clustering theorem would yield (X). Compare it with Balaban's effective-action bounds at the first scale where g_k² > γ.
2. R2: test a coarse-scale Poincaré constant on the exact 2D decimated measures (E01), then on a 3D Z₂/U(1) toy, contrasting U(1) with SU(2) per S-127/128.
3. Pin ME2′ against the Lean target once LATTICE's formal target (L-09) is fixed.
