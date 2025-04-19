# Subtask 9.2: Implement CIF parsing integration tests

**Status:** pending

**Dependencies:** 9.1

**Description:** Create integration tests to verify CIF file parsing with real-world examples.

## Details

# CIF Parsing Integration Tests Implementation Plan

## Test Objectives
- Verify parsing of real-world CIF files
- Test handling of various CIF dialects and formats
- Validate structure extraction from complex CIF data
- Ensure proper error handling for malformed CIF files

## Test Data Sources
- Crystallography Open Database (COD)
- Cambridge Structural Database (CSD) samples
- Custom CIF files with known challenging features
- Published structures from literature

## Test Categories
1. **Standard Format Parsing**
   - Simple crystal structures
   - Multiple data blocks
   - Various crystal systems

2. **Complex Format Handling**
   - Multi-model structures
   - Loop structures with multiple categories
   - Files with extended syntax features

3. **Error Case Handling**
   - Malformed syntax
   - Incomplete data
   - Contradictory information

## Implementation Example
```python
import pytest
from pathlib import Path
from crystal_symmetry.io import CIFParser
from crystal_symmetry.structure import CrystalStructure

def test_parse_simple_cubic(sample_cif_files):
    """Test parsing a simple cubic structure CIF file."""
    # Get the CIF file path from the fixture
    cif_path = sample_cif_files["simple_cubic"]
    
    # Parse the CIF file
    parser = CIFParser()
    structure = parser.parse_file(cif_path)
    
    # Validate structure properties
    assert isinstance(structure, CrystalStructure)
    assert structure.lattice_type == "cubic"
    assert len(structure.atoms) > 0
    
    # Check specific properties
    a, b, c, alpha, beta, gamma = structure.lattice_parameters
    assert a == pytest.approx(b)
    assert b == pytest.approx(c)
    assert alpha == pytest.approx(90.0)
    assert beta == pytest.approx(90.0)
    assert gamma == pytest.approx(90.0)

def test_parse_multiblock_cif(sample_cif_files, tmp_path):
    """Test parsing a CIF file with multiple data blocks."""
    cif_path = sample_cif_files["multi_block"]
    
    parser = CIFParser()
    structures = parser.parse_file(cif_path, multi_block=True)
    
    # Verify multiple structures were parsed
    assert isinstance(structures, list)
    assert len(structures) > 1
    
    # Check that each structure has valid properties
    for structure in structures:
        assert isinstance(structure, CrystalStructure)
        assert hasattr(structure, "lattice_parameters")
        assert hasattr(structure, "space_group")
        assert len(structure.atoms) > 0
```

## Performance Considerations
- Benchmark parsing speed for large CIF files
- Test memory usage during parse operations
- Evaluate incremental parsing for large files

## Validation Strategy
- Compare parsed results against reference data
- Verify key properties (unit cell, space group, atom positions)
- Validate symmetry operation generation from parsed data


## Navigation
- [Back to Task Overview](overview.md)
- [Previous Subtask](subtask_001.md)
- [Next Subtask](subtask_003.md)

