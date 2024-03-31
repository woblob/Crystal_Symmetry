from collections import defaultdict

import Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_new as mat
import \
    Crystal_Symmetry.krysztalki.workDir.Matrix.matrices_with_translation_new as mat_t
from Crystal_Symmetry.krysztalki.workDir.Matrix.Matrixes import *


def translate_point_to_index(cell, mapper):
    cell_reduced = np.empty(cell.shape[:-1], dtype=int)
    all_trans, all_points = cell_reduced.shape
    for t in range(all_trans):
        for p in range(all_points):
            cell_reduced[t, p] = mapper[cell[t, p].tostring()] - 1
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


def full_transform(cell: np.ndarray[float], lattice_vectors: np.ndarray[float]):
    rotation_cell = cell @ mat.matrices
    backwards_rotation_cell = cell @ mat.matrices_inverse
    matrices_with_translations = mat_t.get_translations(rotation_cell)

    # all_cells = np.concatenate(
    #     (rotation_cell, backwards_rotation_cell, matrices_with_translations), axis=0
    # )
    #
    # all_real_cells = all_real_cells @ lattice_vectors
    # all_real_cells = np.around(all_real_cells, 6)
    #
    rotation_cell = rotation_cell @ lattice_vectors
    backwards_rotation_cell = backwards_rotation_cell @ lattice_vectors
    matrices_with_translations = matrices_with_translations @ lattice_vectors

    rotation_cell = np.around(rotation_cell, 6)
    backwards_rotation_cell = np.around(backwards_rotation_cell, 6)
    matrices_with_translations = np.around(matrices_with_translations, 6)

    all_cells = [rotation_cell, backwards_rotation_cell, matrices_with_translations]

    # all_possible_values_in_cell = np.unique(matrices_with_translations)
    # unique_replace = make_replacer(all_possible_values_in_cell)
    # unique_vaules = set(unique_replace.keys())
    # show_unevenness(unique_vaules)

    # changed = True
    # while changed:
    #     changed = False
    #     for a, arr in enumerate(all_cells):
    #         for t, trans in enumerate(arr):
    #             for p, point in enumerate(trans):
    #                 for c, cord in enumerate(point):
    #                     if cord in unique_vaules:
    #                         arr[t, p, c] = unique_replace[cord]
    #                         changed = True
    #     print("lol")

    # all_possible_values_in_cell = np.unique(matrices_with_translations)
    # show_unevenness(all_possible_values_in_cell)

    real_cell = cell @ lattice_vectors
    real_cell = np.around(real_cell, 6)
    point_to_index = {p.tostring(): index for index, p in enumerate(real_cell, 1)}
    translator_from_point_to_index = defaultdict(lambda: -1, point_to_index)

    lst = []
    for arr in all_cells:
        out = translate_point_to_index(arr, translator_from_point_to_index)
        lst.append(out)

    return lst


def reduce_cell(a, b, c):
    mask = c > 18  # invertible matrices
    mask2 = c[mask]
    mask3 = c[~mask]
    mask_all_syms_backwards = mask2 - 19
    trans_above_threshhold = a[mask2]
    trans_below_threshhold = a[mask3]
    inv_trans_of_interest = b[mask_all_syms_backwards]

    reduced_cell = set(range(len(a[0])))

    # jezeli chcemy usunac wszystkie rownowazne punkty dla np osi 6 to
    # odejmujemy nastepny punkt po transformacji oraz wczesniejszy dla osi
    # 6, jezeli os 6 jest w zbiorze to rowniez jest 3 oraz 2 a one same
    # zajmuja sie swoimi rownowaznosciami

    # TODO: sprawdzic czy dla osi minus 4,6 ta zaleznosc jest pokryta
    for trans1, trans2 in zip(trans_above_threshhold, inv_trans_of_interest):
        for i, points in enumerate(zip(trans1, trans2)):
            p1, p2 = points
            if i in reduced_cell and p1 != p2:
                reduced_cell.discard(p1)
                reduced_cell.discard(p2)

    for trans in trans_below_threshhold:
        for i, p in enumerate(trans):
            if i in reduced_cell and i != p:
                reduced_cell.discard(p)

    # TODO: sprawdzic ile(/ktore?) potrzeba sprawdzic transformacji zeby pozbyc
    #  się wszystkich zbędnych punktów.

    return reduced_cell
