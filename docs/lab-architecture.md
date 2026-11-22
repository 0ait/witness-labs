<!--
title: Lab architecture
id: WL/docs/lab-architecture
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Lab architecture

## Two layers
- **Internal lab (primary, complete).** A private git repository holding the WITNESS LAB tree, the raw records, third-party source archives (PDFs, cloned repositories), and session material. It is the working copy.
- **Public archive (this repository).** A curated counterpart: same technical content, plus introductions, summaries and navigation, with transparent redactions. Third-party material is linked and hashed, not copied.

## Internal WITNESS LAB layout (for orientation)
| Internal folder | Public location |
|---|---|
| `00_GOVERNANCE` | `docs/` (integrity standards, publication protocol), `programs/…/00-official-problem/` |
| `01_PROBLEM_FORMALIZATION` | `programs/…/01-formalization/` (copied, bodies unchanged) |
| `02_FOUNDATIONAL_RESEARCH` | empty in v0.1.0 |
| `03_LITERATURE_AND_SOURCE_ARCHIVE` | `programs/…/02-literature/` (register only; files not redistributed) |
| `04_CANDIDATE_SOLUTIONS`, `08_FORMAL_VERIFICATION` | `programs/…/03-candidate-audits/` |
| `05_RESEARCH_WORKSTREAMS` (WS01–WS11), `06_QUASAR_RESEARCH`, `11_FAILED_APPROACHES` | `programs/…/04-INV-001-lattice-to-continuum-gap/` |
| `07_LATTICE_INDEPENDENT_REVIEW` | `programs/…/05-lattice-independent-review/` (verbatim) |
| `09_COMPUTATIONAL_ENVIRONMENT` | `environment/` |
| `13_EVOLUTION_AND_IMPROVEMENT`, `14_SESSION_LOGS` | `programs/…/06-session-logs/` |
| `10_`, `12_`, `15_`, `16_` | empty or internal-only in v0.1.0 |

## Workstreams (internal WS01–WS11)
WS01 spectral gap · WS02 lattice transfer matrix · WS03 continuum limit · WS04 infinite volume · WS05 constructive RG · WS06 correlation functions · WS07 Hamiltonian methods · WS08 stochastic quantization · WS09 alternative formulations · WS10 general gauge groups · WS11 novel approaches. INV-001 used WS01–WS04.

## Operating cycle
RESEARCH → EXPERIMENT → ANALYZE → VERIFY → DOCUMENT LOCALLY → PREPARE PUBLICATION → HUMAN REVIEW → APPROVAL → GITHUB PUBLICATION → UPDATE INDEX.

## Command authority
Only the Commander issues START / STOP / RESUME / CHECKPOINT / STATUS. Research routes and every publication need the Commander's explicit authorization. The agents do not run between turns unless woken; no persistent monitoring is claimed.

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
