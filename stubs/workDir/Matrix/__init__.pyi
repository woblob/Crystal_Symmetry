"""Type stubs for Matrix package.

This package provides matrix operations for crystallographic calculations.
"""

from .matrices_new_extended import _matrix_ID_000, all_matrices
from . import matrices_new

__all__ = ['_matrix_ID_000', 'all_matrices', 'matrices_new']