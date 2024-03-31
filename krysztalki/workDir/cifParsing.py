import pathlib

import numpy as np
from crystals import Crystal


def get_super_cell(
    file_name: str, size: int
) -> tuple[
    np.ndarray, np.ndarray, np.ndarray, tuple[np.ndarray, np.ndarray, np.ndarray], str
]:
    # """
    # Get cell from cod/cif/else.
    # Expand it to super_cell size.
    # Place points between -1 and less than 1
    # Add missing walls of a cell.
    # """
    file = getfile(file_name)
    base_type = miller_or_weber(file)
    lattice_vectors = np.around(file.lattice_vectors, 10)

    full_cell, output_atomic_numbers = all_eq_points(file, size)
    compact_cell = full_cell / (size / 2) - 1
    output_cell = np.around(compact_cell, 10)
    _handle_negative_zeroes(output_cell)

    output_cell_indexes = np.arange(len(output_cell))

    return (
        output_cell,
        output_atomic_numbers,
        output_cell_indexes,
        lattice_vectors,
        base_type,
    )


def getfile(file_name: str) -> Crystal:
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


def miller_or_weber(cell_info):
    # """
    # Determine which coordinates to choose:
    # 3D for Parallelepiped or '4'D for hexagonal.
    # All numbers between [143-194] are for hexagonal groups.
    # """
    international_number = cell_info.symmetry()["international_number"]
    if 194 >= international_number >= 143:
        return "w"  # "hP, hR"
    return "m"  # "rest"


def all_eq_points(file: Crystal, size: int) -> tuple[np.ndarray, np.ndarray]:
    # """
    # building missing outer walls of a cell
    # with labels
    # """
    reduced_cell = file.supercell(size, size, size).itersorted()
    whole_cell = np.array(
        [
            np.append(point.coords_fractional, point.atomic_number)
            for point in reduced_cell
        ]
    )

    for i in range(3):
        mask = np.where(whole_cell[:, i] == 0)
        points_with_zeroes = whole_cell[mask]
        points_with_zeroes[:, i] += size
        whole_cell = np.append(whole_cell, points_with_zeroes, axis=0)
    sorted_cell = np.unique(whole_cell, axis=0)

    return sorted_cell[:, :-1], sorted_cell[:, -1]


def _handle_negative_zeroes(cell: np.ndarray):
    mask = np.where(cell == 0)
    cell[mask] += 1
    cell[mask] -= 1


if __name__ == "__main__":
    args = get_super_cell("cif files/ZnS-Sfaleryt.cif", size=2)
    print(args)
