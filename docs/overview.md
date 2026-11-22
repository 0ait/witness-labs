<!--
title: Overview
id: WL/docs/overview
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Overview

## The problem, in plain terms
Quantum Yang–Mills theory is the theory behind the strong nuclear force (with SU(3)) and, more generally, behind every non-abelian gauge theory. Physicists use it with great success, and computer simulations strongly suggest that its lightest particle has a positive mass, the **mass gap**. Yet nobody has shown mathematically that the four-dimensional quantum theory *exists* as a rigorous quantum field theory, let alone that it has a mass gap. The Clay Mathematics Institute lists this as one of its Millennium Prize Problems; its official description is by Jaffe and Witten.

## What makes it hard
The standard way to define the theory is on a lattice (a grid with spacing *a*), where everything is finite and well-defined, and then to take *a* → 0 and the volume to infinity. On a lattice one can often prove a gap. The difficulty is to show that the gap **survives both limits at a uniform physical rate**. That uniformity is exactly what nobody knows how to prove.

## What this lab did first (program QL-20261121-01)
1. **Pinned down the target.** Transcribed the official statement and turned it into a precise theorem with sixteen proof obligations ([01-formalization](../programs/QL-20261121-01-yang-mills-mass-gap/01-formalization/)).
2. **Audited claims.** Audited the 2026 OpenAI Lean existence construction (it does not claim a mass gap) and six public "complete solutions" (all defective or inaccessible on first pass) ([03-candidate-audits](../programs/QL-20261121-01-yang-mills-mass-gap/03-candidate-audits/)).
3. **First investigation, INV-001.** Asked *exactly* what a bridge from a lattice gap to a continuum gap must contain. Result: the passage itself is easy and standard; all the difficulty is in one uniform estimate (ME1) plus existence of the continuum limit (ME2), and no current method supplies either in 4D. Proved counterexamples show why the obvious shortcuts fail. Small exact computations illustrate each point ([04-INV-001](../programs/QL-20261121-01-yang-mills-mass-gap/04-INV-001-lattice-to-continuum-gap/)).
4. **Independent review.** LATTICE reconstructed the arguments, reproduced three experiments with its own code, and returned **REQUIRES CORRECTION (minor)** with ten defects ([05-lattice-independent-review](../programs/QL-20261121-01-yang-mills-mass-gap/05-lattice-independent-review/)).

## What this is not
It is not a proof of the mass gap, not a proof of existence, and not a claim that the problem is close to solved. Lattice gaps, strong-coupling gaps, area laws, 2D results and numerical observations are recorded as what they are and never as the 4D mass gap.

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
