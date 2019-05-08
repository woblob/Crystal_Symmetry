import numpy as np
from bisect import bisect_right as BSR, bisect_left as BSL
from itertools import combinations as itrtls_combinations

def generateSymetryBase():
    s3d2 = np.sqrt(3)/2
    return {
        "c":{
            "000":np.array([[-1,0,0],[0,-1,0],[0,0,-1]])
        },
        "m":{
            "100":np.array([[-1,0,0],[0,1,0],[0,0,1]]),
            "010":np.array([[1,0,0],[0,-1,0],[0,0,1]]),
            "001":np.array([[1,0,0],[0,1,0],[0,0,-1]]),

            "110":np.array([[0,-1,0],[-1,0,0],[0,0,1]]),            
            "011":np.array([[1,0,0],[0,0,-1],[0,-1,0]]),
            "101":np.array([[0,0,-1],[0,1,0],[-1,0,0]]),
            
            "-101":np.array([[0,0,1],[0,1,0],[1,0,0]]),
            "-110":np.array([[0,1,0],[1,0,0],[0,0,1]]),
            "0-11":np.array([[1,0,0],[0,0,1],[0,1,0]])
        },
        "2":{
            "100":np.array([[1,0,0],[0,-1,0],[0,0,-1]]),
            "010":np.array([[-1,0,0],[0,1,0],[0,0,-1]]),
            "001":np.array([[-1,0,0],[0,-1,0],[0,0,1]]),

            "110":np.array([[0,1,0],[1,0,0],[0,0,-1]]),
            "101":np.array([[1,0,0],[0,-1,0],[0,0,1]]),
            "011":np.array([[-1,0,0],[0,0,1],[0,1,0]]),

            "-110":np.array([[0,-1,0],[-1,0,0],[0,0,-1]]),
            "-101":np.array([[0,0,-1],[0,-1,0],[-1,0,0]]),
            "0-11":np.array([[-1,0,0],[0,0,-1],[0,-1,0]])
        },
        "3":{
#             "001":np.array([[-0.5,-s3d2,0],[s3d2,-0.5,0],[0,0,1]]),
            "111":np.array([[0,0,1],[1,0,0],[0,1,0]]),
            "-111":np.array([[0,-1,0],[0,0,1],[-1,0,0]]),
            "1-11":np.array([[0,-1,0],[0,0,-1],[1,0,0]]),
            "11-1":np.array([[0,1,0],[0,0,-1],[-1,0,0]])
        },
        "-3":{
#             "001":np.array([[0.5,s3d2,0],[-s3d2,0.5,0],[0,0,-1]]),
            "111":np.array([[0,0,-1],[-1,0,0],[0,-1,0]]),
            "-111":np.array([[0,1,0],[0,0,-1],[1,0,0]]),
            "1-11":np.array([[0,1,0],[0,0,1],[-1,0,0]]),
            "11-1":np.array([[0,-1,0],[0,0,1],[1,0,0]])        
        },
        "4":{
            "100":np.array([[1,0,0],[0,0,-1],[0,1,0]]),
            "010":np.array([[0,0,1],[0,1,0],[-1,0,0]]),
            "001":np.array([[0,-1,0],[1,0,0],[0,0,1]])
        },
        "-4":{
            "100":np.array([[-1,0,0],[0,0,1],[0,-1,0]]),
            "010":np.array([[0,0,-1],[0,-1,0],[1,0,0]]),
            "001":np.array([[0,1,0],[-1,0,0],[0,0,-1]])
        }#,
#         "6":{
#             "001":np.array([[0.5,-s3d2,0],[s3d2,0.5,0],[0,0,1]])
#         },
#         "-6":{
#             "001":np.array([[-0.5,s3d2,0],[-s3d2,-0.5,0],[0,0,-1]])
#         }
    }

# def listadous(macierz, punktprzes):
#     punkt = np.matmul(macierz,punktprzes)  # np.matmul
#     punkt = np.around(punkt,6)
#     while not np.allclose(punkt, punktprzes):   # porownajPunkty
#         yield punkt
#         punkt = np.matmul(macierz,punkt)   
#         punkt = np.around(punkt,6) 
        
def listadous(macierz, punktprzes):
    punkt = np.matmul(macierz,punktprzes)  
    while not porownajPunkty(punkt, punktprzes):
        yield punkt
        punkt = np.matmul(macierz,punkt)        
        
def makelist():
    Matrixes = generateSymetryBase()
    mylist = []
    for Mainkey in Matrixes.keys():
        for Subkey in Matrixes[Mainkey].keys():
            mylist.append((Mainkey,Subkey))
    return mylist[::-1]

def porownajPunkty(p1,p2):
    for a, b in zip(p1,p2):
        if a!=b:
            return False
    return True

def findindex(searched, points):         
    indexL, indexR = 0, len(points[0])        
    for xyz in range(len(points)): 
        numR = BSR(points[xyz][indexL: indexR], searched[xyz])
        numL = BSL(points[xyz][indexL: indexR], searched[xyz])        
        if numL < numR:
            indexR = indexL + numR
            indexL += numL
        elif numL == numR:
            indexL += numL
            if indexL != len(points[0]):
                return indexL
            return -1
        else:
            return -1        
    return indexL 

def findPoints(listofps, allpoints2, Anti = False):
    for ps in listofps:
        indx = findindex(ps,allpoints2)    
        if (indx + 1 and porownajPunkty(allpoints2[:,indx],ps)) == Anti:
            return False
    return True 

def findAntiSym_InnerLoop(Matrix, allpoints, vacancies):
    for vac in vacancies:
        listofvacsym = listadous(Matrix,vac)
        if not findPoints(listofvacsym, allpoints.T, Anti=True):
            return False
    return True

def findAntiSym_MOD(matrixes, allpoints, vacancies):
    allsymmerties = makelist()
    if vacancies.shape == (3,):
        vacancies = np.array([vacancies])
    possymmerties = []    
    for el0, el1 in allsymmerties:
        if findAntiSym_InnerLoop(matrixes[el0][el1], allpoints, vacancies):
            possymmerties.append((el0, el1))           
    return possymmerties 

def findSym_Base_mod2_innerLoop(Matrix, allpoints):
    for p in allpoints:
        listofps = listadous(Matrix,p)          
        if not findPoints(listofps,allpoints.T):
            return False
    return True

def findSym_Base_mod2(matrixes, allpoints, vacancies):
    symmerties = []
    possym = findAntiSym_MOD(matrixes, allpoints, vacancies)
    for el0, el1 in possym:                
        if findSym_Base_mod2_innerLoop(matrixes[el0][el1], allpoints):
            symmerties.append((el0, el1))
    return symmerties

def makeCellWithVacancies(cell,indexes):
    indexes = set(indexes)
    cellVac = []
    Vac = []
    for nr, p in enumerate(cell):
        if nr not in indexes:
            cellVac.append(p)
        else:
            Vac.append(p)
    return np.array(cellVac), np.array(Vac)


def abcde(scell,sumVac):
    Matrixes = generateSymetryBase()
    mylist = []
    for indexes in itrtls_combinations(range(len(scell)),sumVac): 
        scellvac, vacancies = makeCellWithVacancies(scell,indexes)
        SYM = findSym_Base_mod2(Matrixes, scellvac, vacancies)
        mylist.append(SYM)
    return mylist

def saveOutput(OUTPUT):
    txtfile = "output of symmetries.txt"
    with open(txtfile, "w") as f:
        for el in sorted(OUTPUT, key=len, reverse=True):
            if el != []:
                f.write(str(el)+"\n")