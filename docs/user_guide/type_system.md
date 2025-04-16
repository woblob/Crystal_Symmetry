# Type System Guide

This guide provides an overview of the type system used in the Crystal Symmetry project and explains how to use it effectively.

## Table of Contents

- [Overview](#overview)
- [Type Annotations](#type-annotations)
- [Custom Type Definitions](#custom-type-definitions)
- [NumPy Array Types](#numpy-array-types)
- [Utility Types](#utility-types)
- [Type Checking](#type-checking)
  - [Static Type Checking](#static-type-checking)
  - [Runtime Type Checking](#runtime-type-checking)
- [Best Practices](#best-practices)
- [Common Pitfalls](#common-pitfalls)
- [Advanced Type Hints Usage](#advanced-type-hints-usage)
  - [Type Variables and Generic Functions](#type-variables-and-generic-functions)
  - [Protocol Classes](#protocol-classes)
  - [Type Guards](#type-guards)
- [Compatibility with Third-Party Libraries](#compatibility-with-third-party-libraries)
  - [Using Stub Files for External Libraries](#using-stub-files-for-external-libraries)
  - [Type Hints for NumPy and Scientific Libraries](#type-hints-for-numpy-and-scientific-libraries)
- [Practical Examples](#practical-examples)
  - [Example 1: Crystallographic Calculations](#example-1-crystallographic-calculations)
  - [Example 2: Type-Safe Configuration Handling](#example-2-type-safe-configuration-handling)
- [Migrating Existing Code to Use Type Hints](#migrating-existing-code-to-use-type-hints)
  - [Incremental Approach](#incremental-approach)
  - [Using Type Comments for Python 3.5 Compatibility](#using-type-comments-for-python-35-compatibility)
  - [Using `# type: ignore` Comments](#using--type-ignore-comments)
  - [Using `Any` as a Placeholder](#using-any-as-a-placeholder)
  - [Dealing with Complex Types](#dealing-with-complex-types)
  - [Using Tools to Help Migration](#using-tools-to-help-migration)
  - [Testing After Adding Type Hints](#testing-after-adding-type-hints)
- [Further Reading](#further-reading)

## Overview

The Crystal Symmetry project uses Python's type annotations to provide static type checking and improve code documentation. The type system consists of:

1. **Type annotations** in function signatures and variable declarations
2. **Custom type definitions** for domain-specific types
3. **Stub files** for external dependencies
4. **Runtime type checking** for validation during execution

## Type Annotations

Type annotations are added to function parameters, return values, and variables to specify their expected types. For example:

```python
def calculate_distance(point1: Tuple[float, float, float],
                       point2: Tuple[float, float, float]) -> float:
    """Calculate the Euclidean distance between two 3D points."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
```

This function signature indicates that:

- `point1` and `point2` should be tuples of three floats
- The function returns a float

## Custom Type Definitions

The project defines custom types for domain-specific concepts in the `krysztalki/core/crystal_types.py` module. These types make the code more readable and provide better type checking. For example:

```python
# Basic type aliases for crystallographic data
Coordinate = Tuple[float, float, float]
FractionalCoordinate = Tuple[float, float, float]
CartesianCoordinate = Tuple[float, float, float]
HKL = Tuple[int, int, int]  # Miller indices
LatticeParameters = Tuple[float, float, float, float, float, float]  # a, b, c, alpha, beta, gamma

# Type aliases for symmetry operations
SymmetryType = str  # e.g., "2", "m", "3", "4", etc.
Direction = str  # e.g., "100", "111", etc.
SymmetryOperation = Tuple[SymmetryType, Direction]
SymmetryMatrix = NDArray[np.float64]  # 3x3 transformation matrix
```

Using these custom types, the previous example could be rewritten as:

```python
def calculate_distance(point1: CartesianCoordinate,
                       point2: CartesianCoordinate) -> float:
    """Calculate the Euclidean distance between two 3D points."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
```

## NumPy Array Types

The project uses `numpy.typing.NDArray` to specify the type and shape of NumPy arrays. For example:

```python
from numpy.typing import NDArray
import numpy as np

def calculate_centroid(points: NDArray[np.float64]) -> NDArray[np.float64]:
    """Calculate the centroid of a set of points."""
    return np.mean(points, axis=0)
```

For more specific array shapes, the project defines custom type aliases:

```python
# Array type aliases with shape specifications
Point3D = NDArray[np.float64]  # Shape (3,)
Matrix3D = NDArray[np.float64]  # Shape (3, 3)
PointArray = NDArray[np.float64]  # Shape (n, 3)
PointArrayTransposed = NDArray[np.float64]  # Shape (3, n)
```

## Utility Types

The project uses utility types from the `typing` module to express more complex type relationships:

- `Optional[T]`: Indicates that a value can be of type `T` or `None`
- `Union[T1, T2, ...]`: Indicates that a value can be of any of the specified types
- `List[T]`, `Dict[K, V]`, `Tuple[T1, T2, ...]`: Specify the types of elements in containers
- `Callable[[Arg1Type, Arg2Type, ...], ReturnType]`: Specifies the signature of a function

For example:

```python
from typing import Optional, Union, List, Dict, Tuple, Callable

def process_data(data: Optional[Dict[str, Union[int, float]]]) -> List[float]:
    """Process data if available, otherwise return an empty list."""
    if data is None:
        return []
    return [float(value) for value in data.values()]

def apply_function(func: Callable[[float], float], values: List[float]) -> List[float]:
    """Apply a function to each value in a list."""
    return [func(value) for value in values]
```

## Type Checking

The project supports both static and runtime type checking:

### Static Type Checking

Static type checking is performed by tools like mypy, which analyze the code without running it. To run mypy on the project:

```bash
mypy --config-file=pyproject.toml krysztalki
```

The project's `pyproject.toml` file contains configuration for mypy:

```toml
[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
disallow_incomplete_defs = false
check_untyped_defs = true
disallow_untyped_decorators = false
no_implicit_optional = true
strict_optional = true

# Configure mypy to use our stub files
mypy_path = "stubs"
```

### Runtime Type Checking

Runtime type checking is performed by the `typeguard` library, which validates function parameters and return values during execution. To enable runtime type checking:

```bash
KRYSZTALKI_ENABLE_TYPE_CHECKING=1 python your_script.py
```

The project provides utilities for runtime type checking in the `krysztalki/utils/type_checking.py` module:

```python
from krysztalki.utils.type_checking import check_types

@check_types
def add(a: int, b: int) -> int:
    return a + b
```

See the [Runtime Type Checking Guide](type_checking.md) for more details.

## Best Practices

When working with the type system in the Crystal Symmetry project, follow these best practices:

1. **Use custom types** from `krysztalki.core.crystal_types` for domain-specific concepts
2. **Be specific about array shapes** when working with NumPy arrays
3. **Add docstrings** to explain the purpose and constraints of functions and types
4. **Use runtime type checking** during development and testing
5. **Run mypy** regularly to catch type errors early

## Common Pitfalls

### Circular Imports

Avoid circular imports when using type annotations by using string literals for forward references:

```python
# Instead of this (which might cause circular imports)
from other_module import OtherClass

def process(obj: OtherClass) -> None:
    ...

# Do this
def process(obj: 'OtherClass') -> None:
    ...
```

### Any Type

Avoid using `Any` unless absolutely necessary, as it bypasses type checking:

```python
# Avoid this
def process_data(data: Any) -> Any:
    return data

# Prefer this
def process_data(data: Dict[str, Union[int, float]]) -> List[float]:
    return [float(value) for value in data.values()]
```

### Type Ignores

Use `# type: ignore` comments sparingly and only when necessary:

```python
# Only use type: ignore when you're sure it's necessary
result = some_function()  # type: ignore  # Function has no type annotations
```

## Advanced Type Hints Usage

### Type Variables and Generic Functions

Type variables allow you to create generic functions that preserve type information. For example:

```python
from typing import TypeVar, List

T = TypeVar('T')  # Define a type variable

def first_element(items: List[T]) -> T:
    """Return the first element of a list with the same type as the list elements."""
    if not items:
        raise ValueError("Empty list")
    return items[0]

# Usage
int_result = first_element([1, 2, 3])  # Type: int
str_result = first_element(['a', 'b', 'c'])  # Type: str
```

The Crystal Symmetry project uses type variables in several places, such as in the `type_checking.py` module:

```python
F = TypeVar('F', bound=Callable[..., Any])  # For function types
T = TypeVar('T')  # For generic values

def check_type(value: T, expected_type: Any) -> T:
    """Check that a value matches an expected type."""
    # Implementation...
```

### Protocol Classes

Protocol classes define interfaces without requiring inheritance. They're useful for structural typing (duck typing with type checking):

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Transformable(Protocol):
    """Protocol for objects that can be transformed by a matrix."""
    def transform(self, matrix: np.ndarray) -> 'Transformable':
        """Apply transformation matrix to the object."""
        ...

def apply_transformation(obj: Transformable, matrix: np.ndarray) -> Transformable:
    """Apply a transformation to any object that implements the transform method."""
    return obj.transform(matrix)
```

The Crystal Symmetry project uses protocols in `crystal_types.py` to define interfaces for transformable objects.

### Type Guards

Type guards are functions that help narrow down types in conditional branches:

```python
from typing import TypeGuard, List, Union

def is_list_of_ints(obj: List[object]) -> TypeGuard[List[int]]:
    """Check if a list contains only integers."""
    return all(isinstance(x, int) for x in obj)

def process_items(items: Union[List[int], List[str]]) -> None:
    if is_list_of_ints(items):
        # Here, items is known to be List[int]
        total = sum(items)
        print(f"Sum: {total}")
    else:
        # Here, items is known to be List[str]
        joined = ", ".join(items)
        print(f"Joined: {joined}")
```

## Compatibility with Third-Party Libraries

### Using Stub Files for External Libraries

The Crystal Symmetry project uses stub files to provide type information for external libraries that don't have built-in type hints. For example, the project includes stubs for the `crystals` package:

```python
# stubs/crystals/__init__.pyi
class Crystal:
    """Type stub for the Crystal class from the crystals package."""

    name: str
    atoms: List['Atom']

    @classmethod
    def from_cif(cls, filename: str) -> 'Crystal': ...

    @property
    def lattice_vectors(self) -> NDArray[np.float64]: ...
```

To create your own stub files for other libraries:

1. Create a `.pyi` file with the same name as the module
2. Define the public API with type annotations
3. Use ellipses (`...`) for method bodies
4. Add the stub file to the `stubs` directory

### Type Hints for NumPy and Scientific Libraries

The project uses `numpy.typing` for NumPy arrays. For other scientific libraries, you can use similar approaches:

```python
# For pandas
from pandas import DataFrame, Series

def process_dataframe(df: DataFrame) -> Series:
    return df.mean()

# For matplotlib
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def create_plot() -> Tuple[Figure, Axes]:
    fig, ax = plt.subplots()
    return fig, ax
```

## Practical Examples

### Example 1: Crystallographic Calculations

```python
from typing import Tuple, List, Optional
import numpy as np
from numpy.typing import NDArray

from krysztalki.core.crystal_types import (
    LatticeParameters, FractionalCoordinate, CartesianCoordinate, SymmetryMatrix
)

def fractional_to_cartesian(
    coord: FractionalCoordinate,
    lattice_params: LatticeParameters
) -> CartesianCoordinate:
    """Convert fractional coordinates to Cartesian coordinates.

    Args:
        coord: Fractional coordinates (a, b, c)
        lattice_params: Lattice parameters (a, b, c, alpha, beta, gamma)

    Returns:
        Cartesian coordinates (x, y, z)
    """
    a, b, c, alpha, beta, gamma = lattice_params

    # Convert angles to radians
    alpha_rad = np.radians(alpha)
    beta_rad = np.radians(beta)
    gamma_rad = np.radians(gamma)

    # Calculate transformation matrix
    v1 = a * np.array([1, 0, 0])
    v2 = b * np.array([np.cos(gamma_rad), np.sin(gamma_rad), 0])
    v3_x = c * np.cos(beta_rad)
    v3_y = c * (np.cos(alpha_rad) - np.cos(beta_rad) * np.cos(gamma_rad)) / np.sin(gamma_rad)
    v3_z = c * np.sqrt(1 - np.cos(beta_rad)**2 - (v3_y / c)**2)
    v3 = np.array([v3_x, v3_y, v3_z])

    # Apply transformation
    x, y, z = coord
    cart_x = x * v1[0] + y * v2[0] + z * v3[0]
    cart_y = x * v1[1] + y * v2[1] + z * v3[1]
    cart_z = x * v1[2] + y * v2[2] + z * v3[2]

    return (cart_x, cart_y, cart_z)

def find_symmetry_equivalent_points(
    point: CartesianCoordinate,
    symmetry_ops: List[SymmetryMatrix],
    tolerance: float = 1e-5
) -> List[CartesianCoordinate]:
    """Find all symmetry-equivalent points for a given point.

    Args:
        point: Cartesian coordinates of the point
        symmetry_ops: List of symmetry operation matrices
        tolerance: Tolerance for considering points as equivalent

    Returns:
        List of symmetry-equivalent points
    """
    result: List[CartesianCoordinate] = []
    point_array = np.array(point)

    for op in symmetry_ops:
        # Apply symmetry operation
        transformed = op @ point_array
        transformed_tuple = (float(transformed[0]),
                            float(transformed[1]),
                            float(transformed[2]))

        # Check if this point is already in the result (within tolerance)
        is_duplicate = any(
            np.linalg.norm(np.array(p) - np.array(transformed_tuple)) < tolerance
            for p in result
        )

        if not is_duplicate:
            result.append(transformed_tuple)

    return result
```

### Example 2: Type-Safe Configuration Handling

```python
from typing import Dict, Any, Optional, cast, TypedDict, Literal

# Define configuration structure using TypedDict
class CrystalConfig(TypedDict):
    name: str
    size: int
    lattice_type: Literal['cubic', 'hexagonal', 'tetragonal', 'orthorhombic',
                          'monoclinic', 'triclinic']
    parameters: Dict[str, float]
    options: Dict[str, Any]

def load_config(config_file: str) -> CrystalConfig:
    """Load configuration from a JSON file."""
    import json
    with open(config_file, 'r') as f:
        data = json.load(f)

    # Validate required fields
    if not isinstance(data, dict):
        raise TypeError("Config must be a dictionary")

    required_fields = ['name', 'size', 'lattice_type', 'parameters']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    # Ensure options field exists
    if 'options' not in data:
        data['options'] = {}

    return cast(CrystalConfig, data)

def get_parameter(
    config: CrystalConfig,
    name: str,
    default: Optional[float] = None
) -> float:
    """Get a parameter from the configuration."""
    if name in config['parameters']:
        return config['parameters'][name]

    if default is not None:
        return default

    raise ValueError(f"Parameter '{name}' not found in configuration")
```

## Migrating Existing Code to Use Type Hints

Adding type hints to existing code can be a gradual process. This section provides guidance on how to approach this task effectively.

### Incremental Approach

You don't need to add type hints to all code at once. Start with the most critical or frequently used modules:

1. **Begin with public APIs**: Focus on functions and classes that are part of the public API
2. **Add type hints to new code**: Ensure all new code includes type hints
3. **Gradually add hints to existing code**: Work module by module

### Using Type Comments for Python 3.5 Compatibility

If you need to maintain compatibility with Python 3.5, you can use type comments instead of annotations:

```python
# Python 3.6+ style
def calculate_distance(point1: Tuple[float, float, float],
                       point2: Tuple[float, float, float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

# Python 3.5 compatible style
def calculate_distance(point1, point2):  # type: (Tuple[float, float, float], Tuple[float, float, float]) -> float
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
```

### Using `# type: ignore` Comments

When migrating code, you may encounter situations where type checking fails but you can't immediately fix the issue. Use `# type: ignore` comments to suppress these errors temporarily:

```python
# Suppress a specific error
result = some_function()  # type: ignore[attr-defined]  # Function has no return_value attribute

# Suppress all errors on a line
result = complex_expression()  # type: ignore
```

Always add a comment explaining why the type check is being ignored and create a task to fix it properly later.

### Using `Any` as a Placeholder

When you're not sure about the correct type, you can use `Any` as a placeholder:

```python
from typing import Any

def process_data(data: Any) -> None:
    # Process the data...
    pass
```

However, try to replace `Any` with more specific types as you gain a better understanding of the code.

### Dealing with Complex Types

Some existing code may use complex data structures that are difficult to type. You can create custom type aliases to make this easier:

```python
# Before
def process_crystal_data(data):
    # Process a complex nested dictionary of crystal data
    pass

# After
from typing import Dict, List, Union, TypedDict

class AtomData(TypedDict):
    element: str
    coordinates: List[float]
    charge: float

class CrystalData(TypedDict):
    name: str
    atoms: List[AtomData]
    properties: Dict[str, Union[int, float, str]]

def process_crystal_data(data: CrystalData) -> None:
    # Process a complex nested dictionary of crystal data
    pass
```

### Using Tools to Help Migration

Several tools can help you add type hints to existing code:

1. **MonkeyType**: Generates type annotations by observing runtime types
2. **pytype**: Infers types for unannotated code
3. **mypy --suggest-type-annotations**: Suggests type annotations based on usage

Example of using MonkeyType:

```bash
# Install MonkeyType
pip install monkeytype

# Run your tests with MonkeyType tracing
monkeytype run your_test_script.py

# Apply the type annotations
monkeytype apply your_module.your_function
```

### Testing After Adding Type Hints

After adding type hints to existing code:

1. Run the test suite to ensure functionality hasn't changed
2. Run mypy to check for type errors
3. Verify that the code still works as expected in all use cases

## Further Reading

- [Python Type Hints Documentation](https://docs.python.org/3/library/typing.html)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [typeguard Documentation](https://typeguard.readthedocs.io/)
- [NumPy Typing Documentation](https://numpy.org/doc/stable/reference/typing.html)
- [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
- [PEP 585 – Type Hinting Generics In Standard Collections](https://peps.python.org/pep-0585/)
- [PEP 593 – Flexible function and variable annotations](https://peps.python.org/pep-0593/)
- [MonkeyType](https://github.com/Instagram/MonkeyType) - A system for Python that generates static type annotations by collecting runtime types
- [pytype](https://github.com/google/pytype) - A static type analyzer for Python code
