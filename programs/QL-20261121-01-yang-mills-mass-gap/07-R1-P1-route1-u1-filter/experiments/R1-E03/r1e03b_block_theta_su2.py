#!/usr/bin/env python3
# Witness Labs, Agentic Swarm, 0ait | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | contributing agent: QUASAR | x-witness-labs-attribution
"""R1-E03b (QL-20261121-01, QUASAR): theta-intertwining of gauge-covariant block averages for SU(2) (2D, T x X periodic).
Same geometry as r1e03_block_theta.py (Lb=3, plane at a block boundary). Coarse link = nonlinear average of the
SU(2) parallel transports along a contour multiset: (P) projection of the sum to SU(2), (E) exp of the mean log
relative to the first transport. Maps: 'corner' (BIJ-style corner base point, one contour pattern) and 'centre'
(centre base point, both axis orderings). Test on gauge-invariant data: (1/2)Tr of coarse plaquettes.
LABEL: Computationally verified finite result.
"""
import json, hashlib, platform
import numpy as np
T = X = 12; Lb = 3; D = 2

def qmul(a, b):
    a0, av = a[0], a[1:]; b0, bv = b[0], b[1:]
    return np.concatenate([[a0*b0 - av @ bv], a0*bv + b0*av - np.cross(av, bv)])
def qdag(a): return np.concatenate([[a[0]], -a[1:]])
def qexp(v):
    th = np.linalg.norm(v); return np.concatenate([[np.cos(th)], (np.sin(th)/th if th > 0 else 1.0)*v])
def qlog(q):
    q = q/np.linalg.norm(q); th = np.arccos(np.clip(q[0], -1, 1)); s = np.sin(th)
    return (th/s if s > 1e-14 else 1.0)*q[1:]
ID = np.array([1.0, 0, 0, 0])

def link(U, t, x, mu, sgn):
    if sgn > 0: return U[mu, t % T, x % X]
    if mu == 0: return qdag(U[0, (t-1) % T, x % X])
    return qdag(U[1, t % T, (x-1) % X])

def transport(U, start, steps):
    t, x = start; q = ID.copy()
    for mu, sgn in steps:
        q = qmul(q, link(U, t, x, mu, sgn))
        if mu == 0: t += sgn
        else: x += sgn
    return q

def staircase(a, b, order):
    st = []
    for mu in order:
        d = b[mu] - a[mu]; st += [(mu, int(np.sign(d)))]*abs(d)
    return st
def inverse(steps): return [(mu, -s) for mu, s in reversed(steps)]

def average(qs, kind):
    qs = np.array(qs)
    if kind == "P":
        s = qs.sum(axis=0); return s/np.linalg.norm(s)
    ref = qs[0]; logs = [qlog(qmul(qdag(ref), q)) for q in qs]
    return qmul(ref, qexp(np.mean(logs, axis=0)))

def coarse(U, mode, kind):
    nT, nX = T//Lb, X//Lb; V = np.zeros((D, nT, nX, 4))
    for s in range(nT):
        for r in range(nX):
            base = (s*Lb, r*Lb) if mode == "corner" else (s*Lb+1, r*Lb+1)
            orders = [(1, 0)] if mode == "corner" else [(0, 1), (1, 0)]
            for mu in range(D):
                sh = (Lb, 0) if mu == 0 else (0, Lb); base2 = (base[0]+sh[0], base[1]+sh[1]); qs = []
                for dt in range(Lb):
                    for dx in range(Lb):
                        xs = (s*Lb+dt, r*Lb+dx)
                        for o in orders:
                            p = staircase(base, xs, o) + [(mu, 1)]*Lb + inverse(staircase(base2, (xs[0]+sh[0], xs[1]+sh[1]), o))
                            qs.append(transport(U, base, p))
                V[mu, s, r] = average(qs, kind)
    return V

def reflect(U):
    n0, n1 = U.shape[1], U.shape[2]; R = np.zeros_like(U)
    for t in range(n0):
        for x in range(n1):
            R[1, (-1-t) % n0, x] = U[1, t, x]
            R[0, (-2-t) % n0, x] = qdag(U[0, t, x])
    return R

def trplaq(V):
    n0, n1 = V.shape[1], V.shape[2]; out = np.zeros((n0, n1))
    for t in range(n0):
        for x in range(n1):
            p = qmul(qmul(V[0, t, x], V[1, (t+1) % n0, x]), qmul(qdag(V[0, t, (x+1) % n1]), qdag(V[1, t, x])))
            out[t, x] = p[0]
    return out

def rand_su2_near_id(rng, sigma, shape):
    v = rng.normal(0, sigma, shape+(3,)); out = np.zeros(shape+(4,))
    for idx in np.ndindex(shape): out[idx] = qexp(v[idx])
    return out

rng = np.random.default_rng(20261121)
res = dict(script_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(), numpy=np.__version__,
           python=platform.python_version(), T=T, X=X, Lb=Lb, trials=[])
for sigma in (0.05, 0.15, 0.3):
    for trial in range(2):
        U = rand_su2_near_id(rng, sigma, (D, T, X)); row = dict(sigma=sigma, trial=trial)
        # gauge transformation for covariance check
        g = rand_su2_near_id(rng, 2.0, (T, X)); Ug = np.zeros_like(U)
        for t in range(T):
            for x in range(X):
                Ug[0, t, x] = qmul(qmul(g[t, x], U[0, t, x]), qdag(g[(t+1) % T, x]))
                Ug[1, t, x] = qmul(qmul(g[t, x], U[1, t, x]), qdag(g[t, (x+1) % X]))
        for mode in ("corner", "centre"):
            for kind in ("P", "E"):
                lhs = trplaq(reflect(coarse(U, mode, kind))); rhs = trplaq(coarse(reflect(U), mode, kind))
                row[f"{mode}_{kind}_theta_maxdiff"] = float(np.max(np.abs(lhs - rhs)))
                row[f"{mode}_{kind}_mean_1minus_trplaq"] = float(np.mean(1 - lhs))
                row[f"{mode}_{kind}_gauge_maxdiff"] = float(np.max(np.abs(trplaq(coarse(Ug, mode, kind)) - trplaq(coarse(U, mode, kind)))))
        res["trials"].append(row); print(row, flush=True)
json.dump(res, open("outputs/e03b_su2_results.json", "w"), indent=1)
