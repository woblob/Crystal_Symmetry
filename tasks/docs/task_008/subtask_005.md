# Subtask 8.5: Add edge case and error condition tests

**Status:** pending

**Dependencies:** 8.3, 8.4

**Description:** Create tests for boundary conditions, error handling, and exceptional cases.

## Details

# Edge Case and Error Condition Tests Implementation Plan

## Error Categories to Test
- Input validation failures
- Boundary conditions
- Numerical precision issues
- Resource limitations
- Error recovery mechanisms

## Testing Techniques
- Use pytest.raises to verify exceptions
- Test with invalid or malformed inputs
- Verify appropriate error messages
- Test recovery from error conditions
- Create stress tests with extreme inputs

## Implementation Examples

### Input Validation Tests
```python
import pytest
from crystal_symmetry.core import calculate_unit_cell_volume
from crystal_symmetry.exceptions import InputError

def test_negative_lattice_parameters():
    """Test that negative lattice parameters raise an exception."""
    with pytest.raises(InputError, match="must be positive"):
        calculate_unit_cell_volume(-1.0, 5.0, 5.0, 90.0, 90.0, 90.0)

def test_invalid_angles():
    """Test that invalid angles raise appropriate exceptions."""
    # Angle too small
    with pytest.raises(InputError, match="between 0 and 180"):
        calculate_unit_cell_volume(5.0, 5.0, 5.0, -10.0, 90.0, 90.0)
    
    # Angle too large
    with pytest.raises(InputError, match="between 0 and 180"):
        calculate_unit_cell_volume(5.0, 5.0, 5.0, 90.0, 190.0, 90.0)

def test_invalid_space_group():
    """Test handling of invalid space group symbols."""
    from crystal_symmetry.symmetry import generate_symmetry_operations
    
    with pytest.raises(ValueError, match="Invalid space group symbol"):
        generate_symmetry_operations("not-a-real-space-group")
```

### Boundary Condition Tests
```python
def test_nearly_zero_cell_parameters():
    """Test behavior with very small cell parameters."""
    # Should still calculate but may have precision issues
    volume = calculate_unit_cell_volume(1e-10, 1e-10, 1e-10, 90.0, 90.0, 90.0)
    assert volume > 0  # Volume should be positive but very small

def test_nearly_equal_angles():
    """Test with angles that are nearly but not exactly the same."""
    # Two calculations with very slightly different angles
    vol1 = calculate_unit_cell_volume(5.0, 5.0, 5.0, 90.0, 90.0, 90.0)
    vol2 = calculate_unit_cell_volume(5.0, 5.0, 5.0, 90.0, 90.0, 90.00001)
    
    # Should be nearly the same volume within numerical precision
    assert abs(vol1 - vol2) < 1e-8
```

### Error Recovery Tests
```python
def test_parser_recovery_from_incomplete_cif():
    """Test parser recovery from incomplete CIF file."""
    from crystal_symmetry.io import CIFParser
    
    incomplete_cif = """
    data_test
    _cell_length_a 5.0
    # Missing other required fields
    """
    
    parser = CIFParser(strict_mode=False)
    structure = parser.parse_string(incomplete_cif)
    
    # Check that parser recovered by using defaults
    assert structure is not None
    assert structure.lattice_parameters[0] == 5.0
    # Other parameters should have default values
    assert structure.lattice_parameters[1] == 1.0  # Default value
```

### Resource Limitation Tests
```python
@pytest.mark.slow
def test_large_structure_handling():
    """Test handling of very large structures that may cause memory issues."""
    from crystal_symmetry.structure import CrystalStructure
    
    # Create a large structure with many atoms
    large_structure = CrystalStructure(
        lattice_parameters=(100.0, 100.0, 100.0, 90.0, 90.0, 90.0),
        space_group="P1"
    )
    
    # Add many atoms (generate a large structure)
    for i in range(10000):
        x, y, z = i % 10 / 10, (i // 10) % 10 / 10, (i // 100) % 10 / 10
        large_structure.add_atom("H", [x, y, z])
    
    # Verify the structure can be processed without errors
    assert large_structure.calculate_volume() == 1000000.0
    assert len(large_structure.atoms) == 10000
```

## Testing Strategies for Edge Cases
- Create focused test groups for specific edge case categories
- Include tests for numerical edge cases (zero, NaN, infinity)
- Test threading and concurrency edge cases if applicable
- Test interaction with file system limits and permissions


## Navigation
- [Back to Task Overview](overview.md)
- [Previous Subtask](subtask_004.md)
- [Next Subtask](subtask_006.md)

