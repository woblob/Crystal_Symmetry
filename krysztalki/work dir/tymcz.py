import numpy as np
import cifParsing as CPRS
from importlib import reload
from Profiling import profiler
import matrices_new as MAT
from itertools import combinations as combinations
from bisect import bisect_right

# CPRS = reload(CPRS)

SUPERCELL, _ = CPRS.getSCell(1000041 , size = 2) 
# SUPERCELL, _ = CPRS.getSCell2(1100043 , size = 2) 
# SUPERCELL, _ = CPRS.getSCell2(1000004 , size = 2) 
SUPERCELL[:2]

def check_antisyms_in_cell(Cell, Vacancies, matrices):
# def funcforsyms(Cell: numpy2darray(float), matrixes: numpy3darray(int)) -> numpy1darray(bool):
    transformed_vacancies = Vacancies @ MAT.all_matrixes
    mask = np.full(len(matrices), True, dtype=bool) # matrixes.shape[0] instaed of len()
    for i, points in enumerate(transformed_vacancies):
        for x,y,z in points:
            if np.any((Cell[:,0] == x) & (Cell[:,1]==y) & (Cell[:,2]==z)):
                mask[i] = False
                break
    return mask

def True_syms(propable_symmetries, present_symmetries):
    true_syms = propable_symmetries.copy()
    j = 0
    for i, mat in enumerate(propable_symmetries):
        if mat:
            true_syms[i] = present_symmetries[j]
            j += 1
    return true_syms

def output_symmetries(Symmerties):
    return np.ma.masked_where(~Symmerties, MAT.all_labels).compressed().tolist()

output_symmetries(np.array([False]*33))

def get_matrixes(allowed_matrixes):
    return np.array([mat for mat, mask in zip(MAT.all_matrixes, np.ma.masked_where(allowed_matrixes, MAT.all_labels).mask) if mask])

def make_cell_with_vacancies(cell,indexes):
    indexes = set(indexes)
    cellVac = []
    Vac = []
    for nr, p in enumerate(cell):
        if nr not in indexes:
            cellVac.append(p)
        else:
            Vac.append(p)
    return np.array(cellVac), np.array(Vac)

# @profiler("tottime")
def check_syms_in_cell(Cell, matrixes):
# def func(Cell: numpy2darray(float),
#          matrixes: numpy3darray(int)) -> mask numpy1darray(bool):
    """
    making all transformations of a cell
    bringing back the order inside each transformed cell
    checking if their are the same cells as original cell
    """ 
    transformed_points = Cell @ matrixes 
    transformed_points_sorted = np.array([np.unique(points, axis=0) for points in transformed_points])
    return np.array([np.array_equal(points, Cell) for points in transformed_points_sorted])

def check_all_cells2(scell, sumVac):
    mylist = []
    labels_in = MAT.all_labels
    matrixes = MAT.all_matrixes
    for indexes in combinations(range(len(scell)), sumVac): 
        scellvac, vacancies = make_cell_with_vacancies(scell, indexes)
        allowed_matrixes = check_antisyms_in_cell(scellvac, vacancies, matrixes)
        if np.any(allowed_matrixes):
            SYM = check_syms_in_cell(scellvac, get_matrixes(allowed_matrixes))
            true_syms = True_syms(allowed_matrixes, SYM)
            output = output_symmetries(true_syms)
        else:
            output = []
        mylist.append((vacancies.tolist(), output))
    return count, count_same  #len(mylist), mylist

def check_all_cells3(scell, sumVac):
    mylist = []
    labels_in = MAT.all_labels
    matrixes = MAT.all_matrixes
    for indexes in combinations(range(len(scell)), sumVac): 
        scellvac, vacancies = make_cell_with_vacancies(scell, indexes)
        allowed_matrixes = check_antisyms_in_cell(scellvac, vacancies, matrixes)
        if np.any(allowed_matrixes):
            output = output_symmetries(allowed_matrixes)
        else:
            output = []
        mylist.append((vacancies.tolist(), output))
    return len(mylist), mylist

def check_all_cells4(scell, sumVac):
    mylist = []
    labels_in = MAT.all_labels
    matrixes = MAT.all_matrixes
    for indexes in combinations(range(len(scell)), sumVac): 
        scellvac, vacancies = make_cell_with_vacancies(scell, indexes)
        allowed_matrixes = check_antisyms_in_cell(scellvac, vacancies, matrixes)
        output = output_symmetries(allowed_matrixes)
        mylist.append((vacancies.tolist(), output))
    return len(mylist), mylist

%time out2 = check_all_cells2(SUPERCELL, 2)

%timeit out3 = check_all_cells3(SUPERCELL, 2)

out2

%time check_syms_in_cell(SUPERCELL, MAT.all_matrixes)

def check_all_cells2(scell, sumVac):
    mylist = []
    labels_in = MAT.all_labels
    matrixes = MAT.all_matrixes
    for indexes in combinations(range(len(scell)), sumVac): 
        scellvac, vacancies = make_cell_with_vacancies(scell, indexes)
        allowed_matrixes = check_antisyms_in_cell(scellvac, vacancies, matrixes)
        if np.any(allowed_matrixes):
            SYM = check_syms_in_cell(scellvac, get_matrixes(allowed_matrixes))
            true_syms = True_syms(allowed_matrixes, SYM)
            output = output_symmetries(true_syms)
        else:
            output = []
        mylist.append((vacancies.tolist(), output))
    return len(mylist), mylist

%time out2 = check_all_cells2(SUPERCELL, 2)

def check_all_cells_recursive(scell, sumVac, previous_point_index=0):
    scellvac, vacancies = make_cell_with_vacancies(scell, indexes)
    allowed_matrixes = check_antisyms_in_cell(scellvac, vacancies, matrixes)
    if sumVac > 0:
        mylist = []
        if np.any(allowed_matrixes):
            SYM = check_syms_in_cell(scellvac, get_matrixes(allowed_matrixes))
            true_syms = True_syms(allowed_matrixes, SYM)
            reduced_cell, reduced_cell_indexes = reduce_cell_by_symmetry(CELL, MATRIXES)

            wskaznik = bisect_right(reduced_cell_indexes, previous_point_index)
        # dla powstalej komorki przejsc po kazdym punkcie i rekursywnie zwrocic powstaly zestaw symmetrii na dane vakancje
        # limit sumVac
            for indexes in reduced_cell_indexes[wskaznik:]:
                check_all_cells_recursive(scell, sumVac-1, wskaznik)
                    output = output_symmetries(true_syms)
                else:
                    output = []
                mylist.append((vacancies.tolist(), output))
        return mylist



%time out2 = check_all_cells_recursive(SUPERCELL, 2)