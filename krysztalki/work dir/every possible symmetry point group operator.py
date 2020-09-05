from collections import defaultdict
from crystals import Crystal
from itertools import combinations
import numpy as np
import matrices_new as mat
import matrices_with_translation_new as mat_t
from time import time


def get_super_cell(file_name, size):
    file = getfile(file_name)
    base_type = miller_or_weber(file)

    full_cell, output_atomic_numbers = all_eq_points(file, size)
    compact_cell = full_cell / (size/2) - 1
    rounded_cell = np.around(compact_cell, 10)
    _handle_negative_zeroes(rounded_cell)
    output_cell = np.column_stack((rounded_cell, np.ones(len(rounded_cell))))

    output_cell_indexes = np.arange(len(output_cell))
    lattice_vectors = prepare_lattice_vectors(file.lattice_vectors)

    return output_cell, output_atomic_numbers, output_cell_indexes, \
        lattice_vectors, base_type


def getfile(file_name):
    """
    open cif file from local repository
    or
    download file from Crystallography Open Database

    file_name can be either:
        integer: COD number
        string:  CIF file

    examples:
        file_name = 1000041 # NaCl Fm-3m
        file_name = 'path/to/file.cif'
    """
    if isinstance(file_name, int):
        func = Crystal.from_cod
    elif isinstance(file_name, str):
        func = Crystal.from_cif
    else:
        raise TypeError("Wrong file type")
    return func(file_name)


def miller_or_weber(cell_info):
    # """
    # Determine which coordinates to choose:
    # (3D for Parallelepiped or '4'D for hexagonal).
    # All numbers between [143-194] are for hexagonal groups.
    # """
    international_number = cell_info.symmetry()['international_number']
    if 194 >= international_number >= 143:
        return "w"    # "hP, hR"
    return "m"  # "rest"


def all_eq_points(file, size):
    # """
    # building missing outer walls of a cell
    # with labels
    # """
    reduced_cell = file.supercell(size, size, size).itersorted()
    whole_cell = np.array(
        [np.append(point.coords_fractional, point.atomic_number)
         for point in reduced_cell]
    )

    for i in range(3):
        mask = np.where(whole_cell[:, i] == 0)
        points_with_zeroes = whole_cell[mask]
        points_with_zeroes[:, i] += size
        whole_cell = np.append(whole_cell, points_with_zeroes, axis=0)
    sorted_cell = np.unique(whole_cell, axis=0)

    return sorted_cell[:, :-1], sorted_cell[:, -1]


def _handle_negative_zeroes(cell):
    mask = np.where(cell == 0)
    cell[mask] += 1
    cell[mask] -= 1


def prepare_lattice_vectors(matrix):
    nest_matrix = np.zeros((4, 4), dtype=float)
    nest_matrix[:3,:3] = matrix
    nest_matrix[-1, -1] = 1
    nest_matrix = np.around(nest_matrix, 10)
    return nest_matrix


def translate_point_to_index(cell, mapper):
    cell_reduced = np.empty(cell.shape[:-1], dtype=int)
    all_trans, all_points = cell_reduced.shape
    for t in range(all_trans):
        for p in range(all_points):
            cell_reduced[t, p] = mapper[cell[t, p].tostring()] - 1
    return cell_reduced


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

    real_cell = cell @ lattice_vectors
    real_cell = np.around(real_cell, 6)
    point_to_index = {p.tostring(): index for index, p in enumerate(real_cell, 1)}
    translator_from_point_to_index = defaultdict(int, point_to_index)

    lst = []
    for arr in all_cells:
        out = translate_point_to_index(arr, translator_from_point_to_index)
        lst.append(out)

    return lst




#
SIZE, VACANCIES = 1, 2

# filename = 'cif files/1001686.cif'
# filename = 'cif files/1000003.cif'
# filename = 'cif files/ZnS-Sfaleryt.cif'
filename = 'cif files/1007035.cif'

start = time()
supercell, supercell_labels, supercell_indexes, lattice_vectors, _ = \
    get_super_cell(filename, size=SIZE)

point = np.array([1,1,1,1])

mat_6_3 = np.array([
    [ 1, 1, 0, 0],
    [-1, 0, 0, 0],
    [ 0, 0, 1, 1],
    [ 0, 0, 0, 1]
])

matrix = np.array([
    [-1, 0, 0, 0],
    [ 0, 1, 0, 1],
    [ 0, 0,-1, 0],
    [ 0, 0, 0, 1]
])

matrix_c = np.array([
    [ 1, 0, 0, 0],
    [ 0,-1, 0, 1],
    [ 0, 0, 1, 1],
    [ 0, 0, 0, 1]
])

# x, -y-1/2, z-1/2

ans = (matrix_c @ supercell.T).T

mask_upper = ans > 1
mask_lower = ans < -1

ans[mask_upper] -= 2
ans[mask_lower] += 2
ans = np.unique(ans, axis=0)
ans = np.around(ans, 6)
print(np.array_equal(supercell, ans))
pass
#
# rotcell, rotcell2, slidecell = full_transform(supercell, lattice_vectors)
#
# trans_id_mask = np.arange(len(mat_t.labels_slide))
# all_existing_symmetries = trans_id_mask[np.all(slidecell != -1, axis=1)]
# slidecell_transposed = slidecell.T
#
# count, count_empty = 0, 0
# output = []
# for points_to_remove in combinations(supercell_indexes, VACANCIES):
#     allowed_sym_per_cell = np.full_like(all_existing_symmetries, True, dtype=bool)
#     vacancies_projection = tuple(set() for _ in range(len(all_existing_symmetries)))
#     for vacancies in points_to_remove:
#         name_to_cha = slidecell_transposed[vacancies, all_existing_symmetries]
#         for i, p in enumerate(name_to_cha):
#             vacancies_projection[i].add(p)
#
#     for i, tm in enumerate(zip(vacancies_projection, all_existing_symmetries)):
#         trans, mask = tm
#         for vac in trans:
#             if not slidecell[mask, vac] in trans:
#                 allowed_sym_per_cell[i] = False
#                 break
#
#     allowed_syms_as_labels = mat.labels[all_existing_symmetries[allowed_sym_per_cell]].tolist()
#     z = (points_to_remove, allowed_syms_as_labels)
#     if z[1]:
#         output.append(z)
#         count += 1
#     else:
#         count_empty += 1
#
# print(time() - start)
# with open("output_dzis.txt", "w") as f:
#     f.write(str(count) + "\n")
#     for el in output:
#         f.write(str(el) + "\n")
#
#

matrices = np.array([_matrix_inv_000,

                     _matrix_m_x00, _matrix_m_0y0, _matrix_m_00z,
                     _matrix_m_xy0, _matrix_m_0yz,_matrix_m_x0z,
                     _matrix_m_mx0z, _matrix_m_mxy0, _matrix_m_0myz,

                     _matrix_2_x00, _matrix_2_0y0, _matrix_2_00z,
                     _matrix_2_xy0, _matrix_2_x0z, _matrix_2_0yz,
                     _matrix_2_mxy0, _matrix_2_mx0z, _matrix_2_0myz,

                     _matrix_3_xxx, _matrix_3_mxxx,
                     _matrix_3_xmxx, _matrix_3_xxmx,

                     _matrix_m3_xyz, _matrix_m3_mxyz,
                     _matrix_m3_xmyz, _matrix_m3_xymz,

                     _matrix_4_x00, _matrix_4_0y0, _matrix_4_00z,
                     _matrix_m4_x00, _matrix_m4_0y0, _matrix_m4_00z],

                    dtype=int)