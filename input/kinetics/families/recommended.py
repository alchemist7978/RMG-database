# This file contains a dictionary of kinetics families.  The families
# set to `True` are recommended by RMG and turned on by default by setting
# kineticsFamilies = 'default' in the RMG input file. Families set to `False` 
# are not turned on by default because the family is severely lacking in data.
# These families should only be turned on with caution.

recommendedFamilies = {
'1+2_Cycloaddition':True,
'1,2-Birad_to_alkene':True,
'1,2_Insertion_CO':True,
'1,2_Insertion_carbene':True,
'1,2_shiftS':True,
'1,3_Insertion_CO2':True,
'1,3_Insertion_ROR':True,
'1,3_Insertion_RSR':True,
'1,4_Cyclic_birad_scission':True,
'1,4_Linear_birad_scission':True,
'2+2_cycloaddition_CCO':True,
'2+2_cycloaddition_CO':True,
'2+2_cycloaddition_Cd':True,
'Birad_recombination':True,
'CO_Disproportionation':True,
'Birad_R_Recombination':True,
'Cyclic_Ether_Formation':True,
'Diels_alder_addition':True,
'Disproportionation':True,
'HO2_Elimination_from_PeroxyRadical':True,
'H_Abstraction':True,
'Intra_Retro_Diels_alder_bicyclic':True,
'Intra_Disproportionation':True,
'Intra_RH_Add_Endocyclic':False,
'Intra_RH_Add_Exocyclic':False,
'Intra_R_Add_Endocyclic':True,
'Intra_R_Add_ExoTetCyclic':False,
'Intra_R_Add_Exocyclic':True,
'Korcek_step1':False,
'Korcek_step2':False,
'R_Addition_COm':True,
'R_Addition_CSm':False,
'R_Addition_MultipleBond':True,
'R_Recombination':True,
'SubstitutionS':False,
'Substitution_O':False,
'intra_H_migration':True,
'intra_NO2_ONO_conversion':True,
'intra_OH_migration':True,
'intra_substitutionCS_cyclization':True,
'intra_substitutionCS_isomerization':True,
'intra_substitutionS_cyclization':True,
'intra_substitutionS_isomerization':True,
'ketoenol':True,
'lone_electron_pair_bond':False,
'Singlet_Carbene_Intra_Disproportionation':True,
'Intra_5_membered_conjugated_C=C_C=C_addition':True,
'Intra_Diels_alder_monocyclic':True,
'Concerted_Intra_Diels_alder_monocyclic_1,2_shiftH':True,
'Intra_2+2_cycloaddition_Cd':True,
'Intra_ene_reaction':True,
'Cyclopentadiene_scission':True,
'6_membered_central_C-C_shift':True
}
