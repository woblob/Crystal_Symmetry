from pathlib import Path
from typing import List, Dict, Any, Iterator, Tuple, Union, Optional
import numpy as np
from numpy.typing import NDArray


class Crystal:
    """Type stub for the Crystal class from the crystals package."""

    name: str
    atoms: List['Atom']

    @classmethod
    def from_cif(cls, filename: str) -> 'Crystal':
        """Load a crystal structure from a CIF file."""

    @classmethod
    def from_cod(cls, cod_id: int) -> 'Crystal':
        """Load a crystal structure from the Crystallography Open Database."""

    def symmetry(self) -> Dict[str, Any]:
        """Return symmetry information about the crystal structure."""

    def symmetry_operations(self) -> List[Tuple[NDArray[np.float64], NDArray[np.float64]]]:
        """Return the symmetry operations for this crystal structure."""

    @property
    def lattice_vectors(self) -> NDArray[np.float64]:
        """Return the lattice vectors of the crystal structure."""

    def supercell(self, a: int, b: int, c: int) -> 'Crystal':
        """Create a supercell of the crystal structure."""

    def itersorted(self) -> Iterator['Atom']:
        """Iterate through the sorted atoms in the crystal structure."""


class Atom:
    """Type stub for the Atom class from the crystals package."""

    element: str
    coords: Tuple[float, float, float]
    coords_fractional: Tuple[float, float, float]
    atomic_number: int

    def __init__(
        self,
        element: str,
        coords: Tuple[float, float, float],
        displacement: Optional[float] = None,
        occupancy: float = 1.0
    ) -> None: ...