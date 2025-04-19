# Subtask 4.4: Create stub files for external dependencies

**Status:** pending

**Dependencies:** 4.1

**Description:** Generate and enhance stub files for external dependencies used in the project.

## Details

# Implementation Details for Creating Stub Files

## Dependency Identification
- Scan project imports using tools like `pipreqs` or `importlib.metadata` to identify external dependencies
- Prioritize dependencies used in core crystallography calculations and data processing
- Create a dependency classification system (critical/secondary/optional) to prioritize stub creation

## Stub Generation Process
- Use mypy's stubgen: `stubgen -p package_name -o stubs/`
- Create a script to batch process all identified dependencies
- Example command: `python -m mypy.stubgen numpy scipy matplotlib -o ./stubs`

## Enhancing Auto-Generated Stubs
- Add proper return types for functions where stubgen uses `Any`
- Document array shapes for numpy functions (e.g., `def func() -> np.ndarray[Shape["n,m"], np.float64]: ...`)
- Use `typing.Protocol` for duck-typed interfaces
- Add `@overload` decorations for functions with multiple signatures

## Scientific Library Handling
- For numpy: focus on ndarray, linalg, and fft modules with crystallography-relevant functions
- For scipy: prioritize spatial, optimize, and signal modules
- Use numpy-stubs project as reference: https://github.com/numpy/numpy-stubs

## Crystallography-Specific Packages
- Create custom stubs for packages like CrystFEL, DIALS, or CCP4
- Document expected data structures for diffraction patterns
- Define proper types for Miller indices, space groups, and unit cell parameters

## Version Compatibility
- Include version conditionals: `if sys.version_info >= (3, 8): ...`
- Add package version checks: `if NUMPY_VERSION >= (1, 20): ...`
- Document minimum supported versions in stub file headers

## Validation Process
- Run mypy with strict mode on sample code using the stubs
- Create test cases that exercise different API aspects
- Implement CI check that verifies stub compatibility with actual packages

## IDE Integration
- Configure VSCode/PyCharm to recognize custom stub directory
- Add mypy.ini configuration to include stub paths
- Document stub usage in project README for new developers


## Navigation
- [Back to Task Overview](overview.md)
- [Previous Subtask](subtask_003.md)
- [Next Subtask](subtask_005.md)

