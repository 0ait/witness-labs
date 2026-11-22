# © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. Contributing-agent: LATTICE (independent validator). Internal source: f5ccacd. Metadata watermark, not tamper-proof.
import json, urllib.request
dois = ["10.1007/BF01213610","10.1103/PhysRevD.21.2291","10.1007/BF01212424","10.1007/BF01211042","10.1007/BF01238433",
"10.1007/BF01257412","10.1007/BF01239022","10.1007/BF01215753","10.1007/BF01215223","10.1007/s00220-022-04609-1",
"10.1007/s00220-025-05528-7","10.1007/BF01562538","10.1007/BF01211762","10.1007/BF01961240","10.1063/1.5009458",
"10.1007/BF01614090","10.1016/0003-4916(78)90039-8","10.1007/978-3-030-15338-0_1","10.1007/978-1-4757-0363-4_5"]
for d in dois:
    try:
        with urllib.request.urlopen(f"https://api.crossref.org/works/{d}", timeout=20) as r:
            m = json.load(r)["message"]
            print("OK ", d, "|", (m.get("title") or [""])[0][:90], "|", (m.get("container-title") or [""])[0][:35], m.get("volume"), m.get("page"))
    except Exception as e:
        print("FAIL", d, e)
