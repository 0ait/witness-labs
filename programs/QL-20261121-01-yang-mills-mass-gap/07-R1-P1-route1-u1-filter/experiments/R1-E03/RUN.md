<!--
title: R1-E03 run record
id: QL-20261121-01/R1-P1/E03
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: experiment completed; see experiments/REGISTRY.md
internal-source: WitnessLab/06_QUASAR_RESEARCH/experiments/R1-E03/RUN.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
## How to reproduce
1. Install the pinned stack in `ENV.txt` (Python 3.13.5, numpy 2.5.5, scipy 1.18.1, mpmath 1.3.0); full freeze in `/environment/`.
2. Copy this folder somewhere writable, `cd` into it, and run `python3 -u r1e03_block_theta.py && python3 -u r1e03b_block_theta_su2.py` (runtime ≈7 s on the original machine).
3. Outputs are written to `outputs/` (this overwrites the archived outputs, so work on a copy). Compare with the archived files and `outputs/SHA256SUMS.txt`.
4. Note: the `.py` files here carry one added attribution comment line, so their sha256 differs from the script hash recorded in `outputs/SHA256SUMS.txt` and in the output JSONs (which is the hash of the original, uncommented script). Code is otherwise identical.
5. Note: `r1e03_block_theta.py` writes `outputs/e03_results.json`; the archived copy of that file is `outputs/e03_u1_results.json` (renamed after the run, before hashing; its `script_sha256` field identifies `r1e03_block_theta.py`).

---


# R1-E03: does a gauge-covariant block-average map intertwine time reflection θ? (check 2)

QL-20261121-01 · QUASAR · Route 1 phase 1 · run 2026-11-21 19:13–19:16 CT.
**Label: Computationally verified finite result.** These are explicit counterexamples and explicit equalities on finite configurations. Scripts:
- `r1e03_block_theta.py` (U(1));
- `r1e03b_block_theta_su2.py` (SU(2)).

Outputs and hashes are in `outputs/`. CPU about 7 s. Seed 20261121.

## Setup
- 2D periodic 12×12 lattice (axis 0 = time), blocks 3×3. Link reflection θ: t ↦ −1−t, with the plane on a block boundary.
- Coarse link = average of fine parallel transports along a contour multiset between block base points (BIJ 1984 §2.3 construction, S-130, opened).
- **Map "corner"** (BIJ-style): base point at the block corner, with one contour pattern (axis 1, then axis 0).
- **Map "centre"**: base point at the block centre, with the contour multiset made of both axis orderings, so it is reflection-invariant.
- Averaging rules:
  - U(1): BIJ's argument average (small-field branch).
  - SU(2), (P): the projection of the quaternion sum to SU(2), a symmetric function of the multiset.
  - SU(2), (E): exp of the mean of logs taken relative to the *first* transport, which is not a symmetric function.
- Test on gauge-invariant data: plaquette angles (U(1)) or ½Tr of coarse plaquettes (SU(2)), comparing θ′(B(U)) with B(θU).

## Results
| case | max |θ′B(U) − B(θU)| (σ = 0.05 / 0.15 / 0.3) | gauge-covariance check |
|---|---|---|
| U(1), corner and centre, argument average (σ=0.02/0.05/0.08) | ≤ 1.9e−16 (all) | ≤ 1.5e−15 |
| SU(2) corner, (P) | 6.8e−3 / 1.0e−1 / 6.0e−1 | ≤ 8e−16 |
| SU(2) corner, (E) | 6.8e−3 / 1.0e−1 / 7.6e−1 | ≤ 1.4e−15 |
| **SU(2) centre, (P)** | **≤ 7.2e−16 (all)** | ≤ 9e−16 |
| SU(2) centre, (E) | 6.5e−4 / 9.1e−2 / 1.06 | ≤ 2.9e−15 |

## Findings
- **Abelian small-field averaging intertwines automatically, which is a trap for testing.**
  - (Proved here, elementary.) The argument average is linear: V(y,y′) = φ(y) − φ(y′) + mean_x A(x→x+Le_μ) with φ(y) = mean_x A(Γ_{y,x}).
  - The contour dependence is therefore a coarse gauge transformation, and coarse plaquettes do not depend on contours at all.
  - Consequence: a U(1) small-field test cannot detect θ-non-equivariance. Our first test showed exactly this.
- **Non-abelian corner-based averaging does NOT intertwine θ.** The discrepancy is of the same order as 1−½Tr itself. LATTICE's concern (check 2) is confirmed, for the BIJ-style construction as transcribed here.
- **The fix works:**
  - Use a θ-invariant contour multiset (centre base point, all axis orderings).
  - Combine it with a *symmetric* averaging rule (projection of the sum).
  - The result intertwines to round-off.
- **Symmetric contours alone are not enough.** A reference-dependent rule (E) breaks equivariance even with a symmetric multiset.
- **Scope.** This is 2D with a 3×3 block and a transcription of the 1984 lecture construction, not Balaban's CMP averaging (S-113, not opened). Whether Balaban's estimates hold for the θ-equivariant variant is Hypothesis R1-H03.
