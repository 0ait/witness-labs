<!--
title: Versioning and preservation policy
id: WL/VERSIONING
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Versioning and preservation policy

1. **Append-only; never delete.** Nothing published here is deleted or force-overwritten. History is never rewritten (no force-push).
2. **Supersede, don't erase.** A correction is published as a new version (e.g. `…-v2.md`), an erratum, or an addendum that names the file it supersedes. The original stays in place.
3. **Failures stay.** Failed proofs, refuted hypotheses, killed runs and broken library results are part of the record.
4. **Semantic release tags.** Each approved publication batch is a git tag `vMAJOR.MINOR.PATCH` with a GitHub release whose notes give the sha256 of `.witness-labs/manifest.json`.
5. **Manifest.** Every release carries a manifest with the sha256 of each published file. It is a provenance record, not a tamper-proof seal.
6. **Human gate.** Each publication needs the Commander's explicit approval (see [`docs/publication-protocol.md`](docs/publication-protocol.md)).
7. **Internal vs public.** The internal lab archive is primary and complete. This repository is its curated public counterpart; it carries the same technical content plus introductions and navigation, with transparent redactions ([`REDACTIONS.md`](REDACTIONS.md)).

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
