"""Module for experimental and testing code."""

__all__ = [
    'generate_matrices',
    'validate_matrices',
    'get_matrix_names', 
    'process_names',
    'combine_matrices',
    'validate_combinations'
]

try:
    from .matrices_generated import generate_matrices, validate_matrices
    from .names_of_matrices import get_matrix_names, process_names
    from .all_combinations_of_matrices import combine_matrices, validate_combinations
except ImportError as e:
    import warnings
    warnings.warn(f"Some imports failed: {str(e)}")
