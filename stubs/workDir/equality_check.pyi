"""Type stubs for equality_check module.

This module provides the Point class for representing and comparing points
in crystallographic calculations.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray
import sympy as sp
from typing import List, Optional, Union, Any, ClassVar

class Point:
    """A class representing a point in crystallographic space.
    
    This class provides methods for comparing points and checking if a point
    can be obtained by applying a transformation matrix to a base point.
    """
    
    base_point: ClassVar[Optional[NDArray[np.float64]]]  # Class variable for the base point
    
    def __init__(self, arr: List[NDArray[np.float64]]) -> None:
        """Initialize a Point with an array of coordinates.
        
        Args:
            arr: List of coordinate arrays
        """
        self.array: NDArray[np.float64]  # The point's coordinate array
    
    def is_got_by(self, matrix: NDArray[np.float64]) -> bool:
        """Check if this point can be obtained by applying a matrix to the base point.
        
        Args:
            matrix: Transformation matrix to apply to the base point
            
        Returns:
            True if this point equals the result of applying the matrix to the base point
        """
        ...
    
    def __eq__(self, other: Point) -> bool:
        """Check if this point is equal to another point.
        
        Args:
            other: Another Point object to compare with
            
        Returns:
            True if the points are equal, False otherwise
        """
        ...
    
    def __repr__(self) -> str:
        """Get a string representation of the point.
        
        Returns:
            A string representation of the point's coordinates
        """
        ...
