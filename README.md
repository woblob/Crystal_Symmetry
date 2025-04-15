# Crystal Symmetry Analysis Package

A Python package for analyzing and working with crystal symmetry operations.

## Features

- Crystal Information File (CIF) parsing
- Symmetry operations analysis
- Crystal structure visualization
- Space group determination

## Package Structure

The package is now organized in a proper Python package structure:

```
krysztalki/
├── __init__.py           # Main package init with public API
├── core/                 # Core algorithms and functionality
│   ├── __init__.py
│   └── symmetry.py       # Symmetry analysis implementation
├── io/                   # Input/output functionality
│   ├── __init__.py
│   └── cif.py            # CIF file parsing functions
├── utils/                # Utility functions and helpers
│   ├── __init__.py
│   └── task_manager.py   # Task management utilities
└── cli/                  # Command-line interface
    ├── __init__.py
    └── main.py           # CLI implementation
```

## Installation

You can install the package directly from the repository:

```bash
# Install in development mode
pip install -e .

# Or install normally
pip install .
```

## Usage

```python
from krysztalki import read_cif, analyze_symmetry

# Load a crystal structure from a CIF file or COD database
crystal = read_cif("path/to/file.cif")  # From file
# or
crystal = read_cif(1000041)  # From COD database (NaCl)

# Analyze symmetry with one vacancy
result = analyze_symmetry(crystal, vacancy_count=1)

# Access the results
print(f"Found {len(result['symmetry_operations'])} symmetry operations")
print(f"Analyzed {len(result['vacancy_configs'])} vacancy configurations")
```

## Development

1. Create a virtual environment and install dependencies:
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

2. Install pre-commit hooks:
```bash
pre-commit install
```

3. Run tests:
```bash
pytest tests/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
