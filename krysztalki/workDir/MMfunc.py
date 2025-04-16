from collections import defaultdict

import numpy as np

from workDir.cifParsing import MyCell

# import workDir.Matrix.matrices_new as mat
# import workDir.Matrix.matrices_with_translation_new as mat_t
# from workDir.Matrix.Matrixes import *


def translate_point_to_index(cell, mapper):
    cell_reduced = np.empty(cell.shape[:-1], dtype=int)
    all_trans, all_points = cell_reduced.shape
    for t in range(all_trans):
        for p in range(all_points):
            tttt = tuple(cell[t, p].tolist())
            mapped = mapper[tttt]
            cell_reduced[t, p] = mapped  # - 1
    return cell_reduced


def show_unevenness(vals):
    if isinstance(vals, set):
        vals = sorted(vals)

    for i in range(len(vals) - 1):
        a = vals[i]
        b = vals[i + 1]
        if abs(a - b) < 0.0000001:
            print(i, a, b)


def make_replacer(vals):
    unique_replace = dict()
    for i in range(len(vals) - 1):
        a = vals[i]
        b = vals[i + 1]
        if abs(a - b) < 0.0000001:
            unique_replace[a] = b
    return unique_replace


def put_points_in_cell(points):
    mask_points_above_cell = points > 1
    mask_points_under_cell = points < -1
    points[mask_points_above_cell] -= 2
    points[mask_points_under_cell] += 2
    mask_zero = points == 0
    points[mask_zero] -= 1
    points[mask_zero] += 1

    return points


def full_transform(cell: MyCell):
    """
    Generate the full transformation of a given cell,
    by applying rotation and translation matrices.

    Args:
        cell (np.ndarray[float]): The input cell array.
        lattice_vectors (np.ndarray[float]): The lattice vectors array.

    Returns:
        list: A list containing the transformed cell arrays
        after applying rotation, inverse rotation, and translations.
    """

    # .transpose((0, 2, 1))

    forward_rotation_cell = cell.super_cell @ cell.symmetry_operations
    forward_rotation_cell2 = cell.symmetry_operations @ cell.super_cell.T
    temp = forward_rotation_cell2.transpose((0, 2, 1))
    backwards_rotation_cell = cell.super_cell @ cell.symmetry_operations_inverses

    points_in_place1 = cell.put_points_in_cell(temp)
    points_in_place2 = cell.put_points_in_cell(backwards_rotation_cell)

    # rotated_cells = np.concatenate([points_in_place1, points_in_place2])
    rotated_cells = (points_in_place1, points_in_place2)

    # all_real_cells = all_real_cells @ lattice_vectors
    # all_real_cells = np.around(all_real_cells, 6)

    # rotated_cells = np.concatenate(
    #     (forward_rotation_cell, backwards_rotation_cell), axis=0
    # )
    #
    # all_real_cells = all_real_cells @ lattice_vectors
    # all_real_cells = np.around(all_real_cells, 6)
    #
    # all_real_cells = rotated_cells @ cell.lattice_vectors
    ###### all_real_cells = [rcell @ cell.lattice_vectors for rcell in rotated_cells]

    # backwards_rotation_cell = backwards_rotation_cell @ cell.lattice_vectors
    # matrices_with_translations = matrices_with_translations @ cell.lattice_vectors

    # all_real_cells = np.around(all_real_cells, 6)
    all_real_cells = [np.around(rcell, 6) for rcell in rotated_cells]
    # all_real_cells = [np.around(rcell, 6) for rcell in all_real_cells]
    # backwards_rotation_cell = np.around(backwards_rotation_cell, 6)
    # matrices_with_translations = np.around(matrices_with_translations, 6)

    # rotated_cells = [forward_rotation_cell, backwards_rotation_cell] #, matrices_with_translations]

    # all_possible_values_in_cell = np.unique(matrices_with_translations)
    # unique_replace = make_replacer(all_possible_values_in_cell)
    # unique_vaules = set(unique_replace.keys())
    # show_unevenness(unique_vaules)

    # changed = True
    # while changed:
    #     changed = False
    #     for a, arr in enumerate(rotated_cells):
    #         for t, trans in enumerate(arr):
    #             for p, point in enumerate(trans):
    #                 for c, cord in enumerate(point):
    #                     if cord in unique_vaules:
    #                         arr[t, p, c] = unique_replace[cord]
    #                         changed = True
    #     print("lol")

    # all_possible_values_in_cell = np.unique(matrices_with_translations)
    # show_unevenness(all_possible_values_in_cell)

    # real_cell = cell.super_cell @ cell.lattice_vectors
    # real_cell = np.around(real_cell, 6)
    real_cell = np.around(cell.super_cell, 6)
    # point_to_index = {p.tostring(): index for index, p in enumerate(real_cell)}
    point_to_index = {tuple(p.tolist()): index for index, p in enumerate(real_cell)}
    translator_from_point_to_index = defaultdict(lambda: -1, point_to_index)

    lst = []
    for arr in all_real_cells:
        out = translate_point_to_index(arr, translator_from_point_to_index)
        lst.append(out)
    return lst


def reduce_cell(
    transformed_points_to_indexes,
    transformed_points_to_indexes_inverse,
    mask_syms_normal,
):
    mask = mask_syms_normal > 18  # invertible matrices
    mask2 = mask_syms_normal[mask]
    mask3 = mask_syms_normal[~mask]
    mask_all_syms_backwards = mask2 - 19
    trans_above_threshold = transformed_points_to_indexes[mask2]
    trans_below_threshold = transformed_points_to_indexes[mask3]
    inv_trans_of_interest = transformed_points_to_indexes_inverse[
        mask_all_syms_backwards
    ]

    reduced_cell = set(range(len(transformed_points_to_indexes[0])))

    # jezeli chcemy usunac wszystkie rownowazne punkty dla np osi 6 to
    # odejmujemy nastepny punkt po transformacji oraz wczesniejszy dla osi
    # 6, jezeli os 6 jest w zbiorze to rowniez jest 3 oraz 2 a one same
    # zajmuja sie swoimi rownowaznosciami

    # TODO: sprawdzic czy dla osi minus 4,6 ta zaleznosc jest pokryta
    for trans1, trans2 in zip(trans_above_threshold, inv_trans_of_interest):
        for i, points in enumerate(zip(trans1, trans2)):
            p1, p2 = points
            if i in reduced_cell and p1 != p2:
                reduced_cell.discard(p1)
                reduced_cell.discard(p2)

    for trans in trans_below_threshold:
        for i, p in enumerate(trans):
            if i in reduced_cell and i != p:
                reduced_cell.discard(p)

    # TODO: sprawdzic ile(/ktore?) potrzeba sprawdzic transformacji zeby pozbyc
    #  się wszystkich zbędnych punktów.

    return reduced_cell
