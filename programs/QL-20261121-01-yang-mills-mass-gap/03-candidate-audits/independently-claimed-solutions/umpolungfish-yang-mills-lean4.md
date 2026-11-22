<!--
title: Independently claimed solution record: umpolungfish-yang-mills-lean4
id: QL-20261121-01/T5/umpolungfish-yang-mills-lean4
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: first-pass register entry
internal-source: WitnessLab/04_CANDIDATE_SOLUTIONS/independently_claimed_solutions/umpolungfish-yang-mills-lean4.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# umpolungfish/yang-mills-lean4: "Formal Verification of 4D SU(N) Yang–Mills Theory and the Strict Mass Gap in Lean 4"

Classification: **CLAIMED "Unconditional" (README). First pass: FALSE CLAIM OF COMPLETENESS. The headline theorem rests on 21 `sorry` placeholders.**

## Identity
- Repo: https://github.com/umpolungfish/yang-mills-lean4
  - Shallow clone at commit 97b840d2278ac28e2e2eb9d18a531cab149fec98, dated 2026-11-20T23:42:45-08:00 = 2026-11-21 01:42 CT.
  - Clone is git-ignored: `…/claimed/umpolungfish-yang-mills-lean4-src/`.
- Toolchain: leanprover/lean4:v4.28.0. Author identity: GitHub handle only.
- README sha256 3c48a24d…5c46. ContinuumClosure.lean sha256 b43ff802…79a2.

## Main theorem (verbatim, ContinuumClosure.lean L436–442)
```lean
theorem clay_yang_mills_strict (N : ℕ) (hN : 2 ≤ N) [...] : ClayYangMillsMassGap4DStrict N hN :=
  clay_yang_mills_strict_from_balaban_and_os N hN
    (canonicalBalaban N hN)
    (canonicalOSContinuation N hN)
```
The reduction `clay_yang_mills_strict_from_balaban_and_os` takes `(B : BalabanRGContinuumHypothesis N hN) (C : OSPoincareContinuationHypothesis B.os)` as hypotheses. The "unconditional" theorem gets them from `canonicalBalaban` and `canonicalOSContinuation`.

## First-pass defects
1. **Contradicts its "0 sorry" badge.** `rg -w sorry` finds 21 occurrences in ContinuumClosure.lean, at L308, 318–326, 360, 411, 417–426. They fill:
   - `non_const`, `so4_inv`, `refl_pos`, `cluster`, `refl_pos_n`, `non_gaussian`, `trans_inv`, `schwinger_conv`;
   - every Wightman field `U, U_unitary, U_vac, φ, covariant, local_comm, cyclic_dense`.

   These are the canonical structures fed into the main theorem. So `clay_yang_mills_strict` depends on `sorryAx`, and all the analytic content (OS axioms, Wightman axioms, convergence, non-Gaussianity) is unproven.

   **Lean `#print axioms` NOT run by us** (no build). The finding comes from source text only.
2. **Strong coupling only.** The proved clustering theorems require `18 * (1 - Real.exp (-12 * β)) < 1`, i.e. β ≲ 0.0047 (strong coupling). The predicate requires β_seq → ∞ (weak coupling). Nothing in the opened files bridges the two regimes. This is exactly the PO-12 gap.
3. **Observables are Wilson loops only.** The observables are lattice Wilson loops on Z⁴ loops, not local fields polynomial in F (PO-05).
4. **Group scope.** Only SU(N), N ≥ 2, out of all compact simple G.

## Pending
None needed for the first-pass verdict. Optionally, a LATTICE build with `#print axioms YangMills.clay_yang_mills_strict` to confirm sorryAx.
