import numpy as np

# do sprawdzenia

_matrix_c_0000 = np.array([[-1, 0, 0, 0],
                           [ 0,-1, 0, 0],
                           [ 0, 0,-1, 0],
                           [ 0, 0, 0,-1]])

_matrix_m_10m10 = np.array([[ 0, 0, 1, 0],
                            [ 0, 1, 0, 0],
                            [ 1, 0, 0, 0],
                            [ 0, 0, 0, 1]]),

_matrix_m_1m210 = np.array([[ 0, 0,-1, 0],
                            [ 0,-1, 0, 0],
                            [-1, 0, 0, 0],
                            [ 0, 0, 0, 1]]),

_matrix_m_01m10 = np.array([[ 1, 0, 0, 0],
                            [ 0, 0, 1, 0],
                            [ 0, 1, 0, 0],
                            [ 0, 0, 0, 1]]),

_matrix_m_m2110 = np.array([[-1, 0, 0, 0],
                            [ 0, 0,-1, 0],
                            [ 0,-1, 0, 0],
                            [ 0, 0, 0, 1]]),

_matrix_m_m1100 = np.array([[ 0, 1, 0, 0],
                            [ 1, 0, 0, 0],
                            [ 0, 0, 1, 0],
                            [ 0, 0, 0, 1]]),

_matrix_m_11m20 = np.array([[ 0,-1, 0, 0],
                            [-1, 0, 0, 0],
                            [ 0, 0,-1, 0],
                            [ 0, 0, 0, 1]]),

_matrix_m_0001 = np.array([[ 1, 0, 0, 0],
                           [ 0, 1, 0, 0],
                           [ 0, 0, 1, 0],
                           [ 0, 0, 0,-1]])

_matrix_3_0001 = np.array([[ 0, 1, 0, 0],
                           [ 0, 0, 1, 0],
                           [ 1, 0, 0, 0],
                           [ 0, 0, 0, 1]])

_matrix_6_0001 = np.array([[ 0, 0,-1, 0],
                           [-1, 0, 0, 0],
                           [ 0,-1, 0, 0],
                           [ 0, 0, 0, 1]])

_matrix_2_10m10 = _matrix_m_10m10 * -1
_matrix_2_1m210 = _matrix_m_1m210 * -1
_matrix_2_01m10 = _matrix_m_01m10 * -1
_matrix_2_m2110 = _matrix_m_m2110 * -1
_matrix_2_m1100 = _matrix_m_m1100 * -1
_matrix_2_11m20 = _matrix_m_11m20 * -1
_matrix_2_0001  = _matrix_m_0001  * -1
_matrix_m3_0001 = _matrix_3_0001  * -1
_matrix_m6_0001 = _matrix_6_0001  * -1

matrices_hex = np.array([_matrix_c_0000,

                         _matrix_m_10m10,
                         _matrix_m_1m210,
                         _matrix_m_01m10,
                         _matrix_m_m2110,
                         _matrix_m_m1100,
                         _matrix_m_11m20,

                         _matrix_m_0001,

                         _matrix_2_10m10,
                         _matrix_2_1m210,
                         _matrix_2_01m10,
                         _matrix_2_m2110,
                         _matrix_2_m1100,
                         _matrix_2_11m20,

                         _matrix_2_0001,

                         _matrix_3_0001,
                         _matrix_m3_0001,

                         _matrix_6_0001,
                         _matrix_m6_0001])

labels = np.array(["c_0000",

                   "m_10m10",
                   "m_1m210",
                   "m_01m10",
                   "m_m2110",
                   "m_m1100",
                   "m_11m20",

                   "m_0001",

                   "2_10m10",
                   "2_1m210",
                   "2_01m10",
                   "2_m2110",
                   "2_m1100",
                   "2_11m20",

                   "2_0001",

                   "3_0001",
                   "m3_0001",

                   "6_0001",
                   "m6_0001"])