<!--
title: LATTICE record: counterexamples/README.md
id: QL-20261121-01/07/counterexamples/README.md
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: LATTICE (independent validator), Witness Labs, Agentic Swarm, 0ait
date: 2026-11-21
version: as committed in internal 9e3dbc7
status: LATTICE record, copied verbatim
internal-source: WitnessLab/07_LATTICE_INDEPENDENT_REVIEW/counterexamples/README.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# counterexamples
Smallest clear counterexamples to claimed implications.
Owner: LATTICE (write area). Naming: `QL-20261121-01_<topic>_vN.md`. Every entry: date (CT), knowledge label (Established theorem / Formally verified / Computationally verified finite result / Numerically supported / Conjecture / Hypothesis / Heuristic / Open problem / PROPOSAL), sources actually opened, reproduction command if computational, and status. Never edit QUASAR files; never delete entries (supersede with vN+1).

## Seeded (Computationally verified finite result, reviews/QL-20261121-01/code/exp_2d_su2_gap.py)
- CE-001: lattice gap at every spacing but zero continuum gap: free scalar with lattice mass a^1.5.
- CE-002: finite-volume gaps 2pi/L closing as L->inf (massless field on a torus).
- CE-003: 2D SU(2): m_lat=O(a)->0 while m_phys->3/8. Shows m_lat>0 is not the content.
- CE-004 (literature, Established theorem): 4D U(1) strong-coupling gap does not persist to weak coupling (Guth 1980; Froehlich-Spencer 1982).

- CE-005 (2026-11-21, Computationally verified finite result): corner block averaging with space-first contours fails θ-intertwining for SU(2), while time-first contours pass. Restricts R1-D02 Prop. 4. File: `QL-20261121-01_theta_contour_v1.md`. (Appended v0.2.0 part 2, internal f5ccacd.)
