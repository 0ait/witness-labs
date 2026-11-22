<!--
title: INV001-E03 run record
id: QL-20261121-01/INV-001/E03
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: experiment completed; see experiments/REGISTRY.md
internal-source: WitnessLab/06_QUASAR_RESEARCH/experiments/INV001-E03/RUN.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
## How to reproduce
1. Install the pinned stack in `ENV.txt` (Python 3.13.5, numpy 2.5.5, scipy 1.18.1, mpmath 1.3.0); full freeze in `/environment/`.
2. Copy this folder somewhere writable, `cd` into it, and run `python3 -u e03_tunneling.py` (runtime ≈10 s on the original machine).
3. Outputs are written to `outputs/` (this overwrites the archived outputs, so work on a copy). Compare with the archived files and `outputs/SHA256SUMS.txt`.
4. Note: the `.py` files here carry one added attribution comment line, so their sha256 differs from the script hash recorded in `outputs/SHA256SUMS.txt` (which is the hash of the original, uncommented script). Code is otherwise identical.

---


# INV001-E03 — finite-volume gap closing by tunnelling

**Run.** `python3 -u e03_tunneling.py` (about 10 s). Outputs are in `outputs/`.

1. **Rigid-column toy (exact, D04 Example A).** T_L=[[e^{LK},e^{−LK}],[e^{−LK},e^{LK}]], m_lat(L)=log coth(LK) ~ 2e^{−2LK}. The table in `e03_results.json` (60-digit) shows m_lat/(2e^{−2LK})→1.
2. **Periodic transverse-field Ising chain, J=1, h∈{0.3,0.5,0.7} (ordered phase), L=4..18.** Exact diagonalisation in the Z₂-even and Z₂-odd sectors, cross-checked against free-fermion NS/R vacuum energies (agreement ≤5e-14 at every L).

| h | tunnelling split d0(L=18) | slope of log d0 vs L (L≥8) | −log(J/h) | next even gap d1(L=18) | 2·2(J−h) |
|---|---|---|---|---|---|
| 0.3 | 1.008e-10 | −1.247 | −1.204 | 2.8259 | 2.8 |
| 0.5 | 9.092e-07 | −0.737 | −0.693 | 2.0599 | 2.0 |
| 0.7 | 3.276e-04 | −0.403 | −0.357 | 1.3343 | 1.2 |

- The lowest finite-volume gap closes exponentially in L, with a rate approaching log(J/h); the fitted slopes include power-law prefactor corrections.
- The gap to the first genuine excitation stays open and approaches 4(J−h) (two fermions of energy 2(J−h)).
- Consistent with D04: a finite-volume gap is neither sufficient nor necessary for an infinite-volume gap in a pure phase. The relevant object is the gap above the vacuum of the local sector (or of a pure phase).

**Cannot:** this is a toy. It does not show that 4D YM has degenerate vacua (it is not expected to in infinite volume), though small-volume YM does have centre/electric-flux sectors. Exact diagonalisation at L≤18 says nothing asymptotic by itself; the asymptotics are supported by the free-fermion closed form.
