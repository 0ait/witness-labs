<!--
title: INV-001 literature baseline
id: QL-20261121-01/INV-001/literature
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: internal record, copied
internal-source: WitnessLab/05_RESEARCH_WORKSTREAMS/WS01_spectral_gap/INV-001_literature.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# INV-001 literature baseline: from a finite-lattice gap to a continuum, infinite-volume gap

QL-20261121-01 · WITNESS LAB · QUASAR · compiled 2026-11-21 (America/Chicago)

**Scope.** Only sources bearing on INV-001. Every DOI below was resolved against the Crossref REST API (api.crossref.org/works/<doi>) on 2026-11-21. Title, authors, venue, volume, pages and year were compared field by field; all matched except where noted. arXiv metadata came from export.arxiv.org. Search order: Tavily first, then the arXiv API, Crossref and direct PDF fetches. Exa was not used.

**Access level legend.**
- **[P]** primary full text opened locally (PDF text-extracted; sha256 in `03_LITERATURE_AND_SOURCE_ARCHIVE/preprints/INV001/SHA256SUMS.txt`).
- **[A]** official abstract or first page only.
- **[S]** content known only through secondary sources that cite it.

Anything not verifiable at one of these levels was dropped (see the end of the file).

Source IDs: register rows S-101…S-126 (appended to `source_register.csv`). Pre-existing rows from the parallel worker (S-001 Jaffe–Witten, S-003/S-004 OS73/75, S-005 OS78, S-006/S-007 Balaban 85/87, S-016 Nissim 2025) are referenced, not duplicated.

---

## 0. The official framing (S-001, [P]; same sha256 3558403c… as the parallel worker's copy)
Jaffe–Witten, *Quantum Yang–Mills Theory* (Clay official description):
- Mass gap definition: "H has no spectrum in the interval (0,Δ) for some Δ>0".
- §5, eq. (2): clustering |⟨Ω,O(x)O(y)Ω⟩| ≤ exp(−C|x−y|) for any C<Δ, as a *consequence* of the gap. They add: "the existence of a uniform gap for finite-volume approximations may play a fundamental role in the proof of existence of the infinite-volume limit."
- §6: "no present ideas point the direction to establish the existence of a mass gap that is uniform in the volume. Nor do present methods suggest how to obtain the existence of the infinite volume limit T⁴→R⁴."
- §6 (lattice paragraph): reflection positivity holds for the Wilson approximation [OS78]. Balaban's 3D and 4D estimates "are uniform in the lattice spacing" on a periodic lattice. "These results need to be extended to the study of expectations of gauge-invariant functions of the fields." "New ideas are needed to prove the existence of a mass gap that is uniform in the volume of space-time."

## 1. Reflection positivity and the transfer matrix (Wilson lattice gauge theory)
| ID | Source | Verified | What is proved (as verified) |
|---|---|---|---|
| S-101 | M. Lüscher, *Construction of a selfadjoint, strictly positive transfer matrix for Euclidean lattice gauge theories*, CMP 54 (1977) 283–292, doi:10.1007/BF01614090 | Crossref ✓; [A] (INSPIRE abstract) | "physical positivity holds in Wilson's lattice gauge theories, i.e. transition probabilities between gauge invariant states are non-negative and the quantum mechanical Hamiltonian has real eigenvalues only"; the title asserts a self-adjoint, strictly positive transfer matrix. Theorem numbers not read. |
| S-005 | K. Osterwalder, E. Seiler, *Gauge field theories on a lattice*, Ann. Phys. 110 (1978) 440–471, doi:10.1016/0003-4916(78)90039-8 | Crossref ✓; [A] (ScienceDirect abstract) + [S] | Abstract: physical (OS) positivity of the lattice Schwinger functions ⇒ "existence of a positive self-adjoint transfer matrix"; "existence and analyticity of the infinite volume limit of strongly coupled Yang–Mills theories on the lattice"; "Wilson's confinement bound"; Higgs mechanism. Per SZZ 2022 §1 [P]: OS78 sketched a convergent cluster expansion at strong coupling, "uniformly in volume", from which exponential clustering (mass gap), the infinite-volume limit and analyticity follow. Section numbers not read (paywalled). |
| S-102 | P. Menotti, A. Pelissetto, *General proof of Osterwalder–Schrader positivity for the Wilson action*, CMP 113 (1987) 369–373, doi:10.1007/BF01221251 | Crossref ✓; title only | Title-level claim: OS positivity for the Wilson action in general. Content not opened; cited only for completeness. |
| S-103 | J. Kogut, L. Susskind, *Hamiltonian formulation of Wilson's lattice gauge theories*, PRD 11 (1975) 395–408, doi:10.1103/PhysRevD.11.395 | Crossref ✓; not opened | Source of the Hamiltonian used in E02 (formulation, not a theorem). |
| S-104 | M. Creutz, *Gauge fixing, the transfer matrix, and confinement on a lattice*, PRD 15 (1977) 1128–1136, doi:10.1103/PhysRevD.15.1128 | Crossref ✓; not opened | Title-level: transfer matrix in temporal gauge. Not relied on. |

**Bridge relevance.** These give, at *each fixed* (β, L), a positive self-adjoint T and hence a lattice Hamiltonian H_lat = −a^{−1}log(T/λ₀) ≥ 0 (D02). Nothing here is uniform in a or L.

## 2. Strong-coupling lattice mass gap
| ID | Source | Verified | What is proved |
|---|---|---|---|
| S-005 | OS78 (above) | [A]+[S] | Strong coupling (β small): convergent cluster expansion uniform in volume ⇒ unique infinite-volume limit, analyticity, exponential clustering (lattice mass gap in lattice units), area law. |
| S-105 | E. Seiler, *Gauge Theories as a Problem of Constructive Quantum Field Theory and Statistical Mechanics*, Lecture Notes in Physics 159, Springer 1982, doi:10.1007/3-540-11559-5 | Crossref ✓ (no author field in Crossref; author confirmed by a library catalogue: Seiler, Erhard, iv+192 pp.) [S] | Monograph on expansion methods for lattice gauge theories. SZZ 2024 [P] cites "[Sei82, Theorem 3.18]" for the mass gap of lattice Yang–Mills–Higgs at small β, κ via cluster expansion and the U-gauge, and "[Sei82, Sec. 3]" for that technique. Chatterjee 2018 cites Seiler [74, Ch. 8] for the continuum-limit programme through Wilson loops. Pure-YM theorem numbers were not verified and are not claimed. |
| S-106 | H. Shen, R. Zhu, X. Zhu, *A stochastic analysis approach to lattice Yang–Mills at strong coupling*, CMP 400 (Crossref issued 2022) 805–851, doi:10.1007/s00220-022-04609-1, arXiv:2204.12737 | Crossref ✓; [P] | Action S=Nβ Re ΣTr Q_p ('t Hooft scaling), G=SO(N) or SU(N), any d≥2. Assumption 1.1: |β|<1/(16(d−1)) for SU(N); for SO(N), |β|<1/(32(d−1))−1/(16N(d−1)). Thm 1.2: unique invariant measure of the Langevin dynamics on ℤ^d; the whole sequence of finite-volume measures converges as L→∞; exponential ergodicity. Thm 1.4: log-Sobolev and Poincaré inequalities (via Bakry–Émery). Cor. 1.6 ("Mass gap"): for cylinder f,g with disjoint supports, Cov(f,g) ≤ c₁e^{−c_N d(Λ_f,Λ_g)}(⦀f⦀_∞⦀g⦀_∞+‖f‖‖g‖), with c₁ depending on \|Λ_f\|,\|Λ_g\| and c_N on K_S,N,d. **In lattice units, infinite volume, at a fixed strong-coupling range.** |
| S-107 | H. Shen, R. Zhu, X. Zhu, *Langevin dynamics of lattice Yang–Mills–Higgs and applications*, CMP 407 (2026), doi:10.1007/s00220-025-05528-7, arXiv:2401.13299v3 | Crossref ✓; [P] | Thm 1.4: mass gap (exponential decay of correlations) for any infinite-volume limit of lattice YM–Higgs at small β and small κ (or κ/m). Includes the remark (p. 3) that "temporal mixing (ergodicity) and spatial mixing (mass gap) are often related". Model with Higgs field, strong coupling, lattice units. |
| S-016 | R. Nissim, *U(N) lattice Yang–Mills in the 't Hooft regime*, arXiv:2510.22788v1 (2025) | [A] (arXiv abstract) | Mass gap, unique infinite-volume limit and large-N limit for U(N) lattice YM in the 't Hooft regime. Bakry–Émery fails for U(N) (Ricci curvature not uniformly positive) and is replaced by a U(1)×SU(N) random-environment decomposition plus cluster expansion. Strong coupling; lattice units. |
| S-108 | S. Cao, R. Nissim, S. Sheffield, *Expanded regimes of area law for lattice Yang–Mills theories*, arXiv:2505.16585v3 (2025) | [P] | Thm 1.2: area law for U(N) for all d≥2, β≤β₀(d), all N≥1: \|⟨W_ℓ⟩\| ≤ C_{1,d}C_N^{\|ℓ\|}exp(−C_{2,d} area(ℓ)). Improves OS78 at large N. Area law, not a mass gap. |
| S-109 | S. Cao, R. Nissim, S. Sheffield, *Dynamical approach to area law for lattice Yang–Mills*, arXiv:2509.04688v2 (2025); author page says "to appear in Proc. AMS" | [P] | Thm 1.6: area law in the 't Hooft regime for G∈{U(N),SU(N),SO(2(N−1))}, obtained by verifying the Durhuus–Fröhlich mass-gap condition for an associated σ-model via the SZZ dynamics. Area law; nontrivial centre needed. |
| S-110 | B. Durhuus, J. Fröhlich, *A connection between ν-dimensional Yang–Mills theory and (ν−1)-dimensional, non-linear σ-models*, CMP 75 (1980) 103–151, doi:10.1007/BF01222514 | Crossref ✓; [S] (via S-109 [P]) | A σ-model mass-gap condition implies an area law (as used in S-109 §2; S-109 refers to "[DF80, Theorem 1.3]"). |
| S-111 | A. Adhikari, S. Cao, *Correlation decay for finite lattice gauge theories at weak coupling*, Ann. Probab. 53 (2025) 140–174, doi:10.1214/24-AOP1702, arXiv:2202.10375v3 | Crossref ✓; [P] | d=4 (the paper says it works only in dimension four), **finite** gauge group G. Thm 1.1: for β ≥ (114+4 log\|G\|)/Δ_G, rectangles B₁,B₂ at ℓ^∞ distance ≥ L, and conjugation-invariant functions of loops in B_i: \|Cov\| ≤ 4(4·10²⁴\|G\|²)^{\|B₁\|+\|B₂\|}‖f₁‖_∞‖f₂‖_∞e^{−(β/2)Δ_G(L−1)}. Uniform in volume, at weak coupling, but the lattice-unit decay rate grows ∝β. There is no continuum limit (finite G). This illustrates D03.2. |

## 3. Balaban's renormalisation-group programme (lattice YM, 3D and 4D)
| ID | Source | Verified |
|---|---|---|
| S-006 | T. Balaban, *Ultraviolet stability of three-dimensional lattice pure gauge field theories*, CMP 102 (1985) 255–275, doi:10.1007/BF01229380 | Crossref ✓ |
| S-112 | Balaban, *Propagators and renormalization transformations for lattice gauge theories. I*, CMP 95 (1984) 17–40, doi:10.1007/BF01215753 | Crossref ✓ |
| S-113 | Balaban, *Averaging operations for lattice gauge theories*, CMP 98 (1985) 17–51, doi:10.1007/BF01211042 | Crossref ✓ |
| S-114 | Balaban, *Spaces of regular gauge field configurations on a lattice and gauge fixing conditions*, CMP 99 (1985) 75–102, doi:10.1007/BF01466594 | Crossref ✓ |
| S-115 | Balaban, *Propagators for lattice gauge theories in a background field*, CMP 99 (1985) 389–434, doi:10.1007/BF01240355 | Crossref ✓ (bibliographic query match) |
| S-116 | Balaban, *The variational problem and background fields in renormalization group method for lattice gauge theories*, CMP 102 (1985) 277–309, doi:10.1007/BF01229381 | Crossref ✓ |
| S-007 | Balaban, *Renormalization group approach to lattice gauge field theories. I. Generation of effective actions in a small field approximation and a coupling constant renormalization in four dimensions*, CMP 109 (1987) 249–301, doi:10.1007/BF01215223 | Crossref ✓; [P-partial] (Project Euclid PDF excerpts via Tavily extract) |
| S-117 | Balaban, *… II. Cluster expansions*, CMP 116 (1988) 1–22, doi:10.1007/BF01239022 | Crossref ✓ |
| S-118 | Balaban, *Large field renormalization. I. The basic step of the R operation*, CMP 122 (1989) 175–202, doi:10.1007/BF01257412 | Crossref ✓ |
| S-119 | Balaban, *Large field renormalization. II. Localization, exponentiation, and bounds for the R operation*, CMP 122 (1989) 355–392, doi:10.1007/BF01238433 | Crossref ✓; [A] (abstract and intro via search excerpt of Project Euclid PDF) |

**What is proved (verified text only).**
- (i) 1987 paper, intro: the analysis is on a periodic lattice T_η (finite volume). For the effective action at the unit lattice the bound "is uniform in the lattice spacing ε. This is the essence of the [ultraviolet stability]". "Ultraviolet stability … has two aspects", namely bounds on effective actions and the behaviour of the effective coupling sequence g_k; "In this paper we prove a theorem concerning the first aspect."
- (ii) 1989-II abstract: "In this paper we conclude the discussion of the basic properties and bounds for the R operation. This allows us to complete the proof of the ultraviolet stability of four-dimensional pure gauge field theories, as formulated in Theorem 1." Its Theorem 1 opens: "If the sequence of the effective coupling constants is contained in an interval ]0,γ] with a sufficiently small positive γ, then the effective densities ρ_k have the form, and satisfy all the conditions …".
- (iii) Jaffe–Witten [P]: Balaban's estimates are uniform in the lattice spacing on a compactified space-time; they "need to be extended to the study of expectations of gauge-invariant functions of the fields".

**Not proved** (per the same texts):
- correlation functions or Schwinger functions of gauge-invariant observables, and hence any OS reconstruction or spectrum;
- the infinite-volume limit;
- control when effective couplings leave ]0,γ]. Under asymptotic freedom, that happens once the RG reaches the physical scale. This is QUASAR's reading (label: Heuristic), not a quotation.

Expository: J. Dimock, *The renormalization group according to Balaban, I. Small fields*, Rev. Math. Phys. 25 (2013) 1330010, doi:10.1142/S0129055X13300100 (Crossref ✓; S-120). It treats φ⁴₃, not gauge theory.

## 4. Magnen–Rivasseau–Sénéor (finite-volume YM₄)
S-121: J. Magnen, V. Rivasseau, R. Sénéor, *Construction of YM₄ with an infrared cutoff*, CMP 155 (1993) 325–383, doi:10.1007/BF02097397 (Crossref ✓). [A]: author-posted mp_arc 92-41 abstract ("Rigorous results on the ultraviolet limit of non-Abelian gauge theories") and the Project Euclid first-page snippet: "rigorous construction of the Schwinger functions of the pure SU(2) Yang–Mills field theory in four dimensions (in the trivial topological sector) with a fixed infrared cutoff but no ultraviolet cutoff, in a regularized axial gauge"; Gribov ambiguities discussed. Chatterjee 2018 [P] adds that the regularisation adds a quadratic term which breaks gauge invariance, restored in a limit. **Not claimed in the verified text:** removal of the infrared cutoff, OS positivity / reconstruction, spectral statements. Theorem numbers not read.

## 5. Probabilistic surveys and formulations
S-122: S. Chatterjee, *Yang–Mills for probabilists*, in *Probability and Analysis in Interacting Physical Systems*, Springer Proc. Math. Stat. (2019) 1–16, doi:10.1007/978-3-030-15338-0_1, arXiv:1803.01950 (Crossref ✓; [P]). It contains:
- Problem 4.1 (area law at all β);
- Problem 5.1 (Mass gap, lattice formulation): for any infinite-volume limit of 4D lattice gauge theory and every β>0, the plaquette correlation length ξ(β)∈(0,∞) exists, and lim_{β→∞}ξ(β)=∞;
- Problem 5.2 (continuum limit through rectangular Wilson loops);
- §6: "there is yet no construction of a continuum limit of a lattice gauge theory in any dimension higher than two where Wilson loop variables have been shown to have nontrivial behavior."

Note: Problem 5.1 is a two-point-function statement for one observable (the plaquette). By D06 it is not by itself the full gap.

## 6. Stochastic quantisation (2D, 3D)
| ID | Source | Verified | What is proved |
|---|---|---|---|
| S-123 | A. Chandra, I. Chevyrev, M. Hairer, H. Shen, *Langevin dynamic for the 2D Yang–Mills measure*, Publ. Math. IHÉS 136 (2022) 1–147, doi:10.1007/s10240-022-00132-0, arXiv:2006.04987 | Crossref ✓; [P] | Thm 2.1 (Banach space Ω¹_α of distributional connections with well-defined holonomies), Thm 2.4 (local existence), Thm 2.9 (gauge covariance), Thm 2.13 (Markov process on the orbit space). §1.3: invariance of the YM measure was left as an open conjecture. |
| S-124 | I. Chevyrev, H. Shen, *Invariant measure and universality of the 2D Yang–Mills Langevin dynamic*, Comm. Pure Appl. Math. 79 (2026) 1973–2102, doi:10.1002/cpa.70043, arXiv:2302.12160 | Crossref ✓; [A] | The 2D YM measure on the torus is invariant for the renormalised Langevin dynamic; universality, including for Wilson, Villain and Manton lattice actions. |
| S-125 | A. Chandra, I. Chevyrev, M. Hairer, H. Shen, *Stochastic quantisation of Yang–Mills–Higgs in 3D*, Invent. Math. 237 (2024) 541–696, doi:10.1007/s00222-024-01264-2, arXiv:2201.03487 | Crossref ✓; [P] | State space S and orbit space O; Thm 1.7 (local existence of the renormalised SYMH flow), Thm 1.9 (unique gauge-covariant renormalisation). §1.2: whether the process admits an invariant measure is open; "we do not even know how to show … that the Markov process survives for all times." |

**Bridge relevance.** These are constructions in 2D/3D, on the torus, of dynamics, not of 4D measures. No mass gap is claimed. SZZ-type results (S-106, S-107) are the lattice analogue in which ergodicity of the dynamics yields spatial decay, but only at strong coupling.

## 7. Uniform clustering ⇒ spectral gap after OS reconstruction
- S-003/S-004 (OS73, OS75): reconstruction theorems (Crossref ✓ by the parallel worker and by QUASAR).
- **Glimm–Jaffe**, *Quantum Physics: A Functional Integral Point of View*, 2nd ed., Springer 1987, doi:10.1007/978-1-4612-4728-9 (Crossref ✓; S-126). [S] only: secondary sources attribute "exponential clustering at rate Δ ⇔ spectral gap ≥ Δ" to Glimm–Jaffe §6.2 / Ch. 6. **No theorem number is claimed.**
- The statement is proved self-contained in **INV001-D01** (with converse), which is what the lab relies on.

## 8. Relevance matrix (what each item supplies toward the bridge)
| Need | Supplied by | Gap |
|---|---|---|
| Positive self-adjoint lattice transfer matrix at fixed (β,L) | S-101, S-005 | none (fixed regulator) |
| Lattice gap in lattice units, infinite volume | S-005, S-106, S-107, S-016 (strong coupling); S-111 (finite G, weak coupling) | only β ≤ β_max (continuous G); finite G has no continuum limit |
| UV stability, uniform in a, finite volume | S-007, S-117–S-119 (+ S-006 for 3D) | conditional on small effective couplings; no correlation functions; no infinite volume |
| Continuum YM₄ Schwinger functions, finite volume | S-121 (SU(2), IR cutoff, axial gauge) | IR cutoff not removed; no OS positivity or spectrum claimed |
| Continuum YM in 2D/3D via dynamics | S-123–S-125 | not 4D; 3D global existence and invariant measure open |
| Clustering ⇒ gap | D01 (self-contained), [S] Glimm–Jaffe | — |
| **Uniform-in-a, uniform-in-L lower bound m^{loc} ≥ Δ·a(β) at weak coupling** | **nothing found** | **this is the missing estimate (report §4)** |

## Dropped or quarantined
- arXiv:2503.15539 ("Pinched multi affine geometry and confinement…"), arXiv:1406.4177 (Farinelli), arXiv:2506.00284 (Jacobsen), the researchsquare and academia.edu "proofs", and the HAL "spectral mass gap" note. These are claimed solutions or secondary material that surfaced in searches. They are not baseline literature and are left to the parallel 04_CANDIDATE_SOLUTIONS audit; nothing from them is used here.
- MathSciNet was not accessible. Glimm–Jaffe, OS78, Seiler LNP 159 and MRS were not opened in full (paywalled or bot-protected; Project Euclid's Incapsula block was not circumvented). Every statement attributed to them above is limited to abstract-level or cited-by-others content, as labelled.

## 9. Addendum (S01-B, after reading LATTICE's initial baseline §11)
- **S-127** Guth, PRD 21 (1980) 2291–2307, doi:10.1103/PhysRevD.21.2291 (Crossref ✓) and **S-128** Fröhlich–Spencer, CMP 83 (1982) 411–454, doi:10.1007/BF01213610 (Crossref ✓). They establish a non-confining, massless phase of 4D U(1) lattice gauge theory at weak coupling (title and standard knowledge; texts not opened, [T]).
  - **Relevance.** In 4D U(1) the strong-coupling lattice mass gap (OS78/Seiler) holds at small β and *fails* at large β. Hence no argument that uses only properties shared by U(1) (compactness, RP, a strong-coupling expansion, and a perturbative scale) can prove ME1. A proof must use non-abelian structure (asymptotic freedom). This is an obstruction on *proof methods*, not on the YM gap (Established theorem for U(1); implication for methods: Heuristic but standard).
- **2026 claimed existence construction** (parallel worker's register S-013 assessment, S-014 Lean source; audit `04_CANDIDATE_SOLUTIONS/candidate_audit_reports/openai_2026_existence_audit.md`).
  - Status: claim, with a first-pass audit by QUASAR-A and no LATTICE rebuild. Per the assessment it constructs Wightman theories as subsequential scaling limits of 4D Wilson LGT for every simple compact G, and "does not prove that the infinite-volume limit is unique or that there is a mass gap" (S-013 p.1, quoted in the audit).
  - Relevance to INV-001. *If* that construction is verified, it would address ME2 (convergence + OS + field content) along subsequences and per phase. The audit records an internal spectral bound `inverse_square`: 0 ≤ ⟨A,(e^{−sH}−P₀)A⟩ ≤ M s^{−2}, with spectral weight of (0,u] ≤ M u². This is polynomial and consistent with gapless spectrum. The missing gap statement then reads ME2′ (report §5).
  - Not relied upon for any INV-001 proof.
