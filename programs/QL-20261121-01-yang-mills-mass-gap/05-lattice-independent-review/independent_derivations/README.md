<!--
title: LATTICE record: independent_derivations/README.md
id: QL-20261121-01/07/independent_derivations/README.md
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: LATTICE (independent validator), Witness Labs, Agentic Swarm, 0ait
date: 2026-11-21
version: as committed in internal 9e3dbc7
status: LATTICE record, copied verbatim
internal-source: WitnessLab/07_LATTICE_INDEPENDENT_REVIEW/independent_derivations/README.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# independent_derivations
LATTICE's own derivations, made before reading QUASAR's version.
Owner: LATTICE (write area). Naming: `QL-20261121-01_<topic>_vN.md`. Every entry: date (CT), knowledge label (Established theorem / Formally verified / Computationally verified finite result / Numerically supported / Conjecture / Hypothesis / Heuristic / Open problem / PROPOSAL), sources actually opened, reproduction command if computational, and status. Never edit QUASAR files; never delete entries (supersede with vN+1).

## Seed: sketch of the sufficiency lemma (INV-001), label: Established-theorem-level standard argument; not yet written in full
Let H be the OS Hamiltonian, P0 the vacuum projection, and D = span{Phi(f)Omega : Phi in F, supp f in t>0} dense in H (cyclicity). If for all psi in D: 0 <= <psi, e^{-tH}(1-P0) psi> <= C_psi e^{-Delta t}, then the spectral measure mu_psi of H restricted to (0,Delta) satisfies int_{(0,Delta)} e^{-t lambda} d mu_psi <= C_psi e^{-Delta t} for all t. As t->inf the left side >= e^{-t Delta'} mu_psi((0,Delta')) for every Delta'<Delta, which forces mu_psi((0,Delta'))=0. Density of D and strong continuity of spectral projections give E((0,Delta))=0. Required inputs: cyclic family, uniform-in-(a,L) truncated decay in Euclidean time, convergence of Schwinger functions, RP + E0' growth, vacuum uniqueness or a per-phase statement. See LATTICE_initial_baseline.md section 11.
