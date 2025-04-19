# Crystal Symmetry Analysis

A Python package for analyzing crystal structures, calculating symmetry operations, and studying vacancy configurations.

## Features

- Load crystal structures from CIF files or the Crystallography Open Database (COD)
- Analyze crystal symmetry operations
- Calculate and visualize vacancy configurations
- Store and retrieve crystal data using SQLite database
- Command-line interface for common operations

## Package Structure

The package is organized in a proper Python package structure:

```
krysztalki/
├── __init__.py           # Main package init with public API
├── core/                 # Core algorithms and functionality
│   ├── __init__.py
│   └── symmetry.py       # Symmetry analysis implementation
├── io/                   # Input/output functionality
│   ├── __init__.py
│   └── cif.py            # CIF file parsing functions
├── db/                   # Database functionality
│   ├── __init__.py
│   ├── connection.py     # Database connection class
│   ├── models.py         # Database models and schema
│   └── utils.py          # Database utility functions
├── utils/                # Utility functions and helpers
│   ├── __init__.py
│   └── task_manager.py   # Task management utilities
└── cli/                  # Command-line interface
    ├── __init__.py
    ├── main.py           # Main CLI implementation
    └── db_commands.py    # Database CLI commands
```

## Installation

```bash
pip install krysztalki
```

Or install directly from the repository:

```bash
# Install in development mode
pip install -e .

# Or install normally
pip install .
```

## Basic Usage

### Python API

```python
from krysztalki import read_cif, analyze_symmetry

# Load a crystal structure from a CIF file or COD ID
crystal = read_cif("path/to/file.cif")  # From file
# or
crystal = read_cif(1000041)  # From COD database (NaCl)

# Analyze symmetry
result = analyze_symmetry(crystal, vacancy_count=1)

# Access the results
print(f"Found {len(result['symmetry_operations'])} symmetry operations")
print(f"Analyzed {len(result['vacancy_configs'])} vacancy configurations")
```

### Command Line Interface

```bash
# Analyze a crystal structure
krysztalki analyze 1000041 --supercell 2 --vacancies 1

# Display information about a crystal structure
krysztalki info 1000041 --verbose
```

## Database Support

The package includes SQLite database support for storing and retrieving crystal structures and analysis results:

```bash
# Initialize the database
krysztalki db init

# Import a crystal structure
krysztalki db import 1000041 --name "Sodium Chloride"

# List all crystal structures
krysztalki db list

# Show details of a crystal structure
krysztalki db show 1
```

For more details on using the database, see the [Database Module README](krysztalki/db/README.md).

## Examples

Example scripts are provided in the `examples` directory:

- `examples/db_example.py`: Demonstrates how to use the SQLite database

## Development

### Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/crystal-symmetry.git
cd crystal-symmetry

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
pytest tests/
```

## License

[MIT License](LICENSE)

## Acknowledgments

- [Crystals](https://github.com/LaurentRDC/crystals) - Python library for crystallography
- [Crystallography Open Database](http://www.crystallography.net/cod/) - Open-access collection of crystal structures
