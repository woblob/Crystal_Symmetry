#!/usr/bin/env python
"""
Test script for the MyCell class in cifParsing.py.
This script instantiates MyCell with different CIF files
and tests its functionality.
"""
import sys
import os
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import the MyCell class
from krysztalki.workDir.cifParsing import MyCell

def test_mycell_instantiation():
    """Test if MyCell can be instantiated with a CIF file."""
    cif_file = "krysztalki/workDir/cif files/1000003.cif"

    print(f"Testing MyCell instantiation with {cif_file}...")

    try:
        cell = MyCell(cif_file, size=1)
        print("✓ Successfully instantiated MyCell")

        # Test some basic properties
        print(f"Base type: {cell.base_type}")
        print(f"Lattice vectors shape: {cell.lattice_vectors.shape}")
        print(f"Super cell shape: {cell.super_cell.shape}")
        print(f"Number of symmetry operations: {len(cell.symmetry_operations)}")

        return True
    except Exception as e:
        print(f"✗ Failed to instantiate MyCell: {str(e)}")
        return False

if __name__ == "__main__":
    print("Running MyCell tests...")
    success = test_mycell_instantiation()

    if success:
        print("\nAll tests passed!")
        sys.exit(0)
    else:
        print("\nSome tests failed.")
        sys.exit(1) 