"""Type stubs for matrices_with_translation_new module.

This module provides translation vectors for crystallographic calculations.
It includes translation vectors along principal axes, diagonal directions,
and with various fractional shifts (1/2, 1/4, etc.).
"""

from typing import List
import numpy as np
from numpy.typing import NDArray

# Translation constants
h1: float  # 1/2 * 2
q1: float  # 1/4 * 2
q2: float  # 2/4 * 2
q3: float  # 3/4 * 2

# Translation vectors along principal axes
_translation_a_h1: NDArray[np.float64]  # Translation along a-axis by 1/2
_translation_b_h1: NDArray[np.float64]  # Translation along b-axis by 1/2
_translation_c_h1: NDArray[np.float64]  # Translation along c-axis by 1/2

# Translation vectors along diagonal directions
_translation_n_ab_h1: NDArray[np.float64]  # Translation along a and b by 1/2
_translation_n_bc_h1: NDArray[np.float64]  # Translation along b and c by 1/2
_translation_n_ac_h1: NDArray[np.float64]  # Translation along a and c by 1/2
_translation_n_abc_h1: NDArray[np.float64]  # Translation along all axes by 1/2

# Translation vectors with quarter shifts
_translation_a_q1: NDArray[np.float64]  # Translation along a-axis by 1/4
_translation_b_q1: NDArray[np.float64]  # Translation along b-axis by 1/4
_translation_c_q1: NDArray[np.float64]  # Translation along c-axis by 1/4

_translation_a_q2: NDArray[np.float64]  # Translation along a-axis by 2/4
_translation_b_q2: NDArray[np.float64]  # Translation along b-axis by 2/4
_translation_c_q2: NDArray[np.float64]  # Translation along c-axis by 2/4

_translation_a_q3: NDArray[np.float64]  # Translation along a-axis by 3/4
_translation_b_q3: NDArray[np.float64]  # Translation along b-axis by 3/4
_translation_c_q3: NDArray[np.float64]  # Translation along c-axis by 3/4

# Diagonal translation vectors with quarter shifts
_translation_d_ab_q1: NDArray[np.float64]  # Translation along a and b by 1/4
_translation_d_bc_q1: NDArray[np.float64]  # Translation along b and c by 1/4
_translation_d_ac_q1: NDArray[np.float64]  # Translation along a and c by 1/4
_translation_d_abc_q1: NDArray[np.float64]  # Translation along all axes by 1/4

# Collection of all translation vectors
all_translations: NDArray[np.float64]  # Array of all translation vectors

# Labels for slide operations
labels_slide: List[str]  # Labels for slide operations

# Functions
def get_translations(
    cells_after_transformation: NDArray[np.float64],  # noqa: U100
    real_translations: NDArray[np.float64] = ...  # noqa: U100
) -> NDArray[np.float64]:
    """Generate translation vectors for cells after transformation.

    Args:
        cells_after_transformation: Coordinates of cells after
            transformation
        real_translations: Translation vectors to apply
            (default: all_translations)

    Returns:
        Array of transformed coordinates with translations applied
    """

def _put_points_back_to_cell(
    points: NDArray[np.float64]  # noqa: U100
) -> None:
    """Adjust points to be within the unit cell.

    This function modifies the input array in-place, adjusting coordinates
    that are outside the unit cell boundaries.

    Args:
        points: Array of points to adjust
    """
