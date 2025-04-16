"""Type stubs for Matrixes as Classes module.

This module provides a class-based approach to working with symmetry matrices.
"""

from typing import Dict, Any
import numpy as np
from numpy.typing import NDArray

def generateSymetryBaseQUAD() -> Dict[str, Dict[str, NDArray[np.float64]]]:
    """Generate a dictionary of symmetry matrices for quadratic systems.
    
    Returns:
        Dictionary mapping symmetry types to dictionaries of direction-matrix pairs
    """
    ...

class Matrix:
    """Class representing a symmetry matrix with transformation and direction information.
    
    Attributes:
        matrix: The transformation matrix
        trans: The translation vector
        direction: The direction of the symmetry operation
    """
    
    matrix: NDArray[np.float64]  # The transformation matrix
    trans: Any  # The translation vector
    direction: str  # The direction of the symmetry operation
    
    def __init__(self, arrs: NDArray[np.float64], trans: Any, dirr: str) -> None:
        """Initialize a Matrix object.
        
        Args:
            arrs: The transformation matrix
            trans: The translation vector
            dirr: The direction of the symmetry operation
        """
        ...
    
    def __mul__(self, other: Any) -> NDArray[np.float64]:
        """Apply the matrix to another object.
        
        Args:
            other: Object with a 'coor' attribute
            
        Returns:
            Result of matrix multiplication
        """
        ...
    
    def __rmul__(self, other: Any) -> NDArray[np.float64]:
        """Right multiplication with another object.
        
        Args:
            other: Object to multiply with
            
        Returns:
            Result of matrix multiplication
        """
        ...
