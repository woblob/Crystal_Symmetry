import numpy as np
from bisect import bisect_right as BSR, bisect_left as BSL 
from itertools import combinations as itrtls_combinations
from Matrixes import *

def symmetryBase(BASE):
  if BASE == "m":
    return generateSymetryBaseQUAD()
  return generateSymetryBaseHEX()
  
'''def zaaplikujprzeksztalceniasymetryczne():
    myset = set()
    for Mainkey in Matrixes.keys():
        for Subkey in Matrixes[Mainkey].keys():
            myset.add((Mainkey,Subkey))
    print(myset)'''

'''def printmat(Matrixes):
    for os in Matrixes:
        print(os)
        for kier in Matrixes[os]:
            print(kier)
            print(Matrixes[os][kier])'''

"""def ortogonalCheck(matrix):
    prod = np.matmul(matrix,matrix.T)
    return np.allclose(prod, np.eye(matrix.shape[0])) 
#all(all(ortogonalCheck(Matrixes[os][kier]) for kier in Matrixes[os]) for os in Matrixes)"""
"""
def supercell(matrix, size):
    if size == 1:
        return np.unique(matrix,axis=0)*2-1
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
    
"""
"""
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
"""
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

def listadous(macierz, punktprzes):
  punkt = macierz @ punktprzes
  while not porownajPunkty(punkt, punktprzes):
    yield punkt
    punkt = macierz @ punkt  

# punkcik = np.array([0.5,0.25,0.33])
# trans = "4"
# for i in listadous(Matrixes[trans]["001"], punkcik):
#     print(i)
'''
if __name__ == "__main__":
    punkcik = np.array([0,1,1])
    trans = "6"
    for el in listadous(Matrixes[trans]["001"], punkcik, myswitch(trans)+1):
        print(el)'''

def usunkoor(koorZEW, oski):# isc od tylu i usuwac sprawdzany punkt
  koorWEW = koorZEW.copy()
  for os in oski:
    j = 1
    while j < len(koorWEW):            
      for punktdous in listadous(os, koorWEW[j]):                
        i = findindex(punktdous, koorWEW.T[:,j:])                
        if i + 1 and porownajPunkty(koorWEW[i+j],punktdous):
          koorWEW = np.delete(koorWEW, i+j, 0)
      j += 1
  return koorWEW

def usunkoor_mod(koorZEW, oski):#, Matrixes):
  koorWEW = koorZEW.copy()
  listofnr = list(range(len(koorWEW)))
  Matrixes = generateSymetryBase()
  for os0, os1 in oski:
    TRANS = Matrixes[os0][os1]
    j = 1
    while j < len(koorWEW):            
      for punktdous in listadous(TRANS, koorWEW[j]):                
        i = findindex(punktdous, koorWEW.T[:,j:])                
        if i + 1 and porownajPunkty(koorWEW[i+j],punktdous):
          koorWEW = np.delete(koorWEW, i+j, 0)
          del listofnr[i+j]
      j += 1
  return listofnr#zip(koorWEW, listofnr)  

'''   
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

"""
def odlegloscmiedzypunktami(px1,py1,pz1,px2,py2,pz2):
    return np.round(np.sqrt((px1-px2)**2+(py1-py2)**2+(pz1-pz2)**2),4)
"""
# def generateSymmetryGroup(transformacje): # sprawdzic 
#     sgroup = transformacje[:]
#     i = 0 
#     while i < len(sgroup)-1:
#         j = len(sgroup)-1
#         while j >0: 
#             pomoc = np.matmul( sgroup[i], sgroup[j])
#             found = False
#             for oska in sgroup:
#                 if np.all(pomoc == oska):
#                     found = True        
#                     break                
#             if not found:
#                 sgroup.append(pomoc)
#             j -= 1            
#         i += 1         
#     for nr, oska in enumerate(sgroup):
#         if np.allclose(np.linalg.inv(oska) == oska):
#             del sgroup[nr]
#             nr -= 1
#     return sgroup

"""def printsym():
    for Mainkey in Matrixes.keys():
        for Subkey in Matrixes[Mainkey].keys():
            print((Mainkey,Subkey))
            print(Matrixes[Mainkey][Subkey],end='\n\n')
        print()"""
        
def makelist(Matrixes):
  mylist = []
  for Mainkey in Matrixes.keys():
    for Subkey in Matrixes[Mainkey].keys():
      mylist.append((Mainkey,Subkey))
  return mylist[::-1]
  

# def makelist(Basetype):
#     if Basetype == "m":
#         Matrixes = generateSymetryBaseQUAD()
#     elif Basetype == "w":
#         Matrixes = generateSymmetryBaseHEX()
#     else:
#         return "wrong base type"
#     mylist = []
#     for Mainkey in Matrixes.keys():
#         for Subkey in Matrixes[Mainkey].keys():
#             mylist.append((Mainkey,Subkey))
#     return mylist[::-1]


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
    if not porownajPunkty(a,b):
      return False
  return True

# m1 = Matrixes['-4']['100']
# m2 = Matrixes['4']['100']
# %timeit -r 10 -n 10000 porownajMacierze(m1, m2)
# %timeit -r 10 -n 10000 np.all(m1 == m2)
# %timeit -r 10 -n 1000 np.allclose(m1, m2)


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

# pmck = komorka.T
# arr = np.array([-1,0,0])
# %timeit findindex(arr, pmck)



# p = np.array([0,1,0])
# somelist = listadous2(Matrixes["4"]["001"],p)
# print(znajdzpunkty(somelist,komorka))


# n=0
# komorkabez = np.append(komorka[:n],komorka[n+1:],axis = 0)
# zaaplikujprzeksztalceniasymetryczne2(komorkabez)

# def odleglosciPomiedzyPunktami():
#     maciorka = []
#     for km in komorka:
#         for el in mojalista1[-2:-1]:
#             od = odlegloscmiedzypunktami(*km,*el)
#             maciorka.append(list((od,el,km)))
#     maciorka = sorted(maciorka, key=lambda maciorka_entry: maciorka_entry[0]) 
#     for m in maciorka:
#         print(m[0],'\t',m[1],m[2])

def findAntiSym_InnerLoop(Matrix, allpoints, vacancies):
  for vac in vacancies:
    if not findPoints(listadous(Matrix,vac), allpoints.T, Anti = True):
      return False
  return True

# def findAntiSym_InnerLoop(Matrix, allpoints, vacancies):
#     for vac in vacancies:
#         listofvacsym = listadous(Matrix,vac)
#         if not findPoints(listofvacsym, allpoints.T, True):
#             return False
#     return True

def findAntiSym(matrixes, allpoints, vacancies):
  allsymmetries = makelist(matrixes)
#   print(vacancies.ndim,vacancies.shape)
  if vacancies.shape == (3,):
    vacancies = np.array([vacancies])
  possymmerties = []    
  for el0, el1 in allsymmetries:
    if findAntiSym_InnerLoop(matrixes[el0][el1], allpoints, vacancies):
      possymmerties.append((el0, el1))
  return possymmerties 
  
# n=14
# komorkabez = np.append(komorka[:n],komorka[n+1:],axis = 0)
# %timeit findAntiSym(komorkabez,komorka[n])

def findPoints(listofps, allpoints, Anti):
  for ps in listofps:
    indx = findindex(ps,allpoints)    
    if (indx + 1 and porownajPunkty(allpoints[:,indx],ps)) == Anti:
      return False
  return True 
    #       if     indx + 1    and np.allclose(zbior2[:,indx],punktprzek): Antipoints/Wakancje
    #       if not indx + 1 or not np.allclose(zbior2[:,indx],punktprzek): TruePoints/Atomy  #porownajPunkty 

def findSym_innerLoop(Matrix, allpoints):
  #to samo co w anty? różnica tylko wartosc Anti
  for p in allpoints:
    listofps = listadous(Matrix,p)          
    if not findPoints(listofps,allpoints.T, Anti=False):
      return False
  return True
  
def findSym(base, allpoints, vacancies):
  matrixes = symmetryBase(base)
  symmerties = []
  possym = findAntiSym(matrixes, allpoints, vacancies)
  for el0, el1 in possym:                
    if findSym_innerLoop(matrixes[el0][el1], allpoints):
      symmerties.append((el0, el1))
  return symmerties



  

  
  
def hashingPoints(lista):#zrobic dla 4 wymiarowych
  thisdict = {}
  for x,y,z in lista:
    thisdict.setdefault(x,{})
    thisdict[x].setdefault(y,{})
    thisdict[x][y].setdefault(z, True)
  return thisdict  

# %timeit mydict = hashingPoints(SUPERCELL2)
  
def searchforpoint(zestaw, x, y, z):
  return zestaw.get(x,{}).get(y,{}).get(z,False)
  
  
# p = (1,1,-2)
# mydict = MM.hashingPoints(SUPERCELL2)
# %timeit -n 100000 v1=searchforpoint(mydict,*p)
# %timeit -n 100000 v2=searchforpoint2(mydict,*p)

def findPointsInDict(listofps, dictAllpoints, Anti):
  for p in listofps:        
    if searchforpoint(dictAllpoints, *p) == Anti:
      return False
  return True 

def findSym_Dict_innerLoop(Matrix, allpoints, hpoints):
  for p in allpoints:        
    if not findPointsInDict(listadous(Matrix,p), hpoints, Anti=False):
      return False
  return True

def findAntiSym_Dict_InnerLoop(Matrix, hpoints, vacancies):
  for vac in vacancies:
    if not findPointsInDict(listadous(Matrix,vac), hpoints, Anti = True):
      return False
  return True

def findAntiSym_Dict(matrixes, hpoints, vacancies):
  allsymmetries = makelist(matrixes)
#   print(vacancies.ndim,vacancies.shape)
  if vacancies.shape == (3,):
    vacancies = np.array([vacancies])
  possymmerties = []    
  for el0, el1 in allsymmetries:
    if findAntiSym_Dict_InnerLoop(matrixes[el0][el1], hpoints, vacancies):
      possymmerties.append((el0, el1))
  return possymmerties 

def findSym_Dict(base, allpoints, hpoints, vacancies):
  matrixes = symmetryBase(base)
  symmerties = []
#   possym = findAntiSym(matrixes, allpoints, vacancies)
  possym = findAntiSym_Dict(matrixes, hpoints, vacancies)
  for el0, el1 in possym:                
    if findSym_Dict_innerLoop(matrixes[el0][el1], allpoints, hpoints):
      symmerties.append((el0, el1))
  return symmerties

from time import time 

def abc_Dict(scell,base,sumVac):
  countempty, countfull = 0, 0
  timeempty , timefull = 0, 0
  mylist = []
  for indexes in itrtls_combinations(range(len(scell)),sumVac): 
    scellvac, vacancies = makeCellWithVacancies(scell,indexes)
    hcell = hashingPoints(scellvac)
    start = time()
    SYM = findSym_Dict(base, scellvac, hcell, vacancies)
    end = time() - start
    if SYM == []:
      countempty += 1 
      timeempty += end
    else:
      countfull += 1 
      timefull += end
      
    mylist.append((vacancies, SYM))
  print(f'AVG E:{(timeempty/countempty):.4f}\nAVG F:{(timefull/countfull):.4f}')
  print(f'\nCOUNT E:{countempty}\nCOUNT F:{countfull}')
  print(f'\nTIME E:{timeempty:.1f}[s]\nTIME F:{timefull:.1f}[s]')
  return mylist
  

# from MMfunc import *
# #import numpy as np
# p = np.array([0,1,0])
# Matrixes = generateSymetryBase()
# somelist = listadous(Matrixes["4"]["001"],p)
# koordynaty = np.array([[0,0,0],[0,0,1],[0,1,0],[1,1,0],[1,0,0],[1,1,1],[1,0,1],[0,1,1],
#               [0.5,0.5,0],[0.5,0,0.5],[0,0.5,0.5],[0.5,0.5,1],[0.5,1,0.5],[1,0.5,0.5],
#              [0.75,0.25,0.25],[0.25,0.75,0.25],[0.25,0.25,0.75],[0.75,0.75,0.75]])
# komorka = supercell(koordynaty, size = 2)

# %timeit findPoints(somelist,komorka.T)
# %timeit findPoints_mod(somelist,komorka.T)


# komorkabez = np.append(komorka[:n],komorka[n+1:],axis = 0)
# mozliwosci = findAntiSym(Matrixes, komorkabez, komorka[n])
# SYM = findSym(Matrixes, komorkabez, mozliwosci)

# %timeit -r 10 -n 100 findAntiSym(Matrixes, komorkabez, komorka[n])
# %timeit -r 10 -n 10 findSym(Matrixes, komorkabez, mozliwosci)
# %timeit -r 10 -n 10 findSym(Matrixes, komorkabez, makelist())

# n = 0
# while n < len(komorka):        
#     komorkaWAK = np.append(komorka[:n],komorka[n+1:],axis = 0)
#     print(n, komorka[n])
#     print(zaaplikujprzeksztalceniasymetryczne2(komorkaWAK),end='\n\n')
#     n+=1

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

# print(SUPERCELL[0],SUPERCELL[3])
# print(makeCellWithVacancies(SUPERCELL,(0,3)))
# print(poprows(SUPERCELL,(0,3)))

# tumpel = (0,3,6,8,9,11)
# %timeit makeCellWithVacancies(SUPERCELL,tumpel)
# %timeit poprows(SUPERCELL,tumpel)

def abc(scell,base,sumVac):
  mylist = []
  for indexes in itrtls_combinations(range(len(scell)),sumVac): 
    scellvac, vacancies = makeCellWithVacancies(scell,indexes)
    SYM = findSym(base, scellvac, vacancies)
    mylist.append((vacancies, SYM))
  return mylist
  
def back2normal(output, size):
  mylist =[]
  for el0, el1 in sorted(output, key=lambda x:len(x[1]), reverse=True):
#     if el1 != []:
      vacs = ((el0+1)*(size/2)).tolist()
      myvar = ''
      for vac in vacs:
        myvar += str(vac)+";\t"
      mylist.append(myvar + str(el1) + "\n")
#     else:
#       break
  return mylist

def saveOutput2(OUTPUT,size,filename):
  from datetime import datetime as dt
  modOUTPUT = back2normal(OUTPUT,size)
  filename = filename + dt.now().strftime("%Y_%m_%d_%H_%M_%S") +'.txt'
  with open(filename, "w") as f:
    for line in modOUTPUT:
      f.write(str(line))