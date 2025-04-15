"""
Functions for reading and processing crystallographic information files (CIF).

This module provides utilities for loading crystal structures from files or databases
and manipulating crystal data for symmetry analysis.
"""
from crystals import Crystal
import numpy as np
import pathlib
from typing import Union, Tuple, Callable, Any, cast


def read_cif(file_path: Union[str, int]) -> Crystal:
    """
    Open a CIF file from local repository or download from Crystallography Open Database.
    
    Args:
        file_path: Can be either an integer (COD number) or a string (path to CIF file)
        
    Returns:
        Crystal: A Crystal object from the crystals library
        
    Examples:
        >>> crystal = read_cif(1000041)  # NaCl Fm-3m
        >>> crystal = read_cif('path/to/file.cif')
    """
    try:
        value = int(file_path)
        return Crystal.from_cod(value)
    except ValueError:
        pass
    
    full_path = pathlib.Path(str(file_path)).absolute()
    return Crystal.from_cif(str(full_path))


def eqPoints(POINT: np.ndarray) -> np.ndarray:
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


def allEqPoints(CELL: np.ndarray) -> np.ndarray:
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


def getSCell(func: Callable[[Union[str, int]], Crystal], 
            filename: Union[str, int], 
            size: int) -> Tuple[np.ndarray, str]:
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
        cell = np.array([
            coords[0] / scale_factor - 1.0,
            coords[1] / scale_factor - 1.0,
            coords[2] / scale_factor - 1.0
        ])
    
    # Add all remaining points to the cell
    for el in points:
        coords = np.array(el.coords_fractional)
        scale_factor = size / 2
        new_point = np.array([
            coords[0] / scale_factor - 1.0,
            coords[1] / scale_factor - 1.0,
            coords[2] / scale_factor - 1.0
        ])
        cell = np.vstack((cell, new_point))
    
    return allEqPoints(cell), basetype
