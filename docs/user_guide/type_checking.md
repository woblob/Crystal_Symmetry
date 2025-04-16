# Runtime Type Checking

This guide explains how to use the runtime type checking features in the Crystal Symmetry project.

## Overview

The Crystal Symmetry project uses Python's type annotations to provide static type checking with tools like mypy. Additionally, it provides optional runtime type checking using the `typeguard` library, which can validate function parameters and return values during execution.

Runtime type checking is particularly useful during development and testing, as it can catch type errors that might otherwise go unnoticed until they cause problems in production.

## Installation

To use runtime type checking, you need to install the `typeguard` library:

```bash
pip install typeguard
```

Or install all development dependencies:

```bash
pip install -r requirements-dev.txt
```

## Enabling Runtime Type Checking

Runtime type checking is disabled by default for performance reasons. To enable it, set the `KRYSZTALKI_ENABLE_TYPE_CHECKING` environment variable to a truthy value (`1`, `true`, `yes`, or `on`):

### On Windows

```powershell
$env:KRYSZTALKI_ENABLE_TYPE_CHECKING = "1"
python your_script.py
```

### On Linux/macOS

```bash
KRYSZTALKI_ENABLE_TYPE_CHECKING=1 python your_script.py
```

## Using Type Checking Decorators

The `check_types` decorator can be applied to functions and methods to enable runtime type checking:

```python
from krysztalki.utils.type_checking import check_types

@check_types
def calculate_distance(point1: tuple[float, float, float], 
                       point2: tuple[float, float, float]) -> float:
    """Calculate the Euclidean distance between two 3D points."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
```

With type checking enabled, calling this function with invalid types will raise a `TypeError`:

```python
# This will raise TypeError if type checking is enabled
calculate_distance(("0", 0.0, 0.0), (1.0, 1.0, 1.0))
```

## Checking Individual Values

You can also check individual values using the `check_type` function:

```python
from krysztalki.utils.type_checking import check_type

# Check that a value is of the expected type
point = check_type((1.0, 2.0, 3.0), tuple[float, float, float])

# This will raise TypeError if type checking is enabled
invalid_point = check_type(("1", 2.0, 3.0), tuple[float, float, float])
```

## Type Checking in Classes

You can apply the `check_types` decorator to class methods, including `__init__`:

```python
from krysztalki.utils.type_checking import check_types

class CrystalAnalyzer:
    @check_types
    def __init__(self, lattice_parameters: tuple[float, float, float, float, float, float]):
        self.lattice_parameters = lattice_parameters
    
    @check_types
    def calculate_volume(self) -> float:
        a, b, c, alpha, beta, gamma = self.lattice_parameters
        # Calculate and return volume
        return volume
```

## Performance Considerations

Runtime type checking adds overhead to function calls, so it's recommended to:

1. Enable it during development and testing, but disable it in production
2. Apply it selectively to critical functions rather than decorating every function
3. Consider using it in test environments to catch type errors early

## Example

See the `examples/type_checking_example.py` file for a complete example of how to use runtime type checking in the Crystal Symmetry project.
