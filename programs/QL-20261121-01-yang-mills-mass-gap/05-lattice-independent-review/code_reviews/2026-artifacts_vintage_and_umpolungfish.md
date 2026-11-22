<!--
title: LATTICE record: code_reviews/2026-artifacts_vintage_and_umpolungfish.md
id: QL-20261121-01/07/code_reviews/2026-artifacts_vintage_and_umpolungfish.md
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: LATTICE (independent validator), Witness Labs, Agentic Swarm, 0ait
date: 2026-11-21
version: as committed in internal 9e3dbc7
status: LATTICE record, copied verbatim
internal-source: WitnessLab/07_LATTICE_INDEPENDENT_REVIEW/code_reviews/2026-artifacts_vintage_and_umpolungfish.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# LATTICE code review: the OpenAI-YM `vintage` metaprogram, and umpolungfish/yang-mills-lean4 sorries
QL-20261121-01. 2026-11-21, about 18:05–18:20 CT. Read from local clones only. No builds were run.

## 1. `vintage` (OpenAI-YM-20261028 @ 3456e5e7, `YM/UVExtension/Orchard/Barrel.lean`, 72 lines, read in full)
**What it does.** `vintage YM.X.foo` takes the existing kernel-checked constant `foo`. It builds `Vintage.YM.X.foo` whose **type and proof term** are the originals with every constant `c` replaced by `Vintage.c`, wherever such a variant already exists in the environment (`ferment`, via `Expr.replace` on `.const` and `.proj`). It does this recursively for YM-prefixed constants whose types mention replaced names. Each result is submitted with `Lean.addDecl` as a `thmDecl` or a safe `defnDecl`.
- It throws on unsafe or partial definitions ("refusing unsafe vintage").
- It throws on every other constant kind, including axioms, opaque constants and inductives ("explicit variant required").

**Can it introduce axioms or bypass `#print axioms`?**
- **Cannot introduce axioms.** It never constructs an `axiomDecl` or `opaqueDecl`. It copies only theorem and safe-definition bodies.
- **Cannot bypass `#print axioms`.** `addDecl` sends the declaration to the kernel. `debug.skipKernelTC` is absent from the tree (grep: 0 hits). The generated declarations are ordinary environment constants, so `#print axioms` traverses them like any other constant. A kernel replay of the .olean files (Comparator / lean4checker-style) re-checks them.
- The group's own log records `REPLAY_PASS project=100168` and endpoint axioms `[propext, Classical.choice, Quot.sound]` (`verification/joint-check.log`). **That is their run; I did not reproduce it.**

**Real risk: statement fidelity, not soundness.** The generated statements never appear in source. Users of a `Vintage.*` lemma depend on what the `Vintage.*` variant *definitions* mean. Where a variant definition differs from the original, the theorem is about a different object, and the kernel will accept it either way. In the group's `declaration-usage.tsv`, 631 lines mention `Vintage`. 601 rows have a `Vintage.*` constant as the declaration or as its immediate user: 567 of them name `YM.SharpGram.habitat` as headline witness, and 34 have none. 208 rows have a `Vintage.*` declaration itself. So these declarations are on the path to advertised endpoints. Whether they sit in `YangMills.jointExistence`'s closure cannot be read from that single-witness column without a build.

**Recommendation (next pass, gated).** Audit the `Vintage.*` variant *definitions* (about 80 files under `YM/UVExtension/`, plus `RG05Readout`, `SharpGram`, `Planned` and `RemainderComparison`) against their originals, i.e. check definitional fidelity. The kernel already covers soundness.

## 2. umpolungfish/yang-mills-lean4 @ 97b840d2278ac28e2e2eb9d18a531cab149fec98
**Clone identity.** QUASAR's git-ignored clone is at `WitnessLab/03_LITERATURE_AND_SOURCE_ARCHIVE/candidate_solutions/claimed/umpolungfish-yang-mills-lean4-src/`. Its HEAD matches remote HEAD per `gh api` at 18:15 CT: 97b840d…, committed 2026-11-20 23:42 −08:00 (2026-11-21 01:42 CT). The repo has 10 `.lean` files.

**Grep (code lines; comment lines excluded):** 21 `sorry`, all in `Imscribing/YangMills/ContinuumClosure.lean`:

| Definition | Sorried fields | Count |
|---|---|---|
| `canonicalObs` | `non_const` | 1 |
| `canonicalOSStrict` | `so4_inv`, `perm_symm`, `refl_pos`, `cluster`, `refl_pos_n`, `schwinger_nonzero`, `non_gaussian`, `trans_inv` | 8 |
| `canonicalBalaban` | `schwinger_conv` | 1 |
| `canonicalOSContinuation` | `h_herm`, `U`, `U_one`, `U_mul`, `U_unitary`, `U_vac`, `U_trans_cont`, `φ`, `covariant`, `local_comm`, `cyclic_dense` | 11 |
| **Total** | | **21** |

The headline `theorem clay_yang_mills_strict` (l.436) is defined as `clay_yang_mills_strict_from_balaban_and_os N hN (canonicalBalaban N hN) (canonicalOSContinuation N hN)`, so it consumes these sorried structures directly. Meanwhile README l.11 says "0 `sorry` placeholders" and README l.158 says "Unproven Axioms (`sorryAx`): 0". `standardBeta0 := 1/300` shows the proved content is strong-coupling.

**Verdict on its "0 sorry / unconditional" claim: REJECTED** (source-level, verified by grep and reading the definitions). Not built: `#print axioms` would be expected to list `sorryAx`, but I did not run it. QUASAR's flag is **confirmed**.
