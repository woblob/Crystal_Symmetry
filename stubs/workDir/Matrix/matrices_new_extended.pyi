"""Type stubs for matrices_new_extended module.

This module provides extended symmetry matrices and related operations for crystallographic calculations,
including 4x4 matrices with translation components.
"""

from typing import List, Dict, Any, Tuple, Union, Optional
import numpy as np
from numpy.typing import NDArray

# Identity matrix
_matrix_ID_000: NDArray[np.int_]  # Identity matrix

# Inversion matrix
_matrix_inv_000: NDArray[np.int_]  # Inversion matrix

# Mirror plane matrices
_matrix_m_0yz: NDArray[np.int_]  # Mirror plane perpendicular to x-axis
_matrix_m_x0z: NDArray[np.int_]  # Mirror plane perpendicular to y-axis
_matrix_m_xy0: NDArray[np.int_]  # Mirror plane perpendicular to z-axis
_matrix_m_xmxz: NDArray[np.int_]  # Mirror plane perpendicular to [110]
_matrix_m_xymy: NDArray[np.int_]  # Mirror plane perpendicular to [011]
_matrix_m_xymx: NDArray[np.int_]  # Mirror plane perpendicular to [101]
_matrix_m_xyx: NDArray[np.int_]  # Mirror plane perpendicular to [-101]
_matrix_m_xxz: NDArray[np.int_]  # Mirror plane perpendicular to [-110]
_matrix_m_xyy: NDArray[np.int_]  # Mirror plane perpendicular to [0-11]

# 2-fold rotation matrices
_matrix_2_x00: NDArray[np.int_]  # 2-fold rotation around x-axis
_matrix_2_0y0: NDArray[np.int_]  # 2-fold rotation around y-axis
_matrix_2_00z: NDArray[np.int_]  # 2-fold rotation around z-axis
_matrix_2_xx0: NDArray[np.int_]  # 2-fold rotation around [110]
_matrix_2_x0x: NDArray[np.int_]  # 2-fold rotation around [101]
_matrix_2_0yy: NDArray[np.int_]  # 2-fold rotation around [011]
_matrix_2_xmx0: NDArray[np.int_]  # 2-fold rotation around [-110]
_matrix_2_mx0x: NDArray[np.int_]  # 2-fold rotation around [-101]
_matrix_2_0myy: NDArray[np.int_]  # 2-fold rotation around [0-11]

# 3-fold rotation matrices
_matrix_3_xxx: NDArray[np.int_]  # 3-fold rotation around [111]
_matrix_3_xmxmx: NDArray[np.int_]  # 3-fold rotation around [1-1-1]
_matrix_3_mxxmx: NDArray[np.int_]  # 3-fold rotation around [-11-1]
_matrix_3_mxmxx: NDArray[np.int_]  # 3-fold rotation around [-1-11]

# -3 rotation matrices (3-fold rotation + inversion)
_matrix_m3_xxx: NDArray[np.int_]  # -3 rotation around [111]
_matrix_m3_xmxmx: NDArray[np.int_]  # -3 rotation around [1-1-1]
_matrix_m3_mxxmx: NDArray[np.int_]  # -3 rotation around [-11-1]
_matrix_m3_mxmxx: NDArray[np.int_]  # -3 rotation around [-1-11]

# 4-fold rotation matrices
_matrix_4_x00: NDArray[np.int_]  # 4-fold rotation around x-axis
_matrix_4_0y0: NDArray[np.int_]  # 4-fold rotation around y-axis
_matrix_4_00z: NDArray[np.int_]  # 4-fold rotation around z-axis

# -4 rotation matrices (4-fold rotation + inversion)
_matrix_m4_x00: NDArray[np.int_]  # -4 rotation around x-axis
_matrix_m4_0y0: NDArray[np.int_]  # -4 rotation around y-axis
_matrix_m4_00z: NDArray[np.int_]  # -4 rotation around z-axis

# Hexagonal system matrices
_matrix_hex_m_x2xz: NDArray[np.int_]  # Hexagonal mirror plane
_matrix_hex_m_2xxz: NDArray[np.int_]  # Hexagonal mirror plane
_matrix_hex_m_x0z: NDArray[np.int_]  # Hexagonal mirror plane
_matrix_hex_m_0yz: NDArray[np.int_]  # Hexagonal mirror plane
_matrix_hex_2_x00: NDArray[np.int_]  # Hexagonal 2-fold rotation
_matrix_hex_2_0y0: NDArray[np.int_]  # Hexagonal 2-fold rotation
_matrix_hex_2_x2x0: NDArray[np.int_]  # Hexagonal 2-fold rotation
_matrix_hex_2_2xx0: NDArray[np.int_]  # Hexagonal 2-fold rotation
_matrix_hex_3_00z: NDArray[np.int_]  # Hexagonal 3-fold rotation
_matrix_hex_m3_00z: NDArray[np.int_]  # Hexagonal -3 rotation
_matrix_hex_6_00z: NDArray[np.int_]  # Hexagonal 6-fold rotation
_matrix_hex_m6_00z: NDArray[np.int_]  # Hexagonal -6 rotation

# Translation matrices
_translation_00H: NDArray[np.float64]  # Translation along z-axis by 1/3
_translation_00h: NDArray[np.float64]  # Translation along z-axis by 1/2
_translation_0h0: NDArray[np.float64]  # Translation along y-axis by 1/2
_translation_h00: NDArray[np.float64]  # Translation along x-axis by 1/2
_translation_0hh: NDArray[np.float64]  # Translation along y and z axes by 1/2
_translation_h0h: NDArray[np.float64]  # Translation along x and z axes by 1/2
_translation_hh0: NDArray[np.float64]  # Translation along x and y axes by 1/2
_translation_hhh: NDArray[np.float64]  # Translation along all axes by 1/2

# Collections of matrices
matrices: NDArray[np.int_]  # Array of all symmetry matrices
matrices_dict: Dict[str, NDArray[np.int_]]  # Dictionary of all symmetry matrices
matrices_dict_hex: Dict[str, NDArray[np.int_]]  # Dictionary of hexagonal symmetry matrices
all_matrices: List[NDArray[np.int_]]  # List of all matrices including extended ones
