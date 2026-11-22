import Challenge
open YangMills
#print axioms YangMills.JointExistence
#print axioms YangMills.jointExistence
#check @YangMills.JointExistence
#print YangMills.JointExistence
#print YangMills.GaugeGroup.IsSimple
#print YangMills.WightmanTheory.W0
-- independent probe: the public target contains no spectral-gap clause; state what a gap clause would be
def HasMassGap {H : HilbertSpace} {L : FieldLabels} (T : WightmanTheory H L) : Prop :=
  ∃ Δ : ℝ, 0 < Δ ∧ T.energyMomentum.projection {p : Spacetime | 0 < time p ∧ time p < Δ} = 0
#check @HasMassGap
