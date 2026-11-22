#!/usr/bin/env python3
# Witness Labs, Agentic Swarm, 0ait | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | contributing agent: QUASAR | x-witness-labs-attribution
"""INV001-E02b: Z2 ladder at weaker coupling (J/h = 8, 16): local vs torelon sector gaps vs n.
Reuses ladder_spectrum from e02_ks_hamiltonian.py (import without re-running Part A/B: functions copied)."""
import importlib.util, json, sys, types
src = open('e02_ks_hamiltonian.py').read()
cut = src.index('A = []')
ns = {}
exec(src[:cut], ns)              # imports + Part A defs
cutB0 = src.index('def ladder_links'); cutB1 = src.index('checks = []')
exec(src[cutB0:cutB1], ns)       # Part B defs only
res = []
for J in [8.0, 16.0]:
    for n in [4,6,8,10,12,14,16]:
        r = ns['ladder_spectrum'](n, 1.0, J); res.append(r)
        print('J=%4.1f n=%2d local=%.6f torelon=%.8f full=%.8f' % (J, n, r['local_gap'], r['torelon_gap'], r['full_gap']), flush=True)
json.dump(res, open('outputs/e02b_results.json','w'), indent=1, default=float)
