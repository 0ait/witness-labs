# © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. Contributing-agent: LATTICE (independent validator). Internal source: f5ccacd. Metadata watermark, not tamper-proof.
"""LATTICE: exact re-derivation of the SZZ -> Wilson threshold conversion and the R1-E02 bookkeeping (claim 4).
SZZ (arXiv:2204.12737v1, eq. (1.2)-(1.3), opened): S(Q) = N*beta_SZZ * Re sum_{p in P+} Tr(Q_p), density exp(+S),
P+ = one orientation per unoriented plaquette (text, Sec. 1.1). SU(N) condition: |beta_SZZ| < 1/(16(d-1)).
Wilson: exp(-beta_W sum_p (1 - (1/N) Re tr U_p)) = const * exp((beta_W/N) sum_p Re tr U_p)  => beta_W = N^2 beta_SZZ.
Wilson g^2 convention: beta_W = 2N/g^2."""
import sympy as sp
N, d, g2, gam = sp.symbols('N d g2 gamma', positive=True)
bSZZ_max = sp.Rational(1,1)/(16*(d-1))
bW_max = sp.simplify(N**2*bSZZ_max)
print('Wilson beta_W threshold:', bW_max, '| d=4:', bW_max.subs(d,4))
for n in (2,3):
    bw = bW_max.subs({d:4,N:n}); print(f' SU({n}): beta_W < {bw} = {float(bw):.5f};  g^2 > {sp.nsimplify(2*n/bw)} ')
# RG exit coefficient under two possible effective-action normalisations
for label, coef in [('(2/g^2) Re Tr(1-V)  [Wilson-normalised, beta_W=2N/g^2]', 2), ('(1/g^2) Re Tr(1-V)  [as written in R1-D04 s.2]', 1)]:
    for n in (2,):
        for gm in (sp.Rational(1,10), sp.Rational(1,20)):
            bW = coef*n/gm   # beta_W/N = coef/g^2
            ratio = bW / bW_max.subs({d:4,N:n})
            print(f' {label}: SU({n}) gamma={gm}: beta_eff={bW} ratio={ratio} (~{float(ratio):.0f}x)')
# R1-E02 bookkeeping
import mpmath as mp
mp.mp.dps = 30
for n in (2,3):
    b0 = mp.mpf(11)*n/(3*(4*mp.pi)**2)
    slope = 1/(4*n*b0*mp.log(2))
    step = 2*b0*mp.log(2)
    print(f'SU({n}) b0={mp.nstr(b0,10)}  dk*/dbeta (1-loop,b=2)={mp.nstr(slope,8)}  d(1/g^2) per b=2 step={mp.nstr(step,8)}')
    for gm in (mp.mpf('0.1'), mp.mpf('0.05')):
        win1 = (1/gm)/step
        lo = gm/(1+step*gm)
        mgam = mp.e**(-1/(2*b0*gm))
        # 1-loop steps from gamma to the physical crossover (Wilson SU(2) beta_W ~ 2.3 -> g^2 = 2N/2.3), heuristic
        gc = 2*n/mp.mpf('2.3') if n == 2 else None
        steps_to_cross = ((1/gm - 1/gc)/step) if gc else None
        print(f'  gamma={gm}: 1-loop steps to pole={mp.nstr(win1,6)}; last-controlled coupling >= {mp.nstr(lo,8)} '
              f'(rel {mp.nstr(1-lo/gm,4)}); heuristic m_gamma ~ exp(-1/(2 b0 gamma)) = {mp.nstr(mgam,4)}'
              + (f'; 1-loop steps gamma -> g^2={mp.nstr(gc,4)} (beta_W=2.3): {mp.nstr(steps_to_cross,6)}' if gc else ''))
