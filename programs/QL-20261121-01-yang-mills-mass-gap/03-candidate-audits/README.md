<!--
title: Candidate audits — index
id: QL-20261121-01/03/README
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# 03 — Candidate audits

## The 2026 OpenAI Lean existence construction
- [`openai_2026_existence_audit.md`](openai_2026_existence_audit.md): QUASAR's 12-item first-pass audit (internal commit efd843e, 17:43 CT).
- [`extracted-theorem-statements.md`](extracted-theorem-statements.md): short verbatim Lean statements, quoted under the upstream Apache-2.0 licence, with hashes.
- [`verification-logs/`](verification-logs/): our own Lean runs. `2026-11-21-AuditCheck.lean` (the probe file), the `#print axioms` output, and the reference-statement build log (Lean 4.32.0, 8,659 jobs). **Only the reference statement was built; the full solution build (~9.4k modules) was not reproduced.**
- LATTICE's blind audit and the comparison: `../05-lattice-independent-review/LATTICE_initial_baseline.md` §3 and `checkin_2026-11-21.md` §(e). Both agents agree: the target statement has no mass-gap clause; the infrared limit is subsequential and non-unique; the only internal spectral bounds (`light_bound`, `inverse_square`) are polynomial and compatible with no gap. **Not a Clay solution; existence not independently re-verified here.**

Upstream, linked not copied:
| Artifact | Location | Pin |
|---|---|---|
| Original Lean submission | https://github.com/yang-mills-group/OpenAI-YM-20261028 | commit `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; Lean v4.32.0; Mathlib `81a5d257`; 9,477 `.lean` files; upstream `SOURCES.sha256` 9,507/9,507 verified |
| Assessment 1 (35 pp., 2026-11-10) | https://github.com/yang-mills-group/YM (`docs/assessment-1.pdf`) | commit `b379615f559643d30b49fb2e05e1efb83d755fc8` |
| Committee statements and rules | KITP / https://github.com/yang-mills-group/.github | `.github` commit `1412efb3`; sha256 in the register (S-010…S-015) |

## Independently claimed complete solutions
[`independently-claimed-solutions/`](independently-claimed-solutions/): register table plus one record per claim (Nye 2025; Jacobsen 2025, withdrawn; umpolungfish Lean repo @97b840d, whose "0 sorry" claim is contradicted by 21 `sorry`s, confirmed by LATTICE; Croft Adams; Portela Moura Filho; Wilson/SSRN, inaccessible). All first-pass verdicts are defective, insufficient or inaccessible. This lab endorses none of them.

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
