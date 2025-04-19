# Subtask 4.1: Analyze codebase and create type annotation plan

**Status:** done

**Dependencies:** None

**Description:** Create a comprehensive plan for adding type annotations throughout the codebase.

## Details

# Type Annotation Implementation Plan

## Analysis Phase
- Scan codebase using tools like `mypy --find-occurrences` to identify frequently used functions/classes
- Map data flow between components to understand type propagation
- Identify crystallographic-specific data structures (unit cells, symmetry operations, atomic coordinates)
- Document common function signatures and return types

## Type Hint Strategy
- For crystallographic data: Use `numpy.ndarray` with shape specifications (e.g., `ndarray[Shape["3, 3"], Float]`)
- For symmetry operations: Create custom type aliases (e.g., `SymmetryOperation = Tuple[ndarray, ndarray]`)
- For atomic structures: Consider dataclasses with typed fields
- Use `TypeVar` for generic crystallographic operations

## Implementation Approach
1. Start with core utility functions that handle basic crystallographic math
2. Create type stubs for numpy-heavy modules first
3. Implement `Protocol` classes for duck-typed interfaces
4. Use `@overload` for functions with multiple valid signatures
5. Add `Optional[]` and `Union[]` types where functions accept variable inputs

## Documentation Integration
- Add typing examples in module-level docstrings
- Create a typing guide document for contributors
- Include type checking in CI pipeline with mypy
- Document any `# type: ignore` comments with explanations

## Stub File Creation
- Generate initial stubs with stubgen
- Manually enhance stubs for scientific/mathematical functions
- Include detailed type information for public API functions

## Systematic Codebase Scanning
- Use `find . -name "*.py" | xargs wc -l | sort -nr` to identify all Python files by size
- Create a dependency graph with `pydeps` to visualize module relationships
- Employ `radon cc` to measure cyclomatic complexity of modules for prioritization
- Use `vulture` to identify dead code that can be excluded from typing efforts

## Prioritization Framework
- **Tier 1**: Core crystallographic calculation modules with high import frequency
- **Tier 2**: Public API and interface modules used by external consumers
- **Tier 3**: Internal utilities and helpers
- **Tier 4**: Test modules and examples
- Score modules by: usage frequency × complexity × external dependency count

## Type Complexity Categorization
1. **Simple**: Basic Python types, minimal generics (1-2 hours per file)
2. **Moderate**: Container types, simple generics, NumPy arrays (2-4 hours per file)
3. **Complex**: Higher-order functions, callbacks, complex generics (4-8 hours per file)
4. **Very Complex**: Dynamic code, metaprogramming, runtime type creation (8+ hours per file)

## API Inconsistency Documentation
- Create a structured YAML template for documenting inconsistencies:
  ```yaml
  module: path.to.module
  function: function_name
  inconsistency_type: return_type_varies | parameter_type_varies | etc
  description: "Detailed explanation"
  affected_modules: [list of modules impacted]
  proposed_solution: "Suggested approach"
  ```
- Maintain a central registry of inconsistencies in `typing_issues.yaml`
- Link inconsistencies to GitHub issues for tracking resolution

## Custom Type Definition Strategy
- Create a `types.py` module in each package for package-specific types
- Implement a central `crystallography_types.py` for cross-cutting type definitions
- For each identified data structure:
  1. Document its shape, constraints, and valid values
  2. Create appropriate type aliases, TypedDict, or Protocol classes
  3. Add validation functions with runtime type checking when appropriate

## External Dependency Inventory
- Use `pipdeptree` to generate complete dependency tree
- For each dependency:
  1. Check for existing type stubs in typeshed or the package itself
  2. Record typing status (fully typed, partially typed, untyped)
  3. Prioritize stub creation for untyped scientific libraries
- Create custom stub files for critical dependencies in a `stubs/` directory

## Typing Coverage Metrics
- Implement a custom mypy plugin to generate coverage reports
- Track metrics:
  - Percentage of functions with complete type annotations
  - Percentage of variables with explicit types
  - Number of `Any` types used (goal: minimize)
  - Number of `# type: ignore` comments (goal: minimize with justification)
- Generate weekly coverage trend reports during implementation

## Dynamic Typing Analysis
- Use static analysis tools like `monkeytype` to trace runtime types
- Identify patterns of:
  - Duck typing that should use Protocol classes
  - Runtime type checking with `isinstance()` that needs Union types
  - Dynamic attribute access that requires careful typing with `__getattr__`
  - Metaprogramming that may require `cast()` or `TypeGuard`
- Document each dynamic typing pattern with example solutions


## Navigation
- [Back to Task Overview](overview.md)
- [Next Subtask](subtask_002.md)

