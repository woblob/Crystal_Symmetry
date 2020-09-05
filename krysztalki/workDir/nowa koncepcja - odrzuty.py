# sgg = all_transformed_points_to_indexes[lol].T
# sgg2 = np.empty_like(sgg, dtype=bool)
#
# for i, row in enumerate(sgg, 1):
#     sgg2[i-1] = (row == i)
#
#
# def find_break_symmetry_points(cell_indexes, trans):
#     cli = np.array(cell_indexes)
#     transpose_trans = all_transformed_points_to_indexes[trans].T
#     return {p for p in cli if np.any(transpose_trans[p-1] == p)}
#     # return {p for p in cli if p not in transpose_trans[p]}
#
#
# dupa = find_break_symmetry_points(SUPERCELL_indexes, lol)
# dupa_len = len(dupa)
# dupa_SC_len = len(SUPERCELL)
