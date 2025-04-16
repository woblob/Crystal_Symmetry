"""Type stubs for MMfunc module."""

import numpy as np
from typing import Tuple, List

def full_transform(cell: 'MyCell') -> Tuple[np.ndarray, np.ndarray]: ...

def reduce_cell(
    all_transformed_points_to_indexes: np.ndarray,
    all_transformed_points_to_indexes_inverse: np.ndarray,
    mask_all_syms_normal: np.ndarray
) -> List[int]: ... 