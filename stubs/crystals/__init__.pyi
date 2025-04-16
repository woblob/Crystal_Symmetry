from pathlib import Path
from typing import List, Dict, Any, Iterator, Tuple, Union, Optional
import numpy as np
from numpy.typing import NDArray


class Crystal:
    """Type stub for the Crystal class from the crystals package."""
    
    @classmethod
    def from_cif(cls, filename: str) -> 'Crystal':
        """Load a crystal structure from a CIF file."""

    @classmethod
    def from_cod(cls, cod_id: int) -> 'Crystal':
        """Load a crystal structure from the Crystallography Open Database."""

    def symmetry(self) -> Dict[str, Any]:
        """Return symmetry information about the crystal structure."""

    def symmetry_operations(self) -> List[Tuple[Any, ...]]:
        """Return the symmetry operations for this crystal structure."""

    @property
    def lattice_vectors(self) -> List[List[float]]:
        """Return the lattice vectors of the crystal structure."""

    def supercell(self, a: int, b: int, c: int) -> 'Crystal':
        """Create a supercell of the crystal structure."""

    def itersorted(self) -> Iterator['AtomicStructure']:
        """Iterate through the sorted atoms in the crystal structure."""


class AtomicStructure:
    """Type stub for AtomicStructure representing an atom in a crystal structure."""
    
    @property
    def atomic_number(self) -> int:
        """Return the atomic number of the atom."""

    @property
    def coords_fractional(self) -> Tuple[float, float, float]:
        """Return the fractional coordinates of the atom."""

    @property
    def coords_cartesian(self) -> Tuple[float, float, float]:
        """Return the cartesian coordinates of the atom."""