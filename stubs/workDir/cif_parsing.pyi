"""Type stubs for cif_parsing module.

This module provides the MyCell class for parsing and processing
crystallographic information files (CIF).
"""

import pathlib
from typing import Union, Dict, Any, List, Tuple, Optional, cast

import numpy as np
from numpy.typing import NDArray
from crystals import Crystal
from krysztalki.utils.task_manager import CrystalTaskManager

class MyCell:
    """Class for parsing and processing crystallographic information files.
    
    This class loads a CIF file, extracts symmetry operations and crystal structure,
    and provides methods for manipulating and analyzing the crystal.
    """
    
    symmetry_operations: NDArray[np.float64]  # Symmetry operations matrices
    symmetry_operations_inverses: NDArray[np.float64]  # Inverse symmetry operations
    lattice_vectors: NDArray[np.float64]  # Lattice vectors of the crystal
    super_cell: NDArray[np.float64]  # Coordinates of atoms in the supercell
    super_cell_atomic_numbers: NDArray[np.int_]  # Atomic numbers of atoms in the supercell
    super_cell_indexes: NDArray[np.int_]  # Indices of atoms in the supercell
    base_type: str  # Coordinate system type: "m" for Miller, "w" for Weber
    task_manager: CrystalTaskManager  # Task manager for tracking operations
    
    def __init__(self, file_name: Union[str, int], size: int) -> None:
        """Initialize a MyCell object by loading a CIF file.
        
        Args:
            file_name: Either a path to a CIF file or a COD ID number
            size: Size of the supercell to create
        
        Raises:
            Exception: If there is an error loading or processing the CIF file
        """
        ...
    
    def prepare_lattice_vectors(self, lattice_vectors: NDArray[np.float64]) -> NDArray[np.float64]:
        """Prepare lattice vectors for use in calculations.
        
        Expands the 3x3 lattice vectors to 4x4 homogeneous coordinates.
        
        Args:
            lattice_vectors: 3x3 array of lattice vectors
            
        Returns:
            4x4 array of expanded lattice vectors
        """
        ...
    
    def get_symmetry_operations_inverses(self) -> NDArray[np.float64]:
        """Calculate the inverse symmetry operations.
        
        Returns:
            Array of inverse symmetry operations that are not already in the
            symmetry_operations array
        """
        ...
    
    def getfile(self, file_name: Union[str, int]) -> Crystal:
        """Open a CIF file from a local repository or download from Crystallography Open Database.
        
        Args:
            file_name: Either an integer (COD number) or a string (path to CIF file)
                Examples:
                    file_name = 1000041  # NaCl Fm-3m
                    file_name = 'path/to/file.cif'
        
        Returns:
            A Crystal object representing the crystal structure
        """
        ...
    
    def miller_or_weber(self, cell_info: Crystal) -> str:
        """Determine which coordinate system to use based on the crystal system.
        
        Args:
            cell_info: Crystal object containing symmetry information
            
        Returns:
            "w" for hexagonal systems (international numbers 143-194),
            "m" for all other systems
        """
        ...
    
    def extract_info(self, file: Crystal, size: int) -> None:
        """Extract crystal information and create the supercell.
        
        Args:
            file: Crystal object containing the crystal structure
            size: Size of the supercell to create
        """
        ...
    
    def _handle_negative_zeroes(self) -> None:
        """Replace negative zeros with positive zeros in the supercell coordinates."""
        ...
    
    def put_points_in_cell(self, points: NDArray[np.float64]) -> NDArray[np.float64]:
        """Adjust points to be within the unit cell boundaries.
        
        Args:
            points: Array of points to adjust
            
        Returns:
            Adjusted points within the unit cell
        """
        ...
    
    def __mul__(self, matrices: NDArray[np.float64]) -> NDArray[np.float64]:
        """Apply transformation matrices to the supercell.
        
        Args:
            matrices: Transformation matrices to apply
            
        Returns:
            Transformed points adjusted to be within the unit cell
        """
        ...
    
    @property
    def volume(self) -> float:
        """Calculate the volume of the unit cell.
        
        Returns:
            Volume of the unit cell
        """
        ...
    
    def __str__(self) -> str:
        """Get a string representation of the MyCell object.
        
        Returns:
            String representation of the object's fields
        """
        ...
