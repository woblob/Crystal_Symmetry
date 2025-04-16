"""
Example demonstrating how to use runtime type checking in the codebase.

This example shows how to use the type_checking utilities to add runtime
type checking to functions and methods in the codebase.

To run this example with type checking enabled:
    KRYSZTALKI_ENABLE_TYPE_CHECKING=1 python examples/type_checking_example.py
"""

import os
import sys
from typing import List, Dict, Any, Optional, Union, Tuple

import numpy as np
from numpy.typing import NDArray

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from krysztalki.utils.type_checking import check_types, check_type


# Example 1: Simple function with type checking
@check_types
def calculate_distance(point1: Tuple[float, float, float], 
                       point2: Tuple[float, float, float]) -> float:
    """
    Calculate the Euclidean distance between two 3D points.
    
    Args:
        point1: First point coordinates (x, y, z)
        point2: Second point coordinates (x, y, z)
        
    Returns:
        Euclidean distance between the points
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


# Example 2: Function with NumPy arrays and type checking
@check_types
def calculate_centroid(points: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Calculate the centroid of a set of points.
    
    Args:
        points: Array of points with shape (n, 3)
        
    Returns:
        Centroid coordinates with shape (3,)
    """
    return np.mean(points, axis=0)


# Example 3: Class with type-checked methods
class CrystalAnalyzer:
    """Example class demonstrating type checking in methods."""
    
    @check_types
    def __init__(self, lattice_parameters: Tuple[float, float, float, float, float, float]):
        """
        Initialize the CrystalAnalyzer with lattice parameters.
        
        Args:
            lattice_parameters: Tuple of (a, b, c, alpha, beta, gamma)
        """
        self.lattice_parameters = lattice_parameters
    
    @check_types
    def calculate_volume(self) -> float:
        """
        Calculate the unit cell volume.
        
        Returns:
            Volume of the unit cell
        """
        a, b, c, alpha, beta, gamma = self.lattice_parameters
        # Convert angles to radians
        alpha_rad = np.radians(alpha)
        beta_rad = np.radians(beta)
        gamma_rad = np.radians(gamma)
        
        # Calculate volume
        volume = a * b * c * (
            1 - np.cos(alpha_rad)**2 - np.cos(beta_rad)**2 - np.cos(gamma_rad)**2
            + 2 * np.cos(alpha_rad) * np.cos(beta_rad) * np.cos(gamma_rad)
        )**0.5
        
        return volume
    
    @check_types
    def analyze_symmetry(self, points: NDArray[np.float64]) -> Dict[str, Any]:
        """
        Analyze the symmetry of a set of points.
        
        Args:
            points: Array of points with shape (n, 3)
            
        Returns:
            Dictionary containing symmetry analysis results
        """
        # This is just a placeholder for demonstration
        centroid = calculate_centroid(points)
        
        return {
            "centroid": centroid,
            "point_count": len(points),
            "symmetry_operations": ["identity"]
        }


def main():
    """Run the example code."""
    # Check if type checking is enabled
    type_checking_enabled = os.environ.get("KRYSZTALKI_ENABLE_TYPE_CHECKING", "0").lower() in ("1", "true", "yes", "on")
    print(f"Runtime type checking is {'enabled' if type_checking_enabled else 'disabled'}")
    
    try:
        # Example 1: Calculate distance between two points
        point1 = (0.0, 0.0, 0.0)
        point2 = (1.0, 1.0, 1.0)
        distance = calculate_distance(point1, point2)
        print(f"Distance between {point1} and {point2}: {distance}")
        
        # Try with invalid types (should raise TypeError if type checking is enabled)
        try:
            invalid_point = ("0", 0.0, 0.0)  # First coordinate is a string, not a float
            calculate_distance(invalid_point, point2)
            print("Type checking failed: Invalid point coordinates accepted")
        except TypeError as e:
            print(f"Type checking succeeded: {e}")
        
        # Example 2: Calculate centroid of points
        points = np.array([
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ])
        centroid = calculate_centroid(points)
        print(f"Centroid of points: {centroid}")
        
        # Example 3: Use the CrystalAnalyzer class
        # Cubic unit cell (a = b = c = 5.0, alpha = beta = gamma = 90.0)
        analyzer = CrystalAnalyzer((5.0, 5.0, 5.0, 90.0, 90.0, 90.0))
        volume = analyzer.calculate_volume()
        print(f"Unit cell volume: {volume}")
        
        # Analyze symmetry
        symmetry_results = analyzer.analyze_symmetry(points)
        print(f"Symmetry analysis results: {symmetry_results}")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
