import pathlib

import numpy as np
from crystals import Crystal
from types import UnionType


class MyCell:
    def __init__(self, file_name: str, size: int):
        file = self.getfile(file_name)

        self.symmetry_operations = file.symmetry_operations()
        self.symmetry_operations_inverses = np.linalg.inv(self.symmetry_operations)
        self.base_type = self.miller_or_weber(file)
        self.lattice_vectors = np.around(file.lattice_vectors, 10)
        self.all_eq_points(file, size)
        self._handle_negative_zeroes()
        self.super_cell_indexes = np.arange(len(self.super_cell))

    def getfile(self, file_name: str | int) -> Crystal:
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
        full_path = pathlib.Path(file_name).absolute()
        return Crystal.from_cif(full_path)

    def miller_or_weber(self, cell_info):
        # """
        # Determine which coordinates to choose:
        # 3D for Parallelepiped or '4'D for hexagonal.
        # All numbers between [143-194] are for hexagonal groups.
        # """
        international_number = cell_info.symmetry()["international_number"]
        if 194 >= international_number >= 143:
            return "w"  # "hP, hR"
        return "m"  # "rest"

    def all_eq_points(self, file: Crystal, size: int) -> tuple[np.ndarray, np.ndarray]:
        """ """
        reduced_cell = file.supercell(size, size, size).itersorted()
        whole_cell = np.array(
            [
                np.append(point.coords_fractional, point.atomic_number)
                for point in reduced_cell
            ]
        )

        # for i in range(3):
        #     mask = np.where(whole_cell[:, i] == 0)
        #     points_with_zeroes = whole_cell[mask]
        #     points_with_zeroes[:, i] += size
        #     whole_cell = np.append(whole_cell, points_with_zeroes, axis=0)
        sorted_cell = np.unique(
            whole_cell, axis=0
        )  # bez dodawania scianek jest to do usuniecia

        self.super_cell_atomic_numbers = sorted_cell[:, -1]

        compact_cell = sorted_cell[:, :-1] / (size / 2) - 1
        self.super_cell = np.around(
            np.column_stack((compact_cell, np.ones(len(compact_cell)))), 10
        )

    def _handle_negative_zeroes(self):
        mask = np.where(self.super_cell == 0)
        self.super_cell[mask] += 1
        self.super_cell[mask] -= 1

    def __str__(self):
        fields = [
            self.super_cell,
            self.super_cell_atomic_numbers,
            self.super_cell_indexes,
            self.lattice_vectors,
            self.base_type,
            self.symmetry_operations,
        ]

        return "\n\n".join([str(field) for field in fields])


if __name__ == "__main__":
    args = MyCell("krysztalki/1100043.cif", size=2)
    print(args)
