# from krysztalki.workDir.Matrix.matrices_new import labels
# from krysztalki.workDir.cifParsing import MyCell
# from krysztalki.workDir.MMfunc import full_transform, reduce_cell
# from krysztalki.SYMfunc import saveOutput

# filename = "krysztalki/workDir/cif files/1001686.cif"
# # filename = 1509138
# supercell_size, vacancies_amount = 1, 1  # Processing time (3, 2): ~5 sec

# start = time()

# # super_cell, super_cell_atomic_numbers, super_cell_indexes
# # SUPERCELL,   SUPERCELL_labels,      SUPERCELL_indexes,   , _
# myCell = MyCell(filename, size=supercell_size)

# (
#     all_transformed_points_to_indexes,
#     all_transformed_points_to_indexes_inverse,
# ) = full_transform(myCell)

# trans_id_mask = np.arange(len(myCell.symmetry_operations))
# trans_id_mask_inverted = np.arange(len(myCell.symmetry_operations_inverses))

# mask_all_syms_normal = trans_id_mask[
#     np.all(all_transformed_points_to_indexes != -1, axis=1)
# ]

# reduced_cell_set = reduce_cell(
#     all_transformed_points_to_indexes,
#     all_transformed_points_to_indexes_inverse,
#     mask_all_syms_normal,
# )

# allowed_sym_per_cell = np.full_like(mask_all_syms_normal, True, dtype=bool)

# all_transformed_points_to_indexes_transposed = all_transformed_points_to_indexes.T

# count = 0
# output = []
# for points_to_remove in combinations(myCell.super_cell_indexes, vacancies_amount):
#     allowed_sym_per_cell = np.full_like(mask_all_syms_normal, True, dtype=bool)
#     vacancies_projection: Tuple[Set[int], ...] = tuple(
#         set() for _ in range(len(mask_all_syms_normal))
#     )
#     for p2r in points_to_remove:
#         for i, p in enumerate(
#             all_transformed_points_to_indexes_transposed[p2r, mask_all_syms_normal]
#         ):
#             vacancies_projection[i].add(p)

#     arr = all_transformed_points_to_indexes

#     for i, (transSet, maskIndex) in enumerate(
#         zip(vacancies_projection, mask_all_syms_normal)
#     ):
#         for vac in transSet:
#             if not arr[maskIndex, vac] in transSet:
#                 allowed_sym_per_cell[i] = False
#                 break

#     z = (
#         points_to_remove,
#         # [SUPERCELL[index].tolist() for index in points_to_remove],
#         labels[mask_all_syms_normal[allowed_sym_per_cell]].tolist(),
#     )
#     if z[1]:
#         output.append(z)
#     else:
#         count += 1

# print(f"processing time: {(time() - start):.1f}s")
