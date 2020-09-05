from crystals import Crystal
import numpy as np

def eqPoints(POINT):
    """
    Get point and make all combinations of ones and zeros by addding numbers in binary 
    """    
    zera = np.where(POINT == 0)[0]
    ilepow = 2**zera.size
    mylist = np.empty((ilepow-1,3))
    for n in range(1,ilepow):
        val = f"{n:b}" 
        jkl = zera.size - len(val)
        if jkl:
            val = '0'*jkl + val
        NP = POINT.copy()
        for indexV, indexP in enumerate(zera):
            if int(val[indexV]):
                NP[indexP] += 1
        mylist[n-1] = NP
    return mylist

def allEqPoints(CELL):
    """
    Find all points with zeros and add their equivalent to make whole cell 
    From [0,0,0] to [1,1,1]
    """
    CELLwith0s = CELL[~CELL.all(axis=1)]
    for point in CELLwith0s:
        CELL = np.append(CELL,eqPoints(point),axis =0)
    return np.unique(CELL,axis=0)

def millerORweber(ITN):
    """
    Determine which kind of coordinates to use
    """
    if  ITN > 194 or ITN < 143:
        return "m" #"rest"
    return "w"    #"hP, hR"

def getSCell(func, filename, size): 
    """
    Get cell from cod/cif/else. 
    Expand it to supercell size.
    Place points between -1 and less than 1
    Add missing walls of a cell.
    """
    file = func(filename)
    basetype = millerORweber(file.symmetry()['international_number'])
    points = file.supercell(size,size,size).itersorted()      
    if size%2:
        cell = np.array([1,1,1])
    else:
        cell = points.__next__().coords_fractional/(size/2)-1
    for el in points:
        cell = np.vstack((cell,el.coords_fractional/(size/2)-1))
    return allEqPoints(cell), basetype
