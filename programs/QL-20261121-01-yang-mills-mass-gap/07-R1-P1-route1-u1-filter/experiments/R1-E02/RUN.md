<!--
title: R1-E02 run record
id: QL-20261121-01/R1-P1/E02
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: experiment completed; see experiments/REGISTRY.md
internal-source: WitnessLab/06_QUASAR_RESEARCH/experiments/R1-E02/RUN.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
## How to reproduce
1. Install the pinned stack in `ENV.txt` (Python 3.13.5, numpy 2.5.5, scipy 1.18.1, mpmath 1.3.0); full freeze in `/environment/`.
2. Copy this folder somewhere writable, `cd` into it, and run `python3 -u r1e02_running_coupling.py` (runtime <1 s on the original machine).
3. Outputs are written to `outputs/` (this overwrites the archived outputs, so work on a copy). Compare with the archived files and `outputs/SHA256SUMS.txt`.
4. Note: the `.py` files here carry one added attribution comment line, so their sha256 differs from the script hash recorded in `outputs/SHA256SUMS.txt` and in the output JSONs (which is the hash of the original, uncommented script). Code is otherwise identical.

---


# R1-E02: perturbative running-coupling bookkeeping for the R1 crossover (1- and 2-loop)

QL-20261121-01 · QUASAR · Route 1 phase 1 · run 2026-11-21 19:07 CT.
**Label: Heuristic.** The flow ODE is perturbation theory. Its arithmetic is exact (mpmath, 30 digits). Script `r1e02_running_coupling.py`; outputs `outputs/e02_stdout.txt` and `e02_results.json`; hashes in `outputs/SHA256SUMS.txt`. CPU < 1 s.

## Model
d(1/g²)/d ln ℓ = −2b₀ − 2b₁g², with b₀ = 11N/(3(4π)²) and b₁ = 34N²/(3(4π)⁴). Wilson normalisation g₀² = 2N/β (lab convention of D03.3; see defect 9). Block factor b=2.
- SU(2): b₀ = 0.04643887584, b₁ = 0.001817934358.
- SU(3): b₀ = 0.06965831375, b₁ = 0.004090352305.
- Pure U(1): b₀ = b₁ = 0. With no charged matter the perturbative photon is free, so k_* = ∞ for every γ > g₀² (non-perturbative monopole effects ~e^{−c/g²} are not modelled).

## Results
- **k_*(β), the steps from g₀² to γ, grows linearly in β.** The slope is 1/(4N b₀ ln 2) = 3.883 per unit β for SU(2). Examples for SU(2), γ=0.1, 2-loop: β=100 → 232.4 steps; 10³ → 3726.0; 10⁴ → 38674.5; 10⁶ → 3883155.6.
- **The window is independent of β.** Counting steps from g² = γ to the perturbative pole (2-loop), SU(2) needs 306.9 (γ=0.05), 152.0 (0.1), 28.7 (0.5), 13.5 (1.0); SU(3) needs 203.6, 100.4, 18.6, 8.6. The flow is autonomous, so once the coupling reaches γ the remaining distance does not depend on the bare β. This is the heuristic basis of R1-D03 (reduction to a β-free problem).
- **The perturbation per step is small.** One b=2 step changes 1/g² by 2b₀ ln 2 = 0.0644 for SU(2) at 1 loop. So the first coupling above γ satisfies γ < g²_{k_*} ≤ γ/(1 − 0.0644γ), which is within 0.7% of γ for γ=0.1. "The first scale with g_k² > γ" is therefore, in effect, a coupling equal to γ.
- **Strong-coupling threshold** (SZZ S-106, |β_tH| < 1/(16(d−1)) in 't Hooft normalisation as recorded in our register; the conversion β_tH = 2/(Ng²) is an assumption, normalisation not re-read): g² > 96/N, i.e. **g² > 48 for SU(2)** (Wilson β < 1/12) and g² > 32 for SU(3). Perturbation theory hits its pole before reaching either value, so the perturbative window length from γ to strong coupling is undefined. This is the quantitative form of "no small parameter in the window".
