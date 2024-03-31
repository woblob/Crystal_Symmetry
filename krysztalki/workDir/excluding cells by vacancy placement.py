def makeUVW(p1, p2=0):
    UVW = p1 - p2
    uvw_max = np.amax(np.abs(UVW))
    if uvw_max:
        UVW = UVW / uvw_max
    return UVW


# def checkUVWforINT(uvw):
#   return issubclass(uvw.dtype.type, np.integer)


def checkforINT(UVW):
    if issubclass(UVW.dtype.type, np.integer):
        return True
    else:
        uvw_int = UVW.astype(int)
        return porownajPunkty(UVW, uvw_int)


def func(UVWs):
    return all(
        checkforINT(makeUVW(UVWs[e1], UVWs[e2])) for e1, e2 in COMB(range(len(UVWs)), 2)
    )


def all_same(func, items):
    val = func(items[0])
    return all(np.array_equal(func(item), val) for item in items[1:])


def funcvar(vacs):
    return (
        all_same(makeUVW, vacs)
        and not all_same(np.linalg.norm, vacs)
        and all_same(checkforINT, list(map(makeUVW, vacs)))
        and func(vacs)
    )


def abc_Dict(scell, base, sumVac):
    mylist = []
    for indexes in itrtls_combinations(range(len(scell)), sumVac):
        scellvac, vacancies = makeCellWithVacancies(scell, indexes)
        hcell = hashingPoints(scellvac)
        SYM = findSym_Dict(base, scellvac, hcell, vacancies)
        mylist.append(
            [
                SYM != [],
                all_same(makeUVW, vacancies),
                all_same(np.linalg.norm, vacancies),
                all_same(checkforINT, list(map(makeUVW, vacancies))),
                func(vacancies),
            ]
        )
        mylist.append([SYM != [], funcvar(vacancies)])
        mylist.append((vacancies, SYM))
    return mylist


myuvw = np.array([1, 1, 2])
issubclass(myuvw.dtype.type, np.integer)

import numpy as np


def makeUVW(p1, p2=0):
    UVW = p1 - p2
    uvw_max = np.amax(np.abs(UVW))
    if uvw_max:
        UVW = UVW / uvw_max
    return UVW


# def checkUVWforINT(uvw):
#   return issubclass(uvw.dtype.type, np.integer)


def checkforINT(UVW):
    if issubclass(UVW.dtype.type, np.integer):
        return True
    else:
        uvw_int = UVW.astype(int)
        return MM.porownajPunkty(UVW, uvw_int)


from itertools import combinations as COMB


def func(UVWs):
    return all(
        checkforINT(makeUVW(UVWs[e1], UVWs[e2])) for e1, e2 in COMB(range(len(UVWs)), 2)
    )


def all_same(func, items):
    val = func(items[0])
    return all(np.array_equal(func(item), val) for item in items[1:])


def funcvar(vacs):
    print(
        all_same(makeUVW, vacs),
        all_same(np.linalg.norm, vacs),
        all_same(checkforINT, list(map(makeUVW, vacs))),
        func(vacs),
    )


#   return all_same(makeUVW, vacs) or \
#          all_same(np.linalg.norm, vacs) or \
#          all_same(checkUVWforINT, list(map(makeUVW,vacs))) or \
#          all_same(func, vacs)

p0 = np.array([0, 0, 0])
p1 = np.array([0, 0, 0.5])
p2 = np.array([1, 2, 1])
p3 = np.array([2, 1, 1])
p4 = np.array([0.5, 1, 0.5])

zpkt = np.array([p2, p3, p4])

funcvar(zpkt)

# np.linalg.norm(p2) # odleglosc punktu od zera

# czy na tej samej osi: all_same(makeUVW)
# czy wartosci sa calkowite  checkUVWforINT(p1)
# czy uvw pomiedzy puntkami jest prostopadle do uwv przechodzacego przez p(0,0,0)
# czy odleglosc jest taka sama, czy ten test ma sens? all_same(np.linalg.norm)


# def abc_Dict(scell,base,sumVac):
#   mylist = []
#   for indexes in itrtls_combinations(range(len(scell)),sumVac):
#     scellvac, vacancies = makeCellWithVacancies(scell,indexes)
#     hcell = hashingPoints(scellvac)
#     SYM = findSym_Dict(base, scellvac, hcell, vacancies)
# #     if SYM == []:
#     mylist.append([vacancies, \
#                             SYM == [],\
#                             all_same(makeUVW, vacs), \
#                             all_same(np.linalg.norm, vacs) , \
#                             all_same(checkforINT, list(map(makeUVW,vacs))) , \
#                             func(vacs)]
#
#                  )
#   return mylist
#
#
#     mylist.append((vacancies, SYM))


# print('checkUVWforINT')
# %timeit checkUVWforINT(p1)
# print()
# print('makeUVW w/o 0 aka jakie jest uvw wzgledem zera')
# %timeit makeUVW(p3)
# print()
# print('makeUVW w 0 aka jakie jest uvw pommiedzy punktami')
# %timeit makeUVW(p4, p2)
#
#
#
# %timeit all_same(makeUVW,p123)
# %timeit all_same(np.linalg.norm, p123)
# %timeit funcvar(p123)


# def checksmth(arr):
# #     arr2 = np.rint(arr)
# #     arr3 = np.isclose(arr,arr2)
# #     print(arr)
# #     print(arr2)
# #     print(arr3)
# #     print(arr[arr3])
