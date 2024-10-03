import datetime
from itertools import combinations
from time import time

import numpy as np

import workDir.Matrix.matrices_new as mat
import workDir.cifParsing as cPrs
from workDir.MMfunc import full_transform, reduce_cell
from SYMfunc import saveOutput

# filename = '1100043.cif'
filename = 1100043
supercell_size, vacancies_amount = 2, 2 # Processing time (3, 2): ~5 sec

start = time()
SUPERCELL, SUPERCELL_labels, SUPERCELL_indexes, lattice_vectors, _ = (
    cPrs.get_super_cell(filename, size=supercell_size)
)

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

all_transformed_points_to_indexes_transposed = all_transformed_points_to_indexes.T

count = 0
output = []
for points_to_remove in combinations(SUPERCELL_indexes, vacancies_amount):
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

print(f"processing time: {(time() - start):.1f}s")

saveOutput(output, count=count)
