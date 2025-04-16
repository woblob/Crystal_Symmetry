"""Type stubs for the test generation module.

This module provides utilities for generating test files for symmetry matrices.
"""

from typing import List

# List of hexagonal symmetry operations
syms_hex: List[str]

# Template for test file header
text: str

# Template for inner test function
inner: str

# Template for test function with additional information
inner_test: str
