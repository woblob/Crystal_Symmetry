import numpy as np

_matrix_c_000 = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])

_matrix_m_100 = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
_matrix_m_010 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
_matrix_m_001 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])

_matrix_m_110 = np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])
_matrix_m_011 = np.array([[1, 0, 0], [0, 0, -1], [0, -1, 0]])
_matrix_m_101 = np.array([[0, 0, -1], [0, 1, 0], [-1, 0, 0]])

_matrix_m_m101 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
_matrix_m_m110 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
_matrix_m_0m11 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])

_matrix_3_111 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
_matrix_3_m111 = np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]])
_matrix_3_1m11 = np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]])
_matrix_3_11m1 = np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])

_matrix_4_100 = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
_matrix_4_010 = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
_matrix_4_001 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])

_matrix_2_100 = _matrix_m_100 * -1
_matrix_2_010 = _matrix_m_010 * -1
_matrix_2_001 = _matrix_m_001 * -1
_matrix_2_110 = _matrix_m_110 * -1
_matrix_2_101 = _matrix_m_101 * -1
_matrix_2_011 = _matrix_m_011 * -1
_matrix_2_m110 = _matrix_m_m110 * -1
_matrix_2_m101 = _matrix_m_m101 * -1
_matrix_2_0m11 = _matrix_m_0m11 * -1
_matrix_m3_111 = _matrix_3_111 * -1
_matrix_m3_m111 = _matrix_3_m111 * -1
_matrix_m3_1m11 = _matrix_3_1m11 * -1
_matrix_m3_11m1 = _matrix_3_11m1 * -1
_matrix_m4_100 = _matrix_4_100 * -1
_matrix_m4_010 = _matrix_4_010 * -1
_matrix_m4_001 = _matrix_4_001 * -1


matrices = np.array(
    [
        _matrix_c_000,
        _matrix_m_100,
        _matrix_m_010,
        _matrix_m_001,
        _matrix_m_110,
        _matrix_m_011,
        _matrix_m_101,
        _matrix_m_m101,
        _matrix_m_m110,
        _matrix_m_0m11,
        _matrix_2_100,
        _matrix_2_010,
        _matrix_2_001,
        _matrix_2_110,
        _matrix_2_101,
        _matrix_2_011,
        _matrix_2_m110,
        _matrix_2_m101,
        _matrix_2_0m11,
        _matrix_3_111,
        _matrix_3_m111,
        _matrix_3_1m11,
        _matrix_3_11m1,
        _matrix_m3_111,
        _matrix_m3_m111,
        _matrix_m3_1m11,
        _matrix_m3_11m1,
        _matrix_4_100,
        _matrix_4_010,
        _matrix_4_001,
        _matrix_m4_100,
        _matrix_m4_010,
        _matrix_m4_001,
    ],
    dtype=int,
)

matrices_inverse = np.linalg.inv(matrices[-14:]).astype(int)


labels = np.array(
    (
        "c_000",
        "m_100",
        "m_010",
        "m_001",
        "m_110",
        "m_011",
        "m_101",
        "m_-101",
        "m_-110",
        "m_0-11",
        "2_100",
        "2_010",
        "2_001",
        "2_110",
        "2_101",
        "2_011",
        "2_-110",
        "2_-101",
        "2_0-11",
        "3_111",
        "3_-111",
        "3_1-11",
        "3_11-1",
        "-3_111",
        "-3_-111",
        "-3_1-11",
        "-3_11-1",
        "4_100",
        "4_010",
        "4_001",
        "-4_100",
        "-4_010",
        "-4_001",
    )
)

# labels = np.array(("c_000",

#                       1        2        3
#                    "m_100", "m_010", "m_001",

#                       4        5        6
#                    "m_110", "m_011", "m_101",

#                       7         8         9
#                    "m_-101", "m_-110", "m_0-11",

#                       10       11       12
#                    "2_100", "2_010", "2_001",

#                       13       14        15
#                    "2_110", "2_101",  "2_011",

#                       16       17        18
#                    "2_-110","2_-101", "2_0-11",


#                       19        20
#                    "3_111", "3_-111",

#                       21        22
#                    "3_1-11", "3_11-1",

#                        23        24
#                    "-3_111", "-3_-111",

#                        25         26
#                    "-3_1-11", "-3_11-1",

#                       27       28       29
#                    "4_100", "4_010", "4_001",

#                        30       31       32
#                    "-4_100","-4_010","-4_001"))


# operations = np.array([1,
#
#                        1, 1, 1,
#                        1, 1, 1,
#                        1, 1, 1,
#
#                        1, 1, 1,
#                        1, 1, 1,
#                        1, 1, 1,
#
#                        2, 2,
#                        2, 2,
#
#                        2, 2,
#                        2, 2,
#
#                        3, 3, 3,
#
#                        3, 3, 3])


def pick_matrices_by_index(masked_indexes, matrices=matrices):
    return np.ma.masked_where(masked_indexes, matrices).compressed().reshape((-1, 3, 3))


# def pick_matrices_by_label(masked_labels, labels=labels, matrices=matrices):
#     mask_id = np.ma.masked_where(masked_labels, all_labels)
#     return pick_matrices_by_index(mask_id)


def is_ortogonal(matrix):
    iloczyn = matrix.T @ matrix
    identity = np.eye(len(matrix), dtype=int)
    return np.array_equal(iloczyn, identity)


def make_matrix_multiplication_table():
    import pandas as pd

    def translate_matrix_to_name(matrices):
        mapper = {m.tostring(): labels[i] for i, m in enumerate(matrices)}
        I = np.eye(3, dtype=int)
        mapper[I.tostring()] = "I_000"

        multi_table = np.empty((len(matrices), len(matrices)), dtype=object)
        x, y = multi_table.shape
        for ix in range(x):
            for iy in range(y):
                result = matrices[ix] @ matrices[iy]
                multi_table[ix, iy] = mapper[result.tostring()]
        return multi_table

    result = translate_matrix_to_name(matrices)
    data = pd.Dataframe(result)
    print(data)


# class Matrices:
#     def __init__(self, matrices, matrices_inverse, labels, indices):
#         self.matrices = matrices
#         self.matrices_inverse = matrices_inverse
#         self.labels = labels
#         self.indices = indices
#
#     def get_labels(self, mask=None):
#         if mask is None:
#             return self.labels
#         return self.labels[mask]
