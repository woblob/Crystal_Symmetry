"""
Type definitions for crystallographic data structures.

This module defines custom type aliases and annotations for crystallographic
data structures used throughout the codebase.
"""
from typing import Dict, List, Tuple, Union, TypeVar, Protocol, Optional, Set, Any, Callable
import numpy as np
from numpy.typing import NDArray, ArrayLike

# Basic type aliases for crystallographic data
Coordinate = Tuple[float, float, float]
FractionalCoordinate = Tuple[float, float, float]
CartesianCoordinate = Tuple[float, float, float]
HKL = Tuple[int, int, int]  # Miller indices
LatticeParameters = Tuple[float, float, float, float, float, float]  # a, b, c, alpha, beta, gamma

# Type aliases for symmetry operations
SymmetryType = str  # e.g., "2", "m", "3", "4", etc.
Direction = str  # e.g., "100", "111", etc.
SymmetryOperation = Tuple[SymmetryType, Direction]
SymmetryMatrix = NDArray[np.float64]  # 3x3 transformation matrix

# Type aliases for collections of symmetry operations
SymOpDict = Dict[Direction, SymmetryMatrix]
SymmetryBaseDict = Dict[SymmetryType, SymOpDict]

# Type aliases for crystal structures
AtomicPosition = Tuple[str, np.ndarray, float, float]  # element, coordinates, occupancy, displacement
AtomicStructure = Dict[str, List[AtomicPosition]]

# Type aliases for crystal analysis results
AnalysisResult = Dict[str, Any]
SymmetryList = List[SymmetryOperation]

# Type variables for generic operations
T = TypeVar('T')
T_Structure = TypeVar('T_Structure')
T_Coordinate = TypeVar('T_Coordinate', bound=np.ndarray)

# Protocol classes for interfaces
class Transformable(Protocol):
    """Protocol for objects that can be transformed by a matrix."""
    def transform(self, matrix: np.ndarray) -> 'Transformable':
        """Apply transformation matrix to the object."""
        ...

# Array type aliases with shape specifications
Point3D = NDArray[np.float64]  # Shape (3,)
Matrix3D = NDArray[np.float64]  # Shape (3, 3)
PointArray = NDArray[np.float64]  # Shape (n, 3)
PointArrayTransposed = NDArray[np.float64]  # Shape (3, n)
