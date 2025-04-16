import pathlib
from typing import Union, Dict, Any, List, Tuple, Optional, cast

import numpy as np
from crystals import Crystal
from krysztalki.utils.task_manager import CrystalTaskManager


class MyCell:
    """
    Class representing a crystallographic cell with symmetry operations.

    This class manages crystal data, extracts symmetry operations,
    and handles transformations of points within the crystal.
    """

    def __init__(self, file_name: Union[str, int], size: int):
        """
        Initialize a crystal cell from a CIF file or COD identifier.

        Args:
            file_name: Path to CIF file or COD database number
            size: Size multiplier for the supercell
        """
        # Initialize instance variables to ensure they're always defined
        self.symmetry_operations = np.array([])
        self.symmetry_operations_inverses = np.array([])
        self.lattice_vectors = np.array([])
        self.super_cell = np.array([])
        self.super_cell_atomic_numbers = np.array([])
        self.super_cell_indexes = np.array([])
        self.base_type = "m"  # Default to Miller indices

        # Create task for analyzing this crystal
        self.task_manager = CrystalTaskManager()
        task: Optional[Dict[str, Any]] = self.task_manager.add_crystal_analysis_task(file_name)

        try:
            file = self.getfile(file_name)
            self.task_manager.create_task(
                f"Parsed {file_name}",
                "Successfully loaded CIF file",
                "medium"
            )

            self.symmetry_operations = np.array(file.symmetry_operations())
            self.task_manager.create_task(
                "Extracted symmetry operations",
                f"Found {len(self.symmetry_operations)} operations",
                "medium"
            )

            self.symmetry_operations_inverses = \
                self.get_symmetry_operations_inverses()
            self.base_type = self.miller_or_weber(file)
            self.extract_info(file, size)
            self._handle_negative_zeroes()
            self.super_cell_indexes = np.arange(len(self.super_cell))

            # Mark main task as complete
            if task:
                self.task_manager.mark_task_done(task['id'])

        except Exception as error:
            self.task_manager.create_task(
                "Error in crystal analysis",
                f"Error processing {file_name}: {str(error)}",
                "high"
            )
            raise

    def prepare_lattice_vectors(self, lattice_vectors: np.ndarray) -> np.ndarray:
        """
        Prepare lattice vectors for transformation calculations.

        Args:
            lattice_vectors: 3×3 array of lattice vectors

        Returns:
            4×4 transformation matrix with augmented dimension
        """
        expanded_lattice_vectors = \
            np.column_stack((lattice_vectors, np.zeros(3)))

        expanded_lattice_vectors = \
            np.vstack((expanded_lattice_vectors, np.zeros(4)))

        expanded_lattice_vectors[-1, -1] = 1

        return np.around(expanded_lattice_vectors, 14)

    def get_symmetry_operations_inverses(self) -> np.ndarray:
        """
        Calculate the inverses of symmetry operations, excluding redundant ones.

        Returns:
            Array of inverse symmetry operations that don't overlap with existing operations
        """
        symmetries = self.symmetry_operations
        all_inverses = np.linalg.inv(symmetries)

        # compare all symmetries with their inverses and subtract overlap
        index_mask = np.ones(len(symmetries), dtype=bool)

        for i, inv in enumerate(all_inverses):
            for sym in symmetries:
                if np.allclose(sym, inv):
                    index_mask[i] = False
                    break

        return cast(np.ndarray, all_inverses[index_mask])

    def getfile(self, file_name: Union[str, int]) -> Crystal:
        """
        Open CIF file from local repository or download from Crystallography Open Database.

        Args:
            file_name: Integer COD number or string path to CIF file

        Returns:
            Crystal object with loaded structure data

        Examples:
            file_name = 1000041  # NaCl Fm-3m
            file_name = 'path/to/file.cif'
        """
        try:
            value = int(file_name)
            return Crystal.from_cod(value)
        except ValueError:
            pass
        full_path = pathlib.Path(str(file_name)).absolute()
        return Crystal.from_cif(str(full_path))

    def miller_or_weber(self, cell_info: Crystal) -> str:
        """
        Determine which coordinate system to use based on crystal system.

        For hexagonal or rhombohedral crystal systems, use Weber (4D) indices.
        For all others, use Miller (3D) indices.

        Args:
            cell_info: Crystal object containing symmetry information

        Returns:
            "w" for Weber (hexagonal) or "m" for Miller (all others)
        """
        international_number = cell_info.symmetry()["international_number"]
        if 194 >= international_number >= 143:
            return "w"  # "hP, hR" (hexagonal or rhombohedral)
        return "m"  # "rest" (all other crystal systems)

    def extract_info(self, file: Crystal, size: int) -> None:
        """
        Extract crystal information and prepare supercell data.

        This method performs the following steps:
        1. Generate a supercell of the specified size
        2. Extract atomic numbers and fractional coordinates
        3. Remove duplicate points and scale to unit cell
        4. Transform to cartesian coordinates

        Args:
            file: Crystal object containing structural data
            size: Size multiplier for the supercell (e.g., 2 creates a 2x2x2 supercell)
        """
        # Generate supercell and convert to list for processing
        supercell = file.supercell(size, size, size)
        full_info_cell = list(supercell.itersorted())

        # Convert Crystal's lattice_vectors to numpy array and prepare for transformations
        lattice_array = np.array(file.lattice_vectors)
        self.lattice_vectors = self.prepare_lattice_vectors(lattice_array)

        # Extract atomic numbers for each point in the supercell
        self.super_cell_atomic_numbers = np.array(
            [atom_point.atomic_number for atom_point in full_info_cell]
        )

        # Extract fractional coordinates from the supercell
        cell = np.array([atom_point.coords_fractional for atom_point in full_info_cell])

        # Remove duplicate points (atoms at the same position)
        sorted_cell = np.unique(cell, axis=0)

        # Scale coordinates back to unit cell (0-1 range)
        compact_cell = sorted_cell / size

        # Prepare for transformation by adding a column of ones (homogeneous coordinates)
        augmented_cell = np.column_stack(
            [compact_cell, np.ones(len(compact_cell))]
        )

        # Transform to cartesian coordinates using lattice vectors
        self.super_cell = (self.lattice_vectors @ augmented_cell.T).T

    def _handle_negative_zeroes(self) -> None:
        """Fix negative zero values in the supercell coordinates."""
        mask = np.where(self.super_cell == 0)
        self.super_cell[mask] += 1
        self.super_cell[mask] -= 1

    def put_points_in_cell(self, points: np.ndarray) -> np.ndarray:
        """
        Adjust points to lie within the unit cell.

        This method transforms points to fractional coordinates, adjusts them to be
        within the unit cell (0-1 range), and transforms them back to cartesian coordinates.

        Args:
            points: Array of points in cartesian coordinates with shape (n, m, 3)
                   where n is the number of matrices and m is the number of points

        Returns:
            Adjusted points that lie within the unit cell with the same shape as input
        """
        inverse = np.linalg.inv(self.lattice_vectors)

        # Transform points to fractional coordinates
        scaled_points = np.einsum("ij,klj->kli", inverse, points)
        scaled_points = np.around(scaled_points, 14)

        # Adjust points that are outside the unit cell
        mask_points_above_cell = scaled_points > 1
        mask_points_under_cell = scaled_points < 0
        scaled_points[mask_points_above_cell] -= 1
        scaled_points[mask_points_under_cell] += 1

        # Handle zero values to avoid negative zeros and precision issues
        mask_zero = scaled_points == 0
        scaled_points[mask_zero] -= 1
        scaled_points[mask_zero] += 1

        # Transform back to cartesian coordinates
        adjusted_points = np.einsum("ij,klj->kli", self.lattice_vectors, scaled_points)

        return cast(np.ndarray, adjusted_points)

    def __mul__(self, matrices: np.ndarray) -> np.ndarray:
        """
        Apply symmetry matrices to the supercell points.

        Args:
            matrices: Array of transformation matrices

        Returns:
            Transformed points adjusted to lie within the unit cell
        """
        result = matrices @ self.super_cell.T
        result_adjusted = self.put_points_in_cell(result)
        return result_adjusted

    @property
    def volume(self) -> float:
        """Calculate the volume of the unit cell."""
        return float(np.linalg.det(self.lattice_vectors))

    def __str__(self) -> str:
        """Generate a string representation for debugging."""
        # Create a list of fields to include in the string representation
        fields: List[Tuple[str, Any]] = [
            ("base_type", self.base_type),
            ("super_cell_shape", self.super_cell.shape if self.super_cell.size > 0 else "empty"),
            ("atomic_numbers_count", len(self.super_cell_atomic_numbers)),
            ("symmetry_operations_count", len(self.symmetry_operations)),
            ("volume", self.volume)
        ]

        # Write detailed symmetry operations to a file for inspection
        with open("symmetry_operations.txt", "w", encoding="utf-8") as f:
            operations = [
                ("symmetry_operations", self.symmetry_operations),
                ("symmetry_operations_inverses", self.symmetry_operations_inverses)
            ]
            for name, value in operations:
                f.write(f"{name}: \n")
                for mat in value:
                    f.write(str(mat) + "\n")
                f.write("\n")

        # Return a concise string representation
        return "MyCell(" + ", ".join(f"{name}={value}" for (name, value) in fields) + ")"


if __name__ == "__main__":
    args = MyCell("krysztalki/workDir/cif files/1000003.cif", size=1)
    print(args)
