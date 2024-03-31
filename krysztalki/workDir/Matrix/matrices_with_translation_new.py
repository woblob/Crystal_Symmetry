import numpy as np

# h1 = 1 / 2
# q1 = 1 / 4
# q2 = 2 / 4
# q3 = 3 / 4

h1 = 1 / 2 * 2
q1 = 1 / 4 * 2
q2 = 2 / 4 * 2
q3 = 3 / 4 * 2


_translation_a_h1 = np.array([h1, 0, 0])
_translation_b_h1 = np.array([0, h1, 0])
_translation_c_h1 = np.array([0, 0, h1])

_translation_n_ab_h1 = np.array([h1, h1, 0])
_translation_n_bc_h1 = np.array([0, h1, h1])
_translation_n_ac_h1 = np.array([h1, 0, h1])
_translation_n_abc_h1 = np.array([h1, h1, h1])

_translation_a_q1 = np.array([q1, 0, 0])
_translation_b_q1 = np.array([0, q1, 0])
_translation_c_q1 = np.array([0, 0, q1])

_translation_a_q2 = np.array([q2, 0, 0])
_translation_b_q2 = np.array([0, q2, 0])
_translation_c_q2 = np.array([0, 0, q2])

_translation_a_q3 = np.array([q3, 0, 0])
_translation_b_q3 = np.array([0, q3, 0])
_translation_c_q3 = np.array([0, 0, q3])

_translation_d_ab_q1 = np.array([q1, q1, 0])
_translation_d_bc_q1 = np.array([0, q1, q1])
_translation_d_ac_q1 = np.array([q1, 0, q1])
_translation_d_abc_q1 = np.array([q1, q1, q1])

all_translations = np.array(
    [
        _translation_a_h1,
        _translation_b_h1,
        _translation_c_h1,
        _translation_n_ab_h1,
        _translation_n_bc_h1,
        _translation_n_ac_h1,
        _translation_n_abc_h1,
        _translation_a_q1,
        _translation_b_q1,
        _translation_c_q1,
        _translation_a_q2,
        _translation_b_q2,
        _translation_c_q2,
        _translation_a_q3,
        _translation_b_q3,
        _translation_c_q3,
        _translation_d_ab_q1,
        _translation_d_bc_q1,
        _translation_d_ac_q1,
        _translation_d_abc_q1,
    ]
)


def _put_points_back_to_cell(open_transformations):
    mask_upper = open_transformations > 1
    mask_lower = open_transformations < -1

    open_transformations[mask_upper] -= 2
    open_transformations[mask_lower] += 2


def get_translations(
    cells_after_transformation, real_translations=all_translations
) -> np.ndarray[float]:
    _b_100 = cells_after_transformation[1] + real_translations[1]
    _c_100 = cells_after_transformation[1] + real_translations[2]
    _n_100 = cells_after_transformation[1] + real_translations[4]
    _d_100 = cells_after_transformation[1] + real_translations[17]

    _a_010 = cells_after_transformation[2] + real_translations[0]
    _c_010 = cells_after_transformation[2] + real_translations[2]
    _n_010 = cells_after_transformation[2] + real_translations[5]
    _d_010 = cells_after_transformation[2] + real_translations[18]

    _a_001 = cells_after_transformation[3] + real_translations[0]
    _b_001 = cells_after_transformation[3] + real_translations[1]
    _n_001 = cells_after_transformation[3] + real_translations[3]
    _d_001 = cells_after_transformation[3] + real_translations[16]

    _c_110 = cells_after_transformation[4] + real_translations[2]
    _n_110 = cells_after_transformation[4] + real_translations[6]
    _d_110 = cells_after_transformation[4] + real_translations[19]

    _a_011 = cells_after_transformation[5] + real_translations[0]
    _n_011 = cells_after_transformation[5] + real_translations[6]
    _d_011 = cells_after_transformation[5] + real_translations[19]

    _b_101 = cells_after_transformation[6] + real_translations[1]
    _n_101 = cells_after_transformation[6] + real_translations[6]
    _d_101 = cells_after_transformation[6] + real_translations[19]

    _b_m101 = cells_after_transformation[7] + real_translations[0]
    _n_m101 = cells_after_transformation[7] + real_translations[6]
    _d_m101 = cells_after_transformation[7] + real_translations[19]

    _c_m110 = cells_after_transformation[8] + real_translations[2]
    _n_m110 = cells_after_transformation[8] + real_translations[6]
    _d_m110 = cells_after_transformation[8] + real_translations[19]

    _a_0m11 = cells_after_transformation[9] + real_translations[0]
    _n_0m11 = cells_after_transformation[9] + real_translations[6]
    _d_0m11 = cells_after_transformation[9] + real_translations[19]

    _2_1_100 = cells_after_transformation[10] + real_translations[0]
    _2_1_010 = cells_after_transformation[11] + real_translations[1]
    _2_1_001 = cells_after_transformation[12] + real_translations[2]

    _4_1_100 = cells_after_transformation[27] + real_translations[7]
    _4_1_010 = cells_after_transformation[28] + real_translations[8]
    _4_1_001 = cells_after_transformation[29] + real_translations[9]

    _4_2_100 = cells_after_transformation[27] + real_translations[10]
    _4_2_010 = cells_after_transformation[28] + real_translations[11]
    _4_2_001 = cells_after_transformation[29] + real_translations[12]

    _4_3_100 = cells_after_transformation[27] + real_translations[13]
    _4_3_010 = cells_after_transformation[28] + real_translations[14]
    _4_3_001 = cells_after_transformation[29] + real_translations[15]

    _m4_1_100 = cells_after_transformation[30] + real_translations[7]
    _m4_1_010 = cells_after_transformation[31] + real_translations[8]
    _m4_1_001 = cells_after_transformation[32] + real_translations[9]

    _m4_2_100 = cells_after_transformation[30] + real_translations[10]
    _m4_2_010 = cells_after_transformation[31] + real_translations[11]
    _m4_2_001 = cells_after_transformation[32] + real_translations[12]

    _m4_3_100 = cells_after_transformation[30] + real_translations[13]
    _m4_3_010 = cells_after_transformation[31] + real_translations[14]
    _m4_3_001 = cells_after_transformation[32] + real_translations[15]

    open_transformations = np.array(
        [
            _b_100,
            _c_100,
            _n_100,
            _d_100,
            _a_010,
            _c_010,
            _n_010,
            _d_010,
            _a_001,
            _b_001,
            _n_001,
            _d_001,
            _c_110,
            _n_110,
            _d_110,
            _a_011,
            _n_011,
            _d_011,
            _b_101,
            _n_101,
            _d_101,
            _b_m101,
            _n_m101,
            _d_m101,
            _c_m110,
            _n_m110,
            _d_m110,
            _a_0m11,
            _n_0m11,
            _d_0m11,
            _2_1_100,
            _2_1_010,
            _2_1_001,
            _4_1_100,
            _4_1_010,
            _4_1_001,
            _4_2_100,
            _4_2_010,
            _4_2_001,
            _4_3_100,
            _4_3_010,
            _4_3_001,
            _m4_1_100,
            _m4_1_010,
            _m4_1_001,
            _m4_2_100,
            _m4_2_010,
            _m4_2_001,
            _m4_3_100,
            _m4_3_010,
            _m4_3_001,
        ]
    )

    _put_points_back_to_cell(open_transformations)

    return open_transformations


labels_slide = [
    "b_100",
    "c_100",
    "n_100",
    "d_100",
    "a_010",
    "c_010",
    "n_010",
    "d_010",
    "a_001",
    "b_001",
    "n_001",
    "d_001",
    "c_110",
    "n_110",
    "d_110",
    "a_011",
    "n_011",
    "d_011",
    "b_101",
    "n_101",
    "d_101",
    "b_m101",
    "n_m101",
    "d_m101",
    "c_m110",
    "n_m110",
    "d_m110",
    "a_0m11",
    "n_0m11",
    "d_0m11",
    "2_1_100",
    "2_1_010",
    "2_1_001",
    "4_1_100",
    "4_1_010",
    "4_1_001",
    "4_2_100",
    "4_2_010",
    "4_2_001",
    "4_3_100",
    "4_3_010",
    "4_3_001",
    "m4_1_100",
    "m4_1_010",
    "m4_1_001",
    "m4_2_100",
    "m4_2_010",
    "m4_2_001",
    "m4_3_100",
    "m4_3_010",
    "m4_3_001",
]


closed_translations = """
_a_100, _b_010, _c_001,
_ab_110, _ac_101, _bc_011,







"""


if __name__ == "__main__":
    import cifParsing as cPrs

    filename = "../cif files/9002506.cif"
    cell, _, _, _, _ = cPrs.get_super_cell(filename, size=1)
    cell = np.column_stack((cell, np.ones(len(cell))))
    mat = np.array([[1, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]])

    mat_inv = np.linalg.inv(mat)

    ans = (mat @ cell.T).T
    ans2 = (mat_inv @ cell.T).T

    mask_upper = ans > 1
    mask_lower = ans < -1

    ans[mask_upper] -= 2
    ans[mask_lower] += 2
    ans = np.unique(ans, axis=0)

    mask_upper = ans2 > 1
    mask_lower = ans2 < -1

    ans2[mask_upper] -= 2
    ans2[mask_lower] += 2
    ans2 = np.unique(ans2, axis=0)

    print(ans)
    print(ans2)
    # cell = np.array([0.9057, 0.0905, 0.01970])
    # cell = cell[0]
    # rotation_cell = cell @ mat.matrices
    # operations = get_translations(rotation_cell)
    # point_21_001 = operations[32]
    pass

"""
    1     1    0.5
    x,    y,     z
    0,    1,     1
  x-y,    x, 1/2+z
   -y  ,x-y,     z
   -x,   -y, 1/2+z
 -x+y,   -x,     z
    y, -x+y, 1/2+z
    
    y, -x+y,    -z
  x-y,    x,    -z
    x,    y, 1/2-z
   -y,  x-y, 1/2-z
 -x+y,   -x, 1/2-z
   -x,   -y,    -z
"""
# all_translations = np.array([_translation_a_h1, 0,
#                              _translation_b_h1, 1,
#                              _translation_c_h1, 2,
#
#                              _translation_n_ab_h1, 3,
#                              _translation_n_bc_h1, 4,
#                              _translation_n_ac_h1, 5,
#                              _translation_n_abc_h1,6,
#
#                              _translation_a_q1, 7,
#                              _translation_b_q1, 8,
#                              _translation_c_q1, 9,
#
#                              _translation_a_q2, 10,
#                              _translation_b_q2, 11,
#                              _translation_c_q2, 12,
#
#                              _translation_a_q3, 13,
#                              _translation_b_q3, 14,
#                              _translation_c_q3, 15,
#
#                              _translation_d_ab_q1, 16,
#                              _translation_d_bc_q1, 17,
#                              _translation_d_ac_q1, 18,
#                              _translation_d_abc_q1]) ,19


# _matrix_b_100 = np.array([[-1, 0, 0, 0],
#                           [ 0, 1, 0,h1],
#                           [ 0, 0, 1, 0]])
# _matrix_c_100 = np.array([[-1, 0, 0, 0],
#                           [ 0, 1, 0, 0],
#                           [ 0, 0, 1,h1]])
# _matrix_n_100 = np.array([[-1, 0, 0, 0],
#                           [ 0, 1, 0,h1],
#                           [ 0, 0, 1,h1]])
# _matrix_d_100 = np.array([[-1, 0, 0, 0],
#                           [ 0, 1, 0,q1],
#                           [ 0, 0, 1,q1]])

# _matrix_a_010 = np.array([[ 1, 0, 0,h1],
#                           [ 0,-1, 0, 0],
#                           [ 0, 0, 1, 0]])
# _matrix_c_010 = np.array([[ 1, 0, 0, 0],
#                           [ 0,-1, 0, 0],
#                           [ 0, 0, 1,h1]])
# _matrix_n_010 = np.array([[ 1, 0, 0,h1],
#                           [ 0,-1, 0, 0],
#                           [ 0, 0, 1,h1]])
# _matrix_d_010 = np.array([[ 1, 0, 0,q1],
#                           [ 0,-1, 0, 0],
#                           [ 0, 0, 1,q1]])

# _matrix_a_001 = np.array([[ 1, 0, 0,h1],
#                           [ 0, 1, 0, 0],
#                           [ 0, 0,-1, 0]])
# _matrix_b_001 = np.array([[ 1, 0, 0, 0],
#                           [ 0, 1, 0,h1],
#                           [ 0, 0,-1, 0]])
# _matrix_n_001 = np.array([[ 1, 0, 0,h1],
#                           [ 0, 1, 0,h1],
#                           [ 0, 0,-1, 0]])
# _matrix_d_001 = np.array([[ 1, 0, 0,q1],
#                           [ 0, 1, 0,q1],
#                           [ 0, 0,-1, 0]])

# _matrix_c_110 = np.array([[ 0,-1, 0, 0],
#                           [-1, 0, 0, 0],
#                           [ 0, 0, 1,h1]])
# _matrix_n_110 = np.array([[ 0,-1, 0,h1],
#                           [-1, 0, 0,h1],
#                           [ 0, 0, 1,h1]])
# _matrix_d_110 = np.array([[ 0,-1, 0,q1],
#                           [-1, 0, 0,q1],
#                           [ 0, 0, 1,q1]])

# _matrix_a_011 = np.array([[ 1, 0, 0,h1],
#                           [ 0, 0,-1, 0],
#                           [ 0,-1, 0, 0]])
# _matrix_n_011 = np.array([[ 1, 0, 0,h1],
#                           [ 0, 0,-1,h1],
#                           [ 0,-1, 0,h1]])
# _matrix_d_011 = np.array([[ 1, 0, 0,q1],
#                           [ 0, 0,-1,q1],
#                           [ 0,-1, 0,q1]])

# _matrix_b_101 = np.array([[ 0, 0,-1, 0],
#                           [ 0, 1, 0,h1],
#                           [-1, 0, 0, 0]])
# _matrix_n_101 = np.array([[ 0, 0,-1,h1],
#                           [ 0, 1, 0,h1],
#                           [-1, 0, 0,h1]])
# _matrix_d_101 = np.array([[ 0, 0,-1,q1],
#                           [ 0, 1, 0,q1],
#                           [-1, 0, 0,q1]])

# _matrix_b_m101 = np.array([[0, 0, 1, 0],
#                            [0, 1, 0,h1],
#                            [1, 0, 0, 0]])
# _matrix_n_m101 = np.array([[ 0, 0, 1,h1],
#                            [ 0, 1, 0,h1],
#                            [ 1, 0, 0,h1]])
# _matrix_d_m101 = np.array([[ 0, 0, 1,q1],
#                            [ 0, 1, 0,q1],
#                            [ 1, 0, 0,q1]])

# _matrix_c_m110 = np.array([[ 0, 1, 0, 0],
#                            [ 1, 0, 0, 0],
#                            [ 0, 0, 1,h1]])
# _matrix_n_m110 = np.array([[ 0, 1, 0,h1],
#                            [ 1, 0, 0,h1],
#                            [ 0, 0, 1,h1]])
# _matrix_d_m110 = np.array([[ 0, 1, 0,q1],
#                            [ 1, 0, 0,q1],
#                            [ 0, 0, 1,q1]])

# _matrix_a_0m11 = np.array([[ 1, 0, 0,h1],
#                            [ 0, 0, 1, 0],
#                            [ 0, 1, 0, 0]])
# _matrix_n_0m11 = np.array([[ 1, 0, 0,h1],
#                            [ 0, 0, 1,h1],
#                            [ 0, 1, 0,h1]])
# _matrix_d_0m11 = np.array([[ 1, 0, 0,q1],
#                            [ 0, 0, 1,q1],
#                            [ 0, 1, 0,q1]])


# _matrix_2_1_100 = np.array([[ 1, 0, 0,h1],
#                             [ 0,-1, 0, 0],
#                             [ 0, 0,-1, 0]])
# _matrix_2_1_010 = np.array([[-1, 0, 0, 0],
#                             [ 0, 1, 0,h1],
#                             [ 0, 0,-1, 0]])
# _matrix_2_1_001 = np.array([[-1, 0, 0, 0],
#                             [ 0,-1, 0, 0],
#                             [ 0, 0, 1,h1]])


# _matrix_4_1_100 = np.array([[ 1, 0, 0,q1],
#                             [ 0, 0,-1, 0],
#                             [ 0, 1, 0, 0]])
# _matrix_4_1_010 = np.array([[ 0, 0, 1, 0],
#                             [ 0, 1, 0,q1],
#                             [-1, 0, 0, 0]])
# _matrix_4_1_001 = np.array([[ 0,-1, 0, 0],
#                             [ 1, 0, 0, 0],
#                             [ 0, 0, 1,q1]])

# _matrix_4_2_100 = np.array([[ 1, 0, 0,q2],
#                             [ 0, 0,-1, 0],
#                             [ 0, 1, 0, 0]])
# _matrix_4_2_010 = np.array([[ 0, 0, 1, 0],
#                             [ 0, 1, 0,q2],
#                             [-1, 0, 0, 0]])
# _matrix_4_2_001 = np.array([[ 0,-1, 0, 0],
#                             [ 1, 0, 0, 0],
#                             [ 0, 0, 1,q2]])
#
# _matrix_4_3_100 = np.array([[ 1, 0, 0,q3],
#                             [ 0, 0,-1, 0],
#                             [ 0, 1, 0, 0]])
# _matrix_4_3_010 = np.array([[ 0, 0, 1, 0],
#                             [ 0, 1, 0,q3],
#                             [-1, 0, 0, 0]])
# _matrix_4_3_001 = np.array([[ 0,-1, 0, 0],
#                             [ 1, 0, 0, 0],
#                             [ 0, 0, 1,q3]])

# _matrix_m4_1_100 = np.array([[-1, 0, 0,q1],
#                              [ 0, 0, 1, 0],
#                              [ 0,-1, 0, 0]])
# _matrix_m4_1_010 = np.array([[ 0, 0,-1, 0],
#                              [ 0,-1, 0,q1],
#                              [ 1, 0, 0, 0]])
# _matrix_m4_1_001 = np.array([[ 0, 1, 0, 0],
#                              [-1, 0, 0, 0],
#                              [ 0, 0,-1,q1]])
#
# _matrix_m4_2_100 = np.array([[-1, 0, 0,q2],
#                              [ 0, 0, 1, 0],
#                              [ 0,-1, 0, 0]])
# _matrix_m4_2_010 = np.array([[ 0, 0,-1, 0],
#                              [ 0,-1, 0,q2],
#                              [ 1, 0, 0, 0]])
# _matrix_m4_2_001 = np.array([[ 0, 1, 0, 0],
#                              [-1, 0, 0, 0],
#                              [ 0, 0,-1,q2]])
#
# _matrix_m4_3_100 = np.array([[-1, 0, 0,q3],
#                              [ 0, 0, 1, 0],
#                              [ 0,-1, 0, 0]])
# _matrix_m4_3_010 = np.array([[ 0, 0,-1, 0],
#                              [ 0,-1, 0,q3],
#                              [ 1, 0, 0, 0]])
# _matrix_m4_3_001 = np.array([[ 0, 1, 0, 0],
#                              [-1, 0, 0, 0],
#                              [ 0, 0,-1,q3]])
# matrices_slide = [
#     _matrix_b_100, _matrix_c_100, _matrix_n_100, _matrix_d_100,
#     _matrix_a_010, _matrix_c_010, _matrix_n_010, _matrix_d_010,
#     _matrix_a_001, _matrix_b_001, _matrix_n_001, _matrix_d_001,
#
#     _matrix_c_110, _matrix_n_110, _matrix_d_110,
#     _matrix_a_011, _matrix_n_011, _matrix_d_011,
#     _matrix_b_101, _matrix_n_101, _matrix_d_101,
#
#     _matrix_b_m101, _matrix_n_m101, _matrix_d_m101,
#     _matrix_c_m110, _matrix_n_m110, _matrix_d_m110,
#     _matrix_a_0m11, _matrix_n_0m11, _matrix_d_0m11,
#
#     _matrix_2_1_100, _matrix_2_1_010, _matrix_2_1_001,
#
#     _matrix_4_1_100, _matrix_4_1_010, _matrix_4_1_001,
#     _matrix_4_2_100, _matrix_4_2_010, _matrix_4_2_001,
#     _matrix_4_3_100, _matrix_4_3_010, _matrix_4_3_001,
#
#     _matrix_m4_1_100, _matrix_m4_1_010, _matrix_m4_1_001,
#     _matrix_m4_2_100, _matrix_m4_2_010, _matrix_m4_2_001,
#     _matrix_m4_3_100, _matrix_m4_3_010, _matrix_m4_3_001
# ]
