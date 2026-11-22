<!--
title: Changelog
id: WL/CHANGELOG
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Changelog

## v0.2.0 — 2026-11-21 — Route 1 phase 1 and LATTICE R1-P1 review

Released after both parts below were on `main` (QUASAR `47f4156`, LATTICE `1be052a`). This commit adds the provenance manifest. The annotated tag `v0.2.0` and the GitHub release name that tag.

The release contains Route 1 phase 1 (report, derivations R1-D01…D04, experiments R1-E01…E03, hypotheses, proof attempt, failed approaches, packet v1, sources S-129…S-135) and LATTICE's independent review v1 (overall verdict REQUIRES CORRECTION (moderate), defects D-R1P1-1…9), counterexample CE-005, second-implementation code, and blind formulation and reconstruction notes. No mass gap is claimed. A corrected v2 will follow as an addendum. Steps B and C were not part of this batch.

## v0.2.0 (in preparation) — part 1 of 2: QUASAR, Route 1 phase 1
Approved by the principal on 2026-11-21 (19:45 CT, "Approve, and change Commander to principal"). Part 2 (LATTICE's R1-P1 review) is pushed separately by LATTICE; the v0.2.0 tag, manifest and release follow after both parts.

Added:
- `programs/QL-20261121-01-yang-mills-mass-gap/07-R1-P1-route1-u1-filter/`: R1-P1 report; derivations R1-D01…D04; experiments R1-E01…E03 (code, ENV, RUN with "How to reproduce", outputs with sha256); hypotheses R1-H01…H03; proof attempt R1-PA01; failed approaches R1-FP01, R1-FE01, lessons R1-LL01; submission packet R1-P1 v1; sources S-129…S-135 (URLs/DOIs only); section README. Published as v1; LATTICE verdict REQUIRES CORRECTION (moderate), defects D-R1P1-1…9; v2 to follow as an addendum.
- New entries in `REDACTIONS.md`, `experiments/REGISTRY.md`, `chronology/TIMELINE.md`, the program README and CHRONOLOGY. In this batch's new files the human principal's role title is written "principal".

## v0.2.0 (in preparation) — part 2 of 2: LATTICE, R1-P1 review
Approved by the principal on 2026-11-21 (19:56 CT, "Yes, LATTICE may push its 20-file review batch"), with the earlier wording change (19:45 CT, "Approve, and change Commander to principal"). The v0.2.0 tag, manifest and release follow this part.

Added:
- `programs/QL-20261121-01-yang-mills-mass-gap/05-lattice-independent-review/`: LATTICE's R1-P1 review v1 (overall verdict REQUIRES CORRECTION (moderate); defects D-R1P1-1…9); counterexample CE-005 (θ-intertwining contour artifact); 14 second-implementation files under `code_reviews/R1-P1/`; blind formulation and reconstruction notes. Innovation register appended with rows L-12…L-15 only; counterexamples README appended with the CE-005 entry. One role title in the review is written "principal".
- New entries in `REDACTIONS.md` (row 15), `chronology/TIMELINE.md`, the program README and CHRONOLOGY.

## v0.1.0 — 2026-11-21 — first publication
Approved by the Commander on 2026-11-21 (18:40 CT, "go ahead with all planned github stuff, publish and push").

Added:
- Repository identity: README, LICENSE (all rights reserved), CITATION.cff, ATTRIBUTION, VERSIONING, REDACTIONS, provenance manifest.
- `docs/`: overview, mission, lab architecture, agents, integrity standards, publication protocol, glossary; public copies of the constitution (4 marked redactions + path redactions) and the immutable mission charter.
- Program QL-20261121-01 (Yang–Mills existence and mass gap): official-problem writeup; formalization (T★, PO-01…PO-16); literature register and INV-001 literature baseline; audit of the 2026 OpenAI Lean construction, register of six claimed solutions, verification logs; INV-001 complete (report, formulation, D01–D08, E01–E04 with code/outputs/failed runs, H01–H03, FP01–FP02, CF01–CF02, A–I packet v1); LATTICE's baseline, check-in, INV-001 review v1, code review and innovation register (verbatim); session logs; chronology.
- `experiments/REGISTRY.md`, `chronology/TIMELINE.md`, `environment/`.

Known open items carried forward: INV-001 v2 corrections (LATTICE defects 1, 3–10) not yet authorized; full rebuild of the 2026 construction not done; Routes R1/R2 closed.

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
