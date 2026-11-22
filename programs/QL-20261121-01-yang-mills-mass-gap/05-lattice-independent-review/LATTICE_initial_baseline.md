<!--
title: LATTICE record: LATTICE_initial_baseline.md
id: QL-20261121-01/07/LATTICE_initial_baseline.md
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: LATTICE (independent validator), Witness Labs, Agentic Swarm, 0ait
date: 2026-11-21
version: as committed in internal 9e3dbc7
status: LATTICE record, copied verbatim
internal-source: WitnessLab/07_LATTICE_INDEPENDENT_REVIEW/LATTICE_initial_baseline.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# LATTICE Initial Baseline — QL-20261121-01 (WITNESS LAB: Yang–Mills Existence and Mass Gap)
Author: LATTICE (independent validator / innovation). Date: 2026-11-21, written 17:30–17:50 CT. Version: v1.
Blinding: written without reading 01_PROBLEM_FORMALIZATION/, 04_CANDIDATE_SOLUTIONS/, 05_RESEARCH_WORKSTREAMS/, 06_QUASAR_RESEARCH/ or any QUASAR text on the 2026 construction. Read: MISSION_CHARTER.md (Parts I–III and the workstream list), 00_GOVERNANCE/, folder layout, QUASAR's invitation message.
Scope stop: per the Commander's 17:38 CT usage directive, this report covers the 11 assigned items only. Nothing beyond them was started.

---
## Executive summary
The Clay Yang–Mills Existence and Mass Gap problem **is still an Open problem.** No primary source I opened claims a mass gap for 4D continuum Yang–Mills. The reported 2026 construction is real, and I verified it from original artifacts. OpenAI's Lean submission of 28 Oct 2026 is preserved by the Douglas–Gross–Jaffe–Klebanov–Nekrasov "Yang–Mills group" at `github.com/yang-mills-group/OpenAI-YM-20261028` (commit `3456e5e7…`). The group's assessment (`yang-mills-group/YM`, `docs/assessment-1.pdf`, dated 10 Nov 2026) and the KITP committee statements of Oct, 3 Nov and 9 Nov 2026 also exist. What the formal statement actually encodes is this. For each compact matrix group with simple non-abelian Lie algebra, and for every sequence of volumes, there is a **subsequence**, taken after a full fixed-volume UV limit of 4D Wilson lattice theory, whose limit has a pure-phase decomposition. A prover-*selected* phase reconstructs to a Wightman theory with a unique translation-invariant vacuum, plus OPE bounds and a log-modified (non-free) trace two-point law. **It states no mass gap.** The only spectral information I found in the source is a *polynomial* low-energy bound: spectral weight in (0,u] is at most M·u², and heat decay goes as M·τ⁻². Both are compatible with a massless theory. The infinite-volume limit is not shown to be unique. I elaborated the public challenge statement myself against its pinned Mathlib (Lean 4.32.0). I did not rebuild the 987,586-line proof, because the shared RAM and the group's recorded ≈184-minute build rule it out. So kernel correctness of the proof rests on the group's records, not on me. The real open core of the Clay problem is the same as before 2026: a **volume-uniform and spacing-uniform positive spectral gap in physical units**. Behind it sit uniqueness of the infinite-volume limit and vacuum, and the question of whether the existence part satisfies Jaffe–Witten footnote 2.

**Verdict on the 2026 construction claim (as a solution of the Clay problem): REJECTED as a full solution.** The artifact itself states no mass gap, and its authors and reviewers concede this. **As an existence claim (Wightman QFT from 4D Wilson theory, subsequential IR limit): UNRESOLVED / not independently verified by LATTICE.** The artifacts exist and the statement is as described, but I did not re-run the kernel check. The informal 1,147-page proof is unreleased. Independence of the infinite-volume limit from the subsequence is unproved. Whether "subsequential limit + axioms" meets footnote 2 is a judgment call.

---
## 1. Official problem text (primary source)
Source: A. Jaffe and E. Witten, *Quantum Yang–Mills Theory*, Clay Mathematics Institute problem description, PDF at <https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf> (downloaded 2026-11-21, sha256 `3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09`, 14 pp., created 2006-08-04). Copy and text extraction: `reviews/QL-20261121-01/sources/yangmills.{pdf,txt}`.

**§4 "The Problem", verbatim (pdftotext; line breaks joined):**
> To establish existence of four-dimensional quantum gauge theory with gauge group G, one should define a quantum field theory (in the above sense) with local quantum field operators in correspondence with the gauge-invariant local polynomials in the curvature F and its covariant derivatives, such as Tr F_ij F_kl(x).¹ Correlation functions of the quantum field operators should agree at short distances with the predictions of asymptotic freedom and perturbative renormalization theory, as described in textbooks. Those predictions include among other things the existence of a stress tensor and an operator product expansion, having prescribed local singularities predicted by asymptotic freedom.
> Since the vacuum vector Ω is Poincaré invariant, it is an eigenstate with zero energy, namely HΩ = 0. The positive energy axiom asserts that in any quantum field theory, the spectrum of H is supported in the region [0, ∞). A quantum field theory has a mass gap ∆ if H has no spectrum in the interval (0, ∆) for some ∆ > 0. The supremum of such ∆ is the mass m, and we require m < ∞.
> **Yang–Mills Existence and Mass Gap.** Prove that for any compact simple gauge group G, a non-trivial quantum Yang–Mills theory exists on R⁴ and has a mass gap ∆ > 0. Existence includes establishing axiomatic properties at least as strong as those cited in [45, 35].

[45] = Streater–Wightman, *PCT, Spin and Statistics and All That* (1964). [35] = Osterwalder–Schrader, CMP 31 (1973) 83–112 and CMP 42 (1975) 281–305.
Footnote 1: "A natural 1–1 correspondence between such classical 'differential polynomials' and quantized operators does not exist… One expects that the space of classical differential polynomials of dimension ≤ d does correspond to the space of local quantum operators of dimension ≤ d."
**Footnote 2 (§6.5), verbatim:** "We specifically exclude weak-existence (compactness) as the solution to the existence part of the Millennium problem, unless one also uses other techniques to establish properties of the limit (such as the existence of a mass gap and the axioms)."
§3 also requires a vacuum "unique up to a phase", positive energy, Poincaré covariance and spacelike commutativity. §6 says "no present ideas point the direction to establish the existence of a mass gap that is uniform in the volume." §6.5 says "New ideas are needed to prove the existence of a mass gap that is uniform in the volume of space-time."

## 2. Target theorem (LATTICE's own formulation) and proof obligations
**Target theorem (T).** For every compact Lie group G whose Lie algebra 𝔤 is simple (in particular non-abelian), there exist all of the following:
- a separable Hilbert space ℋ;
- a strongly continuous unitary representation U of the proper orthochronous Poincaré group 𝒫₊↑ (or of its universal cover);
- a vector Ω, unique up to phase among translation-invariant vectors;
- a family of operator-valued tempered distributions Φ_v(f), indexed by a graded label space V = ⊕_d V_d.

V_d must be finite-dimensional and correspond to gauge-invariant local polynomials in F and D of dimension ≤ d (JW fn. 1). The Wightman axioms W0–W3 must hold. The theory must be **non-trivial** and **Yang–Mills**: short-distance behaviour given by asymptotic freedom for G, with a stress tensor and an OPE with the AF-predicted singularities. Finally there must be Δ>0 with σ(H) ∩ (0,Δ) = ∅, where H = generator of time translations, and m := sup Δ < ∞.
Equivalent Euclidean route: Schwinger functions obeying OS0–OS4 (with OS0′ growth / linear-growth condition of OS-II), Euclidean invariance, reflection positivity, symmetry and clustering. Then OS reconstruction gives the above. The gap is equivalent to exponential decay of truncated Euclidean correlations at a uniform rate on a generating set. Two-line form: **∀ compact simple G, ∃ an interacting Wightman/OS QFT on ℝ⁴ whose local fields are the renormalized gauge-invariant curvature polynomials of G with AF short-distance behaviour, such that its Hamiltonian satisfies σ(H) ⊂ {0} ∪ [Δ,∞) for some Δ>0, with Ω the unique vacuum.**

**Proof obligations** (each must be proven for every G):
| # | Obligation | Notes |
|---|---|---|
| P1 | Construction: Schwinger functions as limits (UV a→0 and IR L→∞) of a regularized theory, or another definition | JW fn. 2: compactness alone is excluded unless properties of the limit are proven |
| P2 | OS0 regularity (distributions, temperedness) + OS0′ growth in n (needed for OS-II reconstruction) | Coincident-point (contact) behaviour must be controlled for distributions on all of S(ℝ⁴ⁿ), not only away from diagonals |
| P3 | OS1 Euclidean invariance (full O(4)/SO(4) + translations) | The lattice breaks it; it must be restored in the limit |
| P4 | OS2 reflection positivity | Must survive every regularization/RG step used (Osterwalder–Seiler 1978 give it for Wilson's action) |
| P5 | OS3 symmetry; OS4 clustering, or a pure-phase decomposition | Clustering ⇔ unique vacuum in the reconstructed theory |
| P6 | Reconstruction theorem applied correctly (OS-II with growth condition) → W0–W3 | |
| P7 | Field content: labels ↔ gauge-invariant curvature polynomials, graded by dimension | Inherently ambiguous (JW fn. 1) |
| P8 | Short-distance: AF running coupling, stress tensor, OPE with predicted singularities | "agree… as described in textbooks": the level of agreement (leading order or all orders) is unspecified |
| P9 | Non-triviality | Not free / not Gaussian |
| P10 | Mass gap: σ(H)∩(0,Δ)=∅, Δ>0, and m<∞ | m<∞ excludes the trivial theory (ℋ=ℂΩ) |
| P11 | Uniqueness of the vacuum (W0) | In a mixed IR limit, uniqueness holds only per pure phase |
| P12 | Every compact simple G | Including exceptional groups and non-simply-connected forms |

**Ambiguities to flag.**
1. *"Non-trivial"*: not defined in JW. The weakest reading is "not a generalized free field". Stronger readings are a non-Gaussian S-matrix or non-zero truncated 4-point functions. I propose a working standard: non-zero connected 4-point function of a gauge-invariant field AND AF log-corrections incompatible with any free/generalized-free field.
2. *"Local quantum field theory" / observable algebra*: Wightman fields on gauge-invariant composites (the JW choice) or a Haag–Kastler net. Wilson loops are non-local and are not required. A gap proven for a smaller algebra (e.g. only Tr F²) does not give σ(H)∩(0,Δ)=∅ on all of ℋ unless that family is cyclic for Ω.
3. *Gap for which H*: the gap must hold on the full ℋ reconstructed from all local fields.
4. *Pure phase vs mixture*: if the IR limit is not unique, whose gap counts? Every phase's? A selected one? Uniformly?
5. *"For any G"*: logically ∀G ∃ theory (one theory per G). A uniform Δ across G is not required. Δ is dimensionful, so only Δ/Λ_G is meaningful.
6. *"Compact simple"*: does it mean simple Lie algebra or simple group? Connected? The centre matters (e.g. SU(N) vs SU(N)/ℤ_N gives different line operators but the same local fields).
7. *Footnote 2*: weak existence plus "other techniques to establish properties of the limit". Is establishing the axioms but not uniqueness enough? This is unsettled. It is directly relevant to §3.
8. *m<∞*: rules out trivial ℋ. Note also that the ∃Δ wording does not require a one-particle (isolated mass-shell) state.

## 3. Audit of the 2026 construction claim from original artifacts
### 3.1 Artifacts found (all opened/cloned 2026-11-21)
| Artifact | Location | Identity |
|---|---|---|
| OpenAI Lean submission (28 Oct 2026) | <https://github.com/yang-mills-group/OpenAI-YM-20261028> | single commit `3456e5e75cf8d4cd558955a5c7638fba2d68f464`, author Michael R Douglas, 2026-11-05 18:01 −05:00 (17:01 CT), "Import original October 28 OpenAI Yang-Mills submission"; repo created 2026-11-05T22:59Z (16:59 CT). 9,477 `.lean` files, 987,586 lines; Lean `v4.32.0`; Mathlib `81a5d257c8e410db227a6665ed08f64fea08e997`; Apache-2.0 |
| Yang–Mills group results repo | <https://github.com/yang-mills-group/YM> | HEAD `b379615f559643d30b49fb2e05e1efb83d755fc8` (2026-11-15, M. R. Douglas); assessment commit `55ba9fc36293b3f4d52c6b1f813169a0be76ee98` (2026-11-10) |
| Assessment 1, "Validation of the OpenAI Yang–Mills construction", Yang–Mills group, 10 Nov 2026, 35 pp. | `YM/docs/assessment-1.pdf` | sha256 `8e658c00…1db219` |
| KITP committee statement (Oct 2026), Douglas, Gross (Chair), Jaffe, Klebanov, Nekrasov | <https://www.kitp.ucsb.edu/sites/default/files/YM_working_group.pdf> | sha256 `dbab31f0…57bd12` |
| 2nd statement, **3 Nov 2026** | <https://www.kitp.ucsb.edu/sites/default/files/2nd-Statement-About-Quantum-YangMills-Theory_Nov-3.pdf> | sha256 `fcd8a6de…2a5c` |
| 3rd statement, 9 Nov 2026 (announces the 10 Nov release) | <https://www.kitp.ucsb.edu/sites/default/files/3rd-Statement-About-Quantum-YangMills-Theory_Nov-9.pdf> | sha256 `27cd200d…7fc8` |
| OpenAI announcement | <https://openai.com/index/building-scientific-understanding-with-academic-communities/> (via search snippet; claims natural-language proof 9 Sep 2026, Lean formalization finished 16 Oct 2026, also QCD/SU(5) claims) | not separately fetched |

Integrity checks run by LATTICE: `sha256sum -c SOURCES.sha256` passed for all 9,507 entries. `diff -rq` between the original repo and `YM/submissions/openai-20261028/submission` found no differences. Mapping to QUASAR's labels: the "3 Nov assessment" is the KITP 2nd statement, a progress note only with no technical findings. The "10 Nov assessment" is Assessment 1. Its statement that the group has "no present connection to the Clay Mathematics Institute" is verbatim on p. 1. **None of this is a Clay ruling.**
Also listed in YM/README but with no artifacts: "OpenAI, 4 November 2026 — work in progress" and "Alpöge and Sussman, 15 November 2026 — work in progress". A Science news article (11 Nov 2026, J. Kwan) says both teams claim existence, not the mass gap. No arXiv preprint by Alpöge/Sussman on Yang–Mills was found (arXiv API author search). The OpenAI informal 1,147-page manuscript is not public (KITP Oct statement; Assessment p. 1).

### 3.2 What the Lean statement actually says (exact)
Public target, `ChallengeSpec.lean` l.186–188:
```lean
def JointExistence : Prop := ∀ g : GaugeGroup, g.IsSimple → ∃ C : WilsonFamily g,
  WilsonRegularity C ∧ ∀ p : ℕ → ℕ, StrictMono p → ∃ q : ℕ → ℕ, StrictMono q ∧
    ∃ T : Hierarchy C, T.Properties (p ∘ q)
```
- `GaugeGroup` is a closed subgroup of U(n+1) with its Lie algebra pinned by `generates`. `IsSimple` means a non-abelian, real-simple Lie algebra. This covers all compact simple G via faithful unitary representations, and it also admits disconnected groups.
- `WilsonFamily` uses the genuine Wilson law: product Haar measure × exp(−β Σ_p (1 − Re tr U_p/(n+1))). The **prover chooses** the spacings `denominator`, the periods, β(N,p), the token type and the insertions. `WilsonRegularity` requires that β/log(1/a) → *some* slope > 0, and that insertions be continuous, gauge-invariant and finitely supported in lattice units.
- `Properties`:
  1. `wilson`: full mesh limit at each suitable fixed volume, then the limit along the extracted volume subsequence equals the *unselected* continuum correlation.
  2. `reconstruction`: a Wightman theory (`Axioms` W0–W3: spectral representation, positive energy on the closed forward cone, unique translation-invariant vector, common dense domain, cyclic vacuum, norm-temperedness, adjoints, Poincaré covariance, spacelike commutativity). Also a phase measure with full support on a compact metric space of "characters". The mixture integral equals the unselected limit. Analytic continuation and boundary values link it to the **selected** phase.
  3. `ope`: OPE remainder bounds.
  4. `nonfree`: the centred grade-4 trace satisfies r⁸ log²(1/r)·S_ΘΘ(r) → 3·dim_ℝ𝔤/π⁴, and S_ΘΘ is not eventually equal to any finite sum of massive/massless Wick kernels.
- **No clause mentions a spectral gap.** I searched for `gap`, `massGap` and `MassGap`: they appear only in unrelated internal names. The spectral content that does exist is internal (`YM/EveryPhase/Light.lean:221` `light_bound`; `YM/EveryPhase/Decay.lean:173` `inverse_square`). It states, per phase i and finite word sum w, **spectral weight of (0,u] ≤ M u² for 0<u≤1** and **0 ≤ ⟨A,(e^{−sH}−P₀)A⟩ ≤ M s⁻²** for s≥1. Both are *polynomial* and consistent with gapless spectrum. A gap would require the weight to vanish on (0,Δ), i.e. decay ≤ M e^{−Δs}.

### 3.3 Formal checks LATTICE actually ran
- Grep over all 9,477 files: one `sorry` (`Challenge.lean:6`, the reference stub, by design). No `axiom` or `opaque` declarations. No `native_decide`, `implemented_by` or `ofReduceBool`. The two "unsafe" hits are a comment and a string. `comparator.json` permits only `propext, Quot.sound, Classical.choice`.
- **Statement elaboration:** I built `PublicTheory`, `PublicWilson`, `ChallengeSpec` and `Challenge` in a fresh project pinned to Lean 4.32.0 and Mathlib `81a5d257…` (`reviews/QL-20261121-01/formal/challenge_check/`). Build succeeded. `#print axioms YangMills.jointExistence` (reference stub) gave `[propext, sorryAx, Classical.choice, Quot.sound]`, as expected for the stub. `#print YangMills.JointExistence` reproduces the statement above. **This checks the statement only, not the proof.**
- **Not run:** a full build of `Solution`/`Construction` and `#print axioms` on the real proof. Reason: about 1M lines, a recorded 184-minute build (Assessment §9.1), and only ~6 GB free of 15 GB shared RAM. Also stopped by the Commander's usage directive. Kernel correctness therefore rests on the group's record (Assessment §9.1–9.2): a clean rebuild of 9,470 modules, an axiom audit, and Comparator passes on 30 Oct and 3 Nov. That run was on macOS with `fake-landrun.sh` (no process isolation) and no second, independent kernel.

### 3.4 Gap analysis: Lean statement vs Clay (T)
| Clay obligation | Status in artifact | Basis |
|---|---|---|
| P1 existence | Fixed-volume UV limit along the full chosen spacing sequence. IR limit **subsequential only** (Arzelà–Ascoli). Limit may depend on the subsequence | Assessment §5, Thm 5.1; Lean `∀ p ∃ q` |
| Fn. 2 (no weak existence) | Arguable. Axioms are proven for the limit, but no uniqueness and no gap. The group itself says it supplies "substantial information beyond compactness" | Assessment §5 |
| P2–P6 OS→Wightman | Claimed and formalized per phase. The group's independent OS check (vs. `xiyin137/OSreconstruction`) covers **only the centred trace field** and only on tests flat at diagonals. Contact extensions are not proven OS-positive | Assessment §10 |
| P7 field content | Not pinned by the public target. Tokens and insertions are prover-chosen. The group says OpenAI told them `jointExistence` "omitted some of the connections to the lattice construction"; the group relies on its stronger `combined_acceptance` target | Assessment §9 |
| P8 AF | Public target only requires *some* positive slope. The detailed theorem claims slope 11C_𝔤/(24π²) = 2b₀ (Assessment eq. 7; I confirmed 2·(11C/48π²) = 11C/24π²). OPE bounds are present; all-orders perturbative agreement is **unproven** | Assessment §7.4–7.5 |
| P9 non-triviality | Log-corrected trace law + exclusion of finite Wick profiles. Excludes finite free-field descriptions, **not** all Gaussian composites (Assessment §7.3). The 3 dim𝔤/π⁴ coefficient was not recomputed by LATTICE | |
| **P10 mass gap** | **Absent.** Only polynomial bounds (§3.2). "The construction provides no evidence for or against a mass gap" | Assessment §2 item 4 |
| P11 unique vacuum | Only inside the prover-*selected* pure phase. Agreement across phases and subsequences is unresolved | Assessment p. 1, §6.1 |
| P12 all G | Yes in the statement's quantifier (∀ simple matrix groups) | ChallengeSpec |

**Usable for the mass-gap research (labelled; not verified by LATTICE):**
- the fixed-volume UV control (a Balaban-type RG, per the assessment) as a potential *input*;
- the `light_bound` u²-spectral estimate as a quantitative starting point to upgrade;
- the phase-decomposition machinery.

All of these depend on an unreleased informal proof and a kernel check I did not repeat. **Verdict lines are in the executive summary.**

## 4. Exact unresolved parts of the full theorem (given the literature)
- **Open problem:** mass gap for 4D continuum YM for any compact simple G. This is not claimed by any source opened, including the 2026 artifacts.
- **Open problem:** uniqueness/convergence of the infinite-volume limit (not just subsequences) and a unique vacuum for the full limit (Assessment §8 Q1). Also universality across spacing sequences and regularizations.
- **Open problem:** a probability measure for the continuum theory (Assessment §8 Q2). In 2D this was done by Driver, Lévy, CCHS; in 3D only Langevin/local results exist (CCHS 2024).
- **Unverified (by the community and by LATTICE):** 4D existence itself. It rests on Lean artifacts reviewed by one group that says "we do not claim to fully understand the proof yet", and on an unreleased manuscript. Treat it as a strong candidate, not an Established theorem.
- **Open problem:** all-orders perturbative agreement / full AF matching (Assessment §7.4–7.5).
- **Open problem (not required by Clay):** confinement / area law in the continuum. On the lattice, area law is known only at strong coupling or in the 't Hooft regime (Osterwalder–Seiler 1978; Cao–Nissim–Sheffield 2025).
- **Mass gap on the lattice at weak coupling (β→∞, continuous G, d=4):** open. Known only at strong coupling (Osterwalder–Seiler 1978; Shen–Zhu–Zhu 2023) or for *finite* G at weak coupling (Adhikari–Cao 2022), which is a different mechanism.

## 5. Existing approaches (sources opened as stated)
Access legend: **[F]** full text read; **[P]** primary PDF/text partly read; **[A]** abstract/metadata page opened (arXiv API or Crossref); **[C]** cited via JW reference list only. DOIs resolved against api.crossref.org on 2026-11-21 unless marked "(arXiv metadata)".
| Approach | Key sources | Status | Gap to full theorem |
|---|---|---|---|
| Axioms & reconstruction | Osterwalder & Schrader 1973, [10.1007/BF01645738](https://doi.org/10.1007/BF01645738); 1975, [10.1007/BF01608978](https://doi.org/10.1007/BF01608978) [A] | Established theorem (OS-II needs the growth condition E0′) | Framework only |
| Constructive QFT | Glimm & Jaffe 1987 *Quantum Physics*, [10.1007/978-1-4612-4728-9](https://doi.org/10.1007/978-1-4612-4728-9) [A]; JW §6.1–6.4 [P] | Established: P(φ)₂, φ⁴₃ with gaps; Higgs₂ abelian (BFS) | Methods are mostly scalar or abelian. Correlation inequalities fail for non-abelian YM (JW §6.1) |
| Wilson lattice / RP | Wilson 1974, [10.1103/PhysRevD.10.2445](https://doi.org/10.1103/PhysRevD.10.2445) [A]; Osterwalder & Seiler 1978, [10.1016/0003-4916(78)90039-8](https://doi.org/10.1016/0003-4916(78)90039-8) [A]; Lüscher 1977 transfer matrix, [10.1007/BF01614090](https://doi.org/10.1007/BF01614090) [A]; Kogut–Susskind 1975, [10.1103/PhysRevD.11.395](https://doi.org/10.1103/PhysRevD.11.395) [A]; Seiler 1982 LNP 159, [10.1007/3-540-11559-5_2](https://doi.org/10.1007/3-540-11559-5_2) [A] | Established: RP, positive self-adjoint transfer matrix, **strong-coupling gap and area law** | Strong coupling is the wrong end. The continuum needs β→∞ |
| **Counter-lesson (abelian)** | Guth 1980, [10.1103/PhysRevD.21.2291](https://doi.org/10.1103/PhysRevD.21.2291) [A]; Fröhlich & Spencer 1982, [10.1007/bf01213610](https://doi.org/10.1007/bf01213610) [A] | Established: 4D U(1) has a massless, non-confining weak-coupling phase | Proves that a strong-coupling lattice gap need not persist to weak coupling. Any gap proof must use non-abelian structure (AF) |
| Balaban RG | Balaban 1985 (3D UV stability), [10.1007/BF01229380](https://doi.org/10.1007/BF01229380); 1987 (4D effective actions), [10.1007/BF01215223](https://doi.org/10.1007/BF01215223); 1989 large fields II, [10.1007/BF01238433](https://doi.org/10.1007/BF01238433) [A]; Dimock, "RG according to Balaban I–III", arXiv [1108.1335](https://arxiv.org/abs/1108.1335), [1212.5562](https://arxiv.org/abs/1212.5562), [1304.0705](https://arxiv.org/abs/1304.0705) [A] | Established: UV stability on T⁴ for effective actions (JW §6.5 calls the 4D extension "a qualitative breakthrough"). Gauge-invariant expectations and IR: incomplete before 2026 | No IR, no gap. The 2026 work claims to complete the UV and the observables |
| Continuum regularization | Magnen, Rivasseau & Sénéor 1993, *Construction of YM₄ with an infrared cutoff*, CMP 155:325, [10.1007/bf02097397](https://doi.org/10.1007/bf02097397) [A] | Established (per JW): YM₄ in finite volume with IR cutoff | IR cutoff removal and gap open. Gribov/gauge-fixing issues are handled locally |
| 2D YM exact | Driver 1989, [10.1007/bf01218586](https://doi.org/10.1007/bf01218586) [A]; Lévy, arXiv [math/0101239](https://arxiv.org/abs/math/0101239) [A]; Witten 1992 "2D gauge theories revisited", arXiv [hep-th/9204083](https://arxiv.org/abs/hep-th/9204083) [A]; Gross & Witten 1980, [10.1103/physrevd.21.446](https://doi.org/10.1103/physrevd.21.446) [A] | Established: full construction, exact solvability, third-order large-N lattice transition (GW) | Super-renormalizable, no propagating gluons. Lesson for 4D: lattice artefacts / phase transitions in N |
| Stochastic quantization | Chandra–Chevyrev–Hairer–Shen 2022 (2D Langevin), [10.1007/s10240-022-00132-0](https://doi.org/10.1007/s10240-022-00132-0) [A]; CCHS 2024 (3D YMH), arXiv [2201.03487](https://arxiv.org/abs/2201.03487), Invent. Math. 237 [A]; Chevyrev–Shen 2023, arXiv [2302.12160](https://arxiv.org/abs/2302.12160) [A]; Chevyrev survey 2022, arXiv [2202.13359](https://arxiv.org/abs/2202.13359) [A] | Established: 2D invariant measure + universality; 3D local-in-time gauge-covariant Markov process | 4D is critical (not subcritical), so regularity structures do not apply directly. No gap |
| Lattice functional inequalities | Shen–Zhu–Zhu 2023, CMP 400:805, [10.1007/s00220-022-04609-1](https://doi.org/10.1007/s00220-022-04609-1) [A]; Nissim 2025, arXiv [2510.22788](https://arxiv.org/abs/2510.22788) [A]; Cao–Nissim–Sheffield, arXiv [2505.16585](https://arxiv.org/abs/2505.16585), [2509.04688](https://arxiv.org/abs/2509.04688) [A]; Adhikari–Cao, arXiv [2202.10375](https://arxiv.org/abs/2202.10375) [A] | Established (preprint/peer-reviewed as marked): lattice mass gap, unique infinite-volume limit, log-Sobolev for |β| < 1/(16(d−1)) (SU(N)); 't Hooft regime; area law in expanded regimes; finite-G weak-coupling decay | All are at fixed lattice spacing in strong/'t Hooft coupling, the opposite of the continuum limit |
| Chatterjee program | "Yang–Mills for probabilists", arXiv [1803.01950](https://arxiv.org/abs/1803.01950) [A]; SO(N) large N, CMP 366, [10.1007/s00220-019-03353-3](https://doi.org/10.1007/s00220-019-03353-3) [A]; confinement via centre symmetry, arXiv [2006.16229](https://arxiv.org/abs/2006.16229) [A]; SU(2) YMH scaling limit, arXiv [2401.10507](https://arxiv.org/abs/2401.10507) [A] | Established: centre symmetry + exponential decay under all boundary conditions ⇒ confinement; Gaussian (massive) YMH limit | 2006.16229 is a conditional link gap⇒confinement (lattice). The YMH limit is Gaussian (trivial) |
| Hamiltonian / variational | Kogan–Kovner 1995, PRD 52:3719, [10.1103/physrevd.52.3719](https://doi.org/10.1103/physrevd.52.3719) [A]; Karabali–Nair 1996, [10.1016/0550-3213(96)00034-x](https://doi.org/10.1016/0550-3213(96)00034-x) [A]; Nair 2026, "Towards a proof of mass gap in 3d YM", arXiv [2608.10133](https://arxiv.org/abs/2608.10133) [A] | Heuristic (variational) / outline (Nair: gap reduces to a Laplacian eigenvalue inequality on gauge-orbit space) | Not rigorous. 3D only |
| Asymptotic freedom | Gross–Wilczek 1973, [10.1103/PhysRevLett.30.1343](https://doi.org/10.1103/PhysRevLett.30.1343) [A] | Established perturbatively | Gives UV, not IR |
| Triviality warning | Aizenman–Duminil-Copin 2021, Ann. Math. 194:163, [10.4007/annals.2021.194.1.3](https://doi.org/10.4007/annals.2021.194.1.3) [A] | Established: φ⁴₄ scaling limits are Gaussian | Shows 4D continuum limits can be trivial. Non-triviality must be proven, not assumed |
| Numerics | Morningstar–Peardon 1999, [10.1103/PhysRevD.60.034509](https://doi.org/10.1103/PhysRevD.60.034509) [A] | Numerically supported: SU(3) glueball spectrum gapped | Not proof |
| 2026 AI construction | §3 above [P] | Candidate existence (unverified by LATTICE); no gap | §3.4 |
| Unrefereed "full solution" claims seen in search | Faizal–Shabir arXiv 2606.19362; Lim arXiv 2307.00788; Mihajlovic arXiv 2611.11534 (spectral bounds, explicitly partial) [A] | **Not reviewed**; abstracts only. Not accepted as solutions by any source opened | Need full candidate audits (charter §8.3). Out of scope today by directive |

## 6. LATTICE map of mass-gap bottlenecks
- **B1 UV / continuum limit in 4D (marginal coupling, AF).** RG control uniform in a, plus gauge-invariant observables and their renormalization. *Status:* claimed by 2026 OpenAI (fixed volume). Unverified.
- **B2 Physical-unit gap transfer.** m_lat(β) ≥ Δ·a(β) with a(β) ~ Λ⁻¹ exp(−β/(4N b₀))-type dimensional transmutation. This is the heart: a lattice gap that is *exponentially small in β at the exact AF rate*, uniformly.
- **B3 IR / infinite volume.** Uniform-in-L gap or clustering. Uniqueness of the limit. Finite-L gaps can close (E3).
- **B4 Weak-to-strong coupling crossover.** Connect the AF regime (small g at short scales) to the confining regime (large effective coupling at Λ⁻¹) without a phase transition. The U(1) counterexample shows this can fail without non-abelian input.
- **B5 Reflection positivity through RG.** Block-spin/gauge-fixed RG typically breaks RP. A gap is derived via the transfer matrix, which needs RP at the final scale.
- **B6 Vacuum uniqueness / phases.** Exclude multiple pure phases (centre symmetry, θ-vacua not present for pure YM at θ=0 but must be checked).
- **B7 Non-triviality.** Must coexist with the gap. A massive Gaussian limit (as in Chatterjee 2401.10507 for YMH) would satisfy "gap" but fail P9.
- **B8 G-dependence.** Constants depend on dim𝔤, Casimir and centre. Exceptional groups have trivial centre (G₂: centre trivial ⇒ centre-symmetry arguments fail, string breaking).
```mermaid
graph TD
  B1[UV: 4D RG, AF, renormalized observables] --> E[Existence on T4]
  B5[RP preserved through RG] --> TM[Transfer matrix / OS Hamiltonian at all scales]
  E --> B3[IR: L->inf, uniqueness]
  B4[Weak->strong crossover, no transition] --> B2[m_lat >= Delta*a(beta) uniformly]
  TM --> B2
  B2 --> GAP[Uniform physical gap on T4]
  GAP --> B3
  B3 --> B6[Unique vacuum / pure phase]
  B6 --> OS[OS reconstruction -> Wightman]
  B7[Non-triviality] --> CLAY[Clay theorem]
  OS --> CLAY
  B8[All compact simple G] --> CLAY
  GAP --> CLAY
```
**Top 3 bottlenecks:** B2 (physical-unit gap at the AF rate), B4 (crossover without a phase transition), B3/B6 (volume uniformity and uniqueness).

## 7. Research directions (every item is a PROPOSAL; none tested)
| ID | Concept | Mathematical basis | Differs from standard | First experiment / derivation | Failure condition | Priority |
|---|---|---|---|---|---|---|
| L-01 PROPOSAL | **Upgrade the u² spectral bound to a gap.** Study the u-exponent of spectral weight near 0 in the 2026 `light_bound`, and look for a bootstrap u^k for all k ⇒ gap | Spectral measure; a weight bound O(u^k) ∀k on a cyclic family plus analyticity ⇒ no spectrum near 0? (needs care: O(u^∞) ≠ 0) | Uses the existing formal construction as input rather than building from scratch | Read `YM/EveryPhase/Light.lean` provenance of the u² (where does 2 come from: Euclidean dimension? OS growth?). Write a 1-page derivation | Exponent tied to kinematics (massless-compatible by construction) | High |
| L-02 PROPOSAL | **Multiscale log-Sobolev / Bakry–Émery across RG scales**: prove a Poincaré inequality for the *effective* action at the scale where the running coupling is O(1), then transfer | SZZ 2023 gives LSI at strong coupling; Balaban RG gives effective actions | Combines functional-inequality methods with RG, rather than at fixed bare β | Compute the Ricci lower bound of the SU(2) single-plaquette-block effective action numerically vs. effective coupling | Curvature lower bound fails at the crossover coupling | High |
| L-03 PROPOSAL | **Centre-symmetry ⇒ clustering converse loop** (Chatterjee 2006.16229 gives decay ⇒ confinement; seek area-law + RP ⇒ gap via transfer matrix) | Transfer-matrix and string-state lower bounds | Reverses the usual implication | Literature check: Durhuus–Fröhlich-type "area law ⇒ mass gap" statements (cited as [DF80] in Cao–Nissim–Sheffield 2509.04688); open and record exact hypotheses | Implication false for gauge-invariant local (non-string) states; does not cover G₂ | Medium-High |
| L-04 PROPOSAL | **Exact finite-volume gap certificates on small lattices** for SU(2) Kogut–Susskind Hamiltonians truncated in representation j, with rigorous interval bounds, scanned in g | Exact diagonalization + Temple/Kato lower bounds (rigorous eigenvalue enclosures) | Rigorous enclosures, not Monte Carlo | 2×2×2 periodic, j≤1, flint/Arb enclosures of E₁−E₀ vs g | Truncation error not controllable uniformly in j | Medium |
| L-05 PROPOSAL | **Gap via OPE + positivity (bootstrap-style)**: use the constructed OPE/positivity to exclude spectral weight in (0,Δ) for Θ two-point function | Källén–Lehmann for Θ, plus a log² short-distance law, plus a sum rule (trace anomaly) | Conformal-bootstrap-type inequalities in a non-conformal, AF theory | Derive which spectral densities ρ(μ²) are compatible with r⁸log²(1/r) behaviour and positivity; check that massless ρ is *not* excluded (expected) | Massless spectral densities remain admissible (likely) → only partial | Medium |
| L-06 PROPOSAL | **Geometric (Singer/Feynman) orbit-space curvature**: lower bound on the Laplacian on 𝒜/𝒢 via Ricci curvature of the orbit space (JW §6.6 refs [44],[11]) | Bochner/Lichnerowicz on infinite-dim quotient, regularized on the lattice | Uses geometry of the configuration space, not expansions | Compute the O'Neill curvature of the lattice orbit space for one plaquette SU(2) | Curvature non-uniform in lattice size / volume | Medium |
| L-07 PROPOSAL | **Large-N first**: prove a gap for SU(N) at N=∞ in the 't Hooft limit with continuum control, then 1/N | Master loop equations (Chatterjee, Cao–Nissim–Sheffield); Gross–Witten phenomenon | Order of limits N→∞ before a→0 | Map which loop-equation estimates are uniform in β at large N | Third-order (GW-type) transition between strong and weak coupling at N=∞ in 4D | Medium |
| L-08 PROPOSAL | **Duality/Debye-screening analogue** (JW §6.6): find a change of variables (e.g. dual/abelian-projected or centre-vortex representation) where the gap is "classical" | Brydges–Federbush Debye screening via sine-Gordon | Non-perturbative variable change | Literature: centre-vortex rigorous results; write the SU(2) lattice dual (spin-foam/character) representation and check positivity of weights | Dual weights not positive (sign problem) | Medium-Low |
| L-09 PROPOSAL | **Formal-statement hardening**: write a Lean `MassGap` predicate on the 2026 `WightmanTheory` (`energyMomentum.projection {p | 0 < time p < Δ} = 0`, all phases) and pin it as the WITNESS LAB target | Lean/Mathlib; existing PublicTheory API | Makes the gap target machine-checkable and prevents drift | Write and elaborate the predicate against the pinned challenge env (already built) | None (low risk); value is infrastructure | High (cheap) |
| L-10 PROPOSAL | **G₂ / trivial-centre stress test**: every proposed mechanism must be checked on G₂ (no centre, string breaking by gluons) | Group theory (WS10) | Prevents SU(N)-only arguments | Tabulate which mechanism (centre symmetry, area law, LSI curvature) uses the centre | Mechanism needs nontrivial centre ⇒ not general | High (as a filter) |
| L-11 PROPOSAL | **Uniqueness via FKG-free mixing**: show uniqueness of the IR limit using the Langevin dynamics' contraction at the crossover scale, combined with UV RG | SZZ-type Wasserstein contraction | Uniqueness via dynamics rather than cluster expansion | Estimate contraction rate of block-spin Langevin at effective coupling g_eff~1 numerically (SU(2), small blocks) | Contraction fails at g_eff where needed | Medium |

**Top 3 directions:** L-09 (pin a formal gap target; cheap and drift-proof), L-02 (multiscale functional inequalities across the crossover), L-01 (mine and upgrade the 2026 u²/heat bounds), always filtered by L-10.

## 8. Adversarial checklist: how a proposed proof can fail
1. **Lattice gap ≠ continuum gap.** Positive m_lat at every spacing can give zero physical gap (E2: m_lat = a^{1.5} > 0 for every a, m_phys → 0). The required statement is m_lat(β) ≥ Δ·a(β) with a(β) at the AF rate.
2. **Wrong units / wrong scale-setting.** Gap measured against a scale that is itself derived from the gap (circularity). The scale must be fixed independently (e.g. by AF running).
3. **Finite-L gap closing.** E3: a massless field on a torus has gap 2π/L > 0 for every L. Uniformity in L must be shown.
4. **Strong-coupling result presented as continuum.** OS 1978 / SZZ hold for small β. U(1) (Guth; Fröhlich–Spencer) shows the gap can disappear at weak coupling.
5. **Different observable algebra.** Gap shown for Wilson loops or for one field (e.g. Tr F²) without proving that the family is cyclic for Ω in the full ℋ, or gap shown in a selected pure phase only.
6. **Triviality of the limit.** Massive Gaussian limits (YMH: Chatterjee 2401.10507; φ⁴₄: Aizenman–Duminil-Copin) satisfy "gap" vacuously. Need P9.
7. **ℋ = ℂΩ.** "No spectrum in (0,Δ)" is vacuous for a trivial theory. Need m<∞ (JW §4).
8. **Gauge fixing / Gribov.** A global gauge in a perturbative argument is ill-defined non-perturbatively (Singer). Local phase-cell gauges (Balaban) must be patched consistently.
9. **RP lost under RG.** Gap derived by a transfer-matrix argument after a non-RP blocking step.
10. **Circular use of the gap.** Clustering/uniqueness used to construct the IR limit, then used to prove the gap. Or "uniform gap" assumed in finite volume (JW §5 notes a uniform finite-volume gap *may* be used for IR existence; it must be proven first).
11. **Subsequence dependence.** Gap proven along one subsequence or phase while the limit is not unique.
12. **Contact terms / test-function class.** Statements proven only away from coincident points. The Wightman distributions need all of S.
13. **Exchange of limits.** a→0 and L→∞ are taken in a convenient order without uniformity.
14. **Group restriction.** SU(2)-only or centre-dependent arguments (fails for G₂, E₈, F₄).
15. **Lean statement weaker than claimed.** Existentially chosen insertions, slopes or phases. Selected-phase theorems. Missing spectral clause (all present in the 2026 public target, §3.2). Always read the exact `def`, check `#print axioms` on the *proof*, and Comparator against a pinned target.
16. **Numerics as proof.** Monte Carlo or truncated ED gaps are evidence only.
17. **Unrefereed claims.** Abstract-level claims (§5 last row) are not results until a full audit is done.

## 9. Independent verification archive (set up)
Folders in `07_LATTICE_INDEPENDENT_REVIEW/`, each with a README stating purpose, naming convention (`QL-20261121-01_<topic>_vN.md`), required fields and evidence rules: `independent_derivations/`, `adversarial_reviews/`, `counterexamples/`, `proof_audits/`, `code_reviews/`, `innovation_proposals/`, `verdicts/`. All seven already existed (created empty by QUASAR at 17:27 CT); LATTICE added the READMEs. Seeded content: `proof_audits/` points to §3 of this report; `counterexamples/` records E2/E3; `verdicts/` records the verdict above. Setup is logged as row L-E001 in `13_EVOLUTION_AND_IMPROVEMENT/evolution_log.md` (QUASAR's rows untouched).
LATTICE's own reproducible record (git repo `reviews/`, user LATTICE): `reviews/QL-20261121-01/` with `LATTICE_initial_baseline.md` (copy), `sources/` (JW PDF + KITP PDFs + hashes), `code/` (`exp_2d_su2_gap.py` + output, crossref/arXiv check scripts and outputs), `formal/challenge_check/` (pinned elaboration project + `build.log`). The cloned artifact repos (`artifacts/`, ~300 MB) are git-ignored and re-clonable at the commits above.

## 10. Innovation register
Created at `innovation_proposals/innovation_register.md`, seeded with L-01…L-11 (status PROPOSAL, untested).

## 11. First adversarial and innovation roadmap for QUASAR
**Comments on INV-001 framing.** The framing is **essentially right**, and it correctly locates the content in the physical-unit transfer. Specific corrections and additions:
1. **Sufficiency lemma: required hypotheses.** It holds as a theorem only with all of these:
   - (a) a family 𝔉 of local gauge-invariant fields whose OS-reconstructed vectors {Φ(f)Ω} are **cyclic** (total) in the *full* reconstructed ℋ. Cyclicity in a sub-sector gives a gap only on that sector.
   - (b) **uniform exponential clustering in physical units**: |S^T(Φ_1(f), τ_t Φ_2(g))| ≤ C(f,g) e^{−Δt}, with Δ independent of a and L, and with C(f,g) controlled by Schwartz seminorms.
   - (c) **convergence of Schwinger functions** (a→0, L→∞) along the *whole* family, not a subsequence, or else the statement made per limit point.
   - (d) the OS axioms incl. **RP and the E0′ growth condition** for the limit, so that OS-II reconstruction applies and H is defined as the generator of the OS semigroup e^{−tH}.
   - (e) uniqueness of the vacuum, or a per-phase statement. Under (a)–(e), ⟨ψ, e^{−tH}(1−P₀)ψ⟩ ≤ Ce^{−Δt} on a dense set ⇒ σ(H)∩(0,Δ)=∅. This is the standard spectral-measure argument; sketch in `independent_derivations/README.md`.
   - Clustering needs exponential decay in *Euclidean time* for the semigroup. Spatial decay alone is insufficient without Lorentz invariance arguments.
2. **Obstruction lemmas are correct.** I reproduced them exactly (`code/exp_2d_su2_gap.py`):
   - E2: a gap at every spacing with continuum gap 0;
   - E3: finite-L gaps 2π/L closing;
   - E1: 2D SU(2) with m_lat = O(a) → 0 while m_phys → g²C₂L/2 = 3/8, matching −log(I₂/I₁) = 3/(2β)+3/(4β²)+O(β⁻³), checked symbolically and to 50 digits.
   - Add a 4th obstruction: **U(1)₄ (Guth; Fröhlich–Spencer)**. A strong-coupling gap does not survive to weak coupling. The proof must use non-abelian AF.
   - Add a 5th: **triviality**. A gapped massive Gaussian limit is not YM.
3. **Can 2D experiments say anything about 4D?** Only about *bookkeeping*: unit conversion, the m_lat ≥ Δa form, transfer-matrix and character technology, and order of limits. They say nothing about the 4D mechanism:
   - pure 2D YM has no propagating degrees of freedom;
   - on ℝ its gauge-invariant Hilbert space is one-dimensional (the "gap" is vacuous);
   - on a cylinder of length L, the gap grows like σL (E1b), a confinement artefact of compact space;
   - 2D YM is super-renormalizable with no AF crossover.

   Recommend replacing "2D experiments" by (i) 3D/4D small-volume Hamiltonian enclosures (L-04) and (ii) U(1) vs SU(2) contrast tests (the counterexample shows which estimates *must* fail).
4. **Recommend INV-001 be stated against the 2026 artifact.** The open item is exactly an upgrade from `inverse_square` (M s⁻²) to M e^{−Δs}, uniformly over phases (and subsequences).

**Ranked roadmap (first concrete steps):**
| Rank | Action | Owner | First step | What it settles |
|---|---|---|---|---|
| 1 | Pin the formal gap target (L-09) | QUASAR drafts, LATTICE audits | Lean `MassGap T Δ` on `WightmanTheory` in the pinned env; require ∀ phases and state the subsequence quantifier explicitly | Prevents target drift; makes every claim checkable |
| 2 | INV-001 sufficiency lemma with hypotheses (a)–(e) above | QUASAR | Written proof; LATTICE reconstructs independently | Whether the bridge is correctly framed |
| 3 | Locate the source of the u² / s⁻² bounds in the 2026 code (L-01) | QUASAR reads, LATTICE checks | Trace `word_bound`, `late`, `annulus` dependencies | Whether these bounds can carry any gap information |
| 4 | Crossover analysis (L-02, L-11) on toy blocks | QUASAR | Ricci/LSI constants of SU(2) block effective actions vs g_eff | Feasibility of a functional-inequality route through B4 |
| 5 | G₂ filter (L-10) on every mechanism | both | Table of centre-dependence | Avoid SU(N)-only proofs |
| 6 | Independent rebuild of the 2026 proof when resources allow | LATTICE (deferred by directive) | Linux build with isolation, `#print axioms` on `YangMills.jointExistence` (solution) and `constructed` | Kernel-level confidence in the existence input |

Outstanding items honestly not done: the full proof rebuild; recomputing the 3 dim𝔤/π⁴ coefficient; reading full texts (most sources are [A] only); audits of the unrefereed claims in §5; the OpenAI 4 Nov and Alpöge–Sussman 15 Nov submissions (no artifacts public).
