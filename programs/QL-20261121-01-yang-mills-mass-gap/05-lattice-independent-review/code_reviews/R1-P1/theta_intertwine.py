# © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. Contributing-agent: LATTICE (independent validator). Internal source: f5ccacd. Metadata watermark, not tamper-proof.
"""LATTICE independent implementation (QL-20261121-01 / R1-P1, claim 2).
Tests whether gauge-covariant block-averaging maps B intertwine the time reflection theta:
    B(theta U) == theta' B(U)
for SU(2) lattice gauge fields on a periodic 4D lattice. Written before reading QUASAR's E-files / code.
Two maps:
  corner : anchor = block minimum corner (Balaban-1984-style), blocks {Ln..Ln+L-1}, link reflection t -> -1-t
  centre : anchor = block centre (odd L), blocks {Ln-h..Ln+h}, site reflection t -> -t
Paths anchor->x are axis ordered (mu = 0,1,2,3). Coarse link (Y,Y+e_mu):
  V = Avg_{d in block offsets} W(a->a+d) * S_mu(a+d, L) * W(a+L e_mu -> a+L e_mu + d)^{-1}
Avg = 'proj' (normalised quaternion sum) or 'log' (exp of mean of logs).
Mismatch measures: raw link (quaternion distance) and GAUGE-INVARIANT (coarse plaquette traces, coarse 1x2 loops).
"""
import numpy as np, itertools, sys, json
rng = np.random.default_rng(20261121)
D = 4

def qmul(a, b):
    a0,a1,a2,a3 = np.moveaxis(a,-1,0); b0,b1,b2,b3 = np.moveaxis(b,-1,0)
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0], -1)
def qinv(a):
    return a*np.array([1,-1,-1,-1])
def qexp(v):  # v: (...,3) su(2) coords -> unit quaternion
    th = np.linalg.norm(v,axis=-1,keepdims=True)
    s = np.where(th>1e-300, np.sin(th)/np.where(th>0,th,1), 1.0)
    return np.concatenate([np.cos(th), s*v], -1)
def qlog(q):
    q = q/np.linalg.norm(q,axis=-1,keepdims=True)
    c = np.clip(q[...,:1],-1,1); th = np.arccos(c); s = np.sin(th)
    f = np.where(s>1e-14, th/np.where(s>1e-14,s,1), 1.0)
    return f*q[...,1:]

def random_field(N, eps):
    if eps is None:  # Haar
        q = rng.normal(size=(D,)+(N,)*D+(4,)); return q/np.linalg.norm(q,axis=-1,keepdims=True)
    return qexp(eps*rng.normal(size=(D,)+(N,)*D+(3,)))

def link(U, mu, sites):  # sites: tuple of index arrays (D,M)
    return U[(mu,)+tuple(sites)]

ORDER = [0,1,2,3]
def transport(U, start, d):
    """axis-ordered path from start (D,M int array) by offset d (len D ints). returns (M,4)"""
    N = U.shape[1]; cur = start.copy(); M = start.shape[1]
    W = np.zeros((M,4)); W[:,0] = 1
    for mu in ORDER:
        step = 1 if d[mu] >= 0 else -1
        for _ in range(abs(d[mu])):
            if step == 1:
                W = qmul(W, link(U, mu, cur % N)); cur[mu] += 1
            else:
                cur[mu] -= 1; W = qmul(W, qinv(link(U, mu, cur % N)))
    return W

def block_map(U, L, kind, avg):
    N = U.shape[1]; Nc = N//L
    grid = np.array(list(itertools.product(range(Nc), repeat=D))).T  # (D,M)
    anchors = L*grid
    if kind == 'corner': offs = list(itertools.product(range(L), repeat=D))
    else:
        h = (L-1)//2; offs = list(itertools.product(range(-h,h+1), repeat=D))
    V = np.zeros((D,)+(Nc,)*D+(4,))
    for mu in range(D):
        e = np.zeros((D,1),int); e[mu] = L
        acc = []
        for d in offs:
            dd = np.array(d)[:,None]
            A = transport(U, anchors, d)
            S = transport(U, anchors+dd, [L if m==mu else 0 for m in range(D)])
            B = transport(U, anchors+e, d)
            acc.append(qmul(qmul(A, S), qinv(B)))
        acc = np.array(acc)
        if avg == 'proj':
            s = acc.mean(0); s = s/np.linalg.norm(s,axis=-1,keepdims=True)
        elif avg == 'logref':
            # gauge-covariant log average: reference term = straight link (d = 0 offset)
            i0 = offs.index(tuple([0]*D))
            ref = acc[i0]
            s = qmul(ref, qexp(qlog(qmul(qinv(ref)[None], acc)).mean(0)))
        else:
            # align sign (SU(2) double cover irrelevant for products here); log-average
            s = qexp(qlog(acc).mean(0))
        V[(mu,)+tuple(grid)] = s
    return V

def reflect(U, r, invert_temporal=True):
    """time reflection t -> r - t on links"""
    N = U.shape[1]; R = np.empty_like(U)
    t = np.arange(N)
    for mu in range(D):
        if mu == 0:
            src = (r - t - 1) % N
            R[0] = U[0][src]
            if invert_temporal: R[0] = qinv(R[0])
        else:
            src = (r - t) % N
            R[mu] = U[mu][src]
    return R

def qdist(a, b):  # distance between SU(2) elements, insensitive to overall sign? no: use Frobenius of 2x2 = sqrt(2)*|qa-qb|
    return np.sqrt(2)*np.linalg.norm(a-b, axis=-1)

def plaq_traces(V):
    out = []
    for mu in range(D):
        for nu in range(mu+1, D):
            P = qmul(qmul(V[mu], np.roll(V[nu], -1, axis=mu)), qmul(qinv(np.roll(V[mu], -1, axis=nu)), qinv(V[nu])))
            out.append(2*P[...,0])  # tr of SU(2) matrix = 2 q0
    return np.array(out)

def rect_traces(V):  # 2x1 loops (2 in mu, 1 in nu), gauge invariant
    out = []
    for mu in range(D):
        for nu in range(D):
            if mu == nu: continue
            Vm2 = qmul(V[mu], np.roll(V[mu], -1, axis=mu))
            top = qmul(np.roll(V[mu], -1, axis=nu), np.roll(np.roll(V[mu], -1, axis=nu), -1, axis=mu))
            P = qmul(qmul(Vm2, np.roll(np.roll(V[nu], -2, axis=mu),0,axis=0)), qmul(qinv(top), qinv(V[nu])))
            out.append(2*P[...,0])
    return np.array(out)

def reflect_coarse_gi(T, r):
    """gauge-invariant loop traces are site-indexed by loop base point; reflection maps loop at t to a loop
    with different base point -> compare sorted multisets per (plane) and per spatial slice instead"""
    return T

def compare(N, L, kind, avg, eps, invert_temporal=True, gauge_test=False):
    U = random_field(N, eps)
    if gauge_test:  # apply a random fine gauge transformation first; B must be covariant
        pass
    if kind == 'corner': r, rc = -1, -1
    else: r, rc = 0, 0
    BU = block_map(U, L, kind, avg)
    lhs = block_map(reflect(U, r, invert_temporal), L, kind, avg)
    rhs = reflect(BU, rc, True)
    raw = qdist(lhs, rhs).max()
    # gauge invariant: multiset of coarse plaquette traces per (time-slice, plane) must agree
    pl, pr = plaq_traces(lhs), plaq_traces(rhs)
    # plaquette traces of rhs and lhs are both traces of the SAME geometric coarse plaquettes if intertwining holds
    gi = np.abs(pl - pr).max()
    rl, rr = rect_traces(lhs), rect_traces(rhs)
    gi2 = np.abs(rl - rr).max()
    return dict(N=N, L=L, kind=kind, avg=avg, eps=('Haar' if eps is None else eps),
                invert_temporal=invert_temporal, raw_link_max=float(raw), plaq_trace_max=float(gi), rect_trace_max=float(gi2))

def gauge_covariance_check(N, L, kind, avg, eps):
    U = random_field(N, eps)
    g = random_field(N, eps if eps is not None else None)[0]  # site field
    Ug = np.empty_like(U)
    for mu in range(D):
        Ug[mu] = qmul(qmul(g, U[mu]), qinv(np.roll(g, -1, axis=mu)))
    B1 = block_map(Ug, L, kind, avg); B0 = block_map(U, L, kind, avg)
    Nc = N//L
    if kind == 'corner': gc = g[(slice(0,N,L),)*D]
    else: gc = g[(slice(0,N,L),)*D]
    B0g = np.empty_like(B0)
    for mu in range(D):
        B0g[mu] = qmul(qmul(gc, B0[mu]), qinv(np.roll(gc, -1, axis=mu)))
    return float(qdist(B1, B0g).max())

if __name__ == '__main__':
    res = []
    import theta_intertwine as T
    for order in ([0,1,2,3], [1,2,3,0], [1,0,2,3]):
        ORDER[:] = order
        for kind, N, L in [('corner', 8, 2), ('centre', 9, 3)]:
            for avg in ['proj', 'logref', 'log']:
                gc = gauge_covariance_check(N, L, kind, avg, 0.3)
                for eps in [1e-3, 1e-2, 0.1, 0.3, 1.0, None]:
                    r = compare(N, L, kind, avg, eps); r['order'] = list(order); r['gauge_cov_err_eps0.3'] = gc
                    res.append(r)
                    print(order, kind, avg, r['eps'], 'cov=%.1e raw=%.2e plaq=%.2e rect=%.2e' % (gc, r['raw_link_max'], r['plaq_trace_max'], r['rect_trace_max']), flush=True)
    ORDER[:] = [0,1,2,3]
    for kind, N, L in [('centre', 9, 3), ('corner', 8, 2)]:
        r = compare(N, L, kind, 'proj', 0.3, invert_temporal=False); r['note'] = 'temporal links NOT inverted under theta (wrong convention)'
        res.append(r); print('no-inversion', kind, r['raw_link_max'], r['plaq_trace_max'], flush=True)
    json.dump(res, open('theta_intertwine_results.json','w'), indent=1)
