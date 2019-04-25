import sympy as sp
import numpy as np

def _getSliceOfEqPosition(LINES):
    for indexL, line in enumerate(LINES,1):
        if '_symmetry_equiv_pos_as_xyz' in line:
            break
    for indexR, line in enumerate(LINES[indexL:],indexL):
        if 'loop_' in line:
            return indexL,indexR
    return None

def _getTypesOfAtoms(LINES):
    index = -1 
    found = False
    mylist = []
    for line in LINES:
        if "_atom" in line:
            if not found:
                index += 1
                if '_atom_site_fract_x' in line:
                    found = True                    
        else:
            if not "loop_" == line:
                mylist.append(line)
            else:
                break
    return mylist, index

def _getBasePos(STRINGS,nr):
    mytepmlist = []
    x,y,z = sp.symbols("x y z")
    for STRING in STRINGS:
        xel, yel, zel = STRING.split()[nr:nr+3]        
        mydict = {x:xel,y:yel,z:zel}
        mytepmlist.append(mydict)
    return mytepmlist

def _getPositionsFromFile(lines,SUBS):
    x,y,z = sp.symbols("x y z")
    mojekoord = []
    for SUB in SUBS:
        for line in lines:
            koord = line.split(',')
            mojalista = []
            for i in range(3):
                expr = float(sp.sympify(line)[i].evalf(2,subs=SUB))
                mojalista.append(expr)
            mojekoord.append(mojalista)
    return np.around(np.unique(mojekoord,axis = 0),6)

def _insideOf1Cell(cell):
    cell[cell<0] += 1
    cell[cell>1] -= 1
    return np.unique(cell,axis=0)

def _allEqPoints(CELL):
    CELLwith0s = CELL[~CELL.all(axis=1)]
    for point in CELLwith0s:
        CELL = np.append(CELL,_eqPoints(point),axis =0)
    return np.unique(CELL,axis=0)

def _eqPoints(POINT):
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

def getCellFromFile(file_name):
    file = [line.rstrip('\n') for line in open(file_name)]
    posL, posR = _getSliceOfEqPosition(file)   
    alist = _getTypesOfAtoms(file[posR+1:])
    SUBS = _getBasePos(*alist)      
    cell = _getPositionsFromFile(file[posL:posR],SUBS)
    cell = _insideOf1Cell(cell)
    cell = _allEqPoints(cell)
    return cell