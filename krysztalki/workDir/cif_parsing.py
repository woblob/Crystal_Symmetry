import pathlib
from typing import Union, Dict, Any, List, Tuple, Optional, cast

import numpy as np
from crystals import Crystal
from krysztalki.utils.task_manager import CrystalTaskManager


class MyCell:
    def __init__(self, file_name: Union[str, int], size: int):
        # Initialize instance variables
        self.symmetry_operations = np.array([])
        self.symmetry_operations_inverses = np.array([])
        self.lattice_vectors = np.array([])
        self.super_cell = np.array([])
        self.super_cell_atomic_numbers = np.array([])
        self.super_cell_indexes = np.array([])
        self.base_type = "m"  # Default to Miller indices

        # Create task for analyzing this crystal
        self.task_manager = CrystalTaskManager()
        task: Optional[Dict[str, Any]] = self.task_manager.add_crystal_analysis_task(str(file_name))

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
        expanded_lattice_vectors = \
            np.column_stack((lattice_vectors, np.zeros(3)))

        expanded_lattice_vectors = \
            np.vstack((expanded_lattice_vectors, np.zeros(4)))

        expanded_lattice_vectors[-1, -1] = 1

        return cast(np.ndarray, np.around(expanded_lattice_vectors, 14))

    def get_symmetry_operations_inverses(self) -> np.ndarray:
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
        open cif file from local repository
        or
        download file from Crystallography Open Database

        file_name can be either:
            integer: COD number
            string:  CIF file

        examples:
            file_name = 1000041 # NaCl Fm-3m
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
        # """
        # Determine which coordinates to choose:
        # 3D for Parallelepiped or '4'D for hexagonal.
        # All numbers between [143-194] are for hexagonal groups.
        # """
        international_number = cell_info.symmetry()["international_number"]
        if 194 >= international_number >= 143:
            return "w"  # "hP, hR"
        return "m"  # "rest"

    def extract_info(self, file: Crystal, size: int) -> None:
        full_info_cell = list(file.supercell(size, size, size).itersorted())

        self.lattice_vectors = self.prepare_lattice_vectors(
            np.array(file.lattice_vectors)
        )

        self.super_cell_atomic_numbers = np.array(
            [p.atomic_number for p in full_info_cell]
        )

        cell = np.array([point.coords_fractional for point in full_info_cell])

        # for i in range(3):
        #     mask = np.where(whole_cell[:, i] == 0)
        #     points_with_zeroes = whole_cell[mask]
        #     points_with_zeroes[:, i] += size
        #     whole_cell = np.append(whole_cell, points_with_zeroes, axis=0)

        sorted_cell = np.unique(cell, axis=0)

        compact_cell = sorted_cell / size

        augmented_cell = np.column_stack(
            [compact_cell, np.ones(len(compact_cell))]
        )

        self.super_cell = (self.lattice_vectors @ augmented_cell.T).T

    def _handle_negative_zeroes(self) -> None:
        mask = np.where(self.super_cell == 0)
        self.super_cell[mask] += 1
        self.super_cell[mask] -= 1

    def put_points_in_cell(self, points: np.ndarray) -> np.ndarray:
        inverse = np.linalg.inv(self.lattice_vectors)
        # Transform points to fractional coordinates
        scaled_points = np.einsum("ij,klj->kli", inverse, points)
        scaled_points = np.around(scaled_points, 14)

        # Adjust points that are outside the unit cell
        mask_points_above_cell = scaled_points > 1
        mask_points_under_cell = scaled_points < 0
        scaled_points[mask_points_above_cell] -= 1
        scaled_points[mask_points_under_cell] += 1

        # Handle zero values
        mask_zero = scaled_points == 0
        scaled_points[mask_zero] -= 1
        scaled_points[mask_zero] += 1

        # Transform back to cartesian coordinates
        adjusted_points = np.einsum("ij,klj->kli", self.lattice_vectors, scaled_points)

        print(adjusted_points)
        print(points)
        print(adjusted_points - points)

        return cast(np.ndarray, adjusted_points)

    def __mul__(self, matrices: np.ndarray) -> np.ndarray:
        result = matrices @ self.super_cell.T
        result_adjusted = self.put_points_in_cell(result)

        return result_adjusted

    @property
    def volume(self) -> float:
        return float(np.linalg.det(self.lattice_vectors))

    def __str__(self) -> str:
        fields: List[Tuple[str, Any]] = [
            # ("super_cell", self.super_cell),
            # ("super_cell_atomic_numbers", self.super_cell_atomic_numbers),
            # ("super_cell_indexes", self.super_cell_indexes),
            # ("lattice_vectors", self.lattice_vectors),
            # ("base_type", self.base_type),
            # ("symmetry_operations", self.symmetry_operations),
            # ("symmetry_operations_inverses", self.symmetry_operations_inverses),
        ]
        with open("file.txt", "w", encoding="utf-8") as f:
            operations = [
                ("symmetry_operations", self.symmetry_operations),
                ("symmetry_operations_inverses", self.symmetry_operations_inverses)
            ]
            for name, value in operations:
                f.write(f"{name}: \n")
                for mat in value:
                    f.write(str(mat) + "\n")
                f.write("\n")

        return "\n\n".join(f"{name}: \n{value}" for (name, value) in fields)


if __name__ == "__main__":
    args = MyCell("krysztalki/workDir/cif files/1000003.cif", size=1)
    print(args)
