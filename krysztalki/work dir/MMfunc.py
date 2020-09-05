# import numpy as np
# from bisect import bisect_right as BSR, bisect_left as BSL
# from itertools import combinations as itertools_combinations
# from Matrixes import *
#
# def symmetryBase(BASE):
#     if BASE == "m":
#         return generateSymetryBaseQUAD()
#     return generateSymetryBaseHEX()
#
# def listadous(macierz, punktprzes):
#     punkt = macierz @ punktprzes
#     while not porownajPunkty(punkt, punktprzes):
#         yield punkt
#         punkt = macierz @ punkt
#
# def makelist(Matrixes):
#     mylist = []
#     for Mainkey in Matrixes.keys():
#         for Subkey in Matrixes[Mainkey].keys():
#             mylist.append((Mainkey,Subkey))
#     return mylist[::-1]
#
# # def makelist(Basetype = "c"):
# #     if Basetype == "c":
# #         Matrixes = generateSymetryBase()
# #     elif Basetype == "h":
# #         Matrixes = generateSymmetryBaseHEX()
# #     mylist = []
# #     for Mainkey in Matrixes.keys():
# #         for Subkey in Matrixes[Mainkey].keys():
# #             mylist.append((Mainkey,Subkey))
# #     return mylist[::-1]
#
#
# def porownajPunkty(p1,p2):
#     for a, b in zip(p1,p2):
#         if a!=b:
#             return False
#     return True
#
# def porownajMacierze(m1,m2):
#     for a, b in zip(m1,m2):
#         if not porownajPunkty(a,b):
#             return False
#     return True
#
# # def hashingPoints(lista):#zrobic dla 4 wymiarowych
# #     thisdict = {}
# #     for x,y,z in lista:
# #         thisdict.setdefault(x,{})
# #         thisdict[x].setdefault(y,{})
# #         thisdict[x][y].setdefault(z, True)
# #     return thisdict
#
# # def searchforpoint(zestaw, x, y, z):
# #     return zestaw.get(x,{}).get(y,{}).get(z,False)
#
# def hashingPoints(lista):#zrobic dla 4 wymiarowych #SET
#     return {tuple(point) for point in lista}
#
# def searchforpoint(zestaw, x, y, z): #SET
#     return tuple((x, y, z)) in zestaw
#
# def findPointsInSet(listofps, dictAllpoints, Anti):
#     for point in listofps:
#         if (tuple(point) in dictAllpoints) == Anti:    #comment buffor
#             return False
#     return True
#
# def findPointsInDict(listofps, dictAllpoints, Anti):
#     for point in listofps:
#         if searchforpoint(dictAllpoints, *point) == Anti:
#             return False
#     return True
#
# def findSym_Dict_innerLoop(Matrix, allpoints, hpoints):
#     for point in allpoints:
#         if not findPointsInDict(listadous(Matrix, point), hpoints, Anti = False):
#             return False
#     return True
#
# # def findSym_Dict_innerLoop2(Matrix, allpoints, hpoints):
# #     return any(map(lambda p: findPointsInDict(listadous(Matrix, p), hpoints, Anti = False), allpoints))
#
# # def findPointsInDict(listofps, dictAllpoints, Anti):
# #   for p in listofps:
# #     if searchforpoint(dictAllpoints, *p) == Anti:
# #       return False
# #   return True
#
# # # def findPointsInDict2(listofps, dictAllpoints, Anti):
# # #   mymap = map(lambda z: searchforpoint(dictAllpoints,*z) == Anti, listofps)
# # #   if Anti:
# # #     return not any(mymap)
# # #   else:
# # #     return not any(mymap)
#
# # def findPointsInDict2(listofps, dictAllpoints, Anti):
# #   return not any(map(lambda z: searchforpoint(dictAllpoints,*z) == Anti, listofps))
#
# # lista = np.array([[-1,-1,-1],[0,0,0],[1,1,1],[0,1,0],[0.6,0,1],[1,0,0]])
# # hpoints = hashingPoints(SUPERCELL2)
# # # anti = True
#
# # %timeit (findPointsInDict(lista, hpoints, anti))
# # %timeit (findPointsInDict2(lista, hpoints, anti))
#
# # listas = [np.array([[-1,-1,-1],[0,0,0],[1,1,1],[0,1,0],[0,0,1],[1,0,0]]), \
# #           np.array([[-1,-1,-1],[0.6,0,0],[1,1,1],[0,1,0],[0,0,1],[1,0,0]])]
# # bools = [True, False]
# # for l in listas:
# #   for s in bools:
# #     print(findPointsInDict(l, hpoints, s) == findPointsInDict2(l, hpoints, s))
#
#
# def findAntiSym_Dict_InnerLoop(Matrix, hpoints, vacancies):
#     for vac in vacancies:
#         if not findPointsInDict(listadous(Matrix, vac), hpoints, Anti = True):
#             return False
#     return True
#
# def findSym_Dict_InnerLoop_universal(Matrix, hpoints, points, boool):
#     for p in points:
#         if not findPointsInDict(listadous(Matrix, p), hpoints, Anti = boool):
#             return False
#     return True
#
# def findAntiSym_Dict(matrixes, hpoints, vacancies):
#     allsymmetries = makelist(matrixes)
# #     print(vacancies.ndim,vacancies.shape)
#     if vacancies.shape == (3,):
#         vacancies = np.array([vacancies])
#     possymmerties = []
#     for el0, el1 in allsymmetries:
#         if findAntiSym_Dict_InnerLoop(matrixes[el0][el1], hpoints, vacancies):
#             possymmerties.append((el0, el1))
#     return possymmerties
#
# def findSym_Dict(base, allpoints, hpoints, vacancies):
#     matrixes = symmetryBase(base)
#     symmerties = []
# #     possym = findAntiSym(matrixes, allpoints, vacancies)
#     possym = findAntiSym_Dict(matrixes, hpoints, vacancies)
#     for el0, el1 in possym:
#         if findSym_Dict_innerLoop(matrixes[el0][el1], allpoints, hpoints):
#             symmerties.append((el0, el1))
#     return symmerties
#
# def findSym_Dict2(matrixes, allpoints, hpoints, vacancies):
#     symmerties = []
#     possym = findAntiSym_Dict(matrixes, hpoints, vacancies)
#     for el0, el1 in possym:
#         if findSym_Dict_innerLoop(matrixes[el0][el1], allpoints, hpoints):
#             symmerties.append((el0, el1))
#     return symmerties
#
# def abc_Dict2(scell,base,sumVac):
#     mylist = []
#     matrixes = symmetryBase(base)
#     for indexes in itertools_combinations(range(len(scell)),sumVac):
#         scellvac, vacancies = makeCellWithVacancies(scell,indexes)
#         hcell = hashingPoints(scellvac) # update dict
#         SYM = findSym_Dict2(matrixes, scellvac, hcell, vacancies)
#         mylist.append((vacancies,SYM))
#     return mylist
#
# def abc_Dict3(scell,base,sumVac):
#     mylist = []
#     matrixes = symmetryBase(base)
#     hcell = hashingPoints(scell)
#     oldvacancies = np.array([])
#     for indexes in itertools_combinations(range(len(scell)),sumVac):
#         scellvac, vacancies = makeCellWithVacancies(scell,indexes)
#         hcell = hashingPoints_update(scellvac, oldvacancies, vacancies)
#         oldvacancies = np.copy(vacancies)
#         SYM = findSym_Dict2(matrixes, scellvac, hcell, vacancies)
#         mylist.append((vacancies,SYM))
#     return mylist
#
# def hashingPoints_update(hdict, points, vacancies):
#     for x, y, z in vacancies:
#         hdict[x][y][z] = False
#     for x, y, z in points:
#         hdict[x][y][z] = True
#     return hdict
#
# def hashingPoints_update2(hdict, points, vacancies):
#     update_dict(hdict, points, True)
#     update_dict(pom, vacancies, False)
#
# def update_dict(hDICT, arrs, boool):
#     for x, y, z in arrs:
#         hDICT[x][y][z] = boool
#
# def makeCellWithVacancies(cell,indexes):
#     indexes = set(indexes)
#     cellVac = []
#     Vac = []
#     for nr, p in enumerate(cell):
#         if nr not in indexes:
#             cellVac.append(p)
#         else:
#             Vac.append(p)
#     return np.array(cellVac), np.array(Vac)
#
# def abc(scell,base,sumVac):
#     mylist = []
#     for indexes in itertools_combinations(range(len(scell)),sumVac):
#         scellvac, vacancies = makeCellWithVacancies(scell,indexes)
#         SYM = findSym(base, scellvac, vacancies)
#         mylist.append((vacancies, SYM))
#     return mylist
#
#
#
#
#
# # import collections
# # import six
#
# # # python 3.8+ compatibility
# # try:
# #     collectionsAbc = collections.abc
# # except:
# #     collectionsAbc = collections
#
# # def dictupdate(d, u):
# #     for k, v in six.iteritems(u):
# #         dv = d.get(k, {})
# #         if not isinstance(dv, collectionsAbc.Mapping):
# #             d[k] = v
# #         elif isinstance(v, collectionsAbc.Mapping):
# #             d[k] = update(dv, v)
# #         else:
# #             d[k] = v
# #     return d
#
# # tymcz = MM.hashingPoints(SUPERCELL2)
# # dictupdate(tymcz,{-1:{-1:{-1:False}}})
# # tymcz
#
# # def abc_Dict(scell,base,sumVac):
# #   hcell = hashingPoints(scell)
# #   mylist = []
# #   for indexes in itrtls_combinations(range(len(scell)),sumVac):
# #     scellvac, vacancies = makeCellWithVacancies(scell,indexes)
# #     hcell = dictupdate(hcell, vacancies)
# #     SYM = findSym_Dict(base, scellvac, hcell, vacancies)
# #     mylist.append((vacancies, SYM))
# #   return mylist
#
#
# # def checkAllCells(scell,sumVac):
# #     Matrixes = generateSymmetryBaseHEX()
# #     mylist = []
# #     for indexes in itrtls_combinations(range(len(scell)),sumVac):
# #         scellvac, vacancies = makeCellWithVacancies(scell,indexes)
# #         SYM = findSym(Matrixes, scellvac, vacancies)
# #         print(SYM,indexes)
# #         if SYM != []:
# #             mylist.append(SYM)
# #     return mylist
#
# # %time lol2 = checkAllCells(ConvSUPERCELL,1)
#

from collections import defaultdict
import matrices_new as mat
import matrices_with_translation_new as mat_t
import numpy as np


def translate_point_to_index(cell, mapper):
    cell_reduced = np.empty(cell.shape[:-1], dtype=int)
    all_trans, all_points = cell_reduced.shape
    for t in range(all_trans):
        for p in range(all_points):
            cell_reduced[t, p] = mapper[cell[t, p].tostring()] #- 1
    return cell_reduced


def show_unevenness(vals):
    if isinstance(vals, set):
        vals = sorted(vals)

    for i in range(len(vals) - 1):
        a = vals[i]
        b = vals[i+1]
        if abs(a - b) < 0.0000001:
            print(i, a, b)


def make_replacer(vals):
    unique_replace = dict()
    for i in range(len(vals) - 1):
        a = vals[i]
        b = vals[i+1]
        if abs(a - b) < 0.0000001:
            unique_replace[a] = b
    return unique_replace


def full_transform(cell, lattice_vectors):
    rotation_cell = cell @ mat.matrices
    backwards_rotation_cell = cell @ mat.matrices_inverse
    matrices_with_translations = mat_t.get_translations(rotation_cell)

    rotation_cell = rotation_cell @ lattice_vectors
    backwards_rotation_cell = backwards_rotation_cell @ lattice_vectors
    matrices_with_translations = matrices_with_translations @ lattice_vectors

    rotation_cell = np.around(rotation_cell, 6)
    backwards_rotation_cell = np.around(backwards_rotation_cell, 6)
    matrices_with_translations = np.around(matrices_with_translations, 6)

    all_cells = np.array([rotation_cell,
                          backwards_rotation_cell,
                          matrices_with_translations])

    # all_possible_values_in_cell = np.unique(matrices_with_translations)
    # unique_replace = make_replacer(all_possible_values_in_cell)
    # unique_vaules = set(unique_replace.keys())
    # show_unevenness(unique_vaules)

    # changed = True
    # while changed:
    #     changed = False
    #     for a, arr in enumerate(all_cells):
    #         for t, trans in enumerate(arr):
    #             for p, point in enumerate(trans):
    #                 for c, cord in enumerate(point):
    #                     if cord in unique_vaules:
    #                         arr[t, p, c] = unique_replace[cord]
    #                         changed = True
    #     print("lol")

    # all_possible_values_in_cell = np.unique(matrices_with_translations)
    # show_unevenness(all_possible_values_in_cell)

    # real_cell = cell @ lattice_vectors
    real_cell = np.around(real_cell, 6)
    point_to_index = {p.tostring(): index for index, p in enumerate(real_cell, 1)}
    translator_from_point_to_index = defaultdict(lambda: -1, point_to_index)

    lst = []
    for arr in all_cells:
        out = translate_point_to_index(arr, translator_from_point_to_index)
        lst.append(out)

    return lst

def reduce_cell(a, b, c):
    mask = c > 18 # invertible matrices
    mask2 = c[mask]
    mask3 = c[~mask]
    mask_all_syms_backwards = mask2 - 19
    trans_above_threshhold = a[mask2]
    trans_below_threshhold = a[mask3]
    inv_trans_of_interest = b[mask_all_syms_backwards]

    reduced_cell = set(range(len(a[0])))

    # jezeli chcemy usunac wszystkie rownowazne punkty dla np osi 6 to
    # odejmujemy nastepny punkt po transformacji oraz wczesniejszy dla osi
    # 6, jezeli os 6 jest w zbiorze to rowniez jest 3 oraz 2 a one same
    # zajmuja sie swoimi rownowaznosciami

    # TODO: sprawdzic czy dla osi minus 4,6 ta zaleznosc jest pokryta
    for trans1, trans2 in zip(trans_above_threshhold, inv_trans_of_interest):
        for i, points in enumerate(zip(trans1, trans2)):
            p1, p2 = points
            if i in reduced_cell and p1 != p2:
                reduced_cell.discard(p1)
                reduced_cell.discard(p2)

    for trans in trans_below_threshhold:
        for i, p in enumerate(trans):
            if i in reduced_cell and i != p:
                reduced_cell.discard(p)

    # TODO: sprawdzic ile(/ktore?) potrzeba sprawdzic transformacji zeby pozbyc
    #  się wszystkich zbędnych punktów.

    return reduced_cell
