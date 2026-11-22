<!--
title: Extracted Lean theorem statements (2026 OpenAI construction)
id: QL-20261121-01/03/extracted
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Extracted Lean statements — OpenAI-YM-20261028

**Upstream:** https://github.com/yang-mills-group/OpenAI-YM-20261028, commit `3456e5e75cf8d4cd558955a5c7638fba2d68f464` (single commit, 2026-11-05).
**Licence check:** the upstream repository is licensed under the **Apache License, Version 2.0** (upstream `LICENSE` and `NOTICE`, read 2026-11-21). The short excerpts below are reproduced unmodified under that licence, with attribution to the upstream authors; the licence text is at https://www.apache.org/licenses/LICENSE-2.0. The full upstream files are not redistributed here.

## The reference statement (`Challenge.lean`, complete, 6 lines; sha256 `d31b227d…a5fe9`)
```lean
import ChallengeSpec

/-! Reference statement for comparison in a separate Lean environment. The proof
placeholder belongs only to the challenge. Solution.lean supplies the proof. -/
theorem YangMills.jointExistence : YangMills.JointExistence := by
  sorry
```

## The target proposition (as printed by Lean in our run; see `verification-logs/2026-11-21-openai-ym-print-axioms.log`)
```lean
def YangMills.JointExistence : Prop :=
∀ (g : GaugeGroup),
  g.IsSimple → ∃ C, WilsonRegularity C ∧ ∀ (p : ℕ → ℕ), StrictMono p → ∃ q, StrictMono q ∧ ∃ T, T.Properties (p ∘ q)
```
Note the subsequence quantifier ∀p ∃q: the limit is taken along a sub-subsequence and is not shown to be unique. There is **no spectral-gap clause**.

## The proof entry point (`Solution.lean`, complete, 10 lines; sha256 `1838214b…ece24`)
```lean
import Construction

/-- The core comparator asks only for existence, reconstruction, the OPE and the trace test. -/
theorem YangMills.jointExistence : YangMills.JointExistence := by
  intro g hg
  obtain ⟨C,_,_,reg,orders⟩ := YangMills.constructed.{0,0} g hg 1 zero_lt_one
  refine ⟨YangMills.wilsonFamily C,reg,fun p hp => ?_⟩
  let a : YM.Extraction.Order := ⟨.full,⟨p,hp⟩⟩
  obtain ⟨q,S,F,L,Q,M,X,core,_⟩ := orders a
  exact ⟨q.per,q.per.monotone,YangMills.hierarchy F Q,core⟩
```

## Comparator configuration (`comparator.json`)
```json
{
  "challenge_module": "Challenge",
  "solution_module": "Solution",
  "theorem_names": ["YangMills.jointExistence"],
  "permitted_axioms": ["propext", "Quot.sound", "Classical.choice"]
}
```

## Hashes of upstream files held in the internal archive (unmodified copies)
| File | sha256 |
|---|---|
| Challenge.lean | `d31b227db6e6e1f2aa5eaa66d3b004609fe7470dc2ac3825e0dce882a5fa4fe9` |
| Solution.lean | `1838214ba7159a2babe703000cfd9c43905fb909c1f27b73c46aae48c11ece24` |
| ChallengeSpec.lean (190 lines, not reproduced) | `e48b0be2b72d16b9b87c6c1923b3ae814270387bf9312b5cb0661dfa3e243749` |
| comparator.json | `23e159f10cdb40b780ad8b42a2fc62d2f8e995ee932d955c97e54526d476b967` |
| upstream joint-check log (58 lines, not reproduced) | `6540b07ac9a7e48fb2dddd4f45d06c0e1590bf29cc050956b10c732ce44052b7` |

The upstream joint-check log reports `REPLAY_PASS project=100168` and endpoint axioms `[propext, Classical.choice, Quot.sound]`. This is the **group's** log; we did not reproduce the full build.

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
