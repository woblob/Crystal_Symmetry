"""Type stubs for cifParsing module."""

import numpy as np
from typing import List, Tuple

class MyCell:
    symmetry_operations: List[np.ndarray]
    symmetry_operations_inverses: List[np.ndarray]
    super_cell_indexes: List[int]

    def __init__(self, filename: str, size: int = 1) -> None: ... 