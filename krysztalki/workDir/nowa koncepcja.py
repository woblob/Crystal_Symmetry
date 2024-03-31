import datetime
from itertools import combinations
from time import time

import numpy as np

import cifParsing as cPrs
import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new as mat
from MMfunc import full_transform, reduce_cell

size_num, vacs_num = 3, 2  # (s=4,v=2) => 9 sec!

start = time()
SUPERCELL, SUPERCELL_labels, SUPERCELL_indexes, lattice_vectors, _ = (
    cPrs.get_super_cell("cif files/1001686.cif", size=size_num)
)
# cPrs.get_super_cell('cif files/ZnS-Sfaleryt.cif', size=size_num)

(
    all_transformed_points_to_indexes,
    all_transformed_points_to_indexes_inverse,
    all_transformed_points_to_indexes_translations,
) = full_transform(SUPERCELL, lattice_vectors)

trans_id_mask = np.arange(len(mat.matrices))
trans_id_mask_inverted = np.arange(len(mat.matrices_inverse))

mask_all_syms_normal = trans_id_mask[
    np.all(all_transformed_points_to_indexes != -1, axis=1)
]

reduced_cell_set = reduce_cell(
    all_transformed_points_to_indexes,
    all_transformed_points_to_indexes_inverse,
    mask_all_syms_normal,
)

allowed_sym_per_cell = np.full_like(mask_all_syms_normal, True, dtype=bool)
# allowed_sym_per_cell_backward = np.full_like(mask_all_syms_backward, True, dtype=bool)
# a, b = np.split(mask_all_syms_normal, [-len(mask_all_syms_backward)])
# vacancies_projection = tuple(set() for _ in range(len(mask_all_syms_normal)))

all_transformed_points_to_indexes_transposed = all_transformed_points_to_indexes.T

count = 0
output = []
for points_to_remove in combinations(SUPERCELL_indexes, vacs_num):
    allowed_sym_per_cell = np.full_like(mask_all_syms_normal, True, dtype=bool)
    vacancies_projection = tuple(set() for _ in range(len(mask_all_syms_normal)))
    for p2r in points_to_remove:
        for i, p in enumerate(
            all_transformed_points_to_indexes_transposed[p2r, mask_all_syms_normal]
        ):
            vacancies_projection[i].add(p)

    arr = all_transformed_points_to_indexes

    for i, (transSet, maskIndex) in enumerate(
        zip(vacancies_projection, mask_all_syms_normal)
    ):
        for vac in transSet:
            if not arr[maskIndex, vac] in transSet:
                allowed_sym_per_cell[i] = False
                break

    z = (
        points_to_remove,
        mat.labels[mask_all_syms_normal[allowed_sym_per_cell]].tolist(),
    )
    if z[1]:
        output.append(z)
    else:
        count += 1

print(time() - start)

# with open("output_dzis.txt", "wb") as f:
#     pickle.dump(output, f)
with open(f"outputs/output_{datetime.datetime.now()}.txt", "w") as f:
    f.write(str(count) + "\n")
    for el in output:
        f.write(str(el) + "\n")


print("lol")
# # np.ix_(list_of_lists)
# # dodac inversy 3 i 4 albo do zestawu macierzy albo na bierząco
#
