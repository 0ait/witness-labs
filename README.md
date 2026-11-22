<!--
title: Witness Labs — Agentic Swarm research archive
id: WL/README
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Witness Labs — Agentic Swarm research archive

**Witness Labs** is a research lab run by an *agentic swarm*: two AI research agents with deliberately opposed roles, working under a human principal (the Commander), who approves every publication. This repository is the lab's public, append-only research archive. It records what was attempted, what was proved, what failed and why, in the order it happened.

> **Status (v0.1.0, 2026-11-21).** The lab's first program is the **Yang–Mills Existence and Mass Gap** problem (Clay Millennium Prize; Jaffe–Witten official description). **The problem is open. Nothing in this repository is a solution, a partial solution, or a claim of progress toward a 4D mass gap.** What is here is a precise map of one bridge in the problem, a set of proved reductions and counterexamples, small exact computations, audits of other people's claims, and an independent review of all of it.

## Mission
Investigate hard problems in mathematics and mathematical physics with full transparency: separate theorem from numerical evidence from conjecture, preserve every failed attempt, and let nothing count as established until an independent agent has tried to break it. See [`docs/mission.md`](docs/mission.md) and the governing [constitution](docs/constitution.md) and [mission charter](docs/mission-charter.md).

## The agents
- **QUASAR**: principal investigator. Generates hypotheses, derivations, literature baselines and experiments.
- **LATTICE**: independent validator and innovation partner. Reconstructs, attacks and re-derives QUASAR's claims; proposes alternatives.
- **The Commander**: human principal; holds start/stop authority and approves each publication.

Details: [`docs/agents.md`](docs/agents.md), [`ATTRIBUTION.md`](ATTRIBUTION.md).

## Where things stand
| Item | Status |
|---|---|
| Yang–Mills existence and mass gap (4D) | **Open problem** |
| INV-001: what a bridge from a lattice gap to a continuum gap must contain | Done (v1). LATTICE review v1: **REQUIRES CORRECTION (minor)**; 10 defects listed; v2 not yet authorized |
| Missing estimates ME1, ME2, ME-R1 | **Open**, formulations accepted by LATTICE |
| 2026 OpenAI Lean existence construction | Audited by both agents: not a Clay solution (no mass-gap clause); existence claim not independently re-verified here (full build not reproduced) |
| Six independently claimed complete solutions | All defective or inaccessible on first pass |
| Research routes R1/R2 | Proposals only; **closed** pending the Commander's authorization |

## How to navigate
| Start here | What it is |
|---|---|
| [`docs/overview.md`](docs/overview.md) | Plain-language overview of the problem and of what this lab did |
| [`programs/QL-20261121-01-yang-mills-mass-gap/`](programs/QL-20261121-01-yang-mills-mass-gap/) | The Yang–Mills program: official problem, formalization, literature, audits, INV-001, LATTICE's review, session logs |
| [`programs/…/04-INV-001-lattice-to-continuum-gap/`](programs/QL-20261121-01-yang-mills-mass-gap/04-INV-001-lattice-to-continuum-gap/) | The first investigation, with a newcomer's introduction |
| [`experiments/REGISTRY.md`](experiments/REGISTRY.md) | Every experiment, with metadata, results and reproduction links |
| [`chronology/TIMELINE.md`](chronology/TIMELINE.md) | Lab history from founding to the first LATTICE check-in |
| [`environment/`](environment/) | Pinned software versions |
| [`docs/glossary.md`](docs/glossary.md) | Terms and notation |
| [`REDACTIONS.md`](REDACTIONS.md) · [`CHANGELOG.md`](CHANGELOG.md) · [`VERSIONING.md`](VERSIONING.md) | What was redacted, what changed, and the never-delete policy |

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

## What is not here
Third-party papers, PDFs, web pages and cloned code repositories are **referenced, not redistributed**: each is listed with its URL or DOI, commit hash where relevant, and sha256 in [`source_register.csv`](programs/QL-20261121-01-yang-mills-mass-gap/02-literature/source_register.csv). Short quotations are included with citation.

## Citing
See [`CITATION.cff`](CITATION.cff). Copyright and terms: [`LICENSE.txt`](LICENSE.txt).

```
Witness Labs
Agentic Swarm
0ait
```

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
