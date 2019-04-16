import numpy as np
from bisect import bisect_right as BSR, bisect_left as BSL 

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
            "101":np.array([[-1,0,0],[0,1,0],[0,0,-1]]),
            
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
            "001":np.array([[-0.5,-s3d2,0],[s3d2,-0.5,0],[0,0,1]]),
            "111":np.array([[0,0,1],[1,0,0],[0,1,0]]),
            "-111":np.array([[0,-1,0],[0,0,1],[-1,0,0]]),
            "1-11":np.array([[0,-1,0],[0,0,-1],[1,0,0]]),
            "11-1":np.array([[0,1,0],[0,0,-1],[-1,0,0]])
        },
        "-3":{
            "001":np.array([[0.5,s3d2,0],[-s3d2,0.5,0],[0,0,-1]]),
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
        },
        "6":{
            "001":np.array([[0.5,-s3d2,0],[s3d2,0.5,0],[0,0,1]])
        },
        "-6":{
            "001":np.array([[-0.5,s3d2,0],[-s3d2,-0.5,0],[0,0,-1]])
        }
    }

'''def zaaplikujprzeksztalceniasymetryczne():
    myset = set()
    for Mainkey in Matrixes.keys():
        for Subkey in Matrixes[Mainkey].keys():
            myset.add((Mainkey,Subkey))
    print(myset)'''

def printmat(Matrixes):
    for os in Matrixes:
        print(os)
        for kier in Matrixes[os]:
            print(kier)
            print(Matrixes[os][kier])

def ortogonalCheck(matrix):
    prod = np.dot(matrix,matrix.T)
    return np.all(abs(prod - np.eye(3)) < 10**-15)
#all(all(ortogonalCheck(Matrixes[os][kier]) for kier in Matrixes[os]) for os in Matrixes)

def supercell(matrix, size):
    if size == 1:
        return matrix
    elif size < 1:
        return None
    cell = matrix.copy()
    for os in range(3):    
        subcell = cell.copy()[cell.T[os]!=0]
        listcell = subcell.copy()
        for _ in range(1,size):        
            subcell[:,os] += 1
            listcell = np.append(listcell,subcell,axis =0)   
        cell = np.append(cell,listcell,axis =0)   
    return np.unique(cell,axis = 0)/(size/2)-1

'''def supercellprob(matrix, size):
"""
wyciac 3 scianki 
powielic do superkomorki
wyciac trzy sciany superkomorki
odjac dlugosc komorki od scian albo pomonozyc przez -1 calosc
(inwersja jest chyba szybsza) 
"""
    if size == 1:
        return matrix
    elif size < 1:
        return None
    cell = matrix.copy()
    pomcell = cell.T
    subcell = cell.copy()[(pomcell[0]!=0)&(pomcell[1]!=0)&(pomcell[2]!=0)]
    for os in range(3):            
        listcell = subcell.copy()
        for _ in range(1,size):        
            subcell[:,os] += 1
            listcell = np.append(listcell,subcell,axis =0)   
        cell = np.append(cell,listcell,axis =0) 
        
#     print(cell)
#     pomcell = cell.T
#     scianki = (cell.copy()[(pomcell[0]==size)|(pomcell[1]==size)|(pomcell[2]==size)])#*-1 + size
#     print(scianki)
#     scianki = scianki*-1 + size
        
    subcellFACEX = matrix.copy()[pomcell[0]==0]
    subcellFACEY = matrix.copy()[(pomcell[1]==0)]
    subcellFACEZ = matrix.copy()[(pomcell[2]==0)]
    tupleofsubcells = (subcellFACEX,subcellFACEY,subcellFACEZ)
    costam = (0,2),(1,2),(0,1)
    for nr,side in enumerate(tupleofsubcells):
        subcell = side.copy()        
        for os in costam[nr]:
            listcell = subcell.copy()
            for _ in range(1,size):
                subcell[:,os] += 1
                listcell = np.append(listcell,subcell,axis =0)   
        cell = np.append(cell,listcell,axis =0) 
    return np.unique(cell,axis = 0)/(size/2)-1
#supercellprob(koordynaty,size = 2)    



SIZE = 2
prob = supercellprob(koordynaty,size = SIZE)
wlas = supercell(koordynaty,size = SIZE)
if np.all(prob == wlas):
    %timeit supercellprob(koordynaty,size = 2)
    %timeit supercell(koordynaty,size = 2)
else:
    print("FALSE")
    print(len(prob),len(wlas))    
    for el1, el2 in zip(prob,wlas):
        print(el1,el2)'''
    


def myswitch(nr):
    mydict = {
        "c": 1,
        "m": 1,
        "2": 1,
        "3": 2,
        "-3": 5,
        "4": 3,
        "-4": 3,
        "6": 5,
        "-6": 5
    }
    return mydict[nr]
#myswitch("m")

'''def listadous(macierz, punkt, ilepow):
    lista = []
    for i in range(ilepow): 
        punkt = np.dot(macierz,punkt)
        punkt = np.around(punkt,5)
        lista.append(punkt)
    return lista'''
'''def listadous2(macierz, punktprzes):
    punkt = np.dot(macierz,punktprzes) 
    lista = []
    while not np.allclose(punkt , punktprzes):   # porownajPunkty
        punkt = np.around(punkt,5)
        lista.append(punkt)        
        punkt = np.dot(macierz,punkt)
    return lista #yield

def listadous(macierz, punktprzes, ilepow):
    punkt = np.dot(macierz,punktprzes)
    punkt = np.around(punkt,5) 
    lista = []
    if not porownajPunkty(punkt, punktprzes):              
        lista.append(punkt)        
        for i in range(ilepow-1): 
            punkt = np.dot(macierz,punkt)
            punkt = np.around(punkt,5)
            lista.append(punkt)
    return lista #yield'''

def listadous(macierz, punktprzes):
    punkt = np.dot(macierz,punktprzes)  
    punkt = np.around(punkt,5)
    while not np.allclose(punkt, punktprzes):   # porownajPunkty
        yield punkt
        punkt = np.dot(macierz,punkt)   
        punkt = np.around(punkt,5) 

# punkcik = np.array([0.5,0.25,0.33])
# trans = "6"
# for i in listadous2mod(Matrixes[trans]["001"], punkcik):
#     print(i)
'''
if __name__ == "__main__":
    punkcik = np.array([0,1,1])
    trans = "6"
    for el in listadous(Matrixes[trans]["001"], punkcik, myswitch(trans)+1):
        print(el)'''

def usunkoor(koorZEW, oski):
    koorWEW = koorZEW.copy().tolist() # sprawdzic
    for os in oski:
        j = 0 
        while j < len(koorWEW):            
            for punktdous in listadous(os, koorWEW[j]):#,myswitch("m")):
                try:
                    i = koorWEW[j+1:].index(punktdous.tolist())
                    del koorWEW[i+j+1]      
                except:
                    pass            
            j += 1
    return np.unique(koorWEW,axis = 0)

'''def usunkoor2(koorZEW, oski):
    koorWEW = koorZEW.copy().tolist() # sprawdzic
    for os in oski:
        j = 0 
        while j < len(koorWEW):            
            for punktdous in listadous(os, koorWEW[j],myswitch("m")):
                try:
                    i = koorWEW.index(punktdous.tolist(),j+1)
                    del koorWEW[i+j+1]      
                except:
                    pass            
            j += 1
    return np.unique(koorWEW,axis = 0)

komorka = supercell(koordynaty,size = 2)
mojalista1 = usunkoor(komorka, oski2) 
mojalista2 = usunkoor2(komorka, oski2) 
if np.all(mojalista2 == mojalista1):
    %timeit usunkoor(komorka, oski2)
    %timeit usunkoor2(komorka, oski2)
else:
    print(len(mojalista2),len(mojalista1))
    print(mojalista2)
    print()
    print(mojalista1)'''    

def odlegloscmiedzypunktami(px1,py1,pz1,px2,py2,pz2):
    return np.round(np.sqrt((px1-px2)**2+(py1-py2)**2+(pz1-pz2)**2),4)

def generateSymmetryGroup(transformacje): # sprawdzic 
    sgroup = transformacje[:]
    i = 0 
    while i < len(sgroup)-1:
        j = len(sgroup)-1
        while j >0: 
            pomoc = np.dot( sgroup[i], sgroup[j])
            found = False
            for oska in sgroup:
                if np.all(pomoc == oska):
                    found = True        
                    break                
            if not found:
                sgroup.append(pomoc)
            j -= 1            
        i += 1         
    for nr, oska in enumerate(sgroup):
        if np.allclose(np.linalg.inv(oska) == oska):
            del sgroup[nr]
            nr -= 1
    return sgroup

def printsym():
    for Mainkey in Matrixes.keys():
        for Subkey in Matrixes[Mainkey].keys():
            print((Mainkey,Subkey))
            print(Matrixes[Mainkey][Subkey],end='\n\n')
        print()
        
def makelist():
    Matrixes = generateSymetryBase()
    mylist = []
    for Mainkey in Matrixes.keys():
        for Subkey in Matrixes[Mainkey].keys():
            mylist.append((Mainkey,Subkey))
    return mylist[::-1]
#makelist()[19:22]  

def porownajPunkty(p1,p2):
    for a, b in zip(p1,p2):
        if a!=b:
            return False
    return True

# p1 = np.array([1,1,1])
# p2 = np.array([1,1,2])
# %timeit -r 10 -n 10000 porownajPunkty(p1, p2)
# %timeit -r 10 -n 10000 np.all(p1 == p2)
# %timeit -r 10 -n 1000 np.allclose(p1, p2)

def porownajMacierze(m1,m2):
    for a, b in zip(m1,m2):
        if porownajPunkty(a,b):
            return False
    return True

# m1 = Matrixes['-4']['100']
# m2 = Matrixes['4']['100']
# %timeit -r 10 -n 10000 porownajMacierze(m1, m2)
# %timeit -r 10 -n 10000 np.all(m1 == m2)
# %timeit -r 10 -n 1000 np.allclose(m1, m2)

'''def znjdzpnktmdCZYSA(punktprzek, zbior2):
    for punkt2 in zbior2:
        if porownajPunkty(punktprzek, punkt2):
            return True
    return False

def znajdzpunktyCZYSAmod(mylist,zbior2):
    for punktprzek in mylist:    
        if not znjdzpnktmd(punktprzek, zbior2):
            return True
    return False'''

# komorka = supercell(koordynaty,2)
# mylist = listadous2(Matrixes['-4']['100'],np.array([1,1,0]))
# %timeit znajdzpunktymod(mylist,komorkamod)

def findindex(szukana, lista):         
    numL, numR = 0, len(lista[0])
    indexL, indexR = 0, len(lista[0])        
    for abc in range(len(lista)): 
        numR = BSR(lista[abc][indexL: indexR], szukana[abc])
        numL = BSL(lista[abc][indexL: indexR], szukana[abc])        
        if numL < numR:
            indexR = indexL + numR
            indexL += numL
        elif numL == numR:
            if not indexL + numL == len(lista[0]):
                return indexL + numL
            return -1
        else:
            return -1        
    return indexL 

# pmck = komorka.T
# arr = np.array([-1,0,0])
# %timeit findindex(arr, pmck)

#findindexmod(punktprzek, lista)
def znajdzpunkty(mylist,zbior2):
    nr = 0 
    for indx,punktprzek in enumerate(mylist,1):  
        for punkt2 in zbior2:
            if np.allclose(punktprzek, punkt2): #porownajPunkty
                nr += 1
                break
        if nr != indx:
            return False
    return True

# p = np.array([0,1,0])
# somelist = listadous2(Matrixes["4"]["001"],p)
# print(znajdzpunkty(somelist,komorka))

def zaaplikujprzeksztalceniasymetryczne2(zbior):
    mylist =  makelist()
    mylist2 = []
    for el1,el2 in mylist:
        numerek = 0
        for punkt in zbior:
            listpunktprzek = listadous2(Matrixes[el1][el2],punkt)    
            
            if znajdzpunkty(listpunktprzek,zbior):
                numerek += 1 
            else:
                break              
                
        if numerek == len(zbior):
            mylist2.append((el1,el2))
    return mylist2

# n=0
# komorkabez = np.append(komorka[:n],komorka[n+1:],axis = 0)
# zaaplikujprzeksztalceniasymetryczne2(komorkabez)

def odleglosciPomiedzyPunktami():
    maciorka = []
    for km in komorka:
        for el in mojalista1[-2:-1]:
            od = odlegloscmiedzypunktami(*km,*el)
            maciorka.append(list((od,el,km)))
    maciorka = sorted(maciorka, key=lambda maciorka_entry: maciorka_entry[0]) 
    for m in maciorka:
        print(m[0],'\t',m[1],m[2])
            

# def findAntiPoints(mylist,zbior2):
#     for punktprzek in mylist:    
#         for punkt2 in zbior2:
#             if np.allclose(punktprzek, punkt2): #porownajPunkty
#                 return False
#     return True

def findAntiPoints(mylist,zbior2):
    for punktprzek in mylist:
        indx = findindex(punktprzek,zbior2)               
        if indx + 1 and np.allclose(zbior2[:,indx],punktprzek): #porownajPunkty()
            return False
    return True

def findAntiSym_InnerLoop(zbior, wycinek, el0, el1):
    for punkt in wycinek:
        listpunktprzek = listadous(Matrixes[el0][el1],punkt)
        if not findAntiPoints(listpunktprzek,zbior.T):
            return False
    return True

def findAntiSym_MOD(zbior, wycinek):
    mylist = makelist()
    if wycinek.shape == (3,):
        wycinek = np.array([wycinek])
    mylist2 = []    
    for el in mylist:
        if findAntiSym_InnerLoop(zbior, wycinek, *el):
            mylist2.append(el)           
    return mylist2 

# def findAntiSym_MOD_gen(zbior, wycinek):
#     mylist = makelist()
#     if wycinek.shape == (3,):
#         wycinek = np.array([wycinek]) 
#     for el in mylist:
#         if findAntiSym_InnerLoop(zbior, wycinek, *el):
#             yield el           

# n=14
# komorkabez = np.append(komorka[:n],komorka[n+1:],axis = 0)
# %timeit findAntiSym_MOD(komorkabez,komorka[n])
