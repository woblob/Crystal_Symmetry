"""Type stubs for usunkoor module.

This module provides functions for removing coordinates based on symmetry operations.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
from numpy.typing import NDArray

def usunkoor_mod_3(koorZEW: NDArray[np.float64], MM: Optional[Any] = None) -> Dict[float, Dict[float, Dict[float, bool]]]:
    """Remove coordinates based on symmetry operations (version 3).
    
    Args:
        koorZEW: Array of coordinates to process
        MM: Module containing symmetry operation functions
        
    Returns:
        Dictionary mapping coordinates to boolean values indicating whether they should be kept
    """
    ...

def usunkoor_mod_2(koorZEW: NDArray[np.float64], MM: Optional[Any] = None) -> Dict[float, Dict[float, Dict[float, bool]]]:
    """Remove coordinates based on symmetry operations (version 2).
    
    Args:
        koorZEW: Array of coordinates to process
        MM: Module containing symmetry operation functions
        
    Returns:
        Dictionary mapping coordinates to boolean values indicating whether they should be kept
    """
    ...
