"""Type stubs for eigenvectors module.

This module provides functions for calculating and manipulating eigenvectors.
"""

import numpy as np
from numpy.typing import NDArray

def get_eigenvectors(mat: NDArray[np.float64]) -> NDArray[np.float64]:
    """Calculate the eigenvectors of a matrix.
    
    Args:
        mat: Input matrix
        
    Returns:
        Matrix of eigenvectors
    """
    ...

def resize_vectors(vectors: NDArray[np.float64]) -> NDArray[np.float64]:
    """Resize vectors so that the maximum absolute value in each vector is 1.
    
    Args:
        vectors: Matrix of vectors to resize
        
    Returns:
        Matrix of resized vectors
    """
    ...
