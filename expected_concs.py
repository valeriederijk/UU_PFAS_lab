# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 16:00:32 2025

@author: 6346650
"""
expected_concs_EIS = {
    'D7-NMeFOSE': 25, 'D9-NEtFOSE': 25, '13C4-PFBA': 10, '13C3-HFPO-DA': 10,
    '13C5-PFPeA': 5, '13C2-4:2FTS': 5, '13C2-6:2FTS': 5, '13C2-8:2FTS': 5,
    'D3-NMeFOSAA': 5, 'D5-NEtFOSAA': 5, '13C5-PFHxA': 2.5, '13C4-PFHpA': 2.5,
    '13C8-PFOA': 2.5, '13C3-PFBS': 2.5, '13C3-PFHxS': 2.5, '13C8-PFOS': 2.5,
    '13C8-PFOSA': 2.5, 'D3-NMeFOSA': 2.5, 'D5-NEtFOSA': 2.5, '13C9-PFNA': 1.25,
    '13C6-PFDA': 1.25,'13C7-PFUnA': 1.25, '13C2-PFDoA': 1.25, '13C2-PFTeDA': 1.25
}
expected_target_conc_1 = [0.8, 2, 5, 10, 20, 50, 250]
expected_target_conc_2 = [2, 5, 12.5, 25, 50, 125, 625]
expected_target_conc_3 = [0.2, 0.5, 1.25, 2.5, 5, 12.5, 62.5]

expected_concs_target_analytes = {
    'PFBA': expected_target_conc_1, '4:2 FTS': expected_target_conc_1,
    '6:2 FTS': expected_target_conc_1, '8:2 FTS': expected_target_conc_1,
    'HFPO-DA': expected_target_conc_1, 'ADONA': expected_target_conc_1,
    '11Cl-PF3OUdS': expected_target_conc_1, '9Cl-PF3ONS': expected_target_conc_1,
    'PFPeA': [0.4, 1, 2.5, 5, 10, 25, 125],
    'NMeFOSE': expected_target_conc_2, 'NEtFOSE': expected_target_conc_2,
    'PFHxA': expected_target_conc_3, 'PFHpA': expected_target_conc_3,
    'PFOA': expected_target_conc_3, 'PFNA': expected_target_conc_3,
    'PFDA': expected_target_conc_3, 'PFUnA': expected_target_conc_3,
    'PFDoA': expected_target_conc_3, 'PFTrDA': expected_target_conc_3,
    'PFTeDA': expected_target_conc_3, 'PFBS': expected_target_conc_3,
    'PFPeS': expected_target_conc_3, 'PFHxS': expected_target_conc_3,
    'PFHpS': expected_target_conc_3, 'PFOS': expected_target_conc_3,
    'PFOSA': expected_target_conc_3, 'NMeFOSA': expected_target_conc_3,
    'NEtFOSA': expected_target_conc_3, 'NMeFOSAA': expected_target_conc_3,
    'NEtFOSAA': expected_target_conc_3, 'PFNS': expected_target_conc_3,
    'PFDS': expected_target_conc_3
}
