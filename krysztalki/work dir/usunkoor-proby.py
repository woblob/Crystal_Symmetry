def check_syms_in_cell(Cell, matrixes):
    transformed_points = Cell @ matrixes 
    transformed_points_sorted = np.array([np.unique(points, axis=0) for points in transformed_points])
    return ~ np.array([np.array_equal(points, Cell) for points in transformed_points_sorted])

# %time check_syms_in_cell(SUPERCELL, MAT.all_matrixes)

# def pick_matrixes_by_index(masked_indexes, matrixes=MAT.all_matrixes):
#     return np.ma.masked_where(masked_indexes, matrixes).compressed()

def compare_points(p1, p2):
    for a, b in zip(p1, p2):
        if a != b:
            return False
    return True

def get_all_transformed_points(matrix, base_point):
    transformed_point = matrix @ base_point
    while not compare_points(transformed_point, base_point):
        yield transformed_point
        transformed_point = matrix @ transformed_point  

def get_matrixes_for_specific_point_group(symmetries):
    output = np.ma.masked_where(symmetries, MAT.all_labels)
    mymask = np.array([np.full((3,3), val) for val in output.mask])
    return MAT.pick_matrices_by_index(mymask)

# @profiler("time")
def reduce_cell_by_symmetry(cell, matrixes):
    cell_dict = {tuple(point): i for i, point in enumerate(cell, 1)}
    for matrix in matrixes:
        for base_point in cell:
            if cell_dict[tuple(base_point)]:
                for point in get_all_transformed_points(matrix, base_point):
                    cell_dict[tuple(point)] = 0
            
    reduced_cell, reduced_cell_indexes = [el for el in zip(*((point, index) for point, index in cell_dict.items() if index))]
    reduced_cell, reduced_cell_indexes = np.array(reduced_cell), np.array(reduced_cell_indexes)
    reduced_cell_indexes -= 1
    return reduced_cell, reduced_cell_indexes

import numpy as np
import cifParsing as CPRS
import MMfunc as MM
import matrices_new as MAT
from Profiling import profiler

SUPERCELL, _ = CPRS.getSCell(1100043, size=10) #'cif files/ZnS-Sfaleryt.cif'
# SUPERCELL

# _ = np.c_[SUPERCELL, np.ones(len(SUPERCELL))] #add ones to each point in SUPERCELL


SYM = check_syms_in_cell(SUPERCELL, MAT.all_matrixes)
matrixes_ZnS = get_matrixes_for_specific_point_group(SYM)
%time new_cell, new_cell_indexes = reduce_cell_by_symmetry(SUPERCELL, matrixes_ZnS)


def sil(num):
    if 0 <= num < 2:
        return 1
    elif num < 0:
        raise ValueError("factorial out of negative number")

    prod = 2
    for i in range(3, num + 1):
        prod *= i
    return prod    

def NchooseK(n, k):
    for i in range(1, k):
        n *= n - i
    return n // sil(k)

vacs = 2

NchooseK(476,vacs), NchooseK(8631,vacs)

def get_all_transformed_points_hash(matrix, base_point):
    transformed_point = base_point * matrix
    while not compare_points(transformed_point, base_point):
        yield transformed_point
        transformed_point = transformed_point * matrix

# @profiler("time")
def reduce_cell_by_symmetry(cell, matrixes):
    cell_copy = [Hashable(point) for point in cell]
    cell_dict = {Hashable(point): True for point in cell}
    for matrix in matrixes:
        for base_point in cell_copy:
            if cell_dict[base_point]:
                for point in get_all_transformed_points(matrix, base_point):
                    cell_dict[Hashable(point)] = False
    return np.array([point for point, v in cell_dict.items() if v])
#     return [point for point, v in cell_dict.items() if v]
