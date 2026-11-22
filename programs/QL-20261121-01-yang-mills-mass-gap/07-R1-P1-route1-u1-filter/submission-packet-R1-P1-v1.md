<!--
title: R1-P1 submission packet v1
id: QL-20261121-01/R1-P1/packet-v1
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: submitted to LATTICE; review v1 returned REQUIRES CORRECTION (moderate)
internal-source: WitnessLab/06_QUASAR_RESEARCH/submissions_to_lattice/QL-20261121-01-R1-P1-v1.md
body: copy of the internal record; only the role title of the human principal was changed to "principal" (see REDACTIONS.md)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
> **Status (added for publication): Submitted to LATTICE 2026-11-21 19:21 CT; review v1 returned REQUIRES CORRECTION (moderate), defects D-R1P1-1…9.** The body is v1 as submitted; corrections will appear in a later v2 addendum.

# QUASAR Submission — QL-20261121-01 (R1-P1) — submission v1

*SUBMITTED to LATTICE 2026-11-21 19:21 CT under Principal t15u ("send the package to lattice").*

## A. Identification
- Title: Route R1, phase 1. The 4D U(1) filter (go/no-go) and LATTICE first-verification checks 1–4 for "multiscale RG to the crossover + clustering of the effective measure".
- ID: QL-20261121-01 / R1-P1. Version: v1. Date: 2026-11-21, 18:57–19:20 CT. Author: QUASAR.
- Authorisation: Principal t14u, 18:56 CT, "begin route 1". Route 2, the Lean lemma, the rebuild and publication are not authorised.
- Files:
  - `WitnessLab/05_RESEARCH_WORKSTREAMS/WS05_constructive_rg/R1-P1_report.md`;
  - `06_QUASAR_RESEARCH/derivations/R1-D01…D04`;
  - `experiments/R1-E01…E03`;
  - `hypotheses/R1-H01…H03`;
  - `proof_attempts/R1-PA01`;
  - `11_FAILED_APPROACHES/{failed_proofs/R1-FP01, failed_experiments/R1-FE01, lessons_learned/R1-LL01}`;
  - sources S-129…S-135.

## B. Original problem (conclusion-free, for blind formulation)
D08.3 reduces the uniform physical gap (ME1, restricted to coarse observables) to hypothesis X: β-uniform clustering of the block-spin pushforward of the 4D SU(N) Wilson measure at a fixed physical scale a_*. Route R1 proposes to obtain X by running Balaban's multiscale RG until the effective coupling first exceeds a small γ, and then proving clustering of the effective measure. The questions:
- (4) which step of R1 must fail for 4D U(1), which has a massless weak-coupling phase, and where does asymptotic freedom enter, uniquely or not;
- (1) which Balaban bounds hold at the first scale with g_k² > γ, on what volume, and what L-uniformity is missing;
- (2) does the block map intertwine θ and translations, and does RP survive blocking, including for gauge-fixed averaging;
- (3) do polymer and cluster expansions accept non-local effective actions uniformly in β, at what threshold, and how does that compare with the RG output.

## C. Executive mathematical summary
1. **U(1) filter: GO, with a qualification** (R1-D01). Two steps fail for U(1).
   - S4 (crossover attainment): b₀ = 0, so k_* = ∞. This is where AF enters.
   - S6 (crossover clustering): Villain U(1) at g₀² ∈ (γ, 0.168) has g² > γ yet is non-confining and massless. Lemma A (Conditional on (M)) shows the U(1) analogue of S6 is false.
   - Hence **AF is not the only place non-abelian input must enter**: S6 must use a non-perturbative property absent from U(1) at the same small coupling.
   - Nothing else hides a U(1)-violating assumption (small/large-field split, gauge fixing, Villain/Wilson).
   - D03.3 circularity does not kill R1 (a coupling-defined a(β)).
2. **X ≡ ME1 restricted to coarse observables** (R1-D03 Prop. 1, Proved here). What R1 adds is the β-free reformulation ME1|𝒦 ⇐ H-Bal + H-Gap (Prop. 2, Conditional). The obstruction is H-Gap: a uniform clustering theorem over a fixed weak-coupling class 𝒜_γ, which is non-perturbative and non-abelian.
3. **Check 1.** At k_* nothing holds (S-119 Thm 1 needs all g_j ≤ γ). ρ_{k_*−1} holds, at coupling ≈ γ (within 0.7%), on a finite periodic lattice. Volume uniformity is not asserted. Needed additions: R1-H01.
4. **Check 2.** D08.3 needs only θ/τ-intertwining + slab support + fine T ≥ 0, not coarse RP. RP survives blocking under intertwining + locality (Lemma 2). Gauge fixing inside the fluctuation integral does not change μ′ (Lemma 3).
   - The BIJ corner averaging fails θ-intertwining for SU(2) (E03: up to 0.6). It passes trivially for U(1).
   - A centre/symmetric-contour/projection rule passes to 7e−16 (Prop. 5).
5. **Check 3.** Cluster expansions accept exponentially decaying non-local tails uniformly in β, but only when the interaction is small (SU(2): β_eff < 1/12). The RG exit gives β_eff ≈ 2N/γ = 40 at γ=0.1, a ≈480× mismatch. "Strong-coupling clustering at the crossover" is refuted (R1-FP01).

## D. Literature (levels: [P] opened / [A] abstract / [T] title)
- [P] S-130 Balaban–Imbrie–Jaffe 1984 (author-hosted scan, sha256 recorded): averaging (§2.3), axial-tree gauge with density unchanged (§2.4), large/small fields (§2.6), "common to the abelian and nonabelian case", and the 4D large-field divergence remark.
- [A] S-127 Guth (APS abstract): Villain, g² < 0.168, non-confining. S-132 Driver (abstract): free-EM continuum limit. S-133 Dimock QED₃ (arXiv abstract). S-119/S-007 (from INV-001).
- [T] S-128 FS82, S-129 Göpfert–Mack, S-131 Balaban–Jaffe 1986 (Springer blocked), S-134 Gross 1979, S-135 Kotecký–Preiss.
- Not circumvented: Springer client challenge, Project Euclid bot block, APS login. Exa was not used.

## E. Mathematical development
- R1-D01: skeleton S0–S9 with needs and sources; per-step U(1) verdict table; Lemma A with proof; §3 verdict.
- R1-D02: Lemmas 1–3 (what D08.3 needs; RP after blocking; gauge fixing is irrelevant to μ′), Prop. 4 (the corner construction fails for SU(2), linear for U(1)), Prop. 5 (equivariant replacement).
- R1-D03: Prop. 1 (X ⇔ ME1|𝒦, m_* = Δa_*), Prop. 2 (H-Bal + H-Gap ⇒ X), and an honest account of what is gained.
- R1-D04: expansion criteria (standard form, [T]), the RG output, the mismatch table.

## F. Computational evidence
- **R1-E01 (Numerical evidence; 488 s CPU).** 4D Wilson heat-bath, U(1) at L=6, 8 and SU(2) at L=6, 8, hot and cold starts.
  - U(1) L=8: P 0.5856 → 0.6551 over β 1.00 → 1.01 (slope 6.87); χ(2,2) 0.353 → 0.166.
  - SU(2): maximum slope ≤ 0.36, χ_P ≤ 0.39.
  - Validated against strong- and weak-coupling limits.
  - No FSS claim; autocorrelations not measured.
- **R1-E02 (Heuristic; exact arithmetic).** SU(2) k_* ≈ 3.883β (b=2). The γ→pole window is 152 steps at γ=0.1, independent of β. U(1): b₀ = b₁ = 0.
- **R1-E03 (Computationally verified finite result).** θ-intertwining table (see R1-E03/RUN.md). Fixed seeds; sha256 of every script and output are in `outputs/SHA256SUMS.txt`; ENV.txt gives python 3.13.5, numpy 2.5.5, scipy 1.18.1, mpmath 1.3.0.

## G. Adversarial considerations (my own weakest points)
1. Lemma A rests on (M) (photon non-exponential decay for coarse observables), which is cited only at [T]/[A] level. Guth's bound is deconfinement, not masslessness.
2. S1–S3 "hold for U(1)" is Heuristic. I did not open a statement that Balaban's 4D theorem covers U(1).
3. The SZZ normalisation conversion (g² > 96/N) is assumed from our register note, not re-read.
4. Whether 𝒜_γ contains the Wilson action at β = 2N/γ (which would make H-Gap imply an open fixed-β problem) is Heuristic.
5. E03 transcribes the 1984 lecture construction in 2D, not S-113's CMP averaging.
6. The Gross/Kotecký–Preiss criteria are stated in standard form without opening the texts.

## H. Specific requests to LATTICE
1. Verify R1-D01 Lemma A and the §3 claim that S6 must carry non-abelian, non-perturbative input. Try to break it: is there a reading of "crossover" under which only S4 discriminates?
2. Verify R1-D02 Lemmas 1–3 and Prop. 4/5. Reproduce E03b independently, with a different averaging rule and a 3D or 4D geometry.
3. Verify R1-D03 Props. 1–2. Is the β-free reformulation a genuine gain, or does H-Gap's class 𝒜_γ smuggle β back in?
4. Locate an accessible source for (M) (photon two-point lower bound in Villain U(1)₄) and for the group class of Balaban's 4D theorem.
5. Your L-04 (computer-assisted window): does R1-E02's β-independence of the window change your assessment?

## I. Current conclusion
- R1 passes the 4D U(1) filter (GO).
- Asymptotic freedom enters at S4, but **also** a non-perturbative non-abelian input is required at S6, and none is known.
- X is ME1 restricted to coarse observables. R1's contribution is the β-free reformulation ME1|𝒦 ⇐ H-Bal + H-Gap.
- The strong-coupling version is refuted.
- **No 4D gap result is claimed; ME1 remains an Open problem.**
