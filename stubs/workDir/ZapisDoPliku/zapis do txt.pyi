"""Type stubs for the text file saving module.

This module provides functions for saving crystallographic data to text files.
"""

from typing import List, Set, Tuple, Any
import numpy as np
from numpy.typing import NDArray

def zapis_zredukowany() -> None:
    """Read symmetry data from a file, reduce it to unique entries, and save to a new file.
    
    Reads from "output of symmetries 2019_09_28_13_06_50.txt" and writes to "plik2.txt".
    """
    ...

def back2normal(output: List[Tuple[float, List[Any]]], size: float) -> List[str]:
    """Convert output data back to a normal format for saving.
    
    Args:
        output: List of tuples containing a float and a list of data
        size: Size parameter for scaling
        
    Returns:
        List of formatted strings ready for writing to a file
    """
    ...

def saveOutput2(OUTPUT: List[Tuple[float, List[Any]]], size: float, filename: str) -> None:
    """Save output data to a text file with a timestamp in the filename.
    
    Args:
        OUTPUT: List of tuples containing a float and a list of data
        size: Size parameter for scaling
        filename: Base filename (timestamp will be appended)
    """
    ...
