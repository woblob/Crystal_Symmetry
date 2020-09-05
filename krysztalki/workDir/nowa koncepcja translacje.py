import numpy as np
import matrices_new as mat
import cifParsing as cPrs
from MMfunc import full_transform, reduce_cell
from itertools import combinations, chain
from time import time
from collections import defaultdict
import matrices_with_translation_new as mat_t

SIZE, VACANCIES = 2, 2 # (s=4,v=2) => 9 sec !

# filename = 'cif files/1001686.cif'
# filename = 'cif files/1000003.cif'
# filename = 'cif files/ZnS-Sfaleryt.cif'
filename = 'cif files/1007035.cif'

start = time()
supercell, supercell_labels, supercell_indexes, lattice_vectors, _ = \
    cPrs.get_super_cell(filename, size=SIZE)

rotcell, rotcell2, slidecell = full_transform(supercell, lattice_vectors)

trans_id_mask = np.arange(len(mat_t.labels_slide))

all_existing_symmetries = trans_id_mask[np.all(slidecell != -1, axis=1)]

# reduced_cell_set = reduce_cell(all_transformed_points_to_indexes,
#                                all_transformed_points_to_indexes_backwards,
#                                all_existing_symmetries)


slidecell_transposed = slidecell.T

count, count_empty = 0, 0
output = []
for points_to_remove in combinations(supercell_indexes, VACANCIES):
    allowed_sym_per_cell = np.full_like(all_existing_symmetries, True, dtype=bool)
    vacancies_projection = tuple(set() for _ in range(len(all_existing_symmetries)))
    for vacancies in points_to_remove:
        for i, p in enumerate(
                all_transformed_points_to_indexes_transposed[
                    vacancies, all_existing_symmetries
                ]):
            vacancies_projection[i].add(p)

    arr = all_transformed_points_to_indexes

    for i, tm in enumerate(zip(vacancies_projection, all_existing_symmetries)):
        trans, mask = tm
        for vac in trans:
            if not arr[mask, vac] in trans:
                allowed_sym_per_cell[i] = False
                break

    allowed_syms_as_labels = mat.labels[all_existing_symmetries[allowed_sym_per_cell]].tolist()
    z = (points_to_remove, allowed_syms_as_labels)
    if z[1]:
        output.append(z)
        count += 1
    else:
        count_empty += 1

print(time() - start)
import pickle
# with open("output_dzis.txt", "wb") as f:
#     pickle.dump(output, f)
with open("output_dzis.txt", "w") as f:
    f.write(str(count) + "\n")
    for el in output:
        f.write(str(el) + "\n")


print("lol")
# # np.ix_(list_of_lists)
# # dodac inversy 3 i 4 albo do zestawu macierzy albo na bierząco
#
# from anytree import NodeMixin
#
#
# class Cell(NodeMixin):
#     def __init__(self, vacancies, last_index, parent=None, children=None):
#         super().__init__()
#         self.vacancies = vacancies
#         self.last_index = last_index
#         self.parent = parent
#         vacancies_projection = \
#             tuple(set() for _ in range(len(all_existing_symmetries))) # self?
#         if parent:
#             self.all_prev_indices = parent.all_prev_indices + [self.last_index]
#         else:
#             self.all_prev_indices = [self.last_index]
#         if children:
#             self.children = children
#
#     def make_tree(self, depth):
#         for i in range(self.last_index + 1, len(supercell)):
#             pass
#
#
# # np.isin