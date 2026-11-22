<!--
title: LATTICE record: R1-P1-02_reconstruction.md
id: QL-20261121-01/07/independent_derivations/R1-P1-02_reconstruction.md
authors: Witness Labs, Agentic Swarm, 0ait
contributing-agent: LATTICE (independent validator), Witness Labs, Agentic Swarm, 0ait
date: 2026-11-21
version: as committed in internal f5ccacd
status: LATTICE record, published v0.2.0 part 2
internal-source: reviews/QL-20261121-01/R1-P1/02_reconstruction.md
body: verbatim copy of the internal record (only this header comment was added)
x-witness-labs-attribution: "Witness Labs, Agentic Swarm, 0ait" | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | metadata watermark, not tamper-proof
-->
# LATTICE reconstruction — QL-20261121-01 / R1-P1 (hand derivations; written after 01_formulation.md)
Knowledge labels per Part IV.5. "Proved (LATTICE, by hand)" = pen-and-paper check by LATTICE; nothing here is Lean-checked.

## R1. Corner anchoring is not the θ-obstruction; the contour family and averaging rule are (Proved, LATTICE, by hand; Computationally verified finite result, code/theta_intertwine.py, code/theta_2d_reproduce.py)
Setting: link reflection θ: t ↦ −1−t, plane on block boundaries (blocks {Ln,…,Ln+L−1} in time), corner anchor y_Y = min corner of block Y. Contours Γ_{y,x} are axis-ordered staircases with the **time axis first**. Coarse link V(Y,Y+e_μ) = Π( Σ_{x∈B(Y)} U(Γ_{y,x}) U(x→x+Le_μ) U(Γ_{y+Le_μ, x+Le_μ})^{-1} ), with Π bi-equivariant: Π(gXh) = gΠ(X)h for g,h ∈ G (true for Π = normalised quaternion sum on SU(2), and for the polar/unitary projection on SU(N)).
Claim: B(θU) = h·(θ′B(U)) with h a coarse gauge transformation depending on U; hence F′∘B∘θ = F′∘θ′∘B for every gauge-invariant coarse F′.
Proof sketch. θ maps the min-time corner y of B(Y) to the max-time corner θy of θB(Y) (same spatial coordinates ȳ). θΓ_{y,x} = [time segment θy → (−1−t_x, ȳ)] ∘ [the reflected spatial staircase at time −1−t_x]. The time-first contour of the reflected block from its own corner y′ = (−L−t₀, ȳ) to θx is [time segment y′ → (−1−t_x, ȳ)] ∘ [same spatial staircase]. Both run on the same time line at ȳ, so as group elements U(θΓ_{y,x}) = U(θy → y′) · U(Γ_{y′,θx}) exactly (back-tracking cancels). The prefix g_Y := U(θy→y′) does not depend on x. Same for the other endpoint block (suffix g_{Y′}^{-1}); for temporal coarse links the two blocks swap roles and the term is inverted, which Π also respects (Π(X^{-1}-family) = Π(X-family)^{-1} for the quaternion projection since conjugation is linear). Bi-equivariance of Π moves g_Y, g_{Y′} outside the sum. ∎
Consequences:
- Space-first contours (QUASAR's E03b corner pattern) do not have the x-independent prefix property ⇒ genuine gauge-invariant mismatch (reproduced: ½Tr coarse plaquette differences 7.0e−3/2.4e−3, 7.7e−2/6.8e−2, 0.74/0.68 at σ = 0.05, 0.15, 0.3, two trials each; QUASAR: 6.8e−3, 1.0e−1, 0.60).
- Time-first contours: ≤ 5.6e−16 (2D, QUASAR geometry), ≤ 4.7e−15 on plaquettes and 2×1 loops (4D, 8⁴, L=2), all field strengths including Haar.
- A reference-dependent log average (Balaban-style exp-mean-log relative to one term) is not bi-equivariant in this sense when the reference term changes under θ ⇒ fails even with time-first contours (corner: 2e−10, 4e−6, 2.6e−2 at ε = 1e−3, 1e−2, 0.1 on Tr plaquettes, 4D). With the centre anchor and the *straight central transport* as reference it passes (≤ 3e−15), so "symmetric contours are not enough" is true only for a non-symmetric choice of reference.
- Raw link-by-link comparison is gauge-variant: the corner map shows raw mismatch ≈ 7ε (7.0e−3 at ε = 1e−3) even when every gauge-invariant quantity agrees to 1e−15. QUASAR's E03 correctly compares gauge-invariant data; this is recorded as a procedure warning, not a defect.
- Only θ (one reflection direction) is needed by D08.3. Time-first ordering breaks spatial reflections and hypercubic symmetry; the centre/odd-L map keeps all of them.

## R2. Lemma A and (M) (Proved, LATTICE, by hand — the implication; (M) is the content)
Lemma A as stated is immediate from X itself: X for a family containing F′ asserts exponential decay of ⟨θF̄′; τ′_n F′⟩_{μ′}, which is literally the fine correlation of F′∘B. (M) negates exactly this. D08.3 is not needed. For the stated conclusion "no block map B" (∀B), (M) must be stated for every admissible B (∀B ∃F′ ∈ 𝒮′_B), which is a block-map-dependent statement about coarse observables. That is not what FS82 gives.
What FS82 gives (secondary source, see review §G): Villain U(1)₄, β ≥ β₁ (unquantified): a translation-invariant state (subsequential limit of translation averages of free-b.c. cube states) in which the **fine** field-strength two-point function is not absolutely summable.
Bridge to coarse observables (Proved, LATTICE, by hand, conditional): if 𝒮′ is cyclic for the gauge-invariant local sector (required anyway at step S9), X ⇒ (D08.3) a gap on the whole local sector ⇒ exponential decay of the fine field-strength correlation ⇒ summable — contradiction with FS82, **provided** the states coincide (periodic torus limits in X vs FS82's free-b.c. translation-averaged state) and γ ≤ 1/β₁(FS82). Without cyclicity, a gap on 𝒦_β alone does not contradict FS82.

## R3. Prop. 1 (X ⇔ U|𝒦) (Proved, LATTICE, by hand, with conditions)
(⇒) D08.3 / D08.1: A = (T/λ₀) ≥ 0 (Lüscher), diagonal decay ⟨ψ, A^{nb^k−s}ψ⟩ ≤ C e^{−m_* n} ⇒ ‖A|_{𝒦_ψ}‖ ≤ e^{−m_*/b^k}; the spectral projection argument passes to the closed span of the union over F′ (E_A((r,1]) kills every generator, hence the closure). With b^k a(β) < b a_*: rate per fine step ≥ m_* a(β)/(b a_*). (⇐) ⟨Qψ, A^{nb^k−s} Qψ⟩ ≤ ‖Qψ‖² e^{−Δa(β)(nb^k−s)} ≤ ‖F′‖²_∞ e^{Δ a(β) s} e^{−Δ a_* n}; a(β)s ≲ b a_* so the prefactor is bounded.
Conditions: (c1) the vector representation ⟨Qψ, A^m Qψ⟩ needs infinite time extent (or L_t → ∞ before n → ∞); on a periodic torus the correlation is a thermal trace; (c2) Lemma 1's (i)–(iii) — intertwining modulo coarse gauge transformations suffices on gauge-invariant 𝒮′ (R1); (c3) constants C(F′,β) may depend on β; (c4) the statement concerns 𝒦_β, not the full sector (cyclicity O1 unchanged); (c5) m_* = Δa_* holds up to the factor b from the window b^k a(β) ∈ [a_*, b a_*).

## R4. "H-Gap at least as hard as the fixed-β gap" (Proved, LATTICE, by hand: direction and conditions)
Two reductions, both in the direction H ⇒ fixed-β:
(a) Unconditional on membership: H-Bal ∧ H-Gap ⇒ X ⇒ (D08.3 at each fixed β) m(T|𝒦_β) ≥ Δ a(β) > 0, uniformly in L, for every β ≥ β₀. So H-Bal ∧ H-Gap imply exponential clustering of the coarse family at every fixed large β — an open statement (special case of Chatterjee 2018 Problem 5.1, which asks for a gap at every β > 0; the coarse-sector version is weaker than Problem 5.1 as stated for plaquettes but is itself not proved at any large β).
(b) QUASAR's version: if the Wilson action at β_γ = 2N/γ lies in 𝒜_γ (Heuristic, unverified), H-Gap alone ⇒ clustering of 𝒮′ for Wilson SU(N) at that single β, uniformly in L. Open.
No converse: a fixed-β gap (even for all β) does not give the β-uniform rate m_γ over a class.

## R5. Threshold conversion (Established from opened source + exact arithmetic, code/conversions_check.py)
SZZ arXiv:2204.12737v1 (opened, local copy in the lab archive): density ∝ exp(Nβ Σ_{p∈P⁺} Re Tr Q_p), P⁺ = one orientation per plaquette; SU(N): |β| < 1/(16(d−1)) (eq. (1.3)). Wilson exp(−β_W Σ(1 − (1/N)Re tr U_p)) ⇒ β_W/N = Nβ ⇒ β_W = N²β. d=4: β_W < N²/48: SU(2) 1/12 (g² > 48), SU(3) 3/16 (g² > 32). QUASAR's conversion is correct.
RG side: R1-E02's docstring uses (2/g²)Σ Re Tr(1−V) (β_W = 2N/g² ⇒ 40 at γ = 0.1); R1-D04 §2 writes (1/g²)Σ Re Tr(1−V) (⇒ β_W = N/g² = 20, ratio 240×). Balaban's normalisation was not checked by either agent. γ is Balaban's unquantified "sufficiently small" constant, so γ = 0.1 is illustrative: the ratio grows as 1/γ.
