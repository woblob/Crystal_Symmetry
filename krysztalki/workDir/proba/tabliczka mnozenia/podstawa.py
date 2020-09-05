import numpy as np

_matrix_ID_000 = np.array([[ 1, 0, 0, 0],
                           [ 0, 1, 0, 0],
                           [ 0, 0, 1, 0],
                           [ 0, 0, 0, 1]])

_matrix_inv_000 = np.array([[-1, 0, 0, 0],
                            [ 0,-1, 0, 0],
                            [ 0, 0,-1, 0],
                            [ 0, 0, 0, 1]])



_matrix_m_0yz = np.array([[-1, 0, 0, 0],
                          [ 0, 1, 0, 0],
                          [ 0, 0, 1, 0],
                          [ 0, 0, 0, 1]])

_matrix_m_x0z = np.array([[ 1, 0, 0, 0],
                          [ 0,-1, 0, 0],
                          [ 0, 0, 1, 0],
                          [ 0, 0, 0, 1]])

_matrix_m_xy0 = np.array([[ 1, 0, 0, 0],
                          [ 0, 1, 0, 0],
                          [ 0, 0,-1, 0],
                          [ 0, 0, 0, 1]])

_matrix_2_x00    = _matrix_m_0yz   @ _matrix_inv_000
_matrix_2_0y0    = _matrix_m_x0z   @ _matrix_inv_000
_matrix_2_00z    = _matrix_m_xy0   @ _matrix_inv_000

_matrix_m_xyy = np.array([[ 1, 0, 0, 0],
                          [ 0, 0, 1, 0],
                          [ 0, 1, 0, 0],
                          [ 0, 0, 0, 1]])

_matrix_m_xyx = np.array([[ 0, 0, 1, 0],
                          [ 0, 1, 0, 0],
                          [ 1, 0, 0, 0],
                          [ 0, 0, 0, 1]])

_matrix_m_xxz = np.array([[ 0, 1, 0, 0],
                          [ 1, 0, 0, 0],
                          [ 0, 0, 1, 0],
                          [ 0, 0, 0, 1]])


_matrix_m_xymy = np.array([[ 1, 0, 0, 0],
                           [ 0, 0,-1, 0],
                           [ 0,-1, 0, 0],
                           [ 0, 0, 0, 1]])

_matrix_m_xymx = np.array([[ 0, 0,-1, 0],
                           [ 0, 1, 0, 0],
                           [-1, 0, 0, 0],
                           [ 0, 0, 0, 1]])

_matrix_m_xmxz = np.array([[ 0,-1, 0, 0],
                           [-1, 0, 0, 0],
                           [ 0, 0, 1, 0],
                           [ 0, 0, 0, 1]])

_matrix_2_0myy = _matrix_m_xyy @ _matrix_inv_000
_matrix_2_mx0x = _matrix_m_xyx @ _matrix_inv_000
_matrix_2_xmx0 = _matrix_m_xxz @ _matrix_inv_000

_matrix_2_0yy = _matrix_m_xymy @ _matrix_inv_000
_matrix_2_x0x = _matrix_m_xymx @ _matrix_inv_000
_matrix_2_xx0 = _matrix_m_xmxz @ _matrix_inv_000



_matrix_3_xxx = np.array([[ 0, 0, 1, 0],
                          [ 1, 0, 0, 0],
                          [ 0, 1, 0, 0],
                          [ 0, 0, 0, 1]])

_matrix_3_xmxmx = np.array([[ 0, 0,-1, 0],
                            [-1, 0, 0, 0],
                            [ 0, 1, 0, 0],
                            [ 0, 0, 0, 1]])

_matrix_3_mxxmx = np.array([[ 0, 0, 1, 0],
                            [-1, 0, 0, 0],
                            [ 0,-1, 0, 0],
                            [ 0, 0, 0, 1]])

_matrix_3_mxmxx = np.array([[ 0, 0,-1, 0],
                            [ 1, 0, 0, 0],
                            [ 0,-1, 0, 0],
                            [ 0, 0, 0, 1]])


_matrix_4_x00 = np.array([[ 1, 0, 0, 0],
                          [ 0, 0,-1, 0],
                          [ 0, 1, 0, 0],
                          [ 0, 0, 0, 1]])

_matrix_4_0y0 = np.array([[ 0, 0, 1, 0],
                          [ 0, 1, 0, 0],
                          [-1, 0, 0, 0],
                          [ 0, 0, 0, 1]])

_matrix_4_00z = np.array([[ 0,-1, 0, 0],
                          [ 1, 0, 0, 0],
                          [ 0, 0, 1, 0],
                          [ 0, 0, 0, 1]])


_matrix_m3_xxx   = _matrix_3_xxx   @ _matrix_inv_000
_matrix_m3_xmxmx = _matrix_3_xmxmx @ _matrix_inv_000
_matrix_m3_mxxmx = _matrix_3_mxxmx @ _matrix_inv_000
_matrix_m3_mxmxx = _matrix_3_mxmxx @ _matrix_inv_000

_matrix_m4_x00   = _matrix_4_x00   @ _matrix_inv_000
_matrix_m4_0y0   = _matrix_4_0y0   @ _matrix_inv_000
_matrix_m4_00z   = _matrix_4_00z   @ _matrix_inv_000


matrices = np.array([_matrix_inv_000,

                     _matrix_m_0yz, _matrix_m_x0z, _matrix_m_xy0,
                     _matrix_m_xmxz, _matrix_m_xymy,_matrix_m_xymx,
                     _matrix_m_xyx, _matrix_m_xxz, _matrix_m_xyy,

                     _matrix_2_x00, _matrix_2_0y0, _matrix_2_00z,
                     _matrix_2_xx0, _matrix_2_x0x, _matrix_2_0yy,
                     _matrix_2_xmx0, _matrix_2_mx0x, _matrix_2_0myy,

                     _matrix_3_xxx, _matrix_3_xmxmx,
                     _matrix_3_mxxmx, _matrix_3_mxmxx,

                     _matrix_m3_xxx, _matrix_m3_xmxmx,
                     _matrix_m3_mxxmx, _matrix_m3_mxmxx,

                     _matrix_4_x00, _matrix_4_0y0, _matrix_4_00z,
                     _matrix_m4_x00, _matrix_m4_0y0, _matrix_m4_00z],

                    dtype=int)

# matrices_inverse = np.linalg.inv(matrices[-14:]).astype(int)

_translation_hhh = np.array([[ 0, 0, 0, 6],
                             [ 0, 0, 0, 6],
                             [ 0, 0, 0, 6],
                             [ 0, 0, 0, 0]])

_translation_0hh = np.array([[ 0, 0, 0, 0],
                             [ 0, 0, 0, 6],
                             [ 0, 0, 0, 6],
                             [ 0, 0, 0, 0]])

_translation_h0h = np.array([[ 0, 0, 0, 6],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 6],
                             [ 0, 0, 0, 0]])

_translation_hh0 = np.array([[ 0, 0, 0, 6],
                             [ 0, 0, 0, 6],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 0]])

_translation_00h = np.array([[ 0, 0, 0, 0],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 6],
                             [ 0, 0, 0, 0]])

_translation_0h0 = np.array([[ 0, 0, 0, 0],
                             [ 0, 0, 0, 6],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 0]])

_translation_h00 = np.array([[ 0, 0, 0, 6],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 0]])

translations = np.array([
    _translation_h00,
    _translation_0h0,
    _translation_00h,
    _translation_hh0,
    _translation_h0h,
    _translation_0hh,
    _translation_hhh
])

_translation_qqq = np.array([[ 0, 0, 0, 3],
                             [ 0, 0, 0, 3],
                             [ 0, 0, 0, 3],
                             [ 0, 0, 0, 0  ]])


# TODO: separate by translation vector
#  (if there is slide then look for symmetry)


matrices_dict = {
    "inv_000": _matrix_inv_000,

    "m_0yz": _matrix_m_0yz, "m_x0z": _matrix_m_x0z, "m_xy0": _matrix_m_xy0,
    "m_xmxz": _matrix_m_xmxz, "m_xymy": _matrix_m_xymy, "m_xymx": _matrix_m_xymx,
    "m_xyx": _matrix_m_xyx, "m_xxz": _matrix_m_xxz, "m_xyy": _matrix_m_xyy,

    "2_x00": _matrix_2_x00, "2_0y0": _matrix_2_0y0, "2_00z": _matrix_2_00z,
    "2_xx0": _matrix_2_xx0, "2_x0x": _matrix_2_x0x, "2_0yy": _matrix_2_0yy,
    "2_xmx0": _matrix_2_xmx0, "2_mx0x": _matrix_2_mx0x, "2_0myy": _matrix_2_0myy,

    "3_xxx": _matrix_3_xxx, "3_xmxmx": _matrix_3_xmxmx,
    "3_mxxmx": _matrix_3_mxxmx, "3_mxmxx": _matrix_3_mxmxx,

    "m3_xxx": _matrix_m3_xxx, "m3_xmxmx": _matrix_m3_xmxmx,
    "m3_mxxmx": _matrix_m3_mxxmx, "m3_mxmxx": _matrix_m3_mxmxx,

    "4_x00": _matrix_4_x00, "4_0y0": _matrix_4_0y0, "4_00z": _matrix_4_00z,
    "-4_x00": _matrix_m4_x00, "-4_0y0": _matrix_m4_0y0, "-4_00z": _matrix_m4_00z
}

labels = np.array(("inv_000",

                   "m_0yz", "m_x0z", "m_xy0",
                   "m_xmxz", "m_xymy", "m_xymx",
                   "m_xyx", "m_xxz", "m_xyy",

                   "2_x00", "2_0y0", "2_00z",
                   "2_xx0", "2_x0x",  "2_0yy",
                   "2_xmx0","2_mx0x", "2_0myy",

                   "3_xxx", "3_xmxmx",
                   "3_mxxmx", "3_mxmxx",

                   "m3_xxx", "m3_xmxmx",
                   "m3_mxxmx", "m3_mxmxx",

                   "4_x00", "4_0y0", "4_00z",

                   "-4_x00","-4_0y0","-4_00z"))
