<!--
title: Independently claimed solution record: nye-2025-ijt-quantum-information
id: QL-20261121-01/T5/nye-2025-ijt-quantum-information
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: QUASAR
date: 2026-11-21
version: v1
status: first-pass register entry
internal-source: WitnessLab/04_CANDIDATE_SOLUTIONS/independently_claimed_solutions/nye-2025-ijt-quantum-information.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# Nye 2025: "Existence and Mass Gap in Quantum Yang–Mills Theory" (Int. J. Topology)

Classification: **CLAIMED, UNCONDITIONAL (as self-described). First pass: DEFECTIVE. Deep review PENDING.** This is not a proof, and nothing in this lab treats it as one.

## Identity
- Author: Logan Nye (School of Computer Science, Carnegie Mellon University), per the article page.
- Venue: International Journal of Topology 2(1), article 2. Published 2025-02-25. DOI 10.3390/ijt2010002 (Crossref-verified; register S-020).
- Access: curl got 403 (bot block, not circumvented). The public article page was then read with WebFetch and archived at `03_LITERATURE_AND_SOURCE_ARCHIVE/candidate_solutions/claimed/nye_mdpi_ijt2010002_webfetch.txt`, sha256 0b734cc5…dc76.
- The archive is **truncated at the start of §6 (The Mass Gap)**. §6 onwards has not been opened.

## Main claim (verbatim, abstract)
> "Our method provides a concrete realization of the Yang–Mills theory that is manifestly gauge-invariant and satisfies the Wightman axioms. We demonstrate the existence of a mass gap by analyzing the entanglement spectrum of the vacuum state…"

End of §5 (verbatim):
> "This provides a definitive resolution to the existence aspect of the Yang–Mills existence and mass gap problem."

## Conditional or unconditional
The author presents it as unconditional. On first pass there is no explicit list of hypotheses.

## First-pass defects (from the opened text only)
1. **The problem is misstated (§1.1).** The paper's quoted "official" statement includes "excluding massless particles mandated by gauge symmetry". No such clause exists in Jaffe–Witten (see `00_GOVERNANCE/official_problem_statement.md`). The official problem requires a gap in the whole spectrum of H above the vacuum.
2. **The mass gap is assumed at the bridge step (Thm 10 proof, eq. (36)).** The text asserts constants C_n and m > 0, "independent of the lattice spacing a", with |G^R_a(x_1…x_n)| ≤ C_n ∏ e^{−m|x_i−x_j|}, justified only by "Using cluster expansion techniques and reflection positivity [10]". This is exactly the uniform bridge PO-12/PO-13, the open core of the problem, stated without a proof.
   - No known cluster expansion gives this at weak coupling as a → 0.
3. **eq. (36) contradicts expected short-distance behaviour.** A bound that stays finite as x_i → x_j is incompatible with the singular short-distance behaviour of renormalized correlators of composite fields such as Tr F², which the paper itself invokes through asymptotic freedom.
4. **Claims for all groups at once.** Thm 10 asserts the result "for all compact simple gauge groups", with constants "depending only on the dimension of the group". No group-dependent estimates are shown.
5. A secondary critique (blog omarora.in; not archived and not relied on) alleges circular area-law and vacuum-uniqueness arguments. That cannot be checked here because §6 is not archived. **PENDING.**

## Pending
§6 (mass gap via entanglement Hamiltonian) needs a full read and a line-by-line check of eqs. (36)–(38) and Thms 10–14.
