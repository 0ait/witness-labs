#!/usr/bin/env python3
# Witness Labs, Agentic Swarm, 0ait | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | contributing agent: QUASAR | x-witness-labs-attribution
"""R1-E01 (QL-20261121-01, WITNESS LAB, QUASAR): 4D U(1) vs 4D SU(2) Wilson lattice gauge theory
on small periodic lattices. Vectorised checkerboard heat-bath:
  U(1): exact von Mises heat bath; SU(2): Creutz/Kennedy-Pendleton heat bath (quaternions).
Observables: mean plaquette P, plaquette susceptibility chi_P = N_p(<P^2>-<P>^2), hot/cold-start hysteresis,
Wilson loops W(R,T) and Creutz ratio chi(2,2).
LABEL: Numerical evidence only (small lattices, short runs). Not a proof of anything.
Usage: python3 r1e01_u1_su2_4d.py <config_name>   (configs defined in CONFIGS) ; writes outputs/<name>.json
"""
import sys, json, time, hashlib, platform
import numpy as np

D = 4

def sh(a, mu, s):  # value at x + s*e_mu placed at x
    return np.roll(a, -s, axis=mu)

def parity_masks(L):
    g = np.indices((L,)*D).sum(axis=0) % 2
    return [g == 0, g == 1]

# ---------------- U(1) ----------------
def u1_staple(th, mu):
    S = np.zeros(th.shape[1:], dtype=complex)
    tm = th[mu]
    for nu in range(D):
        if nu == mu: continue
        tn = th[nu]
        up = sh(tn, mu, 1) - sh(tm, nu, 1) - tn
        tn_m = sh(tn, nu, -1)
        lo = -sh(tn_m, mu, 1) - sh(tm, nu, -1) + tn_m
        S += np.exp(1j*up) + np.exp(1j*lo)
    return S

def u1_sweep(th, beta, rng, masks):
    for mu in range(D):
        for m in masks:
            S = u1_staple(th, mu)
            k = beta*np.abs(S[m]); phi = -np.angle(S[m])
            th[mu][m] = rng.vonmises(phi, k)
    return th

def u1_plaq_angles(th, mu, nu):
    return th[mu] + sh(th[nu], mu, 1) - sh(th[mu], nu, 1) - th[nu]

def u1_meas(th, Rmax=2):
    P = []; W = {}
    for mu in range(D):
        for nu in range(mu+1, D):
            P.append(np.cos(u1_plaq_angles(th, mu, nu)).mean())
    # Wilson loops in all planes, both orientations averaged
    for R in range(1, Rmax+1):
        for T in range(1, Rmax+1):
            acc = []
            for mu in range(D):
                for nu in range(D):
                    if nu == mu: continue
                    lm = sum(sh(th[mu], mu, j) for j in range(R))          # line R along mu from x
                    ln = sum(sh(th[nu], nu, j) for j in range(T))          # line T along nu from x
                    ang = lm + sh(ln, mu, R) - sh(lm, nu, T) - ln
                    acc.append(np.cos(ang).mean())
            W[f"{R}x{T}"] = float(np.mean(acc))
    return float(np.mean(P)), W

# ---------------- SU(2) quaternions: array shape (..., 4) with q = a0 + i a.sigma ----------------
def qmul(a, b):
    a0, av = a[..., 0], a[..., 1:]; b0, bv = b[..., 0], b[..., 1:]
    c0 = a0*b0 - np.sum(av*bv, axis=-1)
    cv = a0[..., None]*bv + b0[..., None]*av - np.cross(av, bv)
    return np.concatenate([c0[..., None], cv], axis=-1)

def qdag(a):
    return np.concatenate([a[..., :1], -a[..., 1:]], axis=-1)

def su2_staple(U, mu):
    A = np.zeros(U.shape[1:])
    Um = U[mu]
    for nu in range(D):
        if nu == mu: continue
        Un = U[nu]
        A += qmul(qmul(sh(Un, mu, 1), qdag(sh(Um, nu, 1))), qdag(Un))
        Un_m = sh(Un, nu, -1)
        A += qmul(qmul(qdag(sh(Un_m, mu, 1)), qdag(sh(Um, nu, -1))), Un_m)
    return A

def kp_sample_a0(alpha, rng):
    n = alpha.size; out = np.empty(n); todo = np.arange(n)
    for _ in range(10000):
        if todo.size == 0: break
        al = alpha[todo]
        r1 = 1.0 - rng.random(todo.size); r2 = rng.random(todo.size); r3 = 1.0 - rng.random(todo.size)
        lam2 = -(np.log(r1) + np.cos(2*np.pi*r2)**2*np.log(r3))/(2*al)
        r4 = rng.random(todo.size)
        ok = r4**2 <= 1.0 - lam2
        out[todo[ok]] = 1.0 - 2.0*lam2[ok]
        todo = todo[~ok]
    if todo.size: raise RuntimeError("KP sampler did not converge")
    return out

def su2_sweep(U, beta, rng, masks):
    for mu in range(D):
        for m in masks:
            A = su2_staple(U, mu)[m]
            k = np.sqrt(np.sum(A*A, axis=-1))
            V = A/k[:, None]
            a0 = kp_sample_a0(beta*k, rng)
            r = np.sqrt(np.clip(1 - a0*a0, 0, None))
            v = rng.normal(size=(a0.size, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
            X = np.concatenate([a0[:, None], r[:, None]*v], axis=1)
            Um = U[mu]; Um[m] = qmul(X, qdag(V))
    # reunitarise against round-off drift
    U /= np.linalg.norm(U, axis=-1)[..., None]
    return U

def su2_line(Ua, mu, n):
    out = Ua.copy()
    for j in range(1, n):
        out = qmul(out, sh(Ua, mu, j))
    return out

def su2_meas(U, Rmax=2):
    P = []; W = {}
    for mu in range(D):
        for nu in range(mu+1, D):
            p = qmul(qmul(U[mu], sh(U[nu], mu, 1)), qmul(qdag(sh(U[mu], nu, 1)), qdag(U[nu])))
            P.append(p[..., 0].mean())
    for R in range(1, Rmax+1):
        for T in range(1, Rmax+1):
            acc = []
            for mu in range(D):
                for nu in range(D):
                    if nu == mu: continue
                    lm = su2_line(U[mu], mu, R); ln = su2_line(U[nu], nu, T)
                    w = qmul(qmul(lm, sh(ln, mu, R)), qmul(qdag(sh(lm, nu, T)), qdag(ln)))
                    acc.append(w[..., 0].mean())
            W[f"{R}x{T}"] = float(np.mean(acc))
    return float(np.mean(P)), W

# ---------------- driver ----------------
def run(group, L, beta, start, ntherm, nmeas, every, seed):
    rng = np.random.default_rng(seed)
    masks = parity_masks(L)
    if group == "U1":
        th = np.zeros((D,)+(L,)*D) if start == "cold" else rng.uniform(-np.pi, np.pi, (D,)+(L,)*D)
        sweep = lambda f: u1_sweep(f, beta, rng, masks); meas = u1_meas; f = th
    else:
        if start == "cold":
            f = np.zeros((D,)+(L,)*D+(4,)); f[..., 0] = 1.0
        else:
            f = rng.normal(size=(D,)+(L,)*D+(4,)); f /= np.linalg.norm(f, axis=-1)[..., None]
        sweep = lambda f: su2_sweep(f, beta, rng, masks); meas = su2_meas
    for _ in range(ntherm): f = sweep(f)
    Ps = []; Ws = []
    for i in range(nmeas):
        f = sweep(f)
        if i % every == 0:
            p, w = meas(f); Ws.append(w)
        else:
            p = None
            # cheap plaquette every sweep
            if group == "U1":
                p = float(np.mean([np.cos(u1_plaq_angles(f, a, b)).mean() for a in range(D) for b in range(a+1, D)]))
            else:
                p = float(np.mean([qmul(qmul(f[a], sh(f[b], a, 1)), qmul(qdag(sh(f[a], b, 1)), qdag(f[b])))[..., 0].mean()
                                   for a in range(D) for b in range(a+1, D)]))
        Ps.append(p)
    return np.array(Ps), Ws

def jackknife_blocks(x, nb=10):
    x = np.asarray(x); n = len(x)//nb*nb; xb = x[:n].reshape(nb, -1)
    return xb

def analyse(Ps, Ws, L):
    Np = 6*L**D
    xb = jackknife_blocks(Ps); nb = xb.shape[0]
    allx = xb.ravel()
    P = allx.mean(); chi = Np*allx.var()
    jP = []; jchi = []
    for i in range(nb):
        y = np.delete(xb, i, axis=0).ravel(); jP.append(y.mean()); jchi.append(Np*y.var())
    jP = np.array(jP); jchi = np.array(jchi)
    errP = np.sqrt((nb-1)*np.mean((jP-jP.mean())**2)); errchi = np.sqrt((nb-1)*np.mean((jchi-jchi.mean())**2))
    Wm = {k: float(np.mean([w[k] for w in Ws])) for k in Ws[0]}
    def creutz(W):
        try:
            v = W["2x2"]*W["1x1"]/(W["2x1"]*W["1x2"])
            return float(-np.log(v)) if v > 0 else None
        except Exception:
            return None
    cr = creutz(Wm)
    # jackknife over W measurements for creutz
    nw = len(Ws); nbw = min(10, nw); bs = nw//nbw; jc = []
    for i in range(nbw):
        sub = Ws[:i*bs] + Ws[(i+1)*bs:nbw*bs]
        c = creutz({k: np.mean([w[k] for w in sub]) for k in Ws[0]}); jc.append(np.nan if c is None else c)
    jc = np.array(jc); errcr = float(np.sqrt((nbw-1)*np.nanmean((jc-np.nanmean(jc))**2))) if np.isfinite(jc).sum() > 1 else None
    return dict(P=float(P), dP=float(errP), chiP=float(chi), dchiP=float(errchi), W=Wm, creutz22=cr, dcreutz22=errcr,
                nmeas=len(Ps), nW=nw)

CONFIGS = {
  # name: (group, L, betas, starts, ntherm, nmeas, every)
  "bench_u1":  ("U1", 6, [1.0], ["hot"], 2, 5, 5),
  "bench_su2": ("SU2", 6, [2.3], ["hot"], 2, 5, 5),
  "valid_u1":  ("U1", 4, [0.2, 3.0], ["hot"], 100, 300, 10),
  "valid_su2": ("SU2", 4, [0.4, 4.0], ["hot"], 100, 300, 10),
  "u1_L6":  ("U1", 6, [0.80, 0.90, 0.95, 0.98, 1.00, 1.02, 1.04, 1.06, 1.10, 1.20, 1.40], ["hot", "cold"], 500, 600, 10),
  "u1_L8":  ("U1", 8, [0.96, 0.99, 1.00, 1.01, 1.02, 1.03, 1.06], ["hot", "cold"], 500, 500, 10),
  "su2_L6": ("SU2", 6, [1.6, 1.9, 2.1, 2.2, 2.3, 2.4, 2.5, 2.7, 3.0], ["hot", "cold"], 150, 300, 10),
  "su2_L8": ("SU2", 8, [2.0, 2.2, 2.3, 2.4, 2.6], ["hot", "cold"], 100, 200, 10),
}

if __name__ == "__main__":
    name = sys.argv[1]; group, L, betas, starts, nth, nme, ev = CONFIGS[name]
    src = open(__file__, "rb").read()
    out = dict(config=name, group=group, L=L, ntherm=nth, nmeas=nme, meas_every=ev,
               script_sha256=hashlib.sha256(src).hexdigest(), numpy=np.__version__, python=platform.python_version(),
               label="Numerical evidence only", results=[])
    t0 = time.process_time()
    for ib, beta in enumerate(betas):
        for js, st in enumerate(starts):
            seed = 20261121 + 1000*ib + js + (0 if group == "U1" else 500000) + 10*L
            t1 = time.process_time()
            Ps, Ws = run(group, L, beta, st, nth, nme, ev, seed)
            a = analyse(Ps, Ws, L); a.update(beta=beta, start=st, seed=seed, cpu_s=time.process_time()-t1)
            out["results"].append(a)
            print(f"{group} L={L} beta={beta:.3f} {st:4s} P={a['P']:.5f}({a['dP']:.5f}) chiP={a['chiP']:.3f}({a['dchiP']:.3f}) "
                  f"creutz22={a['creutz22']} W11={a['W']['1x1']:.4f} W22={a['W']['2x2']:.5f} cpu={a['cpu_s']:.1f}s", flush=True)
    out["total_cpu_s"] = time.process_time()-t0
    json.dump(out, open(f"outputs/{name}.json", "w"), indent=1)
    print("total cpu s", out["total_cpu_s"])
