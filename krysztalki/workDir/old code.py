def usunkoor(koorZEW, oski):  # isc od tylu i usuwac sprawdzany punkt
    koorWEW = koorZEW.copy()
    for os in oski:
        j = 1
        while j < len(koorWEW):
            for punktdous in listadous(os, koorWEW[j]):
                i = findindex(punktdous, koorWEW.T[:, j:])
                if i + 1 and porownajPunkty(koorWEW[i + j], punktdous):
                    koorWEW = np.delete(koorWEW, i + j, 0)
            j += 1
    return koorWEW


def usunkoor_mod(koorZEW, oski):  # , Matrixes):
    koorWEW = koorZEW.copy()
    listofnr = list(range(len(koorWEW)))
    Matrixes = generateSymetryBase()
    for os0, os1 in oski:
        TRANS = Matrixes[os0][os1]
        j = 1
        while j < len(koorWEW):
            for punktdous in listadous(TRANS, koorWEW[j]):
                i = findindex(punktdous, koorWEW.T[:, j:])
                if i + 1 and porownajPunkty(koorWEW[i + j], punktdous):
                    koorWEW = np.delete(koorWEW, i + j, 0)
                    del listofnr[i + j]
            j += 1
    return listofnr  # zip(koorWEW, listofnr)
