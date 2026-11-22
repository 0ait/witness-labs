<!--
title: Proof attempt R1-PA01_abelian_obstruction_lemma
id: QL-20261121-01/R1-P1/PA01
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: proof attempt; LATTICE review v1: VERIFIED WITH CONDITIONS, hypothesis (M) UNRESOLVED
internal-source: WitnessLab/06_QUASAR_RESEARCH/proof_attempts/R1-PA01_abelian_obstruction_lemma.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# R1-PA01: attempt to make the U(1) filter rigorous (Lemma A of R1-D01)
- **Label:** Conditional proof (QUASAR's; pending LATTICE). The input hypothesis (M) is at title/abstract level only.
- **Goal.** Show rigorously that the U(1) analogue of R1 step S6 is false, so that S6 must use non-abelian structure.
- **Achieved.**
  - D08.3 is group-agnostic. If a U(1) block-spin measure clustered as in X on a family containing a massless observable, the fine correlations would decay exponentially uniformly in L, which is a contradiction.
  - Done for Villain U(1) at bare coupling g₀² ∈ (γ, 0.168): non-confining by Guth [A]; masslessness from S-128 [T] and S-132 [A].
- **Gap in the attempt.**
  - (M) needs a theorem that some *coarse-local gauge-invariant* observable has non-exponential time-direction decay in that regime. Guth's bound is on Wilson loops (deconfinement), which does not by itself give masslessness.
  - The masslessness statements are at title/abstract level (FS82 [T]; Driver [A], whose "coupling sufficiently large" convention is not checked).
- **Next.** Locate a legitimately accessible statement of the photon two-point lower bound, e.g. a modern exposition of the Villain massless phase (Chevyrev 2025 PMC / Dario, found in search, not opened). Check its observable class against coarse block observables.
