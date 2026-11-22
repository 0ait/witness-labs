#!/usr/bin/env python3
# Witness Labs, Agentic Swarm, 0ait | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | contributing agent: QUASAR | x-witness-labs-attribution
"""R1-E03 (QL-20261121-01, QUASAR): does a gauge-covariant block-average map intertwine time reflection theta?
2D U(1) lattice (T x X periodic), blocks of side Lb=3 aligned with the reflection plane between t=-1 and t=0.
Map A ("corner", BIJ-1984 style, S-130 Sec. 2.3): base point = block corner, one fixed contour pattern (axis 1 then axis 0).
Map B ("centre-symmetric"): base point = block centre, multiset of contours = both axis orderings.
Coarse link = argument-average of the parallel-transport phases (BIJ small-field branch). Test:
   theta'(B(U)) == B(theta U)  on gauge-invariant coarse plaquette angles.
LABEL: Computationally verified finite result (a counterexample for map A on explicit configurations; equality for map B to round-off).
"""
import json, hashlib, platform
import numpy as np
T = X = 12; Lb = 3; D = 2   # axis 0 = time, axis 1 = space

def link(U, t, x, mu, sgn):
    """phase of the oriented step from site (t,x) along +mu (sgn=+1) or -mu (sgn=-1)."""
    if sgn > 0: return U[mu, t % T, x % X]
    if mu == 0: return -U[0, (t-1) % T, x % X]
    return -U[1, t % T, (x-1) % X]

def path_phase(U, start, steps):
    t, x = start; ph = 0.0
    for mu, sgn in steps:
        ph += link(U, t, x, mu, sgn)
        if mu == 0: t += sgn
        else: x += sgn
    return ph, (t, x)

def staircase(a, b, order):
    """steps from site a to site b (no wrap ambiguity: within one block), in the given axis order."""
    st = []
    for mu in order:
        d = b[mu] - a[mu]; st += [(mu, int(np.sign(d)))]*abs(d)
    return st

def inverse(steps):
    return [(mu, -s) for mu, s in reversed(steps)]

def argavg(phases):
    ref = phases[0]; d = np.angle(np.exp(1j*(np.array(phases) - ref)))
    assert np.max(np.abs(d)) < np.pi/2, "large field: half-circle branch not applicable"
    return ref + d.mean()

def coarse(U, mode):
    nT, nX = T//Lb, X//Lb; V = np.zeros((D, nT, nX))
    for s in range(nT):
        for r in range(nX):
            base = (s*Lb, r*Lb) if mode == "corner" else (s*Lb+1, r*Lb+1)
            orders = [(1, 0)] if mode == "corner" else [(0, 1), (1, 0)]
            for mu in range(D):
                shift = (Lb, 0) if mu == 0 else (0, Lb)
                base2 = (base[0]+shift[0], base[1]+shift[1])
                ph = []
                for dt in range(Lb):
                    for dx in range(Lb):
                        xs = (s*Lb+dt, r*Lb+dx)
                        for o in orders:
                            p = staircase(base, xs, o) + [(mu, 1)]*Lb + inverse(staircase(base2, (xs[0]+shift[0], xs[1]+shift[1]), o))
                            ph.append(path_phase(U, base, p)[0])
                V[mu, s, r] = argavg(ph)
    return V

def reflect(U):
    """link reflection t -> -1-t (plane between t=-1 and t=0), periodic; works at any level (fine or coarse)."""
    n0, n1 = U.shape[1], U.shape[2]; R = np.zeros_like(U)
    for t in range(n0):
        for x in range(n1):
            R[1, (-1-t) % n0, x] = U[1, t, x]               # spatial link at t -> spatial link at -1-t
            R[0, (-2-t) % n0, x] = -U[0, t, x]              # time link t->t+1 -> reversed link (-2-t)->(-1-t)
    return R

def plaq(V):
    return V[0] + np.roll(V[1], -1, axis=0) - np.roll(V[0], -1, axis=1) - V[1]

def wrap(a): return np.angle(np.exp(1j*a))

rng = np.random.default_rng(20261121)
res = dict(script_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(), numpy=np.__version__,
           python=platform.python_version(), T=T, X=X, Lb=Lb, trials=[])
# sanity: reflect is an involution and maps fine plaquettes to minus reflected plaquettes (as a set)
U0 = rng.normal(0, 0.05, (D, T, X))
assert np.allclose(reflect(reflect(U0)), U0)
for sigma in (0.02, 0.05, 0.08):
    for trial in range(3):
        U = rng.normal(0, sigma, (D, T, X))
        row = dict(sigma=sigma, trial=trial)
        for mode in ("corner", "centre"):
            lhs = plaq(reflect(coarse(U, mode)))
            rhs = plaq(coarse(reflect(U), mode))
            row[mode+"_maxdiff"] = float(np.max(np.abs(wrap(lhs - rhs))))
            row[mode+"_rms_coarse_plaq"] = float(np.sqrt(np.mean(wrap(lhs)**2)))
        # gauge covariance check: random gauge transform leaves coarse plaquettes unchanged
        lam = rng.uniform(-np.pi, np.pi, (T, X))
        Ug = U.copy(); Ug[0] = U[0] + np.roll(lam, -1, 0) - lam; Ug[1] = U[1] + np.roll(lam, -1, 1) - lam
        for mode in ("corner", "centre"):
            row[mode+"_gauge_invariance_maxdiff"] = float(np.max(np.abs(wrap(plaq(coarse(Ug, mode)) - plaq(coarse(U, mode))))))
        res["trials"].append(row)
        print(row)
json.dump(res, open("outputs/e03_results.json", "w"), indent=1)
