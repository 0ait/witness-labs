# Witness Labs, Agentic Swarm, 0ait | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | contributing agent: QUASAR | x-witness-labs-attribution
"""INV001-E04: Poincare (spectral) gap of the Langevin generator for the single-link SU(2) measure
   mu_beta(dU) ∝ exp((beta/2) Re Tr U) dU on SU(2) = unit S^3, versus beta, compared with
   (a) the Bakry-Emery bound K = Ric + inf Hess V = 2 - beta (positive only for beta<2),
   (b) the Holley-Stroock bound 3*exp(-osc V) = 3*exp(-2 beta),
   (c) the Gaussian (Ornstein-Uhlenbeck) asymptote beta.
   Here V(theta) = -beta cos(theta), theta = geodesic distance to identity, (1/2)Tr U = cos theta.
   Generator: L f = Δf - <∇V,∇f>; self-adjoint in L^2(e^{-V} dvol).
   Separation f = g(theta) Y_l(omega), omega in S^2; weighted 1D form
     Q[g] = ∫ w g'^2 + l(l+1) (w/sin^2) g^2 ,  N[g] = ∫ w g^2 ,  w = sin^2(theta) e^{beta(cos theta - 1)}.
   Discretisation: piecewise-linear FEM on a theta grid graded towards 0 (theta = pi*s^p), generalized eigenproblem.
"""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, json, sys, time

def gap(beta, l, n=4000, p=2.0):
    s = np.linspace(0, 1, n+1); th = np.pi * s**p
    # element quadrature: 3-point Gauss on each element
    gx, gw = np.polynomial.legendre.leggauss(4)
    h = np.diff(th)
    K = sp.lil_matrix((n+1, n+1)); M = sp.lil_matrix((n+1, n+1))
    rows=[];cols=[];kv=[];mv=[]
    for (xi, wi) in zip(gx, gw):
        t = th[:-1] + (xi+1)/2*h
        w = np.sin(t)**2 * np.exp(beta*(np.cos(t)-1))
        c = l*(l+1)*np.exp(beta*(np.cos(t)-1))  # w/sin^2
        phi0 = (1-xi)/2; phi1 = (1+xi)/2
        jac = h/2*wi
        for a,pa,da in ((0,phi0,-1.0),(1,phi1,1.0)):
            for b,pb,db in ((0,phi0,-1.0),(1,phi1,1.0)):
                idx_a = np.arange(n)+a; idx_b = np.arange(n)+b
                rows.append(idx_a); cols.append(idx_b)
                kv.append(jac*(w*da*db/h**2 + c*pa*pb)); mv.append(jac*w*pa*pb)
    r=np.concatenate(rows); cc=np.concatenate(cols)
    K = sp.csr_matrix((np.concatenate(kv),(r,cc)),shape=(n+1,n+1))
    M = sp.csr_matrix((np.concatenate(mv),(r,cc)),shape=(n+1,n+1))
    if l >= 1:  # Dirichlet at both poles (Y_l regularity)
        keep = np.arange(1, n)
    else:
        # drop nodes where the weight underflows entirely (far from identity at large beta)
        keep = np.arange(0, n+1)
    K = K[keep][:, keep]; M = M[keep][:, keep]
    d = M.diagonal(); good = d > 1e-280
    K = K[good][:, good]; M = M[good][:, good]
    # symmetric scaling for conditioning
    D = sp.diags(1/np.sqrt(M.diagonal()))
    A = (D@K@D).tocsc(); B = (D@M@D).tocsc()
    k = 3
    vals = sla.eigsh(A, k=k, M=B, sigma=-1e-3, which='LM', return_eigenvectors=False)
    vals = np.sort(vals)
    return vals[1] if l == 0 else vals[0]

if __name__ == '__main__':
    t0=time.time(); out={}
    betas=[0,0.5,1,2,4,8,16,32,64,128,256]
    for b in betas:
        row={}
        for l in (0,1):
            g1=gap(b,l,n=4000); g2=gap(b,l,n=8000)
            row[f'l{l}']=g2; row[f'l{l}_n4000']=g1; row[f'l{l}_relchange']=abs(g2-g1)/abs(g2)
        row['gap']=min(row['l0'],row['l1'])
        row['BE']=2-b; row['HS']=3*np.exp(-2*b); row['OU']=b
        out[str(b)]=row
        print(f"beta={b:6g} gap_l0={row['l0']:.8f} gap_l1={row['l1']:.8f} gap={row['gap']:.8f} "
              f"rel(n4000->8000) {max(row['l0_relchange'],row['l1_relchange']):.1e}  BE={2-b:+.1f} HS={3*np.exp(-2*b):.3e} gap/beta={row['gap']/max(b,1e-300):.5f}", flush=True)
    json.dump(out, open('outputs/e04_results.json','w'), indent=1)
    print('elapsed', time.time()-t0)
