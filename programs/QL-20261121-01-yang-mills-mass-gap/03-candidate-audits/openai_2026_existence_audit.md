<!--
title: Audit of the reported 2026 OpenAI Lean existence construction
id: QL-20261121-01/T7/audit
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: first-pass audit; compared with LATTICE baseline in the 2026-11-21 check-in
internal-source: WitnessLab/04_CANDIDATE_SOLUTIONS/candidate_audit_reports/openai_2026_existence_audit.md
body: copy of the internal record; only local absolute paths were redacted (see REDACTIONS.md)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
> **Public-archive note:** paths such as `official_sources/…`, `../openai_2026_existence/extracted/` and `candidate_solutions/openai_2026/` refer to the internal archive. Third-party PDFs, text extractions and the cloned repositories are not redistributed; see `../02-literature/source_register.csv` (URLs, commits, sha256) and `extracted-theorem-statements.md`. LATTICE's comparison is in `../05-lattice-independent-review/checkin_2026-11-21.md` §(e).

# Audit: reported 2026 AI existence construction (OpenAI Lean submission of 2026-10-28)

Research ID QL-20261121-01 · Auditor: QUASAR · 2026-11-21 (CT) · Status: **first-pass audit. Not reviewed by LATTICE.**
Everything below about the construction is a **claim** by OpenAI or by the Yang–Mills group, unless it is marked "QUASAR-verified". Nothing here is a Clay determination. The Clay page still labels the problem "Unsolved" (retrieved 2026-11-21 17:32 CT; `official_sources/clay_page.html`). The group itself writes: "Our group has no present connection to the Clay Mathematics Institute" (assessment p.1).

## 0. Sources located (all opened; sha256 in `source_register.csv`)
| ID | What | Where |
|---|---|---|
| S-010 | 1st committee statement, "October 2026" (no day). Douglas, Gross (Chair), Jaffe, Klebanov, Nekrasov | KITP `YM_working_group.pdf`; archived copy in yang-mills-group/.github |
| S-011 | **2nd statement, 3 Nov 2026** (the "shepherding committee" statement named in the mission order) | KITP `2nd-Statement-About-Quantum-YangMills-Theory_Nov-3.pdf` (copy via .github repo; sha256 matches the group's `sources.json`) |
| S-012 | 3rd statement, 9 Nov 2026 (announces the 10 Nov release) | KITP `3rd-Statement-About-Quantum-YangMills-Theory_Nov-9.pdf` (downloaded directly) |
| S-013 | **Assessment 1, "Validation of the OpenAI Yang–Mills construction", dated Nov 10 2026, 35 pp.** (the "November 10 assessment") | yang-mills-group/YM `docs/assessment-1.pdf`, repo commit b379615f… |
| S-014 | **Original Lean submission** | github.com/yang-mills-group/OpenAI-YM-20261028, commit 3456e5e7… (single commit) |
| S-015 | Group's rules and procedures (undated; archived 2026-11-08) | .github repo |
Not obtained: the informal proof manuscript ("1147-page LLM proofs", S-010 p.2). It has not been released, and S-013 p.1 says the assessment "does not draw on the separate informal proof manuscript". Also not obtained: OpenAI's announcement page (only a secondary snippet seen), and the "OpenAI, 4 November 2026" submission, listed as "work in progress" in the YM README with no materials.

Verbatim key sentences:
- S-011 (3 Nov): "Currently, we are focused on checking the Lean proof of the existence of pure Yang-Mills theory, specifically that the definitions and problem statements correspond with those that are standard in physics and mathematics, and that the formalization aligns with the informal treatment."
- S-013 p.1: "In our judgment the submission proves that a relativistic quantum field theory satisfying the Wightman axioms can be constructed as a scaling limit of four-dimensional Wilson lattice gauge theory for any simple compact gauge group. It does not prove that the infinite-volume limit is unique or that there is a mass gap."
- S-013 p.1: "OpenAI's construction does not certify the full Jaffe–Witten problem: no mass gap is claimed. Uniqueness across volume subsequences and agreement of the component theories are also unresolved."
- S-013 p.3 item 4: "The construction provides no evidence for or against a mass gap in the theory."

## 1. Locate the original Lean submission — DONE
S-014. Toolchain `leanprover/lean4:v4.32.0`. Single dependency Mathlib rev `81a5d257c8e410db227a6665ed08f64fea08e997` (plus Mathlib's transitive deps per `lake-manifest.json`). Size: 9,477 `.lean` files, 987,586 lines. **QUASAR-verified:** all 9,507 hashes in `SOURCES.sha256` match the clone.

## 2. Full source and specifications — DONE (formal); informal — INACCESSIBLE
Formal source obtained in full. Public statement layer copied verbatim to `../openai_2026_existence/extracted/`. The informal manuscript is inaccessible (§0).

## 3. Theorem statements actually proved (verbatim)
Main public theorem (`Solution.lean`), checked by Comparator against the `sorry` reference in `Challenge.lean`:
```lean
theorem YangMills.jointExistence : YangMills.JointExistence
```
with (`ChallengeSpec.lean`, verbatim):
```lean
def JointExistence : Prop := ∀ g : GaugeGroup, g.IsSimple → ∃ C : WilsonFamily g,
  WilsonRegularity C ∧ ∀ p : ℕ → ℕ, StrictMono p → ∃ q : ℕ → ℕ, StrictMono q ∧
    ∃ T : Hierarchy C, T.Properties (p ∘ q)

structure Properties (order : ℕ → ℕ) : Prop where
  wilson : C.Converges order (fun v => T.correlation none (T.project ∘ v))
  reconstruction : T.Reconstructed
  ope : T.OperatorProductExpansion
  nonfree : T.TraceTest
```
Detailed theorem `YangMills.constructed (g) (hg : g.IsSimple) (b : ℝ) (hb : 0 < b)` (`Construction.lean`). The public theorem is a projection of it at penalty b = 1. Other advertised endpoints (upstream `verification/joint-headlines.txt`): `YangMills.su2Simple`, `YangMills.su2Theory`, `YM.Nonperturbative.existence`, `YM.Nonperturbative.continuum`, `…continuum_with_position_tests`, `YM.Contacts.Solstice.celestial`, `YM.Pert.Position.finite_leading`, `…normalized_four`, `YM.Pert.Parity.parityEndpoint`, `…low_read`, `YM.Pert.Asymptotics.comparison`, `YM.SharpGram.habitat`, `…inletFirst`, `…outletFirst`, `YM.Independent.Core.point` (17 in total).

**Reading of the quantifiers [QUASAR]:** for each group, ONE Wilson family (spacings, volumes, couplings, renormalized insertions, all existentially chosen). Then, for EVERY volume sequence p, SOME subsequence q and SOME hierarchy T satisfy the four properties. The hierarchy may depend on p and q.

## 4. Definitions used for "Yang–Mills"
- **Gauge group** (`PublicTheory.lean`): a closed `Subgroup` of U(n+1) with a real Lie algebra characterized by the exponential, and `IsSimple` = nonabelian, with no proper nonzero ideal. This covers every compact Lie group with simple 𝔤 via a faithful unitary representation, including disconnected ones (see `../../01_PROBLEM_FORMALIZATION/group_scope.md`).
- **Lattice theory** (`PublicWilson.lean`): periodic lattice `Site l = Fin 4 → ZMod l`. `wilsonEnergy U = Σ_{x, μ<ν} (1 − Re tr U_□ / (n+1))`. `wilsonLaw` = product Haar measure with density e^{−β·energy}, normalized. Mesh a_N = 1/denominator N. Lattice side = period p · denominator N, so the physical side length is period p.
- **Fields / observables:** `Token` and `insertion N p v x U` are *existential components of `WilsonFamily`*. `WilsonRegularity` requires them to be continuous, gauge invariant, and supported on a fixed finite stencil in lattice units. **QUASAR observation (spec level):** the public statement does not tie the insertions to the curvature. The identification with gauge-invariant polynomials in F, DF and the stress trace lives in the detailed theorem (`YM/Nonperturbative/HeadlineSpec.lean`) and in the group's `OperatorContent` check (A2). We did not audit that check.
- **Running coupling:** `WilsonRegularity.running`: ∃ slope > 0, β_{N,p}/log(1/a_N) → slope uniformly in p. **QUASAR observation:** the public statement does not fix slope = 11C_g/(24π²). The assessment states that value in eq. (7) (p.6) for the construction. We did not locate it in the public spec. It may be in internal specs (`Spec.Calibrated`, `LatticeAndScale`). Pending.

## 5. Assumptions and imported dependencies
- **Axioms:** the upstream log (`verification/joint-check.log`) reports `ENDPOINT_AXIOMS YangMills.jointExistence [propext, Classical.choice, Quot.sound]`, with the same for all 17 endpoints, and a kernel replay of 100,168 project declarations. **Not reproduced by us** (no full build; see item 11).
- **QUASAR grep audit (whole tree, 9,477 files):**
  - `sorry`: 1 occurrence, `Challenge.lean:6`. This is the intentional reference placeholder, outside Solution's import closure according to the README and `archive-graph.log`.
  - `axiom` declarations: 0.
  - `opaque`: 0.
  - `@[implemented_by]` / `@[extern]`: 0.
  - `native_decide` / `ofReduceBool` / `trustCompiler`: 0.
  - `unsafe`: 2 hits, both in comments/strings.
  - `admit`: hits only as an identifier or field name (`x.admit`) or in comments, never as a tactic.
  - `debug.skipKernelTC`: 0.
  - Metaprogramming: one custom command `elab "vintage"` (`YM/UVExtension/Orchard/Barrel.lean`). It builds theorem/definition declarations by renaming constants and submits them through `Lean.addDecl`, which is kernel-checked. It refuses unsafe definitions. We flag it for LATTICE because it generates declarations whose statements are not written in source.
- **External libraries:** Mathlib at the pinned rev. README: "nine public repositories pinned in the Lake manifest".

## 6. Construction of the continuum limit (claims, per S-013 §4 and the spec)
Route: **Wilson lattice gauge theory on the periodic 4-torus.** At **fixed physical volume** L_p, the mesh a_N → 0 along a **construction-chosen spacing sequence**. Renormalized insertions I_{N,p}(v,x) = Σ_j c_j(N,p;v) L_{v_j}(x) have coefficients given by the proof's RG maps, "not explicitly expressed" (S-013 p.6). Smeared correlations are shown Cauchy in N via a Balaban-type RG with "a gauge fixing invariant under discrete lattice symmetries" (S-013 p.6). Limits hold only for test functions supported off the coincidence diagonals and strictly inside the box. Spec: `Converges` requires, for each suitable fixed volume p, the **full** limit in N (not a subsequence). S-013 p.6: "there is no universality result for the types of sequences of spacings a_N → 0".

## 7. Infinite volume, subsequences, uniqueness (claims)
- The volume limit is **subsequential**: for every strictly increasing p there is q, and the limit is along p∘q (spec). This is obtained "via compactness through an Arzelà–Ascoli argument" from local boundedness and equicontinuity uniform in volume (S-013 p.7, eq. (11)), "based on reflection positivity, chessboard estimates, transfer-operator representation, and Cauchy estimates".
- **Uniqueness: not proved.** "it remains unresolved whether the limiting correlations depend on the chosen subsequence" (S-013 p.7).
- **Phase decomposition:** S^mix = ∫ S^ξ dν(ξ) over a compact metric space of "characters" (Gelfand + Riesz–Markov). Each component satisfies OS axioms *including clustering*. OS reconstruction is applied **per component**. The public theorem reconstructs one `selected` character, which is existentially chosen. The phase measure has full support. Agreement of the components is unresolved (S-013 p.1).
- **Relation to JW fn 2 [QUASAR]:** S-013 p.7 itself notes that JW regard a compactness limit as insufficient "unless additional arguments establish the requisite properties of the limit". The construction proves the axioms for the components. It does not prove fn 2's other example property, the mass gap. Whether this meets fn 2 is ambiguity A1/PO-16. **No determination by us.**

## 8. Properties established (claimed), per item of `theorem_specification.md`
| T★ clause | Claimed by S-014/S-013? | Notes |
|---|---|---|
| 1–2 Wightman / OS axioms | **Yes, for the selected component** | W0 including the spectrum condition and unique translation-invariant vacuum; W1; W2 (restricted Poincaré); W3 (`PublicTheory.lean`). The YM group's *independent* OS bridge covers only "the selected centered stress-trace scalar family", "not a separately specified all-field OS interface" (YM `docs/checks.md`, A1). |
| 3 YM field content | Claimed (detailed theorem) | Quotient label spaces F_d ≅ classical Maxwell-type polynomial spaces (S-013 p.4). Not visible in the public statement. |
| 4 Short distance | **Partial** | Leading log law of the trace 2-point function; OPE with error bounds, "but does not show that it matches the predictions of a perturbative expansion" (S-013 p.3). "This is not all-orders perturbative matching" (checks.md A4). |
| 5 Non-triviality | Claimed (weak form) | `TraceTest`: r⁸ log²(1/r)·⟨Θ(x)Θ(0)⟩ → 3 dim 𝔤/π⁴, and it is not eventually equal to any **finite** sum of mass-shell Wick profiles. **QUASAR remark:** this excludes free/Wick fields with finitely many modes. It is weaker than the D7 notion. The log² factor is non-free behavior. The field's identification as the physical stress trace sits in the detailed theorem only. The README says that "general exclusion of continuous-mass generalized free fields" is "outside its scope". |
| 6 Existence standard (fn 2) | Disputed / open | §7. |
| 7 Mass gap | **No** | "A positive mass gap … outside its scope" (README); S-013 p.1 and p.3. |
| Group scope | Claimed for all 𝒢 | Existence only. |
| Intrinsic scale | **No** | YM checks.md A5: the scale calibration and positive lattice probe "do not establish a nonzero intrinsic continuum reference mass". |

## 9. Exactly where the mass-gap argument is absent [QUASAR]
1. **Spec level:** `JointExistence` has no spectral clause beyond W0 (`positiveEnergy`, `uniqueVacuum`). **QUASAR-verified by `#print`** on the elaborated definition (local log `08_FORMAL_VERIFICATION/verification_logs/2026-11-21-openai-ym-print-axioms.log`). A gap clause in their own vocabulary would be `∃ Δ > 0, T.theory.energyMomentum.projection {p | 0 < time p ∧ time p < Δ} = 0`. We wrote and elaborated it as `HasMassGap` (local `AuditCheck.lean`). It appears nowhere in the target.
2. **Volume-uniform IR control:** the uniform-in-L bounds (eq. (11)) are local boundedness and equicontinuity on compact distinct-point sets. They are not decay bounds, so they give no exponential clustering rate uniform in L. This is precisely PO-11/PO-12 [JW p.7, p.12].
3. **Infinite-volume uniqueness / phases:** with a non-unique, phase-mixed limit, even a gap in one component would not give a gap for "the" theory without the agreement of components (PO-09).
4. **Scale:** no nonzero intrinsic continuum mass is established (A5). So dimensional transmutation is not controlled at the level needed for PO-12.
5. **Transfer-matrix gap uniform in a:** none is claimed. The finite-volume UV control is RG in the small-field / asymptotically free regime. There is no strong-coupling (IR) end of the flow.

## 10. Reusable for the mass-gap research [QUASAR, provisional]
- (R1) The **statement layer** (`PublicTheory.lean`, `PublicWilson.lean`, `ChallengeSpec.lean`, Mathlib-only, builds locally in about 30 s on top of Mathlib cache) is a ready Lean vocabulary for stating T★'s gap clause. Our `HasMassGap` already elaborates against it. Use: WITNESS LAB formal target `08_FORMAL_VERIFICATION/theorem_specifications/` (to do).
- (R2) **Fixed-volume UV limit + RG trajectory** (if correct) supplies PO-02/03 and a candidate renormalization trajectory β(a). A transfer-matrix gap argument must live on this same trajectory.
- (R3) **Volume-uniform local bounds via RP/chessboard + transfer operator** (S-013 p.7): this is the right machinery to upgrade to *decay* bounds (WS04/WS06). Key question for WS01: can the chessboard/transfer-operator argument give a decay rate, or only boundedness?
- (R4) **Phase decomposition framework** (characters, Gelfand/Riesz–Markov): directly relevant to PO-09. A gap in every component with a uniform ∆ would give the T★ clause for each component theory.
- (R5) **Formal OS reconstruction** in Lean: if reusable, it gives PO-08 formally.
Caveats: (i) direct reuse of internal declarations requires the full build, which we have not done. (ii) Mathematical reuse requires LATTICE review and, ideally, the informal manuscript.

## 11. Independent tests performed by QUASAR (local, this session)
| Test | Result |
|---|---|
| Integrity: `sha256sum -c SOURCES.sha256` (9,507 files) | PASS |
| Build of the **reference statement** (`Challenge.lean` + public spec, Mathlib-only) with Lean 4.32.0, Mathlib 81a5d257, in a separate directory `<local-build-dir>` (never under `reviews/`) | PASS (8,659 jobs; Mathlib from cache; only warning: the intentional `sorry`) |
| `#print axioms YangMills.JointExistence` (the Prop definition) | `[propext, Classical.choice, Quot.sound]` |
| `#print axioms YangMills.jointExistence` (*reference* version) | `[propext, sorryAx, Classical.choice, Quot.sound]`, as expected for the placeholder |
| `#print axioms` on the **solution** `jointExistence` / `constructed` | **NOT RUN.** It needs a full build of about 9,458 YM modules (~1M lines, `maxHeartbeats = 0`). We estimate this far exceeds the ~30 CPU-minute budget. Not attempted. |
| Grep audit (item 5) | 1 sorry (reference only); 0 axiom/opaque/implemented_by/extern/native_decide |
| Spec-level gap check (item 9.1) | No spectral-gap clause in the target. Confirmed by elaborated `#print`. |
**Checked:** integrity, the statement layer, its axioms, absence of escape hatches by grep. **Not checked:** the 100,168-declaration kernel replay, the solution's axioms, the internal definitions' fidelity (OperatorContent, Calibrated, contact prescription), and the informal mathematics.

## 12. Gap analysis (concise)
The submission (claim; supported by the group's checks, not by us) constructs, for every compact G with simple 𝔤, Wightman theories as **per-phase** OS reconstructions of a **subsequential** infinite-volume limit of a **fixed-volume** continuum limit of Wilson lattice gauge theory. It has partial short-distance (asymptotic-freedom-type) information and a weak non-freeness test. Relative to T★ it leaves **open**:
- PO-06: uniqueness / full infinite-volume limit.
- PO-09: agreement of phases.
- PO-04: perturbative matching beyond leading order.
- PO-10 in the strong form.
- **PO-11–PO-13: the entire mass gap.**
It provides no uniform-in-volume decay estimate, which is the object JW single out [JW p.7, p.12]. It is the best currently available candidate input for PO-02/03/05/07/08, *conditional on its correctness*.

**Recommended LATTICE checks:**
- (a) Rerun the full build plus `#print axioms` on a larger budget.
- (b) Audit that `Token`/`insertion` cannot be degenerate, i.e. that the public spec forces dependence on the Wilson dynamics (spec-level fidelity).
- (c) Locate the 11C_g/(24π²) slope in the formal statements.
- (d) Audit the `vintage` metaprogram.
- (e) Decide ambiguity A1 (fn 2).
