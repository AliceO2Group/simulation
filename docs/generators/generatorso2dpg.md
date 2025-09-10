---
sort: 2
title: Generators implemented in O2DPG
---

# Generators implemented in O2DPG

This table provides an overview of all available Monte Carlo generator configurations (`.ini` files) in the O2DPG framework. Each configuration specifies the generator setup for different physics processes, collision systems, and experimental conditions. More detailed info are contained in the `.C` macros inside the `.ini` configurations.

**Current Generator Types:**
- **Pythia8**: Pythia8 event generator (includes standard and custom implementations)
- **HepMC**: Generators using HepMC interface (e.g., EPOS4)
- **Starlight**: Starlight generator for photon-induced processes
- **Custom**: Standalone custom generator implementations (with macro filename)
- **Cocktail**: Multiple particle species with specified ratios using `GeneratorCocktail.C`
- **Gen1 + Gen2 + ...**: Combination of multiple generators

| Custom configuration | Description | Main Folder | Generators Used |
| :--- | :--- | :--- | :--- |
| basic.ini | Basic generator configuration. | common | Pythia8 |
| GeneratorLoopersFlatGas.ini | TPC loopers with flat gas distribution using WGAN neural network models for pair and Compton electron generation. | common | Custom (`TPCLoopers.C`) |
| GeneratorTPCloopers.ini | TPC loopers with Poisson-distributed pairs and Gaussian-distributed Compton electrons using WGAN neural network models. | common | Custom (`TPCLoopers.C`) |
| GeneratorTPCloopers_fixNPairs.ini | TPC loopers generator with a fixed number of pairs and Compton electrons using neural network models. | common | Custom (`TPCLoopers.C`) |
| pythia8_NeNe_536.ini | Pythia8 for NeNe collisions at 5.36 TeV. | common | Pythia8 |
| pythia8_OO_536.ini | Pythia8 for OO collisions at 5.36 TeV. | common | Pythia8 |
| pythia8_pO_961.ini | Pythia8 for pO collisions at 9.61 TeV. | common | Pythia8 |
| GeneratorHF_bbbar_PsiAndJpsi_fwdy_triggerGap.ini | bb̅, Psi and J/psi at forward rapidity with trigger gap. | PWGDQ | Pythia8 |
| GeneratorHF_bbbar_PsiAndJpsi_midy_triggerGap.ini | bb̅, Psi and J/psi at mid-rapidity with trigger gap. | PWGDQ | Pythia8 |
| GeneratorHF_bbbar_PsiToJpsi_midy_triggerGap.ini | bb̅, Psi to J/psi at mid-rapidity with trigger gap. | PWGDQ | Pythia8 |
| GeneratorHF_bbbarToBplus_midy_triggerGap.ini | bb̅ to B+ at mid-rapidity with trigger gap. | PWGDQ | Pythia8 |
| GeneratorHF_bbbarToDDbarToMuons_fwdy_TriggerGap.ini | bb̅ to DD̅ to muons at forward rapidity with trigger gap. | PWGDQ | Pythia8 |
| GeneratorHF_bbbarToDDbarToMuons_fwdy_TriggerGap_inel.ini | bb̅ to DD̅ to muons at forward rapidity with trigger gap (inelastic). | PWGDQ | Pythia8 |
| GeneratorHF_bbbarToDDbarToMuons_fwdy_TriggerGap_natural.ini | bb̅ to DD̅ to muons at forward rapidity with trigger gap (natural). | PWGDQ | Pythia8 |
| GeneratorHF_bbbarToDDbarToMuons_fwdy_TriggerGap_natural_inel.ini | bb̅ to DD̅ to muons at forward rapidity with trigger gap (natural, inelastic). | PWGDQ | Pythia8 |
| GeneratorHF_ccbarToMuonsSemileptonic_fwdy_inel_TriggerGap.ini | cc̅ to semileptonic muons at forward rapidity with trigger gap (inelastic). | PWGDQ | Pythia8 |
| GeneratorHF_ccbarToMuonsSemileptonic_fwdy_inel_TriggerGap_natural.ini | cc̅ to semileptonic muons at forward rapidity with trigger gap (natural, inelastic). | PWGDQ | Pythia8 |
| GeneratorHF_JPsiToMuons_fwdy.ini | J/psi to muons at forward rapidity. | PWGDQ | Pythia8 |
| GeneratorJPsiHFCorr_ccbar.ini | J/psi-HF correlations with cc̅. | PWGDQ | Pythia8 |
| Generator_InjectedBottomoniaFwdy_TriggerGap.ini | Injected bottomonia at forward rapidity with trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedChiCToElectronMidy_TriggerGap.ini | Injected chi_c to electron at mid-rapidity with trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedInclusiveJpsiMidy_Pythia8_TriggerGap.ini | Injected inclusive J/psi at mid-rapidity with Pythia8 and trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedInclusiveJpsiPsi2SMidy_Pythia8_TriggerGap.ini | Injected inclusive J/psi and Psi(2S) at mid-rapidity with Pythia8 and trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedPromptCharmoniaFwdy_TriggerGap.ini | Injected prompt charmonia at forward rapidity with trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedPromptCharmoniaFwdy_TriggerGap_OO5TeV.ini | Injected prompt charmonia at forward rapidity with trigger gap in OO at 5TeV. | PWGDQ | Pythia8 |
| Generator_InjectedPromptCharmoniaFwdy_TriggerGap_PbPb5TeV.ini | Injected prompt charmonia at forward rapidity with trigger gap in PbPb at 5TeV. | PWGDQ | Pythia8 |
| Generator_InjectedPromptCharmoniaFwdy_TriggerGap_pp5TeV.ini | Injected prompt charmonia at forward rapidity with trigger gap in pp at 5TeV. | PWGDQ | Pythia8 |
| Generator_InjectedPromptCharmoniaMidy_TriggerGap.ini | Injected prompt charmonia at mid-rapidity with trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedPromptCharmoniaMidy_TriggerGap_OO5TeV.ini | Injected prompt charmonia at mid-rapidity with trigger gap in OO at 5TeV. | PWGDQ | Pythia8 |
| Generator_InjectedPromptJpsiFwdy_PythiaOnia_TriggerGap.ini | Gap-triggered J/psi production at forward rapidity using Pythia8 heavy quarkonia processes combined with minimum bias events. | PWGDQ | Pythia8 |
| Generator_InjectedPromptJpsiFwdy_PythiaOnia_TriggerGap_pp5TeV.ini | Gap-triggered J/psi production at forward rapidity in pp at 5 TeV using Pythia8 heavy quarkonia processes combined with minimum bias events. | PWGDQ | Pythia8 |
| Generator_InjectedPromptJpsiFwdy_TriggerGap.ini | Injected prompt J/psi at forward rapidity with trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedPromptJpsiMidy_PythiaOnia_TriggerGap.ini | Injected prompt J/psi at mid-rapidity with Pythia heavy quarkonia and trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedPromptJpsiPsi2SFwdy_Pythia8_TriggerGap.ini | Injected prompt J/psi and Psi(2S) at forward rapidity with Pythia8 and trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedPromptJpsiPsi2SFwdy_Pythia8_TriggerGap_pp5TeV.ini | Injected prompt J/psi and Psi(2S) at forward rapidity with Pythia8 and trigger gap in pp at 5TeV. | PWGDQ | Pythia8 |
| Generator_InjectedPromptPsi2SFwdy_TriggerGap.ini | Injected prompt Psi(2S) at forward rapidity with trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedPromptPsi2SToJpsiPiPiMidy_TriggerGap.ini | Injected prompt Psi(2S) to J/psi pi pi at mid-rapidity with trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedPromptX3782andPsi2SMidy_TriggerGap.ini | Injected prompt X(3782) and Psi(2S) at mid-rapidity with trigger gap. | PWGDQ | Pythia8 |
| Generator_InjectedPromptX3782Midy_TriggerGap.ini | Injected prompt X(3782) at mid-rapidity with trigger gap. | PWGDQ | Pythia8 |
| configOmegaAnd20Pions_randomCharge.ini | Omega and 20 pions with random charge. | PWGHF | Pythia8 |
| GeneratorHF_D2H_bbbar_Bforced_gap5_Mode2.ini | D2H with bb̅, B forced, gap 5, mode 2. | PWGHF | Pythia8 |
| GeneratorHF_D2H_bbbar_BtoDK_gap5_Mode2.ini | D2H with bb̅, B to DK, gap 5, mode 2. | PWGHF | Pythia8 |
| GeneratorHF_D2H_bbbar_gap5.ini | D2H with bb̅, gap 5. | PWGHF | Pythia8 |
| GeneratorHF_D2H_bbbar_Mode2_OmegaC.ini | D2H with bb̅, mode 2, Omega_c. | PWGHF | Pythia8 |
| GeneratorHF_D2H_bbbar_Mode2_OmegaC_NoDecay.ini | D2H with bb̅, mode 2, Omega_c without decay. | PWGHF | Pythia8 |
| GeneratorHF_D2H_bbbar_Mode2_OmegaC_NoDecay_pp_ref.ini | D2H with bb̅, mode 2, Omega_c without decay in pp. | PWGHF | Pythia8 |
| GeneratorHF_D2H_bbbar_Mode2_XiC0_XiCplus.ini | D2H with bb̅, mode 2, Xi_c0 and Xi_c+. | PWGHF | Pythia8 |
| GeneratorHF_D2H_bbbar_Mode2_XiC_NoDecay.ini | D2H with bb̅, mode 2, Xi_c without decay. | PWGHF | Pythia8 |
| GeneratorHF_D2H_bbbar_Mode2_XiC_NoDecay_pp_ref.ini | D2H with bb̅, mode 2, Xi_c without decay in pp. | PWGHF | Pythia8 |
| GeneratorHF_D2H_bbbar_Mode2_XiCplus_NoDecay.ini | D2H with bb̅, mode 2, Xi_c+ without decay. | PWGHF | Pythia8 |
| GeneratorHF_D2H_bbbar_Mode2_XiCplus_NoDecay_pp_ref.ini | D2H with bb̅, mode 2, Xi_c+ without decay in pp. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap3.ini | D2H with cc̅ and bb̅, gap 3. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap3_Mode2.ini | D2H with cc̅ and bb̅, gap 3, mode 2. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap3_Mode2_XiC.ini | D2H with cc̅ and bb̅, gap 3, mode 2, Xi_c. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap5.ini | D2H study with cc̅ and bb̅ production using gap-triggered events (gap size 5 units in η). | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap5_DReso.ini | D2H with cc̅ and bb̅, gap 5, D resonance. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap5_DResoTrigger.ini | D2H with cc̅ and bb̅, gap 5, D resonance trigger. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap5_Mode2.ini | D2H study with cc̅ and bb̅ production, gap-triggered mode 2 with heavy flavor injection. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap5_Mode2_CharmBaryons.ini | D2H with cc̅ and bb̅, gap 5, mode 2, charm baryons. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap5_Mode2_CharmBaryons_pp_ref.ini | D2H with cc̅ and bb̅, gap 5, mode 2, charm baryons in pp. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap5_Mode2_corrBkg.ini | D2H with cc̅ and bb̅, gap 5, mode 2, correlated background. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap5_Mode2_corrBkgSigmaC.ini | D2H with cc̅ and bb̅, gap 5, mode 2, correlated background with Sigma_c. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap5_Mode2_pp_ref.ini | D2H with cc̅ and bb̅, gap 5, mode 2 in pp. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap5_Mode2_XiC.ini | D2H with cc̅ and bb̅, gap 5, mode 2, Xi_c. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap5_Mode2_XiC_OmegaC.ini | D2H with cc̅ and bb̅, gap 5, mode 2, Xi_c and Omega_c. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap8.ini | D2H study with cc̅ and bb̅ production using gap-triggered events (gap size 8 units in η). | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_gap8_Mode2_XiC.ini | D2H with cc̅ and bb̅, gap 8, mode 2, Xi_c. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_Mode2_ptHardBins.ini | D2H with cc̅ and bb̅, mode 2, pT hard bins. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_PbPb.ini | D2H with cc̅ and bb̅ in PbPb. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_PbPb_corrBkg.ini | D2H with cc̅ and bb̅ in PbPb with correlated background. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_and_bbbar_PbPb_ptHardBins.ini | D2H with cc̅ and bb̅ in PbPb with pT hard bins. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_gap5.ini | D2H with cc̅, gap 5. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_Mode2_OmegaC.ini | D2H with cc̅, mode 2, Omega_c. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_Mode2_OmegaC_NoDecay_pp_ref.ini | D2H with cc̅, mode 2, Omega_c without decay in pp. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_Mode2_OmegaC_to_Omega.ini | D2H with cc̅, mode 2, Omega_c to Omega. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_Mode2_XiC0_XiCplus.ini | D2H with cc̅, mode 2, Xi_c0 and Xi_c+. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_Mode2_XiC_NoDecay.ini | D2H with cc̅, mode 2, Xi_c without decay. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_Mode2_XiC_NoDecay_pp_ref.ini | D2H with cc̅, mode 2, Xi_c without decay in pp. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_Mode2_XiCplus_NoDecay.ini | D2H with cc̅, mode 2, Xi_c+ without decay. | PWGHF | Pythia8 |
| GeneratorHF_D2H_ccbar_Mode2_XiCplus_NoDecay_pp_ref.ini | D2H with cc̅, mode 2, Xi_c+ without decay in pp. | PWGHF | Pythia8 |
| GeneratorHF_HFe_ccbar_and_bbar_gap5_Mode2.ini | HF electrons from cc̅ and bb̅, gap 5, mode 2. | PWGHF | Pythia8 |
| GeneratorHF_mu_bbbar_gap3_Mode2_accSmall.ini | Muons from bb̅, gap 3, mode 2, small acceptance. | PWGHF | Pythia8 |
| GeneratorHF_mu_bbbar_gap5_Mode2_accInt_muTrig.ini | Muons from bb̅, gap 5, mode 2, intermediate acceptance, muon trigger. | PWGHF | Pythia8 |
| GeneratorHF_mu_bbbar_gap5_Mode2_accLarge.ini | Muons from bb̅, gap 5, mode 2, large acceptance. | PWGHF | Pythia8 |
| GeneratorHF_mu_bbbar_gap5_Mode2_accLarge_muTrig.ini | Muons from bb̅, gap 5, mode 2, large acceptance, muon trigger. | PWGHF | Pythia8 |
| GeneratorHF_mu_bbbar_gap5_Mode2_accSmall.ini | Muons from bb̅, gap 5, mode 2, small acceptance. | PWGHF | Pythia8 |
| GeneratorHF_mu_ccbar_gap3_Mode2_accSmall.ini | Muons from cc̅, gap 3, mode 2, small acceptance. | PWGHF | Pythia8 |
| GeneratorHF_mu_ccbar_gap5_Mode2_accInt_muTrig.ini | Muons from cc̅, gap 5, mode 2, intermediate acceptance, muon trigger. | PWGHF | Pythia8 |
| GeneratorHF_mu_ccbar_gap5_Mode2_accLarge.ini | Muons from cc̅, gap 5, mode 2, large acceptance. | PWGHF | Pythia8 |
| GeneratorHF_mu_ccbar_gap5_Mode2_accLarge_muTrig.ini | Muons from cc̅, gap 5, mode 2, large acceptance, muon trigger. | PWGHF | Pythia8 |
| GeneratorHF_mu_ccbar_gap5_Mode2_accSmall.ini | Muons from cc̅, gap 5, mode 2, small acceptance. | PWGHF | Pythia8 |
| GeneratorHFOmegaCEmb.ini | Omega_c particles generated using box generator embedded in Pythia8 background events. | PWGHF | Box + Pythia8 |
| GeneratorHFOmegaCToXiPiEmb.ini | Omega_c to Xi pi decay channels generated using box generator embedded in Pythia8 background events. | PWGHF | Box + Pythia8 |
| GeneratorHFTrigger_bbbar.ini | Gap-triggered beauty quark production (gap size 3) with enhanced bb̅ pair generation in rapidity range -5 to 5. | PWGHF | Pythia8 |
| GeneratorHFTrigger_Bforced.ini | Trigger for B meson forced decays with enhanced heavy flavor production. | PWGHF | Pythia8 |
| GeneratorHFTrigger_ccbar.ini | Gap-triggered charm quark production (gap size 3) with enhanced cc̅ pair generation in rapidity range -5 to 5. | PWGHF | Pythia8 |
| GeneratorHFTrigger_LambdaBToNuclei.ini | Gap-triggered Lambda_b baryon production with decays to light nuclei for hypernuclei studies. | PWGHF | Pythia8 |
| GeneratorHFTrigger_OmegaCToXiPi.ini | Gap-triggered Omega_c baryon production with forced decay to Xiπ channel for charm baryon studies. | PWGHF | Pythia8 |
| GeneratorHFTrigger_XiCToXiPi.ini | Gap-triggered Xi_c baryon production (PDG 4132) with forced decay to Xiπ channel in mid-rapidity. | PWGHF | Pythia8 |
| GeneratorHFTrigger_Xi_Omega_C.ini | Gap-triggered charm baryon production targeting both Xi_c and Omega_c baryons for baryon spectroscopy. | PWGHF | Pythia8 |
| GeneratorHFXiCToXiPiEmb.ini | Xi_c to Xi pi decay channels generated using box generator embedded in Pythia8 background events. | PWGHF | Box + Pythia8 |
| trigger_hf.ini | Trigger for heavy flavor. | PWGHF | Pythia8 |
| GeneratorEMCocktail.ini | Electromagnetic cocktail with multiple meson species (π⁰, η, ρ, ω, φ, η') for dielectron studies. | PWGEM | Cocktail |
| GeneratorEMCocktail_Run3pp.ini | Electromagnetic cocktail optimized for Run 3 pp collisions with updated meson ratios. | PWGEM | Cocktail |
| GeneratorEMCocktail_Run3pp_lowBeta.ini | Electromagnetic cocktail for Run 3 pp with low β particles and specific detector acceptance. | PWGEM | Cocktail |
| GeneratorEMCocktail_Run3pp_v2.ini | Electromagnetic cocktail for Run 3 pp (version 2) with updated parametrizations. | PWGEM | Cocktail |
| GeneratorEMCocktailwithFlow3040.ini | Electromagnetic cocktail with elliptic flow v₂ for centrality 30-40% in heavy-ion collisions. | PWGEM | Cocktail |
| GeneratorEMCocktailwithFlow4050.ini | Electromagnetic cocktail with elliptic flow v₂ for centrality 40-50% in heavy-ion collisions. | PWGEM | Cocktail |
| GeneratorHF_bbbarToDDbarToDielectrons.ini | bb̅ to DD̅ to dielectrons. | PWGEM | Pythia8 |
| GeneratorHF_bbbarToDielectrons.ini | bb̅ to dielectrons. | PWGEM | Pythia8 |
| GeneratorHF_ccbarToDielectrons.ini | cc̅ to dielectrons. | PWGEM | Pythia8 |
| GeneratorHFFull_bbbarToDDbarToDielectrons.ini | Full bb̅ to DD̅ to dielectrons. | PWGEM | Pythia8 |
| GeneratorHFFull_bbbarToDielectrons.ini | Full bb̅ to dielectrons. | PWGEM | Pythia8 |
| GeneratorHFFull_ccbarToDielectrons.ini | Full cc̅ to dielectrons. | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_BeautyForcedDecay_Gap3.ini | Beauty with forced decay and gap trigger (Gap 3). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_BeautyForcedDecay_Gap4.ini | Beauty with forced decay and gap trigger (Gap 4). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_BeautyForcedDecay_Gap5.ini | Beauty with forced decay and gap trigger (Gap 5). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_BeautyForcedDecay_Gap6.ini | Beauty with forced decay and gap trigger (Gap 6). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_BeautyForcedDecay_Gap7.ini | Beauty with forced decay and gap trigger (Gap 7). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_BeautyNoForcedDecay_Gap3.ini | Beauty without forced decay and gap trigger (Gap 3). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_BeautyNoForcedDecay_Gap4.ini | Beauty without forced decay and gap trigger (Gap 4). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_BeautyNoForcedDecay_Gap5.ini | Beauty without forced decay and gap trigger (Gap 5). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_BeautyNoForcedDecay_Gap6.ini | Beauty without forced decay and gap trigger (Gap 6). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_BeautyNoForcedDecay_Gap7.ini | Beauty without forced decay and gap trigger (Gap 7). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_Charm_Gap3.ini | Charm with gap trigger (Gap 3). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_Charm_Gap4.ini | Charm with gap trigger (Gap 4). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_Charm_Gap5.ini | Charm with gap trigger (Gap 5). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_Charm_Gap6.ini | Charm with gap trigger (Gap 6). | PWGEM | Pythia8 |
| GeneratorHFGapTriggered_Charm_Gap7.ini | Charm with gap trigger (Gap 7). | PWGEM | Pythia8 |
| GeneratorLFCocktailPbPb.ini | Light-flavor meson cocktail (π⁰, η', ρ, ω, φ, η) with randomized species selection for PbPb dielectron background studies. | PWGEM | Cocktail |
| GeneratorLFCocktailpp.ini | Light-flavor meson cocktail (π⁰, η', ρ, ω, φ, η) with randomized species selection for pp dielectron background studies. | PWGEM | Cocktail |
| Generator_GapTriggered_LFee.ini | Light-flavor dielectron with gap trigger. | PWGEM | Pythia8 |
| Generator_GapTriggered_LFee_all_np1_gap3.ini | Light-flavor dielectron with gap trigger (all, np1, gap3). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFee_all_np1_gap5.ini | Light-flavor dielectron with gap trigger (all, np1, gap5). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFee_all_np1_gap8.ini | Light-flavor dielectron with gap trigger (all, np1, gap8). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFee_all_np1_gap10.ini | Light-flavor dielectron with gap trigger (all, np1, gap10). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFee_random_np1_gap0.ini | Light-flavor dielectron with random gap (np1, gap0). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFee_random_np1_gap2.ini | Light-flavor dielectron with random gap (np1, gap2). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFee_random_np1_gap4.ini | Light-flavor dielectron with random gap (np1, gap4). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFee_random_np1_gap6.ini | Light-flavor dielectron with random gap (np1, gap6). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFee_random_np3_gap0.ini | Light-flavor dielectron with random gap (np3, gap0). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFee_random_np5_gap0.ini | Light-flavor dielectron with random gap (np5, gap0). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFgamma.ini | Light-flavor gamma with gap trigger. | PWGEM | Pythia8 |
| Generator_GapTriggered_LFgamma_np1_gap2.ini | Light-flavor gamma with gap trigger (np1, gap2). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFgamma_np1_gap4.ini | Light-flavor gamma with gap trigger (np1, gap4). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFgamma_np1_gap6.ini | Light-flavor gamma with gap trigger (np1, gap6). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFgamma_np3_gap5.ini | Light-flavor gamma with gap trigger (np3, gap5). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFgamma_np5_gap5.ini | Light-flavor gamma with gap trigger (np5, gap5). | PWGEM | Pythia8 |
| Generator_GapTriggered_LFmumu.ini | Light-flavor dimuon with gap trigger. | PWGEM | Pythia8 |
| Pythia8_Beauty_Cocktail.ini | Pythia8 beauty cocktail. | PWGEM | Pythia8 |
| Pythia8_Beauty_Cocktail_pp13.ini | Pythia8 beauty cocktail for pp at 13 TeV. | PWGEM | Pythia8 |
| Pythia8_Beauty_Cocktail_pp502.ini | Pythia8 beauty cocktail for pp at 5.02 TeV. | PWGEM | Pythia8 |
| Pythia8_Beauty_Cocktail_pp536.ini | Pythia8 beauty cocktail for pp at 5.36 TeV. | PWGEM | Pythia8 |
| Pythia8_Charm_Cocktail.ini | Pythia8 charm cocktail. | PWGEM | Pythia8 |
| Pythia8_Charm_Cocktail_pp13.ini | Pythia8 charm cocktail for pp at 13 TeV. | PWGEM | Pythia8 |
| Pythia8_Charm_Cocktail_pp502.ini | Pythia8 charm cocktail for pp at 5.02 TeV. | PWGEM | Pythia8 |
| Pythia8_Charm_Cocktail_pp536.ini | Pythia8 charm cocktail for pp at 5.36 TeV. | PWGEM | Pythia8 |
| GeneratorHFJETrigger_ccbar.ini | HF JE trigger for cc̅. | PWGGAJE | Pythia8 |
| GeneratorJE_gapgen2_hook_pp5360GeV.ini | JE gap generator 2 hook for pp at 5.36 TeV. | PWGGAJE | Pythia8 |
| GeneratorJE_gapgen5_hook.ini | JE gap generator 5 hook. | PWGGAJE | Pythia8 |
| GeneratorPythia8POWHEG_beauty.ini | POWHEG NLO beauty quark production interfaced with Pythia8 parton shower and hadronization. | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_beauty_F05.ini | POWHEG beauty with factorization scale factor F=0.5 (μ_F = 0.5 * μ_0). | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_beauty_F05_R05.ini | POWHEG beauty with factorization scale F=0.5 and renormalization scale R=0.5. | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_beauty_F2.ini | POWHEG beauty with factorization scale factor F=2 (μ_F = 2 * μ_0). | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_beauty_F2_R2.ini | POWHEG beauty with factorization scale F=2 and renormalization scale R=2. | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_beauty_MHigh.ini | POWHEG beauty with high invariant mass cuts for b quark pair production. | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_beauty_MLow.ini | POWHEG beauty with low invariant mass cuts for b quark pair production. | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_beauty_R05.ini | POWHEG beauty with renormalization scale factor R=0.5 (μ_R = 0.5 * μ_0). | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_beauty_R2.ini | POWHEG beauty with renormalization scale factor R=2 (μ_R = 2 * μ_0). | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_charm.ini | POWHEG NLO charm quark production interfaced with Pythia8 parton shower and hadronization. | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_charm_F05.ini | POWHEG charm with factorization scale factor F=0.5 (μ_F = 0.5 * μ_0). | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_charm_F05_R05.ini | POWHEG charm with factorization scale F=0.5 and renormalization scale R=0.5. | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_charm_F2.ini | POWHEG charm with factorization scale factor F=2 (μ_F = 2 * μ_0). | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_charm_F2_R2.ini | POWHEG charm with factorization scale F=2 and renormalization scale R=2. | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_charm_MHigh.ini | POWHEG charm with high invariant mass cuts for c quark pair production. | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_charm_MLow.ini | POWHEG charm with low invariant mass cuts for c quark pair production. | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_charm_R05.ini | POWHEG charm with renormalization scale factor R=0.5 (μ_R = 0.5 * μ_0). | PWGGAJE | Pythia8 + POWHEG |
| GeneratorPythia8POWHEG_charm_R2.ini | POWHEG charm with renormalization scale factor R=2 (μ_R = 2 * μ_0). | PWGGAJE | Pythia8 + POWHEG |
| hook_jets.ini | Hook for jets. | PWGGAJE | Pythia8 |
| hook_prompt_gamma.ini | Hook for prompt gamma. | PWGGAJE | Pythia8 |
| hook_prompt_gamma_allcalo.ini | Hook for prompt gamma in all calorimeters. | PWGGAJE | Pythia8 |
| hook_prompt_gamma_focal.ini | Hook for prompt gamma in FOCAL. | PWGGAJE | Pythia8 |
| trigger_decay_gamma.ini | Trigger for decay gamma. | PWGGAJE | Pythia8 |
| trigger_decay_gamma_allcalo_TrigPt3_5.ini | Trigger for decay gamma in all calorimeters with Pt > 3.5. | PWGGAJE | Pythia8 |
| trigger_decay_gamma_allcalo_TrigPt7.ini | Trigger for decay gamma in all calorimeters with Pt > 7. | PWGGAJE | Pythia8 |
| trigger_decay_gamma_TrigPt3_5.ini | Trigger for decay gamma with Pt > 3.5. | PWGGAJE | Pythia8 |
| trigger_decay_gamma_TrigPt7.ini | Trigger for decay gamma with Pt > 7. | PWGGAJE | Pythia8 |
| trigger_prompt_gamma.ini | Trigger for prompt gamma. | PWGGAJE | Pythia8 |
| trigger_prompt_gamma_allcalo.ini | Trigger for prompt gamma in all calorimeters. | PWGGAJE | Pythia8 |
| trigger_prompt_gamma_focal.ini | Trigger for prompt gamma in FOCAL. | PWGGAJE | Pythia8 |
| GeneratorLF_antid_and_highpt.ini | Antideuteron and high pT particles. | PWGLF | Pythia8 |
| GeneratorLF_Coalescence.ini | Light flavor production with nucleon coalescence model for (anti)deuteron formation. | PWGLF | Pythia8 |
| GeneratorLF_deuteron_wigner.ini | Deuteron with Wigner function. | PWGLF | Pythia8 |
| GeneratorLF_ExoticResonances_pp1360.ini | Exotic resonances in pp at 13.6 TeV. | PWGLF | Pythia8 |
| GeneratorLF_HighPt.ini | High-pT triggered events requiring antiprotons (PDG -2212) and leading particles with pT > 5.0 GeV in \|η\| < 0.8. | PWGLF | Pythia8 |
| GeneratorLF_highpt_strangeness.ini | High-pT triggered events (pT > 5.0 GeV) containing strange hadrons (K⁰, Λ, Ξ, Ω) randomly selected for strangeness studies. | PWGLF | Pythia8 |
| GeneratorLF_pp1360_wDeCoal.ini | pp at 13.6 TeV with deuteron coalescence. | PWGLF | Pythia8 |
| GeneratorLF_pp1360_wDeInel.ini | pp at 13.6 TeV with deuteron inelastic. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_PbPb.ini | Resonances in PbPb. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_PbPb_exotic.ini | Exotic resonances in PbPb. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_PbPb5360_injection.ini | Resonances in PbPb at 5.36 TeV with injection. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_PbPb5360_trigger.ini | Resonances in PbPb at 5.36 TeV with trigger. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_pp.ini | Resonances in pp. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_pp900.ini | Resonances in pp at 900 GeV. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_pp900_injection.ini | Resonances in pp at 900 GeV with injection. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_pp900_trigger.ini | Resonances in pp at 900 GeV with trigger. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_pp1360.ini | Resonances in pp at 13.6 TeV. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_pp1360_injection.ini | Resonances in pp at 13.6 TeV with injection. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_pp1360_trigger.ini | Resonances in pp at 13.6 TeV with trigger. | PWGLF | Pythia8 |
| GeneratorLF_Resonances_pp_exotic.ini | Exotic resonances in pp. | PWGLF | Pythia8 |
| GeneratorLF_Strangeness_OO5360_injection.ini | Strangeness in OO at 5.36 TeV with injection. | PWGLF | Pythia8 |
| GeneratorLF_Strangeness_PbPb5360_injection.ini | Strangeness in PbPb at 5.36 TeV with injection. | PWGLF | Pythia8 |
| GeneratorLF_SyntheFlow.ini | Synthetic flow generator for light flavor particles with parameterized collective flow. | PWGLF | Pythia8 |
| GeneratorLF_SyntheFlowXi.ini | Synthetic flow generator specialized for Ξ baryons with collective flow effects. | PWGLF | Pythia8 |
| GeneratorLFDeTrHe.ini | Deuteron, triton, helium generator. | PWGLF | Pythia8 |
| GeneratorLFExoticNucleiPbPb.ini | Exotic nuclei in PbPb. | PWGLF | Pythia8 |
| GeneratorLFHyperNucleiPbPbGap.ini | Hypernuclei in PbPb with gap. | PWGLF | Pythia8 |
| GeneratorLFHyperNucleiPbPbGapWithFlow.ini | Hypernuclei in PbPb with gap and flow. | PWGLF | Pythia8 |
| GeneratorLFHyperNucleippGap.ini | Hypernuclei in pp with gap. | PWGLF | Pythia8 |
| GeneratorLFHyperNucleippGapXSection.ini | Hypernuclei in pp with gap and cross-section. | PWGLF | Pythia8 |
| GeneratorLFHyperppGap.ini | Hyper in pp with gap. | PWGLF | Pythia8 |
| GeneratorLFHypertritonPbPbGap.ini | Hypertriton in PbPb with gap. | PWGLF | Pythia8 |
| GeneratorLFHypertritonppGap.ini | Hypertriton in pp with gap. | PWGLF | Pythia8 |
| GeneratorLFLambdapp.ini | Lambda baryon injection generator (PDG 3122) with 10 particles injected per event for strange baryon studies in pp collisions. | PWGLF | Pythia8 |
| GeneratorLFNucleiFwdppGap.ini | Nuclei forward in pp with gap. | PWGLF | Pythia8 |
| GeneratorLFNucleiPbPbInHMPIDAcceptance.ini | Nuclei in PbPb in HMPID acceptance. | PWGLF | Pythia8 |
| GeneratorLFNucleippInHMPIDAcceptance.ini | Nuclei in pp in HMPID acceptance. | PWGLF | Pythia8 |
| GeneratorLFOmegaEmb.ini | Omega particles generated using box generator embedded in Pythia8 background events. | PWGLF | Box + Pythia8 |
| GeneratorLFSigmaPiResonances.ini | Sigma pi resonances. | PWGLF | Pythia8 |
| GeneratorLFSigmapp.ini | Sigma± baryon injection generator producing both Sigma⁻ (PDG 3112) and Sigma+ (PDG 3222) particles with 5 injected per event in pT range 1-9 GeV. | PWGLF | Pythia8 |
| GeneratorLFStrangeness.ini | Strange baryon injection generator producing Omega⁻ and Xi⁻ baryons (PDG 3334, 3312) with their antiparticles using gun mechanism. | PWGLF | Pythia8 |
| GeneratorLFStrangenessTriggered.ini | Strangeness triggered generator. | PWGLF | Pythia8 |
| GeneratorLFStrangenessTriggered_900gev.ini | Strangeness triggered generator at 900 GeV. | PWGLF | Pythia8 |
| GeneratorLFStrangenessTriggered_gap2.ini | Strangeness triggered generator with gap 2. | PWGLF | Pythia8 |
| GeneratorLFStrangenessTriggered_gap3.ini | Strangeness triggered generator with gap 3. | PWGLF | Pythia8 |
| GeneratorLFStrangenessTriggered_gap5.ini | Strangeness triggered generator with gap 5. | PWGLF | Pythia8 |
| GeneratorLFXipp.ini | Xi⁻ baryon injection generator (PDG 3312) with 10 particles injected per event for cascade baryon studies in pp collisions. | PWGLF | Pythia8 |
| pythia8_ArAr.ini | Pythia8 for ArAr collisions. | ALICE3 | Pythia8 |
| pythia8_KrKr.ini | Pythia8 for KrKr collisions. | ALICE3 | Pythia8 |
| pythia8_OO.ini | Pythia8 for OO collisions. | ALICE3 | Pythia8 |
| pythia8_PbPb.ini | Pythia8 for PbPb collisions. | ALICE3 | Pythia8 |
| pythia8_PbPb_536tev.ini | Pythia8 for PbPb at 5.36 TeV. | ALICE3 | Pythia8 |
| pythia8_PbPb_D0toKpi.ini | Pythia8 for PbPb with D0 to Kpi. | ALICE3 | Pythia8 |
| pythia8_pp.ini | Pythia8 for pp collisions. | ALICE3 | Pythia8 |
| pythia8_pp_7tev.ini | Pythia8 for pp at 7 TeV. | ALICE3 | Pythia8 |
| pythia8_pp_13tev.ini | Pythia8 for pp at 13 TeV. | ALICE3 | Pythia8 |
| pythia8_pp_136tev.ini | Pythia8 for pp at 13.6 TeV. | ALICE3 | Pythia8 |
| pythia8_pp_502tev.ini | Pythia8 for pp at 5.02 TeV. | ALICE3 | Pythia8 |
| pythia8_pp_536tev.ini | Pythia8 for pp at 5.36 TeV. | ALICE3 | Pythia8 |
| pythia8_pp_cr_136tev.ini | Pythia8 with color reconnection for pp at 13.6 TeV. | ALICE3 | Pythia8 |
| pythia8_pp_hardQCD_136tev.ini | Pythia8 with hard QCD processes enhanced for high-pT studies in pp at 13.6 TeV. | ALICE3 | Pythia8 |
| pythia8_pp_hf_hardQCD_136tev.ini | Pythia8 with hard QCD processes focusing on heavy flavor production in pp at 13.6 TeV. | ALICE3 | Pythia8 |
| pythia8_pp_ropes.ini | Pythia8 with rope hadronization model for enhanced collective effects in pp collisions. | ALICE3 | Pythia8 |
| pythia8_pp_ropes_13tev.ini | Pythia8 with rope hadronization model for pp collisions at 13 TeV. | ALICE3 | Pythia8 |
| pythia8_pp_ropes_136tev.ini | Pythia8 with rope hadronization model for pp collisions at 13.6 TeV. | ALICE3 | Pythia8 |
| pythia8_pp_shoving.ini | Pythia8 with QCD-based shoving model for parton interactions in pp collisions. | ALICE3 | Pythia8 |
| pythia8_pp_shoving_13tev.ini | Pythia8 with QCD-based shoving model for pp collisions at 13 TeV. | ALICE3 | Pythia8 |
| pythia8_pp_shoving_136tev.ini | Pythia8 with QCD-based shoving model for pp collisions at 13.6 TeV. | ALICE3 | Pythia8 |
| pythia8_XeXe.ini | Pythia8 for XeXe collisions. | ALICE3 | Pythia8 |
| xi_PbPb.ini | Xi⁻ baryon (PDG 3312) gun generator embedded in PbPb collision background for ALICE3 detector studies. | ALICE3 | Pythia8 |
| xi_pp.ini | Xi⁻ baryon (PDG 3312) gun generator embedded in pp collision background for ALICE3 detector studies. | ALICE3 | Pythia8 |
| xicc_background_PbPb.ini | Doubly charmed baryon Xi_cc background events in PbPb collisions for ALICE3 studies. | ALICE3 | Pythia8 |
| xicc_PbPb.ini | Doubly charmed baryon Xi_cc++ (PDG 4422) gun generator embedded in PbPb collision background for ALICE3 detector studies. | ALICE3 | Pythia8 |
| xicc_pp.ini | Doubly charmed baryon Xi_cc++ (PDG 4422) gun generator embedded in pp collision background for ALICE3 detector studies. | ALICE3 | Pythia8 |
| xic_PbPb.ini | Charmed baryon Xi_c+ (PDG 4232) gun generator embedded in PbPb collision background for ALICE3 detector studies. | ALICE3 | Pythia8 |
| xic_pp.ini | Charmed baryon Xi_c+ (PDG 4232) gun generator embedded in pp collision background for ALICE3 detector studies. | ALICE3 | Pythia8 |
| GenStarlight_kCohJpsiToMu_PbPb_5360_Muon.ini | Starlight generator for coherent J/psi → μ⁺μ⁻ photoproduction in PbPb at 5.36 TeV with muon acceptance cuts. | PWGUD | Starlight |
| GenStarlight_kCohPsi2sToElPi_PbPb_5360_Cent.ini | Starlight generator for coherent psi(2S) → e⁺e⁻π⁺π⁻ photoproduction in central PbPb at 5.36 TeV. | PWGUD | Starlight |
| adaptive_pythia8.ini | Adaptive Pythia8 configuration. | examples | Pythia8 |
| GeneratorEPOS4.ini | EPOS4 hadronic event generator using HepMC interface with core-corona model. | examples | HepMC |
| GeneratorEPOS4HQ.ini | EPOS4 generator with enhanced heavy quark production and transport. | examples | HepMC |
| GeneratorEPOS4_pp13TeV.ini | EPOS4 generator optimized for pp collisions at 13 TeV center-of-mass energy. | examples | HepMC |
| trigger_mpi.ini | Trigger generator for multi-parton interaction (MPI) studies with event selection. | examples | Pythia8 |
| trigger_multiplicity.ini | Trigger generator with charged particle multiplicity-based event selection. | examples | Pythia8 |
| trigger_multiplicity_stableparticles_inFIT.ini | Trigger generator for stable particle multiplicity in Forward Interaction Trigger (FIT) acceptance. | examples | Pythia8 |