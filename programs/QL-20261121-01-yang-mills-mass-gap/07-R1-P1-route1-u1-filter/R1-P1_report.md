<!--
title: Route 1 phase 1 report (R1-P1)
id: QL-20261121-01/R1-P1/report
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: v1; LATTICE review v1: REQUIRES CORRECTION (moderate)
internal-source: WitnessLab/05_RESEARCH_WORKSTREAMS/WS05_constructive_rg/R1-P1_report.md
body: copy of the internal record; only the role title of the human principal was changed to "principal" (see REDACTIONS.md)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
> **Public-archive note (added for publication):** LATTICE review v1 of R1-P1 returned **REQUIRES CORRECTION (moderate)**, with nine defects D-R1P1-1…9 (see this section's README). This v1 is published as reviewed; corrections will appear in a later v2 addendum. The body below is unchanged in technical content.

# Route R1, phase 1: report (QL-20261121-01, WITNESS LAB, QUASAR)

2026-11-21, 18:57–19:20 CT. Authorised by the principal at 18:56 CT (t14u, "begin route 1"). Not authorised and not done: Route 2, the Lean measure lemma, the 2026 rebuild, publication, and any messaging.

**Nothing in this report proves, or claims progress toward, the Yang–Mills mass gap.** All 4D gap statements remain Open problems. Labels: Established / Proved here / Conditional / Numerical evidence / Heuristic / Conjecture.

Citation levels:
- [P] primary text opened this session;
- [A] abstract or excerpt opened;
- [T] title or Crossref only.

## Files
- Derivations (06_QUASAR_RESEARCH/derivations/):
  - `R1-D01_skeleton_and_U1_filter.md` (check 4);
  - `R1-D02_block_map_reflection.md` (check 2);
  - `R1-D03_X_vs_ME1_and_fixed_coupling_reduction.md`;
  - `R1-D04_cluster_expansion_threshold.md` (check 3).
- Experiments: `R1-E01` (4D U(1) vs SU(2) Monte Carlo), `R1-E02` (running-coupling bookkeeping), `R1-E03` (block-map θ test).
- Hypotheses: `R1-H01` (H-Bal), `R1-H02` (H-Gap), `R1-H03` (θ-equivariant averaging). Proof attempt: `R1-PA01`.
- Failed approaches: `11_FAILED_APPROACHES/failed_proofs/R1-FP01`, `failed_experiments/R1-FE01`, `lessons_learned/R1-LL01`.
- Sources: S-129…S-135 appended to the register.

## 1. Go/no-go: the 4D U(1) filter (check 4), verdict GO, with a qualification
R1 is written as steps S0–S9 (R1-D01 §1). For 4D U(1):
- **S0–S3 hold.** RP; Balaban's small-field step, large-field control and iteration are group-agnostic. BIJ [P]: "the overall strategy and many of the details are common to the abelian and nonabelian case". Labelled Heuristic for 4D U(1).
- **S7 and S8 hold** (block-map compatibility; D08.3 is group-agnostic).
- **S5 and S9** are open for both groups.
- **Two steps fail:**
  - **S4 (crossover attainment) FAILS.** Pure U(1) has b₀ = b₁ = 0 (free photon), so with g₀² < γ the effective coupling never leaves ]0,γ] and k_* = ∞. **This is exactly where asymptotic freedom enters**: b₀ > 0 makes k_*(β) ≈ β/(4N b₀ ln b) finite (R1-E02).
  - **S6 (crossover clustering) FAILS.** Villain U(1) with bare g₀² ∈ (γ, 0.168) has "g² > γ" already at k=0, yet it is non-confining (Guth S-127 [A]: bound "holds for g² < 0.168 … electric charges are not confined") and massless (S-128 [T]; Driver S-132 [A]: converges to "a renormalized free electromagnetic field"). Lemma A (Conditional) then shows the U(1) analogue of S6 is false.
- **So AF at S4 is not the only place non-abelian structure must enter.** S6 must use a property of SU(N) that is
  - (i) non-perturbative: target rate ~exp(−1/(2b₀γ)), Heuristic;
  - (ii) absent from U(1) at the *same* small coupling.
- **No hidden reliance elsewhere.** The small/large-field split, gauge fixing (an exact axial tree, Landau-type only on small fields, so no Gribov issue), and Villain versus Wilson (the U(1) obstruction is Established for Villain [A] and for general energy functions including Wilson in Driver's sense [A]) are all group-agnostic.
- **D03.3 circularity does not kill R1.** a(β) = a_* b^{−(k_*−1)} is a coupling-defined, non-gap scale.
- **"X is ME1 relabelled" is TRUE as a statement** (R1-D03 Prop. 1, Proved here) but does not kill the method. See §5.

## 2. Check 1: Balaban's bounds at the first scale with g_k² > γ
What we opened:
- BIJ 1984 (S-130, author-hosted scan) [P];
- S-119 abstract and the Theorem 1 opening [A, from INV-001];
- the S-007 introduction [A, from INV-001];
- Jaffe–Witten (S-001) [P].

The Balaban–Jaffe 1986 Erice exposition (S-131) and the CMP texts S-112…S-118 were **not opened**: the Springer PDF returned HTML, the article pages gave a client challenge (not circumvented), and Project Euclid blocks bots.
- **At k_* itself nothing holds.** S-119 Theorem 1 requires the *whole* coupling sequence to lie in ]0,γ] [A]. At the first k with g_k² > γ the hypothesis is violated, and the theorem says nothing about ρ_{k_*}.
- **What does hold is ρ_{k_*−1}, with the Theorem 1 form and bounds.** Apply the theorem to the truncated sequence, i.e. take scale k_*−1 as the "unit lattice". Per step, 1/g² moves by only 2b₀ ln b (0.064 for SU(2), b=2; R1-E02), so g²_{k_*−1} ∈ (γ/(1+0.064γ), γ]. In practice "the first scale with g² > γ" is a *weak-coupling* scale with coupling ≈ γ.
- **Volume: a finite periodic lattice** ("periodic lattice T_η", S-007 intro [A]). The bounds are "uniform in the lattice spacing" [A] and local in form (polymer localisation; BIJ [P] "multi-scale cluster expansion"). Uniformity in the number of unit blocks is **not asserted** in any text we opened.
  - Balaban's coupling-sequence control ("the second aspect") is also not proved in S-007 by its own introduction [A]. Whether S-117…S-119 supply it was not verified.
- **L-uniformity that would have to be added (R1-H01):**
  - (a) block-number-independent constants in the large-field R-operation, including the per-block vacuum-energy subtraction. BIJ [P] identify exactly this as the 4D difficulty: "the sum over k would diverge … we are not cancelling the vacuum energy contribution from large fields at each step";
  - (b) a uniform polymer-decay rate;
  - (c) an infinite-volume limit of the polymer representation;
  - (d) compatibility with a θ-equivariant averaging (R1-H03).
- **Secondary-literature note.** The INV-001 baseline already has the JW quotes that Balaban's results "need to be extended to the study of expectations of gauge-invariant functions" and "New ideas are needed to prove the existence of a mass gap that is uniform in the volume" [P].

## 3. Check 2: block map, θ, translations, RP (R1-D02; R1-E03)
- **D08.3 needs** (i) θ-intertwining, (ii) τ^{b^k}-intertwining and (iii) slab support, together with fine T ≥ 0. It does **not** need coarse RP. The "s_k < b^k" condition can be dropped, since any fixed offset is absorbed (Proved here).
- **RP survives blocking** under (i) plus locality (L), with blocks not straddling the reflection plane (link reflection at block boundaries) (Proved here, Lemma 2).
- **Gauge-fixed averaging.** The axial-tree gauge fix inside the fluctuation integral leaves the density unchanged (BIJ [P]: "The density ρ₁(v,ψ) is unchanged"). Intertwining is therefore a property of the averaging map alone. Block maps *defined* through a gauge condition fail (i) or (ii): temporal-axial needs a reference slice, and Landau-type gauges have Gribov non-uniqueness at large fields (Proved here, Lemma 3).
- **The BIJ corner construction does not intertwine θ for SU(2)** (R1-E03). The coarse ½Tr-plaquette discrepancy is 6.8e−3, 0.10 and 0.60 at σ = 0.05, 0.15 and 0.3, while gauge covariance holds to 1e−15.
- **For U(1) small fields it intertwines automatically.** The average is linear, so the contour dependence is pure gauge. This makes the abelian version a degenerate test (R1-FE01).
- **Fix:** a centre base point, a reflection-symmetric contour multiset and a symmetric averaging rule (projection of the sum) intertwine to ≤7e−16. A non-symmetric rule fails even with symmetric contours. Whether Balaban's estimates survive the change is R1-H03 (plausible, unverified).

## 4. Check 3: cluster expansions for non-local actions (R1-D04)
- **Yes, uniformly in β.** Dobrushin/Gross-type and Kotecký–Preiss-type criteria (S-134, S-135 [T]; standard forms stated, texts not opened) accept infinite-range interactions with exponentially decaying tails. They depend only on weighted interaction norms, hence are uniform over norm-bounded classes.
- **Threshold.** The interaction must be small in a weighted norm: near-Haar link marginals, and an effective plaquette coupling below the strong-coupling threshold. For SZZ (S-106) converted, that is **β_eff < 1/12 (g² > 48) for SU(2)** and g² > 32 for SU(3).
- **RG output at the crossover:** coupling ≈ γ, i.e. β_eff ≈ 2N/γ = **40 for SU(2) at γ=0.1**. That is a **≈480× mismatch**, with link marginals concentrated near 1. The perturbative flow from γ hits its pole (152 steps at γ=0.1) before reaching the threshold.
- **Verdict:** the literal plan "strong-coupling clustering of the effective measure at the crossover" is **refuted** (R1-FP01).

## 5. The real obstruction, and what X adds beyond ME1 (R1-D03)
- **X ≡ ME1 restricted to coarse-resolution observables**, with m_* = Δa_* (Prop. 1, Proved here). As a statement, X adds nothing.
- **What R1 adds is a β-free reformulation (Prop. 2, Conditional):** ME1|𝒦 ⇐ **H-Bal** (R1-H01: L-uniform Balaban up to the γ-exit, effective measures in a β-independent class 𝒜_γ) + **H-Gap** (R1-H02: uniform clustering over 𝒜_γ at fixed weak coupling γ). In the model flow, the remaining IR distance from γ is independent of β (R1-E02). The asymptotic β→∞ problem becomes one fixed-coupling problem. This is real structure, and the only setting in which a computer-assisted step (LATTICE L-04) is even conceivable.
- **The real obstruction is H-Gap.** It is a lattice mass gap at one fixed *weak* coupling for a class of effective actions. Plausibly it is at least as hard as the open fixed-β Wilson lattice gap (if 𝒜_γ ∋ Wilson at β = 2N/γ; Heuristic). It is false for the U(1) analogue (Lemma A), and non-perturbative in γ.
- **Secondary obstructions:** H-Bal (volume uniformity; group-blind) and H-Cyc (cyclicity of the coarse family, O1 of D08).

## 6. Computation (all CPU ≈ 8.5 min total; within the 20-min budget)
- **R1-E01, 4D Monte Carlo (Numerical evidence), 488 s production CPU.**
  - Validated against strong-coupling limits (U(1) β=0.2: 0.0988(11) vs 0.0995; SU(2) β=0.4: 0.0995(7) vs 0.0993) and against weak coupling (U(1) β=3: 0.9129 vs ≈0.913).
  - **U(1), L=8:** P jumps 0.5856 → 0.6551 between β=1.00 and 1.01 (slope 6.87), χ(2,2) goes 0.353 → 0.166, and χ_P peaks at 2.68 at β=1.00.
  - **SU(2), L=6/8:** smooth. Maximum slope 0.36/0.33, χ_P ≤ 0.39, no hot/cold separation beyond 1.9σ.
  - No finite-size-scaling claim; integrated autocorrelation times were not measured.
  - One under-thermalised validation run is kept and explained in RUN.md.
- **R1-E02, running coupling (Heuristic; exact arithmetic).**
  - SU(2): b₀ = 0.0464389, b₁ = 0.00181793.
  - k_*(β) ≈ 3.883β steps (b=2).
  - γ→pole window: 306.9 / 152.0 / 28.7 / 13.5 steps for γ = 0.05 / 0.1 / 0.5 / 1, independent of β.
  - U(1): b₀ = b₁ = 0.
- **R1-E03, block-map θ test (Computationally verified finite result).** Numbers in §3.

## 7. Recommended next step
1. **Make the reformulation precise (QUASAR, small).** Define 𝒜_γ concretely from S-119's Theorem 1 conditions, which needs a legitimately accessible text of S-119/S-117 or of the Balaban–Jaffe exposition (S-131; ask the principal whether library access exists). Then check whether 𝒜_γ provably contains the Wilson action at β = 2N/γ. If so, H-Gap ⇒ fixed-β lattice gap, and R1 is cleanly reduced to a known open problem.
2. **Probe H-Gap's non-abelian mechanism (QUASAR, small).** List the properties that separate SU(2) from U(1) at fixed weak coupling (centre/vortex free energies, the monopole sector, continuation of the coupling flow beyond γ). Design a bounded numerical diagnostic, e.g. a 4D U(1) vs SU(2) step-scaling of a finite-volume coupling across γ on 4⁴–8⁴, as numerical evidence only.
3. **LATTICE (after the principal routes the packet):** verify R1-D01 Lemma A, R1-D02 Lemmas 1–3 and R1-D03 Props. 1–2. Reproduce R1-E03b independently. Locate an accessible statement for hypothesis (M) (R1-PA01).
4. **Do not** spend effort extending strong-coupling expansions toward the crossover (R1-FP01).
