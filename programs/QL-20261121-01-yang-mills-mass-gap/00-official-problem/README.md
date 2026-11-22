<!--
title: Official problem statement (writeup)
id: QL-20261121-01/00
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v0.1.0
status: published v0.1.0
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# The official problem

## Statement (short verbatim quotation)
> **Yang–Mills Existence and Mass Gap.** Prove that for any compact simple gauge group G, a non-trivial quantum Yang–Mills theory exists on R⁴ and has a mass gap ∆ > 0. Existence includes establishing axiomatic properties at least as strong as those cited in [45, 35].

— A. Jaffe and E. Witten, *Quantum Yang–Mills Theory*, official problem description, Clay Mathematics Institute, §4 "The Problem", p. 6. <https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf>

References [45] and [35] are Streater–Wightman, *PCT, Spin and Statistics and All That* (1964), and Osterwalder–Schrader, *Axioms for Euclidean Green's functions*, Comm. Math. Phys. 31 (1973) 83–112 (doi:10.1007/BF01645738) and 42 (1975) 281–305 (doi:10.1007/BF01608978).

Definition of the mass gap (same page, short quotation):
> A quantum field theory has a mass gap ∆ if H has no spectrum in the interval (0, ∆) for some ∆ > 0. The supremum of such ∆ is the mass m, and we require m < ∞.

Footnote 2 (p. 12), which constrains what counts as existence:
> We specifically exclude weak-existence (compactness) as the solution to the existence part of the Millennium problem, unless one also uses other techniques to establish properties of the limit (such as the existence of a mass gap and the axioms).

## Our reading (summary; full formalization in `../01-formalization/`)
- The theory must have local quantum fields corresponding to gauge-invariant local polynomials in the curvature (e.g. Tr F∧F-type fields), whose short-distance behaviour matches asymptotic freedom and perturbative renormalization, including a stress tensor and an operator product expansion (p. 6).
- Axioms: Wightman, or Osterwalder–Schrader with reconstruction; a unique Poincaré-invariant vacuum; positive energy.
- The description itself names the central obstacles: a gap uniform in the volume, and the infinite-volume limit (pp. 6, 7, 12).
- The Clay web page (<https://www.claymath.org/millennium/yang-mills-the-maths-gap/>) labelled the problem **"Unsolved"** when retrieved on 2026-11-21 17:32 CT.

## Source integrity
| Source | URL | sha256 (as downloaded 2026-11-21 17:32 CT) |
|---|---|---|
| S-001 Jaffe–Witten PDF (14 pp., PDF CreationDate 2006-08-04) | https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf | `3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09` |
| S-002 Clay web page (HTML, changes over time) | https://www.claymath.org/millennium/yang-mills-the-maths-gap/ | `fba5695b4ae07fee796613917174302a51d87425257038c2646d35c0e0734b12` |

The PDF, the web page and our full per-page text extractions are kept in the internal archive and **not redistributed**. Quotations come from `pdftotext` output checked page by page; only line-break hyphenation was rejoined.

**Citation note.** The description cites [36] as "Gauge theories on the lattice", Ann. Phys. 110 (1978) 440–471 (Osterwalder–Seiler); Crossref gives the title "Gauge field theories on a lattice", doi:10.1016/0003-4916(78)90039-8. We cite the Crossref form.

---
<sub>© 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. · Provenance: [`.witness-labs/manifest.json`](/.witness-labs/manifest.json)</sub>
