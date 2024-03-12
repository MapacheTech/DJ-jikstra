from lib import *

import sys

"""dicc = {
    'nom' : "Zaira",
    'edad' : 35,
    'tel' : {
        'cel' : 5,
        'fij' : 6,
    }
}

print(dicc['tel']['cel'])"""


diccRel = {
    'A':{'B':5,'C':3},
'B':{'A':5,'C':2,'D':4},
'C':{'A':3,'B':2,'D':6,'E':7},
'D':{'B':4,'C':6,'E':8},
'E':{'C':7,'D':8},
}



            
printDicc(diccRel)