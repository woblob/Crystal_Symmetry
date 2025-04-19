# Subtask 4.3: Add type hints to class attributes and methods

**Status:** done

**Dependencies:** 4.1

**Description:** Apply type hints to all class attributes and methods throughout the codebase.

## Details

# Implementation Details for Class Type Hints

## Crystallographic Data Structures
- Define `UnitCell` type as a dataclass with lattice parameters (a, b, c, alpha, beta, gamma)
- Create `SymmetryOperation` type alias for transformation matrices: `SymmetryOperation = tuple[np.ndarray, np.ndarray]`  
- Use `AtomicPosition = tuple[str, np.ndarray, float, float]` for element, coordinates, occupancy, and displacement
- Implement `SpaceGroup` class with proper typing for symmetry operations

## Custom Type Aliases
- `HKL = tuple[int, int, int]` for Miller indices
- `LatticeParameters = tuple[float, float, float, float, float, float]`
- `AtomicStructure = dict[str, list[AtomicPosition]]`
- `DiffractionPattern = dict[HKL, float]`

## Generic Types
- `DataSeries[T] = list[tuple[float, T]]` for various data series
- `StructureCollection[T_Structure] = dict[str, T_Structure]`
- `ResultMap[T_Input, T_Output] = dict[T_Input, T_Output]`

## Protocol Classes
- Define `Transformable` protocol with `transform(matrix: np.ndarray) -> Self`
- Create `Serializable` protocol with `to_dict()` and `from_dict()` methods
- Implement `Measurable` protocol for objects that provide physical measurements

## Type Integration with Class Hierarchy
- Use `TypeVar` with bounds for crystallographic class hierarchies
- Implement proper return type annotations for inheritance chains
- Add `@overload` decorators for methods with multiple signatures

## Serialization Types
- Define `JSONDict = dict[str, Union[str, int, float, list, dict]]`
- Create type aliases for different serialization formats
- Implement `TypedDict` classes for strict dictionary structure typing

## Runtime Type Checking
- Add `isinstance()` checks at critical boundaries
- Implement custom validators using `@validate_argument` decorators
- Add optional runtime type enforcement with `typeguard` integration


## Navigation
- [Back to Task Overview](overview.md)
- [Previous Subtask](subtask_002.md)
- [Next Subtask](subtask_004.md)

