"""
Example script demonstrating how to use the SQLite database in the Crystal Symmetry project.

This script shows how to:
1. Initialize the database
2. Store crystal structures
3. Retrieve and analyze crystal data
4. Work with symmetry analyses and vacancy configurations
"""

import os
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from krysztalki.db.connection import DatabaseConnection
from krysztalki.db.models import create_tables
from krysztalki.db.utils import (
    init_database,
    store_crystal,
    get_crystal_by_cod_id,
    get_crystal_with_analyses,
    list_all_crystals
)
from krysztalki.io.cif import read_cif
from krysztalki.core.symmetry import analyze_symmetry


def main():
    """Run the database example."""
    # Create a temporary database file
    db_path = Path("example_database.db")
    
    # Initialize the database
    print(f"Initializing database at {db_path}...")
    db_conn = init_database(db_path)
    
    try:
        # Import a crystal structure from COD
        cod_id = 1000041  # NaCl
        print(f"Importing crystal structure from COD ID: {cod_id}...")
        crystal = read_cif(cod_id)
        
        # Store the crystal in the database
        crystal_id = store_crystal(
            crystal,
            name="Sodium Chloride",
            source="COD",
            cod_id=cod_id,
            db_conn=db_conn
        )
        print(f"Crystal structure stored with ID: {crystal_id}")
        
        # Perform symmetry analysis
        print("Analyzing crystal symmetry...")
        result = analyze_symmetry(crystal, vacancy_count=1)
        
        # Store the analysis results
        from krysztalki.db.models import SymmetryAnalysis, VacancyConfiguration
        
        # Store symmetry analysis
        analysis_id = SymmetryAnalysis.create(
            db_conn,
            crystal_id=crystal_id,
            supercell_size=1,
            symmetry_operations=result["symmetry_operations"],
            point_group="Fm-3m"
        )
        print(f"Symmetry analysis stored with ID: {analysis_id}")
        
        # Store vacancy configurations
        for i, config in enumerate(result["vacancy_configs"]):
            config_id = VacancyConfiguration.create(
                db_conn,
                crystal_id=crystal_id,
                analysis_id=analysis_id,
                num_vacancies=1,
                vacancy_positions=config["positions"],
                is_stable=True
            )
            print(f"Vacancy configuration {i+1} stored with ID: {config_id}")
        
        # Retrieve and display crystal data
        print("\nRetrieving crystal data...")
        crystal_data = get_crystal_with_analyses(crystal_id, db_conn)
        
        print(f"Crystal: {crystal_data['name']}")
        print(f"Formula: {crystal_data['formula']}")
        print(f"Space Group: {crystal_data['space_group']}")
        print(f"Number of atoms: {len(crystal_data['atoms'])}")
        print(f"Number of analyses: {len(crystal_data['analyses'])}")
        
        for analysis in crystal_data['analyses']:
            print(f"\nAnalysis ID: {analysis['id']}")
            print(f"Supercell size: {analysis['supercell_size']}")
            print(f"Point group: {analysis['point_group']}")
            print(f"Number of vacancy configurations: {len(analysis['vacancy_configurations'])}")
        
        # List all crystals
        print("\nListing all crystal structures:")
        crystals = list_all_crystals(db_conn)
        for crystal in crystals:
            print(f"- {crystal['name']} (ID: {crystal['id']})")
    
    finally:
        # Close the database connection
        db_conn.close()
        
        # Clean up the example database file
        if db_path.exists():
            os.remove(db_path)
            print(f"\nRemoved example database file: {db_path}")


if __name__ == "__main__":
    main()
