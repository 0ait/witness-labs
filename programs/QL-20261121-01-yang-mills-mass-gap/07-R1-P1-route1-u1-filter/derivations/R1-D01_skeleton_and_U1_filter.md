<!--
title: R1-P1 derivation R1-D01
id: QL-20261121-01/R1-P1/D01
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: proposed by QUASAR; LATTICE review v1 (REQUIRES CORRECTION (moderate)) gives per-claim verdicts
internal-source: WitnessLab/06_QUASAR_RESEARCH/derivations/R1-D01_skeleton_and_U1_filter.md
body: copy of the internal record; only the role title of the human principal was changed to "principal" (see REDACTIONS.md)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# R1-D01: Route R1 as an explicit step skeleton, and the 4D U(1) filter (LATTICE check 4, the go/no-go)

QL-20261121-01 · WITNESS LAB · QUASAR · Route 1 phase 1 · 2026-11-21 (authorised by the principal 18:56 CT, "begin route 1").
- **Status.** The skeleton is QUASAR's own organisation. The per-step verdicts are labelled individually. Lemma A is a *conditional* proof by QUASAR, pending LATTICE verification. **Nothing here proves, or claims progress toward, a 4D mass gap.**
- **Depends on:** D02, D03.3, D08.1–D08.3, H03; sources S-007, S-112…S-119, S-127, S-128, S-129…S-133.
- **Used by:** R1-D03, R1-D04, R1-P1 report.

Citation levels used below:
- [P] primary text opened;
- [A] abstract or excerpt opened;
- [T] title or Crossref only.

## 1. The R1 skeleton (numbered; each step lists what it needs)
Objects: G = SU(N) (N≥2) and the Wilson measure μ_{β,L} on a periodic lattice, with β = 2N/g₀² (the D03.3 convention; lab-wide convention still open, defect 9). The block factor b is a small integer, and k counts RG steps.

| Step | Content | Hypotheses and estimates it needs | Source / level |
|---|---|---|---|
| **S0** | Lattice measure, reflection positivity, transfer matrix | Wilson (or Villain) action; RP for link reflection; T ≥ 0 self-adjoint | OS78 S-005, Lüscher S-101 [T/A]; D02 |
| **S1** | One small-field RG step k→k+1 | (a) gauge-covariant block averaging (S-113 [T]; BIJ §2.3 [P]); (b) an *exact* gauge fix in the fluctuation integral (axial on a maximal tree per block; leaves the density unchanged, BIJ §2.4 [P]); (c) background-field variational problem and its minimiser (S-116 [T]); (d) propagator decay bounds for the fluctuation covariance (S-112, S-115 [T]); (e) a small coupling g_k ≤ γ; (f) localisation of the effective action into polymers with exponential decay ("multi-scale cluster expansion", BIJ §1 [P]; S-117 [T]) | — |
| **S2** | Large-field control | A partition of unity into small and large fields. Large fields are controlled by "the basic positivity of the action" (BIJ §2.6 [P]), with suppression ~exp(−c p(g_k)²/g_k²). In 4D this needs the R-operation (S-118/S-119 [T/A]) to localise and exponentiate large-field factors; BIJ 1984 states the naive method "breaks down in four dimensional Yang–Mills theory, because the effective coupling constant is expected to be only logarithmically small" [P] | — |
| **S3** | Iterate to scale k | S-119 Theorem 1 [A]: "If the sequence of the effective coupling constants is contained in an interval ]0,γ] with a sufficiently small positive γ, then the effective densities ρ_k have the form, and satisfy all the conditions …". The analysis is on a periodic lattice, with bounds "uniform in the lattice spacing" (S-007 intro [A]) | — |
| **S4** | Crossover attainment | The coupling recursion g_{k+1}^{−2} = g_k^{−2} − 2b₀ ln b + O(g_k²) with **b₀ > 0**. Then there is a finite k_*(β) with g_{k_*}² > γ, and k_*(β) ≈ β/(4N b₀ ln b) (R1-E02: 3.883 β for SU(2), b=2). Define a(β) := a_*·b^{−(k_*(β)−1)} (last controlled scale) | b₀>0: perturbative, Established in perturbation theory. Balaban's control of the g_k sequence is the "second aspect" (S-007 intro [A]: that paper proves only the first); **not verified from text** |
| **S5** | Volume uniformity / infinite volume | Bounds for ρ_{k_*−1} uniform in the number of blocks; an infinite-volume limit of its polymer representation | Not asserted in any opened text (Hypothesis R1-H01) |
| **S6** | Crossover clustering | The effective measure at scale k_*−1 (coupling ≈ γ, R1-E02) clusters with a rate m_* in its own units, uniformly in β, for a coarse-local family 𝒮′. This is H03 = X. Originally planned via a strong-coupling cluster expansion | Open (R1-H02). R1-D04 shows the strong-coupling route does not apply |
| **S7** | Block-map compatibility | B intertwines θ and translations by b^k; coarse observables are supported in fine slabs | R1-D02; E03 |
| **S8** | D08.3 | X + S7 ⇒ m(T|𝒦_β) ≥ (m_*/(b a_*))·a(β) | D08.3, Proved (LATTICE: VERIFIED WITH CONDITIONS) |
| **S9** | Continuum conclusion | Cyclicity of the coarse family, convergence (ME2), D01 | Open; outside phase 1 |

## 2. The 4D U(1) filter, step by step
4D compact U(1) lattice gauge theory is non-confining at weak coupling. Guth S-127 [A]: for the Villain form, a rigorous Coulomb-type lower bound on Wilson loops "holds for g² < 0.168" and "guarantees that electric charges are not confined". It is massless there (Fröhlich–Spencer S-128 [T]: "massless phases … in abelian gauge theories"). Driver S-132 [A]: "the compact U(1) lattice gauge theory with general energy function converges to a renormalized free electromagnetic field on the current sector as the lattice spacing approaches zero, provided the coupling constant is sufficiently large" (Driver's coupling convention not checked). For the Wilson energy function this holds for arbitrary coupling with a suitable Gibbs state. 3D U(1) is not a valid control, because it confines at all couplings (Göpfert–Mack S-129 [T]).

| Step | Holds verbatim for 4D U(1)? | Justification and label |
|---|---|---|
| S0 | **Holds** | RP for the Wilson and Villain U(1) actions; the transfer matrix exists. Group-agnostic. (Established, [T]) |
| S1 | **Holds** (expected) | BIJ [P]: "the overall strategy and many of the details are common to the abelian and nonabelian case". Their worked model *is* abelian. The axial-tree gauge fix is exact for any compact group; Gribov copies never arise, because no global continuum gauge is fixed and Landau-type fixing is only used on small fields (S-114 [T]). Dimock S-133 [A] runs Balaban's RG for abelian QED₃. (Heuristic for 4D U(1): text-supported, not a theorem we opened) |
| S2 | **Holds** (expected) | Large fields are controlled by positivity of 1−Re U_p, which is group-agnostic. U(1) large fields are monopole and Dirac-string configurations, suppressed at small g. The BIJ "logarithmically small coupling" obstruction concerns the *slow running*. For U(1) the coupling does not run at all, so whatever S-118/119 does is needed there too, and no group-specific input is visible. (Heuristic) |
| S3 | **Holds**, and more easily | Theorem 1's hypothesis "all g_j ∈ ]0,γ]" holds for all k when g₀² < γ, because the U(1) coupling does not run perturbatively. The conclusion (UV stability on a torus) is consistent with Driver's free-field continuum limit [A]. (Heuristic: we did not open whether Balaban's 4D theorem is stated for U(1)) |
| **S4** | **FAILS** | Pure U(1) has b₀ = b₁ = 0 to all orders (free photon). With g₀² < γ the sequence g_k never leaves ]0,γ], so k_* = ∞ and the crossover is never reached. Non-perturbative corrections are monopole effects ~e^{−c/g²}, consistent with a *finite* renormalised charge (Driver [A]: "renormalized free electromagnetic field"). (FAILS: perturbatively exact; non-perturbatively Heuristic, consistent with Established [A]) |
| S5 | No discrimination | Volume uniformity is open for both groups. For U(1), Guth [A] proves the infinite-volume limit of ⟨A[C]⟩ exists. (Group-blind) |
| **S6** | **FAILS** (Lemma A) | Take a Villain U(1) theory with bare coupling g₀² ∈ (γ, 0.168), which is non-empty because γ is "sufficiently small". Here "g_k² > γ" already holds at k=0, so S4 is *satisfied*, yet the theory is non-confining (Guth [A]) and massless (S-128 [T], S-132 [A]). By Lemma A, the U(1) analogue of S6 is false there. (Conditional proof below) |
| S7 | **Holds** | For U(1) small fields the argument average is linear, so θ-intertwining on gauge-invariant data is automatic (R1-E03, Proved here). (Proved / Computationally verified) |
| S8 | **Holds** | D08.3 is group-agnostic. (Proved; LATTICE verified with conditions) |
| S9 | No discrimination | — |

### Lemma A (abelian obstruction to S6; Conditional, proof QUASAR's)
*Hypothesis (M):* in the U(1) theory at bare coupling g₀², there is a coarse-local gauge-invariant observable F′ (e.g. a coarse plaquette field-strength function) whose connected time-direction correlation does not decay exponentially, uniformly in the volume. This is the standard meaning of "massless photon". It is consistent with S-128 [T] and S-132 [A], but we have not opened a theorem stating it for coarse observables, so it carries Hypothesis status.

*Claim.* Under (M), there is no block map B satisfying D08.2 (intertwining θ and τ^{b^k}, slab support) and no m_* > 0 such that the pushforward clusters as in X on a family containing F′.

*Proof.* Suppose it did. D08.3 is proved for any compact G (it uses only D08.1, D08.2 and T ≥ 0). It gives ⟨θF̄′∘B; τ_n(F′∘B)⟩ ≤ C e^{−(m_*/b^k) n} for all n, uniformly in L, contradicting (M). ∎

*Meaning.* This is the honest content of the filter. Lemma A is formally trivial (X ⇒ gap, and U(1) has no gap). The non-trivial point is *which step's proof* can distinguish the groups, and §3 answers that.

## 3. Verdict of the filter and where non-abelian structure must enter
**GO (with a qualification).** R1 is not dead in its current form: two steps fail for U(1).
- **S4: this is where asymptotic freedom enters, and it is the expected candidate.** b₀ > 0 is used *only* to guarantee a finite k_*(β) with g_{k_*}² > γ. That is exactly the perturbative recursion while g_k ≤ γ, so the mechanism is under control *within* Balaban's regime (modulo the unverified "second aspect", S4 row).
- **S6: NOT the expected answer.** The filter shows that AF at S4 is **not the only place** non-abelian structure must enter. U(1) at bare couplings g₀² ∈ (γ, 0.168) satisfies "g_k² > γ" (trivially, at k=0) and is still massless. So any proof of S6 must use a property of SU(N) that is
  - (i) non-perturbative: the target rate at coupling γ is ~exp(−1/(2b₀γ)) (Heuristic, D03.3), whose Taylor series in γ vanishes identically;
  - (ii) not shared by U(1) at the *same* small coupling. "Small coupling + positivity + locality + Balaban-type bounds" is not enough, since U(1) has all four.
  - Candidate properties (Conjecture-level only): continuation of the coupling growth beyond γ with no infrared fixed point; centre symmetry/vortices (but G₂, with trivial centre, is believed gapped); simple connectivity of SU(N) versus the U(1) monopole sector.
- **No other step secretly relies on something U(1) violates:**
  - Small-field/large-field split (S1–S2): group-agnostic (BIJ [P]).
  - Gribov/gauge fixing: the axial-tree gauge is exact and Landau-type fixing is used only on small fields. Group-agnostic, and irrelevant to the pushforward measure (R1-D02).
  - Villain versus Wilson: the U(1) obstruction is Established for Villain (Guth [A]) and for general energy functions including Wilson in Driver's continuum sense [A]. R1's skeleton is action-agnostic (S0 RP holds for both, and after one RG step the action is neither). No reliance.
  - D03.3 circularity: does **not** kill R1. a(β) := a_* b^{−(k_*(β)−1)} is fixed by a *coupling* condition (the first exit of Balaban's effective coupling from ]0,γ]), which is a non-gap renormalisation condition of the "running coupling held fixed" type, explicitly allowed in D03.3. (Logic: Proved here)
  - "X is just ME1 relabelled": **true at the level of statements** (R1-D03 Prop. 1, Proved here). It does not kill the route as a *method*, but it moves all the content into S6 (R1-D03 §2).

## 4. Numerical support (not proof)
- R1-E01: U(1) shows a jump in P of 0.0695 between β=1.00 and 1.01 at L=8 (slope 6.87, versus ≤0.36 for SU(2)), and a halving of χ(2,2). At β≈1.01, g₀² ≈ 1 ≫ any small γ, yet it is the massless side. (Numerical evidence)
- R1-E02: the U(1) running is identically zero. SU(2) k_*(β) grows linearly, and the γ→pole window has a fixed length independent of β (152 steps at γ=0.1, 2-loop). (Heuristic)
