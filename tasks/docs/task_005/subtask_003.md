# Subtask 5.3: Implement automated code formatting

**Status:** pending

**Dependencies:** 5.1, 5.2

**Description:** Set up and execute automatic code formatting tools to standardize code style.

## Details

# Automated Code Formatting Implementation

## Formatter Selection
- Recommend **Black** as primary formatter due to its deterministic output and popularity in scientific Python projects
- Add **isort** for import sorting, configured to be compatible with Black
- Consider **docformatter** for standardizing docstring formats

## Configuration
- Create `pyproject.toml` with Black configuration:
  ```toml
  [tool.black]
  line-length = 88
  target-version = ['py38']
  include = '\.pyx?$'
  exclude = '''
  /(
      \.eggs
    | \.git
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
- Configure isort to be compatible with Black:
  ```toml
  [tool.isort]
  profile = "black"
  line_length = 88
  ```

## Workflow Integration
- Implement pre-commit hooks using `.pre-commit-config.yaml`:
  ```yaml
  repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
    - id: black
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
    - id: isort
  ```
- Create `format.sh` script to run formatters on the entire codebase:
  ```bash
  #!/bin/bash
  python -m black .
  python -m isort .
  ```

## IDE Integration
- VSCode: Add settings.json configuration:
  ```json
  {
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.formatting.blackPath": "${workspaceFolder}/.venv/bin/black",
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    },
    "python.sortImports.path": "${workspaceFolder}/.venv/bin/isort"
  }
  ```
- PyCharm: Document installation of Black and isort plugins

## CI Implementation
- Add GitHub Actions workflow for format checking:
  ```yaml
  name: Code Formatting
  on: [push, pull_request]
  jobs:
    format:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Set up Python
          uses: actions/setup-python@v4
          with:
            python-version: '3.8'
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install black isort
        - name: Check formatting
          run: |
            black --check .
            isort --check .
  ```

## Batch Processing
- Run initial formatting across all files:
  ```bash
  black crystal_symmetry/ tests/
  isort crystal_symmetry/ tests/ 
  docformatter --in-place --recursive crystal_symmetry/ tests/
  ```
- Document before/after metrics of formatting changes


## Navigation
- [Back to Task Overview](overview.md)
- [Previous Subtask](subtask_002.md)
- [Next Subtask](subtask_004.md)

