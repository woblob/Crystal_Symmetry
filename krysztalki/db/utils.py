"""
Database utility functions for Crystal Symmetry project.

This module provides utility functions for common database operations.
"""

import os
from pathlib import Path
from typing import Optional, Union, Dict, Any, List

from crystals import Crystal

from krysztalki.db.connection import DatabaseConnection
from krysztalki.db.models import (
    create_tables,
    CrystalStructure,
    SymmetryAnalysis,
    VacancyConfiguration,
)


def get_default_db_path() -> Path:
    """
    Get the default database path.

    Returns:
        Path to the default database file
    """
    # Use the user's home directory
    home_dir = Path.home()
    app_dir = home_dir / ".krysztalki"
    os.makedirs(app_dir, exist_ok=True)
    return app_dir / "crystal_symmetry.db"


def init_database(db_path: Optional[Union[str, Path]] = None) -> DatabaseConnection:
    """
    Initialize the database.

    Args:
        db_path: Path to the database file (optional)

    Returns:
        Database connection
    """
    if db_path is None:
        db_path = get_default_db_path()

    db_conn = DatabaseConnection(db_path).connect()
    create_tables(db_conn)
    return db_conn


def store_crystal(
    crystal: Crystal,
    name: str,
    source: str = "CIF",
    cod_id: Optional[int] = None,
    file_path: Optional[str] = None,
    db_conn: Optional[DatabaseConnection] = None,
) -> int:
    """
    Store a crystal structure in the database.

    Args:
        crystal: Crystal object
        name: Crystal name
        source: Source of the crystal data
        cod_id: Crystallography Open Database ID
        file_path: Path to the CIF file
        db_conn: Database connection (optional)

    Returns:
        ID of the created record
    """
    # Get lattice parameters
    a, b, c = crystal.lattice_vectors
    lattice_params = [
        float(a[0]),
        float(b[1]),
        float(c[2]),  # a, b, c
        90.0,
        90.0,
        90.0,  # alpha, beta, gamma (assuming orthogonal)
    ]

    # Get space group if available
    space_group = getattr(crystal, "spacegroup", None)

    # Get formula if available
    formula = None
    try:
        if hasattr(crystal, "chemical_formula") and len(crystal.atoms) > 0:
            formula = crystal.chemical_formula
    except (IndexError, AttributeError):
        # Handle case where chemical_formula property raises an exception
        pass

    # Create database connection if not provided
    close_conn = False
    if db_conn is None:
        db_conn = init_database()
        close_conn = True

    try:
        # Create crystal structure record
        crystal_id = CrystalStructure.create(
            db_conn,
            name=name,
            source=source,
            lattice_parameters=lattice_params,
            cod_id=cod_id,
            file_path=file_path,
            space_group=space_group,
            formula=formula,
        )

        # Store atoms
        for atom in crystal.atoms:
            db_conn.execute(
                """
                INSERT INTO atoms (crystal_id, element, atomic_number, x, y, z)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    crystal_id,
                    atom.element,
                    atom.atomic_number,
                    float(atom.coords_cartesian[0]),
                    float(atom.coords_cartesian[1]),
                    float(atom.coords_cartesian[2]),
                ),
            )

        db_conn.commit()
        return crystal_id
    finally:
        if close_conn:
            db_conn.close()


def store_symmetry_analysis(
    crystal_id: int,
    supercell_size: int,
    symmetry_operations: Dict[str, Any],
    point_group: Optional[str] = None,
    db_conn: Optional[DatabaseConnection] = None,
) -> int:
    """
    Store a symmetry analysis in the database.

    Args:
        crystal_id: Crystal structure ID
        supercell_size: Size of the supercell
        symmetry_operations: Symmetry operations
        point_group: Point group symbol
        db_conn: Database connection (optional)

    Returns:
        ID of the created record
    """
    # Create database connection if not provided
    close_conn = False
    if db_conn is None:
        db_conn = init_database()
        close_conn = True

    try:
        # Create symmetry analysis record
        analysis_id = SymmetryAnalysis.create(
            db_conn,
            crystal_id=crystal_id,
            supercell_size=supercell_size,
            symmetry_operations=symmetry_operations,
            point_group=point_group,
        )

        return analysis_id
    finally:
        if close_conn:
            db_conn.close()


def get_crystal_by_cod_id(
    cod_id: int, db_conn: Optional[DatabaseConnection] = None
) -> Optional[Dict[str, Any]]:
    """
    Get a crystal structure by COD ID.

    Args:
        cod_id: Crystallography Open Database ID
        db_conn: Database connection (optional)

    Returns:
        Crystal structure record as a dictionary, or None if not found
    """
    # Create database connection if not provided
    close_conn = False
    if db_conn is None:
        db_conn = init_database()
        close_conn = True

    try:
        # Get crystal structure
        crystal = CrystalStructure.get_by_cod_id(db_conn, cod_id)

        if crystal:
            # Get atoms
            db_conn.execute(
                "SELECT * FROM atoms WHERE crystal_id = ?", (crystal["id"],)
            )
            atoms = db_conn.fetchall()
            crystal["atoms"] = atoms

        return crystal
    finally:
        if close_conn:
            db_conn.close()


def get_crystal_with_analyses(
    crystal_id: int, db_conn: Optional[DatabaseConnection] = None
) -> Optional[Dict[str, Any]]:
    """
    Get a crystal structure with its symmetry analyses and vacancy configurations.

    Args:
        crystal_id: Crystal structure ID
        db_conn: Database connection (optional)

    Returns:
        Crystal structure record with analyses, or None if not found
    """
    # Create database connection if not provided
    close_conn = False
    if db_conn is None:
        db_conn = init_database()
        close_conn = True

    try:
        # Get crystal structure
        crystal = CrystalStructure.get_by_id(db_conn, crystal_id)

        if not crystal:
            return None

        # Get atoms
        db_conn.execute("SELECT * FROM atoms WHERE crystal_id = ?", (crystal_id,))
        atoms = db_conn.fetchall()
        crystal["atoms"] = atoms

        # Get symmetry analyses
        analyses = SymmetryAnalysis.get_by_crystal_id(db_conn, crystal_id)
        crystal["analyses"] = analyses

        # Get vacancy configurations for each analysis
        for analysis in analyses:
            configs = VacancyConfiguration.get_by_analysis_id(db_conn, analysis["id"])
            analysis["vacancy_configurations"] = configs

        return crystal
    finally:
        if close_conn:
            db_conn.close()


def list_all_crystals(
    db_conn: Optional[DatabaseConnection] = None,
) -> List[Dict[str, Any]]:
    """
    List all crystal structures in the database.

    Args:
        db_conn: Database connection (optional)

    Returns:
        List of crystal structure records
    """
    # Create database connection if not provided
    close_conn = False
    if db_conn is None:
        db_conn = init_database()
        close_conn = True

    try:
        # Get all crystal structures
        return CrystalStructure.get_all(db_conn)
    finally:
        if close_conn:
            db_conn.close()
