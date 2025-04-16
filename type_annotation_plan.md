# Type Annotation Plan for Crystal Symmetry Project

## 1. Overview

This document outlines the plan for adding type annotations to the Crystal Symmetry project. The goal is to improve code quality, documentation, and IDE support by adding proper type hints throughout the codebase and creating stub files for external dependencies.

## 2. Current State

The codebase already has some type annotations in place, particularly in:
- `krysztalki/core/symmetry.py`
- `krysztalki/io/cif.py`
- `krysztalki/utils/task_manager.py`

There are also some stub files in the `stubs` directory:
- `stubs/workDir/cifParsing.pyi`
- `stubs/crystals/__init__.pyi`
- `stubs/workDir/MMfunc.pyi`
- `stubs/workDir/Matrix/matrices_new.pyi`

However, these stubs are incomplete and need to be updated to match the current implementation.

## 3. Custom Types to Define

Based on the codebase analysis, we need to define the following custom types:

### 3.1 Core Types

```python
# For symmetry operations
SymOpDict = Dict[str, np.ndarray]
SymmetryBaseDict = Dict[str, Dict[str, np.ndarray]]

# For crystal data
CrystalPoint = Tuple[float, float, float]
CrystalCell = np.ndarray  # Shape (n, 3) for n points
SymmetryOperation = Tuple[str, str]  # (type, direction)
SymmetryList = List[SymmetryOperation]

# For task management
TaskDict = Dict[str, Any]
TaskList = List[Dict[str, Any]]
```

### 3.2 Function Signatures

Key functions that need proper type annotations:

```python
def generateSymetryBase() -> SymmetryBaseDict: ...
def findSym(matrixes: SymmetryBaseDict, allpoints: np.ndarray, vacancies: np.ndarray) -> List[Tuple[str, str]]: ...
def checkAllCells(scell: np.ndarray, base: str, sumVac: int) -> List[List[Tuple[str, str]]]: ...
def analyze_symmetry(crystal: Any, vacancy_count: int = 1) -> Dict[str, Any]: ...
def read_cif(file_path: Union[str, int]) -> Crystal: ...
def getSCell(func: Callable[[Union[str, int]], Crystal], filename: Union[str, int], size: int) -> Tuple[np.ndarray, str]: ...
```

## 4. Implementation Plan

### 4.1 Update Existing Type Annotations

1. Review and update existing type annotations in:
   - `krysztalki/core/symmetry.py`
   - `krysztalki/io/cif.py`
   - `krysztalki/utils/task_manager.py`

2. Ensure consistency in type annotations across related functions and classes.

### 4.2 Add Type Annotations to Core Modules

1. Add type annotations to:
   - `krysztalki/workDir/cifParsing.py`
   - `krysztalki/workDir/MMfunc.py`
   - `krysztalki/workDir/Matrix/matrices_new.py`

2. Focus on:
   - Function parameters and return types
   - Class attributes
   - Variable declarations

### 4.3 Update Stub Files

1. Update existing stub files:
   - `stubs/workDir/cifParsing.pyi`
   - `stubs/crystals/__init__.pyi`
   - `stubs/workDir/MMfunc.pyi`
   - `stubs/workDir/Matrix/matrices_new.pyi`

2. Create new stub files for external dependencies:
   - Complete the `crystals` package stubs

### 4.4 Configure Type Checking

1. Create a `mypy.ini` configuration file:

```ini
[mypy]
python_version = 3.8
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_decorators = True
no_implicit_optional = True
strict_optional = True

[mypy.plugins.numpy.*]
follow_imports = skip

[mypy.stubs.*]
ignore_errors = True
```

2. Add type checking to the development workflow.

## 5. Priority Order

1. Core data structures and custom types
2. Public API functions and classes
3. Internal implementation details
4. Stub files for external dependencies
5. Type checking configuration

## 6. Documentation

Add documentation for complex type annotations with explanatory comments:

```python
# Example
def transform_points(
    points: np.ndarray,  # Shape (n, 3) for n points in 3D space
    matrix: np.ndarray,  # Shape (4, 4) for homogeneous transformation matrix
) -> np.ndarray:  # Returns transformed points with same shape as input
    """
    Transform points using a 4x4 homogeneous transformation matrix.
    """
    ...
```

## 7. Testing

1. Run mypy on the codebase to validate type annotations
2. Fix any type errors that are identified
3. Add type checking to CI/CD pipeline

## 8. Timeline

1. Define custom types and update existing annotations (1 day)
2. Add annotations to core modules (2 days)
3. Update and create stub files (1 day)
4. Configure type checking and fix errors (1 day)
5. Documentation and testing (1 day)

Total estimated time: 6 days
