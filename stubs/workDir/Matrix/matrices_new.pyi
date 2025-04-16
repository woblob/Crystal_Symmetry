"""Type stubs for matrices_new module.

This module provides symmetry matrices and related operations for crystallographic calculations.
"""

from typing import List, Dict, Any, Tuple, Union, Optional
import numpy as np
from numpy.typing import NDArray

# Matrix definitions
_matrix_c_000: NDArray[np.int_]  # Inversion matrix
_matrix_m_100: NDArray[np.int_]  # Mirror plane perpendicular to x-axis
_matrix_m_010: NDArray[np.int_]  # Mirror plane perpendicular to y-axis
_matrix_m_001: NDArray[np.int_]  # Mirror plane perpendicular to z-axis
_matrix_m_110: NDArray[np.int_]  # Mirror plane perpendicular to [110]
_matrix_m_011: NDArray[np.int_]  # Mirror plane perpendicular to [011]
_matrix_m_101: NDArray[np.int_]  # Mirror plane perpendicular to [101]
_matrix_m_m101: NDArray[np.int_]  # Mirror plane perpendicular to [-101]
_matrix_m_m110: NDArray[np.int_]  # Mirror plane perpendicular to [-110]
_matrix_m_0m11: NDArray[np.int_]  # Mirror plane perpendicular to [0-11]

# 2-fold rotation matrices
_matrix_2_100: NDArray[np.int_]  # 2-fold rotation around x-axis
_matrix_2_010: NDArray[np.int_]  # 2-fold rotation around y-axis
_matrix_2_001: NDArray[np.int_]  # 2-fold rotation around z-axis
_matrix_2_110: NDArray[np.int_]  # 2-fold rotation around [110]
_matrix_2_101: NDArray[np.int_]  # 2-fold rotation around [101]
_matrix_2_011: NDArray[np.int_]  # 2-fold rotation around [011]
_matrix_2_m110: NDArray[np.int_]  # 2-fold rotation around [-110]
_matrix_2_m101: NDArray[np.int_]  # 2-fold rotation around [-101]
_matrix_2_0m11: NDArray[np.int_]  # 2-fold rotation around [0-11]

# 3-fold rotation matrices
_matrix_3_111: NDArray[np.int_]  # 3-fold rotation around [111]
_matrix_3_m111: NDArray[np.int_]  # 3-fold rotation around [-111]
_matrix_3_1m11: NDArray[np.int_]  # 3-fold rotation around [1-11]
_matrix_3_11m1: NDArray[np.int_]  # 3-fold rotation around [11-1]

# -3 rotation matrices (3-fold rotation + inversion)
_matrix_m3_111: NDArray[np.int_]  # -3 rotation around [111]
_matrix_m3_m111: NDArray[np.int_]  # -3 rotation around [-111]
_matrix_m3_1m11: NDArray[np.int_]  # -3 rotation around [1-11]
_matrix_m3_11m1: NDArray[np.int_]  # -3 rotation around [11-1]

# 4-fold rotation matrices
_matrix_4_100: NDArray[np.int_]  # 4-fold rotation around x-axis
_matrix_4_010: NDArray[np.int_]  # 4-fold rotation around y-axis
_matrix_4_001: NDArray[np.int_]  # 4-fold rotation around z-axis

# -4 rotation matrices (4-fold rotation + inversion)
_matrix_m4_100: NDArray[np.int_]  # -4 rotation around x-axis
_matrix_m4_010: NDArray[np.int_]  # -4 rotation around y-axis
_matrix_m4_001: NDArray[np.int_]  # -4 rotation around z-axis

# Collections of matrices
matrices: NDArray[np.int_]  # Array of all symmetry matrices
labels: List[str]  # Labels for all symmetry matrices
all_matrices: List[NDArray[np.int_]]  # List of all matrices including extended ones
all_labels: List[str]  # Labels for all matrices including extended ones

# Functions
def pick_matrices_by_index(masked_indexes: List[bool], matrices: Optional[NDArray[np.int_]] = None) -> NDArray[np.int_]:
    """Pick matrices from the collection based on a boolean mask.

    Args:
        masked_indexes: Boolean mask for selecting matrices
        matrices: Optional custom matrix collection to use instead of the default

    Returns:
        Selected matrices reshaped to (-1, 3, 3)
    """

def make_matrix_multiplication_table() -> None:
    """Create and print a multiplication table for all matrices."""
