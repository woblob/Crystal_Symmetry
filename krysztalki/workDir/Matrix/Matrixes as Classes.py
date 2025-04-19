"""Matrix classes for symmetry operations.

This module provides a class-based approach to working with symmetry matrices,
including functions for generating symmetry matrices for quadratic systems.
"""

from typing import Dict, Any

import numpy as np
from numpy.typing import NDArray


def generateSymetryBaseQUAD() -> Dict[str, Dict[str, NDArray[np.float64]]]:
    """Generate a dictionary of symmetry matrices for quadratic systems.

    Returns:
        Dictionary mapping symmetry types to dictionaries of direction-matrix pairs
    """
    return {
        "c": {"000": np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])},
        "m": {
            "100": np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            "010": np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]]),
            "001": np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]]),
            "110": np.array([[0, -1, 0], [-1, 0, 0], [0, 0, 1]]),
            "011": np.array([[1, 0, 0], [0, 0, -1], [0, -1, 0]]),
            "101": np.array([[0, 0, -1], [0, 1, 0], [-1, 0, 0]]),
            "-101": np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]),
            "-110": np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]]),
            "0-11": np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]]),
        },
    }


class Matrix:
    """Class representing a symmetry matrix with transformation and direction information.

    Attributes:
        matrix: The transformation matrix
        trans: The translation vector
        direction: The direction of the symmetry operation
    """

    matrix: NDArray[np.float64]
    trans: Any
    direction: str

    def __init__(self, arrs: NDArray[np.float64], trans: Any, dirr: str) -> None:
        """Initialize a Matrix object.

        Args:
            arrs: The transformation matrix
            trans: The translation vector
            dirr: The direction of the symmetry operation
        """
        self.matrix = arrs
        self.trans = trans
        self.direction = dirr

    def __mul__(self, other: Any) -> NDArray[np.float64]:
        """Multiply this matrix by another object.

        Args:
            other: The object to multiply with

        Returns:
            The result of the matrix multiplication
        """
        return self.matrix @ other.coor

    def __rmul__(self, other: Any) -> NDArray[np.float64]:
        """Right multiplication operation.

        Args:
            other: The object to multiply with

        Returns:
            The result of the matrix multiplication
        """
        return Matrix.__mul__(self, other)
