"""
Functions for reading and processing crystallographic information files (CIF).

This module provides utilities for loading crystal structures from files or databases
and manipulating crystal data for symmetry analysis.
"""

import json
import pathlib
from typing import Tuple, Callable, Dict, Any, List, Optional

import numpy as np
from crystals import Crystal, Atom
from numpy.typing import NDArray

# Import custom type definitions
from krysztalki.core.crystal_types import Point3D, PointArray
from krysztalki.utils.type_definitions import FilePath


def crystal_from_db_record(crystal_data: Dict[str, Any]) -> Crystal:
    """
    Convert a database crystal record to a Crystal object.

    Args:
        crystal_data: Dictionary containing crystal data from the database

    Returns:
        Crystal object constructed from the database data
    """
    # Extract lattice parameters
    lattice_params = json.loads(crystal_data["lattice_parameters"])
    a, b, c = lattice_params[0:3]

    # Create lattice vectors (assuming orthogonal for now)
    lattice_vectors = np.array([[a, 0, 0], [0, b, 0], [0, 0, c]])

    # Create atoms list
    atoms = []
    for atom_data in crystal_data["atoms"]:
        # Create an Atom object for each atom in the database
        atom = Atom(
            element=atom_data["element"],
            coords=[atom_data["x"], atom_data["y"], atom_data["z"]],
        )
        atoms.append(atom)

    # Create and return the Crystal object
    return Crystal(unitcell=atoms, lattice_vectors=lattice_vectors)


def read_cif(file_path: FilePath) -> Crystal:
    """
    Open a CIF file from local repository or download from Crystallography Open Database.
    If a COD ID is provided, first checks if the structure exists in the database.

    Args:
        file_path: Can be either an integer (COD number) or a string (path to CIF file)

    Returns:
        Crystal: A Crystal object from the crystals library

    Examples:
        >>> crystal = read_cif(1000041)  # NaCl Fm-3m
        >>> crystal = read_cif('path/to/file.cif')
    """
    try:
        # If file_path is a COD ID, first check if it exists in the database
        cod_id = int(file_path)

        # Import here to avoid circular imports
        from krysztalki.db.utils import get_crystal_by_cod_id, init_database

        # Check if the crystal structure exists in the database
        db_conn = init_database()
        try:
            crystal_data = get_crystal_by_cod_id(cod_id, db_conn)

            if crystal_data:
                # Structure found in database, but for now we'll still fetch from COD
                # to ensure we have all the data we need
                print(f"Found crystal structure with COD ID {cod_id} in local database")
                # TODO: Implement proper conversion from database record to Crystal object
                # return crystal_from_db_record(crystal_data)
                return Crystal.from_cod(cod_id)
        finally:
            db_conn.close()

        # If not found in database, fetch from COD
        print(
            f"Fetching crystal structure with COD ID {cod_id} from Crystallography Open Database"
        )
        return Crystal.from_cod(cod_id)
    except ValueError:
        pass

    full_path = pathlib.Path(str(file_path)).absolute()
    return Crystal.from_cif(str(full_path))


def eqPoints(POINT: Point3D) -> PointArray:
    """
    Generate equivalent points by adding 1 to coordinates with zero values.

    Args:
        POINT: A 3D point array [x, y, z] with some zero values

    Returns:
        Array of equivalent points with zeros replaced by ones in various combinations
    """
    zera = np.where(POINT == 0)[0]
    ilepow = 2**zera.size
    mylist = np.empty((ilepow - 1, 3))
    for n in range(1, ilepow):
        val = f"{n:b}"
        jkl = zera.size - len(val)
        if jkl:
            val = "0" * jkl + val
        NP = POINT.copy()
        for indexV, indexP in enumerate(zera):
            if int(val[indexV]):
                NP[indexP] += 1
        mylist[n - 1] = NP
    return mylist


def allEqPoints(CELL: PointArray) -> PointArray:
    """
    Find all points with zeros and add their equivalent to make whole cell.

    Args:
        CELL: Array of points in fractional coordinates

    Returns:
        Array with additional equivalent points added
    """
    CELLwith0s = CELL[~CELL.all(axis=1)]
    for point in CELLwith0s:
        CELL = np.append(CELL, eqPoints(point), axis=0)
    # Explicitly cast the return value to satisfy mypy
    result: np.ndarray = np.unique(CELL, axis=0)
    return result


def millerORweber(ITN: int) -> str:
    """
    Determine which coordinate system to use based on international table number.

    Args:
        ITN: International table number of the space group

    Returns:
        "w" for Weber indices (hexagonal) or "m" for Miller indices (others)
    """
    if ITN > 194 or ITN < 143:
        return "m"  # "rest"
    return "w"  # "hP, hR"


def getSCell(
    func: Callable[[FilePath], Crystal], filename: FilePath, size: int
) -> Tuple[PointArray, str]:
    """
    Get cell from CIF file or database and process it into a supercell.

    Args:
        func: Function to read the crystal structure (e.g., read_cif)
        filename: Path to CIF file or COD identifier
        size: Size of the supercell

    Returns:
        Tuple of (points array, coordinate system type)
    """
    file = func(filename)
    basetype = millerORweber(file.symmetry()["international_number"])
    points = file.supercell(size, size, size).itersorted()

    # Initialize cell with first point or default values
    if size % 2:
        cell = np.array([1.0, 1.0, 1.0])
    else:
        first_point = next(points)
        coords = np.array(first_point.coords_fractional)
        scale_factor = size / 2
        cell = np.array(
            [
                coords[0] / scale_factor - 1.0,
                coords[1] / scale_factor - 1.0,
                coords[2] / scale_factor - 1.0,
            ]
        )

    # Add all remaining points to the cell
    for el in points:
        coords = np.array(el.coords_fractional)
        scale_factor = size / 2
        new_point = np.array(
            [
                coords[0] / scale_factor - 1.0,
                coords[1] / scale_factor - 1.0,
                coords[2] / scale_factor - 1.0,
            ]
        )
        cell = np.vstack((cell, new_point))

    return allEqPoints(cell), basetype
