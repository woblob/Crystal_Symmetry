"""Type stubs for the symmetry group classification module.

This module provides classes for representing and classifying point groups
and symmetry transformations in crystallographic calculations.
"""

from typing import Any, Set, Tuple, Union, Hashable

class PG:
    """Point Group class for representing crystallographic point groups.
    
    A point group is a set of symmetry operations that leave at least one point fixed.
    """
    
    def __init__(self, *args: 'T') -> None:
        """Initialize a Point Group with symmetry operations.
        
        Args:
            *args: Symmetry transformation objects
        """
        self.args: Tuple['T', ...]  # The symmetry operations passed as arguments
        self.symmetries: Set['T']   # Set of symmetry operations in this point group
    
    def __repr__(self) -> str:
        """Get a string representation of the point group.
        
        Returns:
            A comma-separated string of the symmetry operations
        """
        ...

class T:
    """Transformation class for representing symmetry operations.
    
    Each transformation is identified by a string code that specifies the type
    of operation and its orientation.
    """
    
    def __init__(self, args: str) -> None:
        """Initialize a Transformation with a string code.
        
        Args:
            args: String code identifying the transformation (e.g., 'm_100', '2_110')
        """
        self.args: str  # The string code identifying this transformation
    
    def __repr__(self) -> str:
        """Get a string representation of the transformation.
        
        Returns:
            The string code of the transformation
        """
        ...
    
    def __str__(self) -> str:
        """Get a string representation of the transformation.
        
        Returns:
            The string code of the transformation
        """
        ...
    
    def __hash__(self) -> int:
        """Get a hash value for the transformation.
        
        Returns:
            Hash value based on the string code
        """
        ...

# Predefined transformation instances
t_c_000: T  # Identity transformation

# Mirror planes
t_m_100: T  # Mirror plane perpendicular to [100]
t_m_010: T  # Mirror plane perpendicular to [010]
t_m_001: T  # Mirror plane perpendicular to [001]
t_m_110: T  # Mirror plane perpendicular to [110]
t_m_011: T  # Mirror plane perpendicular to [011]
t_m_101: T  # Mirror plane perpendicular to [101]
t_m_m101: T  # Mirror plane perpendicular to [-101]
t_m_m110: T  # Mirror plane perpendicular to [-110]
t_m_0m11: T  # Mirror plane perpendicular to [0-11]

# 2-fold rotation axes
t_2_100: T  # 2-fold rotation around [100]
t_2_010: T  # 2-fold rotation around [010]
t_2_001: T  # 2-fold rotation around [001]
t_2_110: T  # 2-fold rotation around [110]
t_2_101: T  # 2-fold rotation around [101]
t_2_011: T  # 2-fold rotation around [011]
t_2_m110: T  # 2-fold rotation around [-110]
t_2_m101: T  # 2-fold rotation around [-101]
t_2_0m11: T  # 2-fold rotation around [0-11]

# 3-fold rotation axes
t_3_111: T  # 3-fold rotation around [111]
t_3_m111: T  # 3-fold rotation around [-111]
t_3_1m11: T  # 3-fold rotation around [1-11]
t_3_11m1: T  # 3-fold rotation around [11-1]

# 3-fold rotoinversion axes
t_m3_111: T  # 3-fold rotoinversion around [111]
t_m3_m111: T  # 3-fold rotoinversion around [-111]
t_m3_1m11: T  # 3-fold rotoinversion around [1-11]
t_m3_11m1: T  # 3-fold rotoinversion around [11-1]

# 4-fold rotation axes
t_4_100: T  # 4-fold rotation around [100]
t_4_010: T  # 4-fold rotation around [010]
t_4_001: T  # 4-fold rotation around [001]

# 4-fold rotoinversion axes
t_m4_100: T  # 4-fold rotoinversion around [100]
t_m4_010: T  # 4-fold rotoinversion around [010]
t_m4_001: T  # 4-fold rotoinversion around [001]

# Example point group
pg_2_div_m_100: PG  # Point group 2/m with operations along [100]

# Lists of transformations
a: list  # List of transformation codes and objects
b: list  # List of transformation objects
