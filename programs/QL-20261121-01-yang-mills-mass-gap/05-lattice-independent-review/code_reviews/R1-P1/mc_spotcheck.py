# © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. Contributing-agent: LATTICE (independent validator). Internal source: f5ccacd. Metadata watermark, not tamper-proof.
"""LATTICE independent spot-check of R1-E01 (QL-20261121-01 / R1-P1, claim 7).
Different algorithm from QUASAR's heat bath: checkerboard multi-hit Metropolis, 4D Wilson action, periodic L^4.
U(1): S = beta sum (1-cos theta_p).  SU(2): S = beta sum (1 - 1/2 Tr U_p).
Plaquette measured EVERY sweep -> integrated autocorrelation time (Madras-Sokal window, c=6) and
error = sqrt(2 tau_int / N) * sd.  Small runs only (verification, not new research)."""
import numpy as np, json, sys, time
D = 4
def sh(a, mu, s): return np.roll(a, -s, axis=mu)
def masks(L):
    g = np.indices((L,)*D).sum(0) % 2; return [g == 0, g == 1]
# ---- U(1)
def u1_staple(th, mu):
    S = np.zeros(th.shape[1:], complex)
    for nu in range(D):
        if nu == mu: continue
        S += np.exp(1j*(sh(th[nu], mu, 1) - sh(th[mu], nu, 1) - th[nu]))
        tnm = sh(th[nu], nu, -1)
        S += np.exp(1j*(-sh(tnm, mu, 1) - sh(th[mu], nu, -1) + tnm))
    return S
def u1_sweep(th, beta, rng, ms, delta=1.0, hits=4):
    acc = 0; tot = 0
    for mu in range(D):
        for m in ms:
            S = u1_staple(th, mu)[m]
            old = th[mu][m]
            for _ in range(hits):
                new = old + delta*(2*rng.random(old.shape)-1)
                dS = -beta*(np.real(np.exp(1j*new)*S) - np.real(np.exp(1j*old)*S))
                ok = rng.random(old.shape) < np.exp(-np.clip(dS, -50, 50))
                old = np.where(ok, new, old); acc += ok.sum(); tot += ok.size
            th[mu][m] = old
    return acc/tot
def u1_plaq(th):
    return np.mean([np.cos(th[m] + sh(th[n], m, 1) - sh(th[m], n, 1) - th[n]).mean() for m in range(D) for n in range(m+1, D)])
# ---- SU(2) quaternions
def qmul(a, b):
    a0, av = a[..., 0], a[..., 1:]; b0, bv = b[..., 0], b[..., 1:]
    return np.concatenate([(a0*b0 - (av*bv).sum(-1))[..., None], a0[..., None]*bv + b0[..., None]*av - np.cross(av, bv)], -1)
def qdag(a): return a*np.array([1, -1, -1, -1])
def su2_staple(U, mu):
    A = np.zeros(U.shape[1:])
    for nu in range(D):
        if nu == mu: continue
        A += qmul(qmul(sh(U[nu], mu, 1), qdag(sh(U[mu], nu, 1))), qdag(U[nu]))
        unm = sh(U[nu], nu, -1)
        A += qmul(qmul(qdag(sh(unm, mu, 1)), qdag(sh(U[mu], nu, -1))), unm)
    return A
def rand_near(rng, n, eps):
    v = eps*(2*rng.random((n, 3))-1); th = np.linalg.norm(v, axis=1, keepdims=True)
    return np.concatenate([np.cos(th), np.sinc(th/np.pi)*v], 1)
def su2_sweep(U, beta, rng, ms, eps=0.5, hits=4):
    acc = 0; tot = 0
    for mu in range(D):
        for m in ms:
            A = su2_staple(U, mu)[m]; old = U[mu][m]
            for _ in range(hits):
                new = qmul(rand_near(rng, old.shape[0], eps), old)
                dS = -beta*(qmul(new, A)[:, 0] - qmul(old, A)[:, 0])   # (1/2)Tr(UA) = q0 of product
                ok = rng.random(old.shape[0]) < np.exp(-np.clip(dS, -50, 50))
                old = np.where(ok[:, None], new, old); acc += ok.sum(); tot += ok.size
            U[mu][m] = old / np.linalg.norm(old, axis=-1, keepdims=True)
    return acc/tot
def su2_plaq(U):
    return np.mean([qmul(qmul(U[m], sh(U[n], m, 1)), qmul(qdag(sh(U[m], n, 1)), qdag(U[n])))[..., 0].mean() for m in range(D) for n in range(m+1, D)])
def tau_int(x, c=6.0):
    x = np.asarray(x) - np.mean(x); n = len(x); v = np.dot(x, x)/n
    if v == 0: return 0.5, 0
    f = np.fft.rfft(np.concatenate([x, np.zeros(n)])); ac = np.fft.irfft(f*np.conj(f))[:n]/(n*v)
    tau = 0.5
    for W in range(1, n//2):
        tau += ac[W]
        if W >= c*tau: return tau, W
    return tau, n//2
def run(group, L, beta, start, ntherm, nmeas, seed):
    rng = np.random.default_rng(seed); ms = masks(L)
    if group == 'U1':
        th = np.zeros((D,)+(L,)*D) if start == 'cold' else 2*np.pi*rng.random((D,)+(L,)*D)
        sweep = lambda: u1_sweep(th, beta, rng, ms, delta=min(np.pi, 1.6/np.sqrt(max(beta, 0.3)))); meas = lambda: u1_plaq(th)
    else:
        if start == 'cold': U = np.zeros((D,)+(L,)*D+(4,)); U[..., 0] = 1
        else:
            U = rng.normal(size=(D,)+(L,)*D+(4,)); U /= np.linalg.norm(U, axis=-1, keepdims=True)
        sweep = lambda: su2_sweep(U, beta, rng, ms, eps=0.6); meas = lambda: su2_plaq(U)
    t0 = time.process_time(); hist_th = []
    for i in range(ntherm):
        a = sweep()
        if i % 25 == 0: hist_th.append(float(meas()))
    P = []
    for i in range(nmeas):
        a = sweep(); P.append(float(meas()))
    P = np.array(P); tau, W = tau_int(P)
    err_naive = P.std(ddof=1)/np.sqrt(len(P)); err = P.std(ddof=1)*np.sqrt(2*tau/len(P))
    # also first-half vs second-half drift check
    h = len(P)//2
    return dict(group=group, L=L, beta=beta, start=start, ntherm=ntherm, nmeas=nmeas, seed=seed, P=float(P.mean()),
                err_naive=float(err_naive), tau_int=float(tau), window=int(W), err_tau=float(err),
                half1=float(P[:h].mean()), half2=float(P[h:].mean()), acc=float(a), therm_trace=hist_th,
                cpu_s=time.process_time()-t0)
if __name__ == '__main__':
    jobs = [('U1', 6, 0.90, 'hot'), ('U1', 6, 0.90, 'cold'), ('U1', 6, 1.00, 'hot'), ('U1', 6, 1.00, 'cold'),
            ('U1', 6, 1.10, 'hot'), ('U1', 6, 1.10, 'cold'), ('SU2', 6, 2.20, 'hot'), ('SU2', 6, 2.50, 'hot'), ('SU2', 6, 2.50, 'cold')]
    out = []
    for k, (g, L, b, s) in enumerate(jobs):
        r = run(g, L, b, s, ntherm=300, nmeas=1200 if g == 'U1' else 600, seed=777000 + k)
        out.append(r); print({k: v for k, v in r.items() if k != 'therm_trace'}, flush=True)
    json.dump(out, open('mc_spotcheck_results.json', 'w'), indent=1)
