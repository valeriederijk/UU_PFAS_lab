# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 10:31:37 2025

@author: 6346650
"""
import pandas as pd

EIS_NIS_compound_recovery_aqueous = pd.DataFrame({
    'compound': [
        '13C4-PFBA',
        '13C5-PFPeA', 
        '13C5-PFHxA',
        '13C4-PFHpA',
        '13C8-PFOA',
        '13C9-PFNA',
        '13C6-PFDA',
        '13C7-PFUnA',
        '13C2-PFDoA',
        '13C2-PFTeDA',
        '13C3-PFBS',
        '13C3-PFHxS',
        '13C8-PFOS',
        '13C2-4:2FTS',
        '13C2-6:2FTS',
        '13C2-8:2FTS',
        '13C8-PFOSA',
        'D3-NMeFOSA',
        'D5-NEtFOSA',
        'D3-NMeFOSAA',
        'D5-NEtFOSAA',
        'D7-NMeFOSE',
        'D9-NEtFOSE',
        '13C3-HFPO_DA',
        '13C3-PFBA',
        '13C2-PFHxA',
        '13C4-PFOA',
        '13C5-PFNA', 
        '13C2-PFDA',
        '18O2-PFHxS',
        '13C4-PFOS'
    ],
    'compound_type': [
        'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS',
        'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS', 'EIS',
        'NIS', 'NIS', 'NIS', 'NIS', 'NIS', 'NIS', 'NIS'
    ],
    'lower_recovery_percent': [
        5, 40, 40, 40, 40, 40, 40, 30, 10, 10, 40, 40, 40, 40, 40, 40, 40, 10, 10, 40, 25, 10, 10, 40, 50,
        50, 50, 50, 50, 50, 50
    ],
    'upper_recovery_percent': [
        130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 135, 130, 130, 200, 200, 300, 130, 130, 130, 170, 135, 130, 130,
        130, 200, 200, 200, 200, 200, 200, 200
    ]
})


IPR_recovery_rsd_solid = pd.DataFrame({
    'compound': [
        'PFBA',
        'PFPeA',
        'PFHxA',
        'PFHpA',
        'PFOA',
        'PFNA',
        'PFDA',
        'PFUnA',
        'PFDoA',
        'PFTrDA',
        'PFTeDA',
        'PFBS',
        'PFPeS',
        'PFHxS',
        'PFHpS',
        'PFOS',
        'PFNS',
        'PFDS',
        'PFDOS',
        '4:2FTS',
        '6:2FTS',
        '8:2FTS',
        'PFOSA',
        'NMeFOSA',
        'NEtFOSA',
        'NMeFOSAA',
        'NEtFOSAA',
        'NMeFOSE',
        'NEtFOSE',
        'HFPO-DA',
        'ADONA',
        'PFMPA',
        'PFMBA',
        '9ClPF3ONS',
        '9Cl-PF3ONS',
        '11Cl-PF3OUdS',
        'PFEESA',
        '3:3FTCA',
        '5:3FTCA',
        '7:3FTCA'
    ],
    'lower_recovery_percent': [
        70, 70, 70, 70, 70, 65, 70, 70, 70, 35, 70, 60, 65, 65, 70, 70, 70, 50, 40, 
        70, 60, 70, 70, 65, 70, 65, 60, 70, 70, 70, 70, 70, 55, 45, 65, 30, 70, 45, 70, 70
    ],
    'upper_recovery_percent': [
        140, 140, 135, 140, 140, 145, 145, 145, 145, 160, 145, 145, 140, 145, 140, 135, 
        140, 150, 140, 135, 160, 140, 140, 145, 135, 145, 150, 140, 135, 140, 155, 140, 
        145, 145, 135, 135, 140, 155, 135, 145
    ],
    'rsd_percent': [
        17, 26, 23, 21, 23, 24, 28, 26, 25, 26, 24, 25, 29, 28, 27, 27, 27, 31, 40, 27, 
        50, 27, 19, 26, 19, 31, 31, 19, 17, 25, 26, 33, 33, 27, 23, 31, 20, 32, 28, 39
    ]
})


OPR_recovery_solid = pd.DataFrame({
    'compound': [
        'PFBA',
        'PFPeA',
        'PFHxA',
        'PFHpA',
        'PFOA',
        'PFNA',
        'PFDA',
        'PFUnA',
        'PFDoA',
        'PFTrDA',
        'PFTeDA',
        'PFBS',
        'PFPeS',
        'PFHxS',
        'PFHpS',
        'PFOS',
        'PFNS',
        'PFDS',
        'PFDOS',
        '4:2FTS',
        '6:2FTS',
        '8:2FTS',
        'PFOSA',
        'NMeFOSA',
        'NEtFOSA',
        'NMeFOSAA',
        'NEtFOSAA',
        'NMeFOSE',
        'NEtFOSE',
        'HFPO-DA',
        'ADONA',
        'PFMPA',
        'PFMBA',
        '9ClPF3ONS',
        '9Cl-PF3ONS',
        '11Cl-PF3OUdS',
        'PFEESA',
        '3:3FTCA',
        '5:3FTCA',
        '7:3FTCA'
    ],
    
    'lower_recovery_percent': [
        70, 60, 65, 65, 70, 70, 70, 70, 70, 35, 65, 65, 55, 60, 65, 65, 35, 40, 25, 
        60, 55, 70, 70, 70, 70, 65, 65, 70, 70, 70, 70, 70, 60, 60, 70, 45, 70, 45, 60, 60
    ],
    'upper_recovery_percent': [
        140, 150, 140, 145, 150, 155, 155, 155, 150, 160, 150, 145, 160, 150, 155, 160, 
        160, 155, 160, 150, 200, 150, 140, 155, 140, 155, 165, 140, 135, 145, 160, 140, 
        150, 155, 150, 160, 140, 150, 130, 150
    ],
    
 })

IPR_recovery_rsd_aqueous =pd.DataFrame({
    'compound': [
        'PFBA',
        'PFPeA',
        'PFHxA',
        'PFHpA',
        'PFOA',
        'PFNA',
        'PFDA',
        'PFUnA',
        'PFDoA',
        'PFTrDA',
        'PFTeDA',
        'PFBS',
        'PFPeS',
        'PFHxS',
        'PFHpS',
        'PFOS',
        'PFNS',
        'PFDS',
        'PFDOS',
        '4:2FTS',
        '6:2FTS',
        '8:2FTS',
        'PFOSA',
        'NMeFOSA',
        'NEtFOSA',
        'NMeFOSAA',
        'NEtFOSAA',
        'NMeFOSE',
        'NEtFOSE',
        'HFPO-DA',
        'ADONA',
        'PFMPA',
        'PFMBA',
        '9ClPF3ONS',
        '9Cl-PF3ONS',
        '11Cl-PF3OUdS',
        'PFEESA',
        '3:3FTCA',
        '5:3FTCA',
        '7:3FTCA'
    ],
    'lower_recovery_percent': [
        70, 70, 70, 70, 65, 70, 65, 70, 70, 60, 70, 70, 70, 70, 70, 70, 70, 70, 45, 
        70, 70, 70, 70, 70, 70, 65, 70, 70, 70, 70, 70, 60, 65, 65, 70, 50, 70, 70, 70, 55
    ],
    'upper_recovery_percent': [
        135, 135, 135, 135, 155, 140, 140, 135, 130, 145, 145, 140, 135, 135, 140, 140, 
        135, 135, 135, 135, 135, 140, 135, 135, 130, 140, 135, 135, 130, 135, 135, 140, 
        145, 140, 145, 150, 135, 130, 130, 130
    ],
    'rsd_percent': [
        21, 23, 24, 28, 27, 28, 26, 29, 21, 29, 27, 23, 25, 27, 30, 29, 29, 30, 35, 27, 
        32, 33, 22, 30, 26, 32, 28, 29, 21, 23, 23, 23, 27, 37, 30, 35, 25, 23, 24, 34
    ]
})

OPR_recovery_aqueous = pd.DataFrame({
    'compound': [
        'PFBA',
        'PFPeA',
        'PFHxA',
        'PFHpA',
        'PFOA',
        'PFNA',
        'PFDA',
        'PFUnA',
        'PFDoA',
        'PFTrDA',
        'PFTeDA',
        'PFBS',
        'PFPeS',
        'PFHxS',
        'PFHpS',
        'PFOS',
        'PFNS',
        'PFDS',
        'PFDOS',
        '4:2FTS',
        '6:2FTS',
        '8:2FTS',
        'PFOSA',
        'NMeFOSA',
        'NEtFOSA',
        'NMeFOSAA',
        'NEtFOSAA',
        'NMeFOSE',
        'NEtFOSE',
        'HFPO-DA',
        'ADONA',
        'PFMPA',
        'PFMBA',
        '9ClPF3ONS',
        '9Cl-PF3ONS',
        '11Cl-PF3OUdS',
        'PFEESA',
        '3:3FTCA',
        '5:3FTCA',
        '7:3FTCA'
    ],
    
    'lower_recovery_percent': [
        70, 65, 70, 70, 70, 70, 70, 65, 70, 65, 60, 60, 65, 65, 70, 55, 65, 60, 50, 
        70, 65, 60, 70, 60, 65, 50, 70, 70, 70, 70, 65, 55, 60, 50, 70, 55, 70, 65, 70, 50
    ],
    'upper_recovery_percent': [
        140, 135, 145, 150, 150, 150, 140, 145, 140, 140, 140, 145, 140, 145, 150, 150, 
        145, 150, 145, 145, 155, 150, 145, 150, 145, 140, 145, 145, 155, 140, 145, 140, 
        150, 150, 155, 150, 140, 130, 135, 145
    ]
}) 
    

    