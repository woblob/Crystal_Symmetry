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

"""def ortogonalCheck(matrix):
    prod = np.matmul(matrix,matrix.T)
    return np.allclose(prod, np.eye(matrix.shape[0])) 
#all(all(ortogonalCheck(Matrixes[os][kier]) for kier in Matrixes[os]) for os in Matrixes)"""

    

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

# from time import time 

# def abc_Dict(scell,base,sumVac):
#   countempty, countfull = 0, 0
#   timeempty , timefull = 0, 0
#   mylist = []
#   for indexes in itrtls_combinations(range(len(scell)),sumVac): 
#     scellvac, vacancies = makeCellWithVacancies(scell,indexes)
#     hcell = hashingPoints(scellvac)
#     start = time()
#     SYM = findSym_Dict(base, scellvac, hcell, vacancies)
#     end = time() - start
#     if SYM == []:
#       countempty += 1 
#       timeempty += end
#     else:
#       countfull += 1 
#       timefull += end
      
#     mylist.append((vacancies, SYM))
#   print(f'AVG E:{(timeempty/countempty):.4f}\nAVG F:{(timefull/countfull):.4f}')
#   print(f'\nCOUNT E:{countempty}\nCOUNT F:{countfull}')
#   print(f'\nTIME E:{timeempty:.1f}[s]\nTIME F:{timefull:.1f}[s]')
#   return mylist


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



# print(SUPERCELL[0],SUPERCELL[3])
# print(makeCellWithVacancies(SUPERCELL,(0,3)))
# print(poprows(SUPERCELL,(0,3)))

# tumpel = (0,3,6,8,9,11)
# %timeit makeCellWithVacancies(SUPERCELL,tumpel)
# %timeit poprows(SUPERCELL,tumpel)

'''def searchforpoint(zestaw, x, y, z):
  return zestaw.get(x,{}).get(y,{}).get(z,False)'''
  
# p = (1,1,-2)
# mydict = MM.hashingPoints(SUPERCELL2)
# %timeit -n 100000 v1=searchforpoint(mydict,*p)
# %timeit -n 100000 v2=searchforpoint2(mydict,*p)


'''def listadous(macierz, punktprzes):
  punkt = macierz @ punktprzes
  while not porownajPunkty(punkt, punktprzes):
    yield punkt
    punkt = macierz @ punkt  
'''
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