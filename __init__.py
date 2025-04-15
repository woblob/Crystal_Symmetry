"""
Crystal Symmetry Analysis Package.

A Python package for analyzing and working with crystal symmetry operations.
"""

__version__ = "0.1.0"

# Import the public API
from krysztalki.io.cif import read_cif
from krysztalki.core.symmetry import analyze_symmetry

# Re-export key functions at the top level for convenience
__all__ = ["read_cif", "analyze_symmetry"] 