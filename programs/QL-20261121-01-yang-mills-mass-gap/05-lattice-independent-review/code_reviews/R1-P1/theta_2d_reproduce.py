# © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. Contributing-agent: LATTICE (independent validator). Internal source: f5ccacd. Metadata watermark, not tamper-proof.
"""LATTICE: rerun my own implementation (theta_intertwine.py) in QUASAR's E03b geometry: 2D 12x12, blocks 3x3,
link reflection t->-1-t, corner anchor; and centre anchor (L=3, site reflection t->-t; my convention).
Contour order (1,0)=space-first (QUASAR's corner pattern) vs (0,1)=time-first. Reports max |1/2 Tr| differences
of coarse plaquettes (QUASAR's metric) over 2 trials per sigma, independent RNG stream."""
import numpy as np, json
import theta_intertwine as T
T.D = 2
out = []
for order in ([1,0],[0,1]):
    T.ORDER[:] = order
    for kind in ['corner','centre']:
        for avg in ['proj','logref']:
            for sigma in [0.05,0.15,0.3]:
                vals=[]
                for trial in range(2):
                    r = T.compare(12, 3, kind, avg, sigma)
                    vals.append(r['plaq_trace_max']/2)   # 1/2 Tr
                cov = T.gauge_covariance_check(12,3,kind,avg,sigma)
                row = dict(order=order, kind=kind, avg=avg, sigma=sigma, half_tr_plaq_maxdiff=vals, gauge_cov=cov)
                out.append(row); print(row, flush=True)
json.dump(out, open('theta_2d_reproduce_results.json','w'), indent=1)
