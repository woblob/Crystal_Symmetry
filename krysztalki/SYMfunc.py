import numpy as np
from bisect import bisect_right as BSR, bisect_left as BSL
from itertools import combinations as itrtls_combinations

def generateSymetryBase():
    """
    All posible transforamtion in crystollographic cell
    Currently hexagonal axis and trigonal axis  in dir [001] are not implemented
    """
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
    """
    Make all points given by transformation
    """
    punkt = np.matmul(macierz,punktprzes)  
    while not porownajPunkty(punkt, punktprzes):
        yield punkt
        punkt = np.matmul(macierz,punkt)        
        
def makelist():
    """
    List all names of Symmetries
    """
    Matrixes = generateSymetryBase()
    mylist = []
    for Mainkey in Matrixes.keys():
        for Subkey in Matrixes[Mainkey].keys():
            mylist.append((Mainkey,Subkey))
    return mylist[::-1]

def porownajPunkty(p1,p2):
    """
    Compare two points
    Faster than numpy.all for small arrays
    """
    for a, b in zip(p1,p2):
        if a!=b:
            return False
    return True

def findindex(searched, points):         
    """
    Binary search for points in a cell
    
    returns index of found point
    if not found then returns -1
    """
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

def findPoints(listofps, allpoints, Anti = False):
    """
    Check if point is in the list
    
    Depends on 'Anti' arg
    for False value: looks for vacancies
    True value: looks for atoms
    
    allpoints list is transposed in this function
    """
    for ps in listofps:
        indx = findindex(ps,allpoints)    
        if (indx + 1 and porownajPunkty(allpoints[:,indx],ps)) == Anti:
            return False
    return True 

def findAntiSym_InnerLoop(Matrix, allpoints, vacancies):
    """
    Check if any of the points is in the list
    diffrence between findSym_innerLoop is 'Anti' value 
    """
    for vac in vacancies:
        if not findPoints(listadous(Matrix,vac), allpoints.T, Anti=True):
            return False
    return True

def findAntiSym(matrixes, allpoints, vacancies):
    """
    check what symmetries cannot exist for vacancies in cell 
    """
    allsymmerties = makelist()
    if vacancies.shape == (3,):
        vacancies = np.array([vacancies])
    possymmerties = []    
    for el0, el1 in allsymmerties:
        if findAntiSym_InnerLoop(matrixes[el0][el1], allpoints, vacancies):
            possymmerties.append((el0, el1))           
    return possymmerties 

def findSym_innerLoop(Matrix, allpoints):
    """
    Check if all of the points are in the list
    """
    for point in allpoints:
        if not findPoints(listadous(Matrix,point), allpoints.T):
            return False
    return True

def findSym(matrixes, allpoints, vacancies):
    """
    check what symmetries are in cell
    """
    symmerties = []
    possym = findAntiSym(matrixes, allpoints, vacancies)
    for el0, el1 in possym:                
        if findSym_innerLoop(matrixes[el0][el1], allpoints):
            symmerties.append((el0, el1))
    return symmerties

def makeCellWithVacancies(cell,indexes):
    """
    make 2 lists: Cell with vacancies and vacancies
    """
    indexes = set(indexes)
    cellVac = []
    Vac = []
    for nr, p in enumerate(cell):
        if nr not in indexes:
            cellVac.append(p)
        else:
            Vac.append(p)
    return np.array(cellVac), np.array(Vac)


def checkAllCells(scell,base,sumVac):
    """
    main fuction
    make all possible combinations of cell and find its symmetries
    TODO: save with vacancies / problem with writing file
    """
    Matrixes = generateSymetryBase()
    mylist = []
    for indexes in itrtls_combinations(range(len(scell)),sumVac): 
        scellvac, vacancies = makeCellWithVacancies(scell,indexes)
        SYM = findSym(Matrixes, scellvac, vacancies)
        if SYM != []:
            mylist.append(SYM)
    return mylist

def saveOutput(OUTPUT, filename = "output of symmetries.txt"):
    """
    write txt file with all symmetries for all possible combinations of vacancies in cell
    """
    with open(filename, "w") as f:
        for el in sorted(OUTPUT, key=len, reverse=True):
            f.write(str(el)+"\n")