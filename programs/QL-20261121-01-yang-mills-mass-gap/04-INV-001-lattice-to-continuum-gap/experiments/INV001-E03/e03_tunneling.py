#!/usr/bin/env python3
# Witness Labs, Agentic Swarm, 0ait | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | contributing agent: QUASAR | x-witness-labs-attribution
"""INV001-E03: finite-volume gap closing by tunnelling (illustration of obstruction lemma D04).

Model 1 (exact, rigorous, D04 Example A): rigid-column Ising strip. Transfer matrix
   T_L = [[e^{LK}, e^{-LK}], [e^{-LK}, e^{LK}]]; lambda_0 = 2cosh(LK), lambda_1 = 2sinh(LK);
   m_lat(L) = log coth(LK) ~ 2 e^{-2LK}.  Evaluated in mpmath (60 digits).
Model 2 (numerical): periodic transverse-field Ising chain H = -J sum s^z_i s^z_{i+1} - h sum s^x_i,
   0<h<J (ordered phase).  Exact diagonalisation in the Z2-even and Z2-odd sectors (P = prod s^x),
   L = 4..18.  Reported: tunnelling splitting d0(L) = E_odd,0 - E_even,0 and the gap to the next
   level in the even sector d1(L) = E_even,1 - E_even,0.
   Cross-check: free-fermion formula E_NS = -1/2 sum_{k in NS} eps_k, E_R = -1/2 sum_{k in R} eps_k,
   eps_k = 2 sqrt(J^2 + h^2 - 2 J h cos k), NS: k = (2m+1)pi/L, R: k = 2 m pi/L  (valid for h<J,
   where both vacua lie in the physical parity sectors; checked against ED, not assumed).
"""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, json, mpmath as mp
out = {}
mp.mp.dps = 60
m1 = []
for K in [mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf(1)]:
    for L in [1,2,4,8,16,32]:
        m = mp.log(mp.coth(L*K))
        m1.append(dict(K=str(K), L=L, m_lat=mp.nstr(m, 20), ratio_to_2exp=mp.nstr(m/(2*mp.exp(-2*L*K)), 15)))
out['rigid_column'] = m1
def tfim_sector_lowest(L, J, h, parity, k=2):
    # basis in s^x eigenbasis would diagonalise P; instead build in s^z basis and use symmetric/antisym combos
    D = 1<<L
    full = (1<<L)-1
    reps = [s for s in range(D) if s < (s ^ full)]
    idx = {s:i for i,s in enumerate(reps)}
    rows, cols, vals = [], [], []
    for i,s in enumerate(reps):
        # diagonal: -J sum s^z s^z (periodic)
        e = 0
        for j in range(L):
            a = (s>>j)&1; b = (s>>((j+1)%L))&1
            e += -J if a==b else J
        rows.append(i); cols.append(i); vals.append(e)
        for j in range(L):
            t = s ^ (1<<j)
            sign = 1.0
            if t not in idx:
                t = t ^ full; sign = 1.0 if parity==+1 else -1.0
            rows.append(idx[t]); cols.append(i); vals.append(-h*sign)
    H = sp.csr_matrix((vals,(rows,cols)), shape=(len(reps),len(reps)))
    if H.shape[0] < 400:
        return np.sort(np.linalg.eigvalsh(H.toarray()))[:k]
    return np.sort(sla.eigsh(H, k=k, which='SA', tol=1e-13)[0])
def ff(L, J, h):
    eps = lambda k: 2*np.sqrt(J*J+h*h-2*J*h*np.cos(k))
    kNS = (2*np.arange(L)+1)*np.pi/L; kR = 2*np.arange(L)*np.pi/L
    return -0.5*eps(kNS).sum(), -0.5*eps(kR).sum()
m2 = []
J = 1.0
for h in [0.3, 0.5, 0.7]:
    for L in range(4, 19, 2):
        ee = tfim_sector_lowest(L, J, h, +1, 2); eo = tfim_sector_lowest(L, J, h, -1, 1)
        ens, er = ff(L, J, h)
        m2.append(dict(h=h, L=L, E_even0=ee[0], E_even1=ee[1], E_odd0=eo[0],
                       split_d0=eo[0]-ee[0], gap_d1=ee[1]-ee[0],
                       ff_NS=ens, ff_R=er, ff_split=er-ens, ed_vs_ff_even=abs(ee[0]-ens), ed_vs_ff_odd=abs(eo[0]-er)))
        print('h=%.1f L=%2d split=%.3e gap1=%.6f |ED-FF| even %.1e odd %.1e' % (h,L,eo[0]-ee[0],ee[1]-ee[0],abs(ee[0]-ens),abs(eo[0]-er)), flush=True)
out['tfim'] = m2
# fit log split vs L
fits = {}
for h in [0.3,0.5,0.7]:
    Ls = np.array([r['L'] for r in m2 if r['h']==h and r['L']>=8]); d = np.array([r['split_d0'] for r in m2 if r['h']==h and r['L']>=8])
    sl, ic = np.polyfit(Ls, np.log(np.abs(d)), 1)
    fits[str(h)] = dict(slope=sl, log_J_over_h=-np.log(J/h))
out['tfim_fit_log_split_vs_L'] = fits
print(fits)
json.dump(out, open('outputs/e03_results.json','w'), indent=1, default=float)
