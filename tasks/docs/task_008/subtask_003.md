# Subtask 8.3: Implement core function tests

**Status:** pending

**Dependencies:** 8.1, 8.2

**Description:** Write tests for core functions focusing on essential crystallographic algorithms.

## Details

# Core Function Tests Implementation Plan

## Test Categories
- Mathematical utility functions
- Crystallographic calculations
- File parsing and handling
- Symmetry operations

## Test Structure
- Each test file should match a source module
- Group tests by function or logical component
- Use clear naming indicating what is being tested

## Testing Approach
- Test normal operation with valid inputs
- Verify results against known expected values
- Use parametrized tests for multiple input scenarios
- Check performance for computationally intensive functions

## Example Test Implementation
```python
import pytest
import numpy as np
from crystal_symmetry.core import calculate_unit_cell_volume

def test_calculate_unit_cell_volume_cubic():
    """Test volume calculation for cubic unit cell."""
    # For a cubic cell with a=b=c=5.0, α=β=γ=90°
    a = b = c = 5.0
    alpha = beta = gamma = 90.0
    
    expected_volume = 125.0  # 5³
    volume = calculate_unit_cell_volume(a, b, c, alpha, beta, gamma)
    
    assert np.isclose(volume, expected_volume, rtol=1e-10)

def test_calculate_unit_cell_volume_triclinic():
    """Test volume calculation for triclinic unit cell."""
    a, b, c = 5.0, 6.0, 7.0
    alpha, beta, gamma = 80.0, 85.0, 100.0
    
    # Pre-calculated reference value
    expected_volume = 204.74271921552555
    volume = calculate_unit_cell_volume(a, b, c, alpha, beta, gamma)
    
    assert np.isclose(volume, expected_volume, rtol=1e-10)

@pytest.mark.parametrize("unit_cell,expected_volume", [
    # (a, b, c, α, β, γ), volume
    ((1.0, 1.0, 1.0, 90.0, 90.0, 90.0), 1.0),
    ((2.0, 2.0, 2.0, 90.0, 90.0, 90.0), 8.0),
    ((3.0, 4.0, 5.0, 90.0, 90.0, 90.0), 60.0),
])
def test_calculate_unit_cell_volume_parametrized(unit_cell, expected_volume):
    """Test volume calculation with multiple unit cells."""
    a, b, c, alpha, beta, gamma = unit_cell
    volume = calculate_unit_cell_volume(a, b, c, alpha, beta, gamma)
    assert np.isclose(volume, expected_volume, rtol=1e-10)
```

## Documentation Integration
- Add doctest examples in code that can also be run as tests
- Verify that documentation examples are correct
- Test edge cases mentioned in documentation

## Performance Testing
- Add benchmarks for performance-critical functions
- Measure execution time for large inputs
- Test memory usage for large structures


## Navigation
- [Back to Task Overview](overview.md)
- [Previous Subtask](subtask_002.md)
- [Next Subtask](subtask_004.md)

