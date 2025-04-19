# SQLite Database Module for Crystal Symmetry Project

This module provides SQLite database connectivity and models for storing and retrieving crystal structure data and analysis results.

## Overview

The database module consists of the following components:

1. **DatabaseConnection**: A class for managing SQLite database connections and executing queries
2. **Models**: Classes for interacting with database tables (CrystalStructure, SymmetryAnalysis, VacancyConfiguration)
3. **Utilities**: Helper functions for common database operations

## Database Schema

The database schema includes the following tables:

- **crystal_structures**: Stores basic information about crystal structures
- **atoms**: Stores atom positions and properties for each crystal structure
- **symmetry_analyses**: Stores symmetry analysis results
- **vacancy_configurations**: Stores vacancy configuration data

## Usage

### Command Line Interface

The database functionality is accessible through the CLI:

```bash
# Initialize the database
krysztalki db init

# Import a crystal structure
krysztalki db import 1000041 --name "Sodium Chloride"

# List all crystal structures
krysztalki db list

# Show details of a crystal structure
krysztalki db show 1

# Delete a crystal structure
krysztalki db delete 1
```

### Python API

You can also use the database module directly in your Python code:

```python
from krysztalki.db.utils import init_database, store_crystal
from krysztalki.io.cif import read_cif

# Initialize the database
db_conn = init_database()

# Import a crystal structure
crystal = read_cif(1000041)
crystal_id = store_crystal(
    crystal,
    name="Sodium Chloride",
    source="COD",
    cod_id=1000041,
    db_conn=db_conn
)

# Close the connection when done
db_conn.close()
```

## Default Database Location

By default, the database is stored at `~/.krysztalki/crystal_symmetry.db`. You can specify a different location using the `--db-path` option in the CLI or by providing a path to the `init_database()` function.

## Example

See the `examples/db_example.py` script for a complete example of how to use the database module.
