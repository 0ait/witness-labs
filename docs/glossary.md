<!--
title: Glossary
id: WL/docs/glossary
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Glossary

| Term | Meaning |
|---|---|
| **Mass gap Δ** | The Hamiltonian H has no spectrum in (0, Δ) for some Δ > 0; the vacuum Ω is the only state of zero energy. The *mass* m is the supremum of such Δ (Jaffe–Witten require m < ∞). |
| **Wilson lattice gauge theory** | Gauge fields as group elements on the links of a lattice with spacing a; action built from plaquette traces with coupling β. |
| **β** | Inverse bare coupling. *Caution:* two conventions are in use in v1 records (β = 1/g₀² and β = 2N/g₀²); LATTICE defect 9 asks to unify them in v2. |
| **a(β)** | Lattice spacing in physical units along a renormalization trajectory. It must be fixed by a condition that does *not* use the gap, otherwise uniformity becomes circular (INV-001 D03.3). |
| **Transfer matrix T** | Positive self-adjoint operator generating one lattice time step; its spectral gap in lattice units is m_lat. |
| **m^loc, m^full** | Lattice gap on the local (contractible-loop) sector vs the full gauge-invariant sector. m^full can be dominated by flux/winding states (torelons). |
| **Torelon** | A flux state winding around a periodic spatial direction; its energy grows with box size. |
| **Continuum limit / infinite-volume limit** | a → 0 at fixed physical scale / box size → ∞. |
| **OS axioms (OS0–OS4)** | Osterwalder–Schrader axioms for Euclidean correlation (Schwinger) functions; reflection positivity (OS2) is the key one. |
| **Wightman axioms** | Axioms for a relativistic QFT in Minkowski space (Streater–Wightman). |
| **Cyclic family** | A set of observables whose vectors span a dense subspace of the physical Hilbert space. |
| **ME1** | Missing estimate 1: a uniform lower bound m^loc(β,L) ≥ Δ·a(β) for all weak enough coupling and large enough boxes. Open. |
| **ME2 / ME2′** | Convergence to a unique, non-free limit with OS properties / a gap statement relative to the 2026 construction (to be split into "min" and "strong" in v2). |
| **ME3** | Upper window m^loc ≤ C·a(β), needed for non-triviality (given ME2). |
| **ME-R1, ME-R2** | Route-specific missing estimates: clustering of block-spin measures at the crossover scale; a β-uniform Poincaré/log-Sobolev inequality. |
| **Bakry–Émery** | A curvature criterion that implies a Poincaré/log-Sobolev inequality; fails for single-link SU(2) once β ≥ 2. |
| **Balaban's program** | Rigorous renormalization-group control of 4D lattice Yang–Mills on a finite torus, valid while the effective coupling stays small. |
| **Crossover** | The intermediate scale between weak coupling (Balaban) and strong coupling (cluster expansions), where no current tool applies. |
| **T★, PO-01…PO-16** | The lab's precise theorem target and its proof obligations (01-formalization). |
| **A–I packet** | The standard QUASAR → LATTICE submission format, sections A to I. |
| **R1 … R5** | Ranked attack routes in the INV-001 report; R1/R2 are proposals, closed pending authorization. |

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
