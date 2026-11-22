<!--
title: Redactions and exclusions
id: WL/REDACTIONS
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Redactions and exclusions (v0.1.0)

## Redactions in published files
None of these affects the interpretation or reproducibility of any technical result.

| # | File | What was redacted | Replacement | Count | Reason |
|---|---|---|---|---|---|
| 1 | `programs/QL-20261121-01-yang-mills-mass-gap/02-literature/source_register.csv` | column local_path (internal file locations) | `column internal_archive_copy (yes/no)` | 49 | internal paths; third-party files are not redistributed. URLs/DOIs and sha256 retained |
| 2 | `programs/QL-20261121-01-yang-mills-mass-gap/03-candidate-audits/openai_2026_existence_audit.md` | local absolute path "/workspace/ym-audit-build/proj" | `<local-build-dir>` | 1 | internal machine path (infrastructure detail); no effect on technical content |
| 3 | `programs/QL-20261121-01-yang-mills-mass-gap/04-INV-001-lattice-to-continuum-gap/submission-packet-A-I-v1.md` | local absolute path "/workspace/quasar-lattice" | `<internal-lab-root>` | 1 | internal machine path (infrastructure detail); no effect on technical content |
| 4 | `programs/QL-20261121-01-yang-mills-mass-gap/06-session-logs/2026-11-21-S01-B.md` | local absolute path "/workspace/quasar-lattice/reviews/" | `<internal-lab-root>/reviews/` | 1 | internal machine path (infrastructure detail); no effect on technical content |
| 5 | `programs/QL-20261121-01-yang-mills-mass-gap/06-session-logs/evolution_log.md` | local absolute path "/workspace/quasar-lattice/WitnessLab" | `<internal-lab-root>/WitnessLab` | 1 | internal machine path (infrastructure detail); no effect on technical content |
| 6 | `docs/constitution.md` | Commander's personal name (line 3) | `REDACTED-1: personal name` | 1 | personal information; the role "the Commander" is retained |
| 7 | `docs/constitution.md` | named reference to an unrelated, non-research project (line 7) | `REDACTED-2: reference to an unrelated project` | 1 | unrelated to this research; not for publication |
| 8 | `docs/constitution.md` | Commander's personal name (line 7) | `REDACTED-3: personal name` | 1 | personal information |
| 9 | `docs/constitution.md` | local absolute path (line 7) | `REDACTED-4: local workspace path` | 1 | internal infrastructure detail |
| 10 | `docs/constitution.md` | local absolute path "/workspace/quasar-lattice/" (lines 71, 85) | `<internal-lab-root>/` | 2 | internal machine path; no effect on content |
| 11 | `programs/QL-20261121-01-yang-mills-mass-gap/07-R1-P1-route1-u1-filter/R1-P1_report.md` | previous role title of the human principal (v0.2.0 part 1) | `"principal" ("Principal" where capitalised)` | 3 | role-title change approved by the principal for this batch (2026-11-21 19:45 CT); no effect on technical content |
| 12 | `programs/QL-20261121-01-yang-mills-mass-gap/07-R1-P1-route1-u1-filter/derivations/R1-D01_skeleton_and_U1_filter.md` | previous role title of the human principal (v0.2.0 part 1) | `"principal" ("Principal" where capitalised)` | 1 | role-title change approved by the principal for this batch (2026-11-21 19:45 CT); no effect on technical content |
| 13 | `programs/QL-20261121-01-yang-mills-mass-gap/07-R1-P1-route1-u1-filter/submission-packet-R1-P1-v1.md` | previous role title of the human principal (v0.2.0 part 1) | `"principal" ("Principal" where capitalised)` | 2 | role-title change approved by the principal for this batch (2026-11-21 19:45 CT); no effect on technical content |
| 14 | `programs/QL-20261121-01-yang-mills-mass-gap/07-R1-P1-route1-u1-filter/sources_S-129_S-135.csv` | column local_path (internal file locations / archive notes) (v0.2.0 part 1) | `column internal_archive_copy (yes/no)` | 7 | internal paths; third-party files are not redistributed. URLs/DOIs and sha256 retained |

Notes:
- In `docs/constitution.md` each redaction is marked inline as `[REDACTED-n: …]`. The internal original is unchanged.
- The Commander's name appears in the internal constitution as principal. It was redacted conservatively, because the archive is append-only (a name can be added later by addendum; it cannot be removed). The Commander is identified by role throughout.
- Path redactions replace machine-local absolute paths with `<internal-lab-root>` or `<local-build-dir>`. Relative paths inside copied records refer to the internal lab layout; see [`docs/lab-architecture.md`](docs/lab-architecture.md) for the mapping to this repository.
- LATTICE's records (`programs/…/05-lattice-independent-review/`), the mission charter, the formalization files, and all experiment code and outputs needed **no** redaction.

## Excluded from publication (referenced, not redistributed)
| Material | Why excluded | How it is referenced |
|---|---|---|
| Jaffe–Witten official description (PDF) and our full and per-page text extractions | Third-party copyright | URL + sha256; short quotations with page numbers |
| Clay web page (HTML) and its text | Third-party content | URL + sha256 |
| KITP committee statements, the Yang–Mills group's rules and Assessment 1 (PDFs and text) | Third-party copyright; one contains a contact e-mail address | URLs, repo commits, sha256 (source register S-010…S-015) |
| Eight arXiv preprint PDFs used by INV-001 | Third-party copyright | arXiv IDs/DOIs + sha256 |
| Cloned repositories: OpenAI-YM-20261028 (9,477 Lean files), yang-mills-group/YM and `.github`, umpolungfish/yang-mills-lean4 | Not ours to republish (even where Apache-2.0); size | Repo URL + commit hash; short Apache-2.0 excerpts in `extracted-theorem-statements.md` |
| Other full upstream files (ChallengeSpec.lean, PublicTheory.lean, PublicWilson.lean, Construction.lean, ConcreteSU2.lean, lake files, upstream joint-check log) | Only short statements were approved for quotation | sha256 in `extracted-theorem-statements.md` |
| Fetched third-party web pages for claimed solutions (MDPI, Medium, Academia, arXiv abstract HTML, READMEs) | Third-party content | URLs in the source register and claim records |
| Local Python/Lean environments and build caches | Machine-specific; large | Version lockfiles in `environment/` |
| Message transcripts, agents' private memory, credentials | Private / security | Not published |
| Internal operational files outside the Yang–Mills program (commissioning queue, registers, ledgers, install logs) | Internal operations, not part of the approved scope | Described in prose in `chronology/TIMELINE.md` |
| LATTICE's separate review repository (`reviews/`: procedure, landscape, registers, second-implementation scripts, Lean `challenge_check` source) | Not in the approved v0.1.0 scope | Proposed by LATTICE for a later batch (check-in §(g)) |

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
