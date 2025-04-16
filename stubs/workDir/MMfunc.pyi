"""Type stubs for MMfunc module.

This module provides functions for transforming crystal cells and reducing them
based on symmetry operations. It includes utilities for applying rotation and
translation matrices to crystal structures and identifying equivalent points.
"""

from typing import Tuple, List, Dict, Set, DefaultDict, Union
from collections.abc import Mapping

import numpy as np
from numpy.typing import NDArray

from krysztalki.workDir.cifParsing import MyCell

def translate_point_to_index(
    cell: NDArray[np.float64],  # noqa: U100
    mapper: Mapping[Tuple[float, ...], int]  # noqa: U100
) -> NDArray[np.int_]:
    """Translate points in a cell to their corresponding indices.

    Args:
        cell: Array of points to translate
        mapper: Dictionary mapping point coordinates to indices

    Returns:
        Array of indices corresponding to the input points
    """

def show_unevenness(vals: Union[Set[float], List[float]]) -> None:  # noqa: U100
    """Print pairs of values that are very close to each other.

    Args:
        vals: Set or list of values to check for near-equality
    """

def make_replacer(vals: List[float]) -> Dict[float, float]:  # noqa: U100
    """Create a dictionary for replacing nearly equal values.

    Args:
        vals: List of values to check for near-equality

    Returns:
        Dictionary mapping values to their nearly equal counterparts
    """

def put_points_in_cell(points: NDArray[np.float64]) -> NDArray[np.float64]:  # noqa: U100
    """Adjust points to be within the unit cell boundaries.

    Args:
        points: Array of points to adjust

    Returns:
        Adjusted points within the unit cell
    """

def full_transform(cell: MyCell) -> List[NDArray[np.int_]]:  # noqa: U100
    """Generate the full transformation of a given cell.

    Applies rotation and translation matrices to the cell coordinates.

    Args:
        cell: MyCell object containing the cell data and symmetry operations

    Returns:
        List of arrays containing indices of transformed points
    """

def reduce_cell(
    transformed_points_to_indexes: NDArray[np.int_],  # noqa: U100
    transformed_points_to_indexes_inverse: NDArray[np.int_],  # noqa: U100
    mask_syms_normal: NDArray[np.int_]  # noqa: U100
) -> Set[int]:
    """Reduce a cell by removing equivalent points based on symmetry operations.

    Args:
        transformed_points_to_indexes: Array of indices after forward transformations
        transformed_points_to_indexes_inverse: Array of indices after inverse
            transformations
        mask_syms_normal: Mask indicating which symmetry operations to apply

    Returns:
        Set of indices for the reduced cell (non-equivalent points)
    """
