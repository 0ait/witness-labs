#!/usr/bin/env python3
# Witness Labs, Agentic Swarm, 0ait | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | contributing agent: QUASAR | x-witness-labs-attribution
"""Summarise R1-E01 outputs: per (group,L) table, combined hot/cold means, max finite-difference slope dP/dbeta,
max chi_P, max |hot-cold| in sigma units. Numerical evidence only."""
import json, glob, numpy as np
rows = []
for f in ["outputs/u1_L6.json", "outputs/u1_L8.json", "outputs/su2_L6.json", "outputs/su2_L8.json"]:
    d = json.load(open(f)); res = d["results"]; betas = sorted(set(r["beta"] for r in res))
    print(f"\n== {d['group']} L={d['L']}  (ntherm={d['ntherm']}, nmeas={d['nmeas']}, script {d['script_sha256'][:12]}, cpu {d['total_cpu_s']:.0f}s)")
    print(" beta    P_hot           P_cold          chiP_hot   chiP_cold  creutz22(hot/cold)   |hot-cold|/sigma")
    Pm = []; chimax = 0; hc = 0
    for b in betas:
        h = [r for r in res if r["beta"] == b and r["start"] == "hot"][0]; c = [r for r in res if r["beta"] == b and r["start"] == "cold"][0]
        z = abs(h["P"]-c["P"])/np.hypot(h["dP"], c["dP"]); hc = max(hc, z)
        Pm.append((h["P"]+c["P"])/2); chimax = max(chimax, h["chiP"], c["chiP"])
        print(f" {b:5.3f}  {h['P']:.5f}({h['dP']:.5f}) {c['P']:.5f}({c['dP']:.5f})  {h['chiP']:7.3f}  {c['chiP']:7.3f}   {h['creutz22']:.3f}/{c['creutz22']:.3f}   {z:.2f}")
    sl = [(Pm[i+1]-Pm[i])/(betas[i+1]-betas[i]) for i in range(len(betas)-1)]
    i = int(np.argmax(sl))
    print(f" max dP/dbeta = {sl[i]:.3f} on [{betas[i]}, {betas[i+1]}];  max chiP = {chimax:.3f};  max |hot-cold|/sigma = {hc:.2f}")
    rows.append(dict(group=d["group"], L=d["L"], max_slope=sl[i], slope_interval=[betas[i], betas[i+1]], max_chiP=chimax, max_hot_cold_sigma=hc))
json.dump(rows, open("outputs/summary.json", "w"), indent=1)
