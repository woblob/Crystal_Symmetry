# Subtask 5.1: Set up linting configuration files

**Status:** pending

**Dependencies:** None

**Description:** Create and configure appropriate linting tools for the Python crystallography project.

## Details

# Linting Configuration Implementation

## Linter Selection
- Use `flake8` for general PEP8 compliance and error detection
- Implement `black` for automatic code formatting (non-negotiable style)
- Add `isort` for import sorting
- Include `mypy` for optional type checking
- Consider `pydocstyle` for docstring validation

## Configuration Files
- `.flake8` configuration:
  ```ini
  [flake8]
  max-line-length = 100
  exclude = .git,__pycache__,build,dist
  ignore = E203,W503  # Black compatibility
  per-file-ignores =
      __init__.py:F401,F403
  ```

- `pyproject.toml` for Black:
  ```toml
  [tool.black]
  line-length = 100
  target-version = ['py38']
  include = '\.pyi?$'
  exclude = '''
  /(
      \.git
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
  )/
  '''
  ```

- `pyproject.toml` for isort:
  ```toml
  [tool.isort]
  profile = "black"
  line_length = 100
  multi_line_output = 3
  include_trailing_comma = true
  ```

## Scientific Python Standards
- Follow NumPy/SciPy docstring conventions
- Allow longer variable names for scientific clarity
- Configure special handling for matrix/vector variable names

## Pre-commit Setup
- Create `.pre-commit-config.yaml`:
  ```yaml
  repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    - id: trailing-whitespace
    - id: end-of-file-fixer
    - id: check-yaml
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
    - id: isort
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
    - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
    - id: flake8
  ```

## CI Integration
- Add linting step to CI pipeline
- Configure GitHub Actions workflow for automated checks
- Set up VSCode integration for developer convenience


## Navigation
- [Back to Task Overview](overview.md)
- [Next Subtask](subtask_002.md)

