import pathlib

import numpy as np
from crystals import Crystal


class MyCell:
    def __init__(self, file_name: str, size: int):
        file = self.getfile(file_name)

        self.symmetry_operations = np.array(file.symmetry_operations())
        # .transpose((0, 2, 1))
        self.symmetry_operations_inverses = \
            self.get_symmetry_operations_inverses()
        self.base_type = self.miller_or_weber(file)
        self.extract_info(file, size)
        self._handle_negative_zeroes()
        self.super_cell_indexes = np.arange(len(self.super_cell))

    def prepare_lattice_vectors(self, lattice_vectors):
        expanded_lattice_vectors = \
            np.column_stack((lattice_vectors, np.zeros(3)))

        expanded_lattice_vectors = \
            np.row_stack((expanded_lattice_vectors, np.zeros(4)))

        expanded_lattice_vectors[-1, -1] = 1

        return np.around(expanded_lattice_vectors, 14)

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

        return all_inverses[index_mask]

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

    def extract_info(self, file: Crystal, size: int):
        full_info_cell = list(file.supercell(size, size, size).itersorted())

        self.lattice_vectors = self.prepare_lattice_vectors(
            file.lattice_vectors
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

    def _handle_negative_zeroes(self):
        mask = np.where(self.super_cell == 0)
        self.super_cell[mask] += 1
        self.super_cell[mask] -= 1

    def put_points_in_cell(self, points):
        inverse = np.linalg.inv(self.lattice_vectors)  # cos tu nie gra
        # scaled_points = inverse @ points.T  #[:, :, np.newaxis]
        result_einsum = np.einsum("ij,klj->kli", inverse, points)

        rounded_result = np.around(result_einsum, 14)

        mask_points_above_cell = scaled_points > 1
        mask_points_under_cell = scaled_points < 0
        scaled_points[mask_points_above_cell] -= 1
        scaled_points[mask_points_under_cell] += 1
        mask_zero = scaled_points == 0
        scaled_points[mask_zero] -= 1
        scaled_points[mask_zero] += 1

        adjusted_points = self.lattice_vectors @ scaled_points.T

        print(adjusted_points)
        print(points)
        print(adjusted_points - points)

        return points

    def __mul__(self, matrices):
        result = matrices @ self.super_cell.T
        result_adjusted = self.put_points_in_cell(result)

        return result_adjusted

    @property
    def volume(self):
        return np.linalg.det(self.lattice_vectors)

    def __str__(self):
        fields = [
            # ("super_cell", self.super_cell),
            # ("super_cell_atomic_numbers", self.super_cell_atomic_numbers),
            # ("super_cell_indexes", self.super_cell_indexes),
            # ("lattice_vectors", self.lattice_vectors),
            # ("base_type", self.base_type),
            # ("symmetry_operations", self.symmetry_operations),
            # ("symmetry_operations_inverses", self.symmetry_operations_inverses),
        ]
        with open("file.txt", "w") as f:
            for name, value in [("symmetry_operations", self.symmetry_operations),
                ("symmetry_operations_inverses", self.symmetry_operations_inverses)]:
                f.write(f"{name}: \n")
                for mat in value:
                    f.write(str(mat) + "\n")
                f.write("\n")

        return "\n\n".join(f"{name}: \n{value}" for (name, value) in fields)


if __name__ == "__main__":
    args = MyCell("krysztalki/workDir/cif files/1000003.cif", size=1)
    print(args)
