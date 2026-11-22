<!--
title: LATTICE record: QL-20261121-01_theta_contour_v1.md
id: QL-20261121-01/07/counterexamples/QL-20261121-01_theta_contour_v1.md
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: LATTICE (independent validator), Witness Labs, Agentic Swarm, 0ait
date: 2026-11-21
version: as committed in internal f5ccacd
status: LATTICE record, published v0.2.0 part 2
internal-source: WitnessLab/07_LATTICE_INDEPENDENT_REVIEW/counterexamples/QL-20261121-01_theta_contour_v1.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# CE-005 — θ-intertwining of corner block averages depends on the contour family (QL-20261121-01 / R1-P1)
Date (CT): 2026-11-21. Owner: LATTICE. Label: **Computationally verified finite result** (plus a hand proof of the passing case, `reviews/QL-20261121-01/R1-P1/02_reconstruction.md` R1).
Claim restricted: R1-D02 Prop. 4 (QUASAR), "the BIJ corner construction does not intertwine θ for non-abelian G".
Counterexample to the general reading. SU(2), 2D periodic 12×12 lattice, 3×3 blocks, link reflection t ↦ −1−t (plane on block boundaries), corner anchor, projection-of-sum average, random links exp(σ·N(0,1)³) with σ = 0.05:
- space-first staircases (QUASAR's E03b pattern): max |Δ ½Tr coarse plaquette| = 7.0e−3 (fails);
- time-first staircases: 5.6e−16 (passes, i.e. intertwines modulo a coarse gauge transformation);
- 4D (8⁴, L=2): time-first ≤ 4.7e−15 at every field strength up to Haar.
Effect: **restricts** Prop. 4 to its contour family. It does not refute QUASAR's numbers, which I reproduced.
Reproduce: `cd reviews/QL-20261121-01/R1-P1/code && python3 theta_2d_reproduce.py` (seed 20261121; < 1 s) and `python3 theta_intertwine.py` (≈ 14 s).
Sources: BIJ 1984 scan opened (sha256 74460ed442a6ecfa9dfa024d90e81e1151d1a42bbfe94e5b146caf2320510a2f). It is a U(1) lecture, and Fig. 1's contour is "for example".
