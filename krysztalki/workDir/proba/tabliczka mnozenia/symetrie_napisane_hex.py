import numpy as np
import podstawa as pod

# 6_mmm

_matrix_hex_m_x2xz = np.array([[-1, 1, 0, 0],
                               [ 0, 1, 0, 0],
                               [ 0, 0, 1, 0],
                               [ 0, 0, 0, 1]]) #8

_matrix_hex_m_2xxz = np.array([[ 1, 0, 0, 0],
                               [ 1,-1, 0, 0],
                               [ 0, 0, 1, 0],
                               [ 0, 0, 0, 1]]) #9

_matrix_hex_m_x0z = np.array([[ 1,-1, 0, 0],
                              [ 0,-1, 0, 0],
                              [ 0, 0, 1, 0],
                              [ 0, 0, 0, 1]]) #11

_matrix_hex_m_0yz = np.array([[-1, 0, 0, 0],
                              [-1, 1, 0, 0],
                              [ 0, 0, 1, 0],
                              [ 0, 0, 0, 1]]) #12

_matrix_hex_2_x00  = _matrix_hex_m_x2xz @ pod._matrix_inv_000
_matrix_hex_2_0y0  = _matrix_hex_m_2xxz @ pod._matrix_inv_000
_matrix_hex_2_x2x0 = _matrix_hex_m_x0z @ pod._matrix_inv_000
_matrix_hex_2_2xx0 = _matrix_hex_m_0yz @ pod._matrix_inv_000


_matrix_hex_3_00z = np.array([[0, -1, 0, 0],
                              [ 1,-1, 0, 0],
                              [ 0, 0, 1, 0],
                              [ 0, 0, 0, 1]])



_matrix_hex_m3_00z = _matrix_hex_3_00z @ pod._matrix_inv_000

_matrix_hex_6_00z  = np.array([[1, -1, 0, 0],
                               [ 1, 0, 0, 0],
                               [ 0, 0, 1, 0],
                               [ 0, 0, 0, 1]])

_matrix_hex_m6_00z = _matrix_hex_6_00z @ pod._matrix_inv_000

matrices_hex = np.array([
    _matrix_hex_m_x2xz,
    _matrix_hex_m_2xxz,
    _matrix_hex_m_x0z,
    _matrix_hex_m_0yz,
    _matrix_hex_2_x00,
    _matrix_hex_2_0y0,
    _matrix_hex_2_x2x0,
    _matrix_hex_2_2xx0,
    _matrix_hex_3_00z,
    _matrix_hex_m3_00z,
    _matrix_hex_6_00z,
    _matrix_hex_m6_00z,
], dtype=int)

labels_hex = np.array([
    "hex_m_x2xz",
    "hex_m_2xxz",
    "hex_m_x0z",
    "hex_m_0yz",
    "hex_2_x00",
    "hex_2_0y0",
    "hex_2_x2x0",
    "hex_2_2xx0",
    "hex_3_00z",
    "hex_m3_00z",
    "hex_6_00z",
    "hex_m6_00z",
])

matrices_dict_hex = {
    "hex_m_x2xz": _matrix_hex_m_x2xz,
    "hex_m_2xxz": _matrix_hex_m_2xxz,
    "hex_m_x0z": _matrix_hex_m_x0z,
    "hex_m_0yz": _matrix_hex_m_0yz,
    "hex_2_x00": _matrix_hex_2_x00,
    "hex_2_0y0": _matrix_hex_2_0y0,
    "hex_2_x2x0": _matrix_hex_2_x2x0,
    "hex_2_2xx0": _matrix_hex_2_2xx0,
    "3_00z": _matrix_hex_3_00z,
    "m3_00z": _matrix_hex_m3_00z,
    "6_00z": _matrix_hex_6_00z,
    "m6_00z": _matrix_hex_m6_00z,
}


_translation_00H = np.array([[ 0, 0, 0, 0],
                             [ 0, 0, 0, 0],
                             [ 0, 0, 0, 2],
                             [ 0, 0, 0, 0]])

_translation_002H = np.array([[ 0, 0, 0, 0],
                              [ 0, 0, 0, 0],
                              [ 0, 0, 0, 4],
                              [ 0, 0, 0, 0]])

_translation_003H = np.array([[ 0, 0, 0, 0],
                              [ 0, 0, 0, 0],
                              [ 0, 0, 0, 6],
                              [ 0, 0, 0, 0]])

_translation_004H = np.array([[ 0, 0, 0, 0],
                              [ 0, 0, 0, 0],
                              [ 0, 0, 0, 8],
                              [ 0, 0, 0, 0]])

_translation_005H = np.array([[ 0, 0, 0, 0],
                              [ 0, 0, 0, 0],
                              [ 0, 0, 0, 10],
                              [ 0, 0, 0, 0]])


all_hex_translations = np.array([
    _translation_00H,
    _translation_002H,
    _translation_003H,
    _translation_004H,
    _translation_005H],
    dtype=int
)

all_labels_hex_translations = np.array([
    "t_00H",
    "t_002H",
    "t_003H",
    "t_004H",
    "t_005H"
])

#P6_3/mcm

_matrix_hex_6_3_00z_00h = matrices_dict_hex["6_00z"] + _translation_003H  #5


#P6/mcc

_matrix_hex_c_x2xz_00h = matrices_dict_hex["hex_m_x2xz"] + _translation_003H  #8
_matrix_hex_c_2xxz_00h = matrices_dict_hex["hex_m_2xxz"] + _translation_003H  #9
_matrix_hex_c_x0z_00h = matrices_dict_hex["hex_m_x0z"] + _translation_003H  #11
_matrix_hex_c_0yz_00h = matrices_dict_hex["hex_m_0yz"] + _translation_003H  #12
_matrix_hex_2_x0q = matrices_dict_hex["hex_2_x00"] + _translation_003H  #20
_matrix_hex_2_0yq = matrices_dict_hex["hex_2_0y0"] + _translation_003H  #21
_matrix_hex_2_x2xq = matrices_dict_hex["hex_2_x2x0"] + _translation_003H  #23
_matrix_hex_2_2xxq = matrices_dict_hex["hex_2_2xx0"] + _translation_003H  #24

#P6_1_22
_matrix_hex_3_1_00z_00t = matrices_dict_hex["3_00z"] + _translation_002H  #2
_matrix_hex_6_1_00z_00H = matrices_dict_hex["6_00z"] + _translation_00H  #5
_matrix_hex_2_xxH = pod.matrices_dict["2_xx0"] + _translation_002H  #7
_matrix_hex_2_0yt = matrices_dict_hex["hex_2_0y0"] + _translation_004H  #9
_matrix_hex_2_xmx5v = pod.matrices_dict["2_xmx0"] + _translation_005H  #
_matrix_hex_2_2xxv = matrices_dict_hex["hex_2_2xx0"] + _translation_00H  #


_matrix_hex_6_2_00z_00t = matrices_dict_hex["6_00z"] + _translation_002H  #
_matrix_hex_6_4_00z_002t = matrices_dict_hex["6_00z"] + _translation_004H  #
_matrix_hex_6_5_00z_005H = matrices_dict_hex["6_00z"] + _translation_005H  #


#P3_2_21

_matrix_hex_3_2_00z_002t = matrices_dict_hex["3_00z"] + _translation_004H  #
_matrix_hex_2_x0H = matrices_dict_hex["hex_2_x00"] + _translation_002H  #


#P3_2_12

_matrix_hex_2_xmxH = pod.matrices_dict["2_xmx0"] + _translation_002H  #4
_matrix_hex_2_x2xt = matrices_dict_hex["hex_2_x2x0"] + _translation_004H  #5


#3_1_12
_matrix_hex_2_xmxt = pod.matrices_dict["2_xmx0"] + _translation_004H  #
_matrix_hex_2_x2xH = matrices_dict_hex["hex_2_x2x0"] + _translation_002H  #


#3_1_21
_matrix_hex_2_x0t = matrices_dict_hex["hex_2_x00"] + _translation_004H  #
_matrix_hex_2_0yH = matrices_dict_hex["hex_2_0y0"] + _translation_002H  #



# _matrix_translation_ = _matrix_ID_000 + _translation_  #