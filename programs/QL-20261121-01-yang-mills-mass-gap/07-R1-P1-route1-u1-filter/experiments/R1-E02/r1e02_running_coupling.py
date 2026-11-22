#!/usr/bin/env python3
# Witness Labs, Agentic Swarm, 0ait | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | contributing agent: QUASAR | x-witness-labs-attribution
"""R1-E02 (QL-20261121-01, QUASAR): perturbative (1- and 2-loop) running-coupling bookkeeping for route R1.
Counts block-spin steps (scale factor b) needed for the running coupling g^2 to go from the bare value
g0^2 = 2N/beta (Wilson normalisation, beta = 2N/g0^2) to a threshold gamma, and from gamma to the 2-loop pole.
Flow in length scale l: d(1/g^2)/d ln l = -2 b0 - 2 b1 g^2, b0 = 11N/(3(4pi)^2), b1 = 34N^2/(3(4pi)^4).
Pure U(1) (no matter): b0 = b1 = 0 to all orders of perturbation theory (free photon); k_* = infinity.
LABEL: Heuristic (perturbation theory is not a theorem beyond Balaban's small-coupling regime) / exact arithmetic of a model ODE.
Strong-coupling threshold conversion: SZZ (S-106) |beta_tH| < 1/(16(d-1)) in 't Hooft normalisation S = N beta_tH sum Re Tr,
assumed here; Wilson S = (2/g^2) sum Re Tr  =>  beta_tH = 2/(N g^2)  =>  g^2 > 32(d-1)/N  (d=4: 96/N).
"""
import json, hashlib, platform
import mpmath as mp
mp.mp.dps = 30
PI = mp.pi

def coeffs(N):
    b0 = mp.mpf(11)*N/(3*(4*PI)**2); b1 = mp.mpf(34)*N**2/(3*(4*PI)**4); return b0, b1

def steps_to(g0sq, target, N, b=2, loops=2):
    """number of b-blocking steps (real-valued) to flow from g0sq up to target; inf if never."""
    if N == 0: return mp.inf
    b0, b1 = coeffs(N)
    if loops == 1:
        return (1/mp.mpf(g0sq) - 1/mp.mpf(target))/(2*b0*mp.log(b))
    # integrate d ln l = - d(u) / (2 b0 + 2 b1 / u), u = 1/g^2, from u0 down to ut
    f = lambda u: 1/(2*b0 + 2*b1/u)
    return mp.quad(f, [1/mp.mpf(target), 1/mp.mpf(g0sq)])/mp.log(b)

def steps_gamma_to_pole(gamma, N, b=2, loops=2):
    b0, b1 = coeffs(N)
    if loops == 1: return (1/mp.mpf(gamma))/(2*b0*mp.log(b))
    f = lambda u: 1/(2*b0 + 2*b1/u)
    return mp.quad(f, [0, 1/mp.mpf(gamma)])/mp.log(b)

out = dict(script_sha256=hashlib.sha256(open(__file__,'rb').read()).hexdigest(), mpmath=mp.__version__,
           python=platform.python_version(), label="Heuristic (perturbative model flow); arithmetic exact to 30 digits", rows=[])
print("N  b0  b1"); 
for N in (2, 3):
    b0, b1 = coeffs(N); print(N, mp.nstr(b0, 10), mp.nstr(b1, 10)); out[f"b0_SU{N}"] = float(b0); out[f"b1_SU{N}"] = float(b1)
print("\nsteps k_*(beta) (b=2) from g0^2=2N/beta to gamma; 1-loop / 2-loop; U(1): infinite")
for N in (2, 3):
    for gamma in (0.05, 0.1, 0.5, 1.0):
        for beta in (100, 1000, 10**4, 10**6):
            g0 = mp.mpf(2*N)/beta
            if g0 >= gamma: continue
            k1 = steps_to(g0, gamma, N, loops=1); k2 = steps_to(g0, gamma, N, loops=2)
            row = dict(group=f"SU{N}", gamma=gamma, beta=beta, g0sq=float(g0), k1=float(k1), k2=float(k2),
                       slope_dk_dbeta_1loop=float(1/(2*N*2*coeffs(N)[0]*mp.log(2))))
            out["rows"].append(row)
            print(f"SU({N}) gamma={gamma:<5} beta={beta:<8} k1={float(k1):10.2f} k2={float(k2):10.2f}")
print("\nwindow: steps from g^2=gamma to the perturbative pole (b=2); strong-coupling threshold g^2 > 96/N (SZZ, converted)")
out["window"] = []
for N in (2, 3):
    for gamma in (0.05, 0.1, 0.5, 1.0):
        w1 = steps_gamma_to_pole(gamma, N, loops=1); w2 = steps_gamma_to_pole(gamma, N, loops=2)
        out["window"].append(dict(group=f"SU{N}", gamma=gamma, to_pole_1loop=float(w1), to_pole_2loop=float(w2),
                                  strong_threshold_gsq=96/N))
        print(f"SU({N}) gamma={gamma:<5} steps to pole: 1-loop {float(w1):9.2f}  2-loop {float(w2):9.2f}   (strong threshold g^2>{96/N:.0f})")
print("\nU(1): b0=b1=0 => d(1/g^2)/dln l = 0 perturbatively; k_* = inf for every gamma > g0^2 (non-perturbative monopole")
print("corrections ~exp(-c/g^2) are not captured).")
out["U1"] = "b0=b1=0; k_* infinite in perturbation theory"
json.dump(out, open("outputs/e02_results.json", "w"), indent=1)
