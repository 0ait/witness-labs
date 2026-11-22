<!--
title: Program QL-20261121-01: Yang–Mills existence and mass gap
id: QL-20261121-01/README
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Program QL-20261121-01 — Yang–Mills Existence and Mass Gap

**Lab:** WITNESS LAB · **Agents:** QUASAR (principal investigator), LATTICE (independent validator) · **Opened:** 2026-11-21 17:26 CT · **State at v0.1.0:** paused at the Commander's gate after the first LATTICE check-in.

## Executive summary
The Clay problem asks for a proof that, for every compact simple gauge group G, a non-trivial quantum Yang–Mills theory exists on ℝ⁴ and has a mass gap Δ > 0. **It is open, and this program has not solved it.**

In its first session the lab (1) transcribed and formalized the official problem into a precise target T★ with sixteen proof obligations; (2) audited the 2026 OpenAI Lean existence construction and six public claimed solutions; and (3) ran its first investigation, **INV-001**, on the bridge from a lattice spectral gap to a continuum mass gap. INV-001 shows that the bridge itself is elementary once three hypotheses hold (convergence, a uniform physical-unit rate, cyclicity), proves why the common shortcuts fail, and isolates the open content in a small set of precisely stated missing estimates (ME1, ME2, ME2′, ME3, ME-R1, ME-R2). LATTICE reviewed it independently and returned **REQUIRES CORRECTION (minor)**.

## Background
On a lattice with spacing a, Yang–Mills theory is a well-defined statistical-mechanics model, and a spectral gap of the transfer matrix can be proved at strong coupling. The continuum theory needs a → 0 (weak coupling) and infinite volume. A lattice gap becomes a continuum gap only if it is bounded below by Δ·a uniformly along the continuum trajectory, and nothing currently known supplies that in 4D. Strong-coupling methods stop before the continuum region; Balaban's renormalization-group control stops when the running coupling stops being small. The gap must be proved in between.

## Research progression
1. **Commissioning** (17:26–17:47 CT): mission charter archived with sha256; official statement transcribed; formal specification; OpenAI-2026 audit; claimed-solution register.
2. **INV-001** (17:40–18:07 CT): experiments E01–E03 → derivations D01–D07 → literature baseline → formulation, D08, E04 → report, hypotheses, failed approaches → A–I packet v1.
3. **Pause** (18:08 CT) at the Commander's order; **publication protocol** received 18:16 CT; packet sent to LATTICE.
4. **LATTICE check-in** (to 18:40 CT): review v1, audit comparison, code review, check-in report.
5. **First publication** v0.1.0 (this repository), authorized by the Commander.

## Status table
| Item | Label / verdict |
|---|---|
| 4D Yang–Mills existence and mass gap | **Open problem** |
| Bridge lemma D01 (cyclic family decaying at one rate ⇔ gap, given a unique vacuum) | Established theorem (standard; own proof) · LATTICE: VERIFIED WITH CONDITIONS |
| D02 lattice clustering and passage to the limit | D02(a) VERIFIED WITH CONDITIONS; D02(b,c) VERIFIED WITH CONDITIONS as stated, REQUIRES CORRECTION as a bridge for Jaffe–Witten fields (defect 1) |
| D03 scale window / triviality lemma | VERIFIED WITH CONDITIONS; 2-loop a(β) Heuristic |
| D04–D07 counterexamples and 2D exact solution | VERIFIED / COMPUTATIONALLY REPRODUCED (D04.2: with conditions) |
| D08 progression lemma; conditional crossover reduction | D08.1 VERIFIED; D08.3 VERIFIED WITH CONDITIONS (all content in hypothesis X) |
| ME1, ME2, ME-R1 | **Open problem** (formulations accepted) |
| ME2′, ME3, ME-R2 | REQUIRES CORRECTION (labels/splitting) |
| E01, E02-B, E04 | Computationally verified finite result · COMPUTATIONALLY REPRODUCED by LATTICE |
| E02-A, E03 | Computationally verified finite result (QUASAR; not separately reproduced) |
| H01–H03 | Hypothesis |
| FP01, FP02 | Refuted (as proof strategies) |
| 2026 OpenAI construction | Not a Clay solution (no gap clause); existence UNRESOLVED here (full build not reproduced) |
| Claimed complete solutions (6) | Defective or inaccessible (first pass) |

## Contents
| Folder | Contents |
|---|---|
| [`00-official-problem/`](00-official-problem/) | The official statement (short quotation), sources and hashes |
| [`01-formalization/`](01-formalization/) | Definitions, theorem T★, axioms, mass-gap forms, group scope, PO-01…PO-16 |
| [`02-literature/`](02-literature/) | Source register (URLs, DOIs, sha256) and the INV-001 literature baseline |
| [`03-candidate-audits/`](03-candidate-audits/) | 2026 OpenAI audit, claimed-solution register, Lean verification logs |
| [`04-INV-001-lattice-to-continuum-gap/`](04-INV-001-lattice-to-continuum-gap/) | The first investigation, complete |
| [`05-lattice-independent-review/`](05-lattice-independent-review/) | LATTICE's records, verbatim |
| [`06-session-logs/`](06-session-logs/) | Session logs and the evolution log |
| [`07-R1-P1-route1-u1-filter/`](07-R1-P1-route1-u1-filter/) | Route 1 phase 1: the 4D U(1) go/no-go filter (v1; LATTICE: REQUIRES CORRECTION (moderate)) |
| [`CHRONOLOGY.md`](CHRONOLOGY.md) | Program chronology |

### Integrity labels
Every claim in this archive carries one of the constitution's **knowledge labels**:

| Label | Meaning |
|---|---|
| Established theorem | A proved result: standard literature, or a complete proof in this archive. Proofs written by QUASAR remain "pending verification" until LATTICE has checked them. |
| Formally verified theorem | Checked by a proof assistant (Lean). **Nothing in INV-001 has this label yet.** |
| Computationally verified finite result | An exact or rigorously controlled computation for a finite system, cross-checked by an independent method. |
| Numerically supported result | Numerical evidence without a rigorous error bound. |
| Conjecture / Hypothesis | A precise statement believed or proposed, not proved. |
| Experimental observation | Something seen in a computation; not a general claim. |
| Heuristic | Plausible reasoning, explicitly non-rigorous. |
| Open problem | Unsolved, here or anywhere. |

LATTICE's **verdict classes** for independent review: VERIFIED · VERIFIED WITH CONDITIONS · COMPUTATIONALLY REPRODUCED · STRONGLY SUPPORTED, NOT PROVEN · REQUIRES CORRECTION · REJECTED · UNRESOLVED. "VERIFIED" here means a hand check by LATTICE, never a formal (machine) check, unless stated.

## Update after v0.1.0: Route 1 phase 1 (2026-11-21)
- 18:56 CT: the principal authorized Route 1. Phase 1 applied the 4D U(1) go/no-go filter and checks 1–4: [`07-R1-P1-route1-u1-filter/`](07-R1-P1-route1-u1-filter/).
- Result: filter GO with qualification; the route reduces to one open question (H-Gap), at least as hard as the open fixed-β lattice gap. **No mass gap is claimed.**
- LATTICE review v1: **REQUIRES CORRECTION (moderate)**, nine defects D-R1P1-1…9; v2 not yet authorized. Steps B and C not started.

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
