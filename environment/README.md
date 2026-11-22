<!--
title: Computational environment
id: WL/environment/README
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Computational environment

| Component | Version |
|---|---|
| OS | Linux 6.12 x86_64, 8 cores |
| Python | 3.13.5 |
| numpy | 2.5.5 |
| scipy | 1.18.1 |
| mpmath | 1.3.0 |
| Lean | 4.32.0 (leanprover/lean4:v4.32.0, commit 8c9756b2) with Mathlib `81a5d257` (for the reference-statement build only) |
| SageMath | 10.10 (installed; not used by INV-001 experiments) |

Files:
- [`qenv-freeze-2026-11-21.txt`](qenv-freeze-2026-11-21.txt): `pip freeze` of the Python environment used for all experiments.
- [`sage-env-2026-11-21.json`](sage-env-2026-11-21.json): package export of the SageMath environment.

Each experiment folder also carries its own `ENV.txt` with the versions recorded at run time. Recreate with e.g. `python3.13 -m venv env && env/bin/pip install -r qenv-freeze-2026-11-21.txt` (only numpy, scipy and mpmath are needed for E01–E04).

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
