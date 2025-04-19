"""
Database models for Crystal Symmetry project.

This module defines the database schema and provides classes for
interacting with database tables.
"""

import json
from datetime import datetime
from typing import Dict, Any, List, Optional, Union, Tuple

import numpy as np

from krysztalki.db.connection import DatabaseConnection


def create_tables(db_conn: DatabaseConnection) -> None:
    """
    Create database tables if they don't exist.

    Args:
        db_conn: Database connection
    """
    # Create crystal_structures table
    db_conn.execute(
        """
    CREATE TABLE IF NOT EXISTS crystal_structures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        source TEXT NOT NULL,
        cod_id INTEGER,
        file_path TEXT,
        lattice_parameters TEXT NOT NULL,
        space_group TEXT,
        formula TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    )

    # Create atoms table
    db_conn.execute(
        """
    CREATE TABLE IF NOT EXISTS atoms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        crystal_id INTEGER NOT NULL,
        element TEXT NOT NULL,
        atomic_number INTEGER NOT NULL,
        x REAL NOT NULL,
        y REAL NOT NULL,
        z REAL NOT NULL,
        FOREIGN KEY (crystal_id) REFERENCES crystal_structures (id) ON DELETE CASCADE
    )
    """
    )

    # Create symmetry_analyses table
    db_conn.execute(
        """
    CREATE TABLE IF NOT EXISTS symmetry_analyses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        crystal_id INTEGER NOT NULL,
        supercell_size INTEGER NOT NULL,
        symmetry_operations TEXT NOT NULL,
        point_group TEXT,
        analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (crystal_id) REFERENCES crystal_structures (id) ON DELETE CASCADE
    )
    """
    )

    # Create vacancy_configurations table
    db_conn.execute(
        """
    CREATE TABLE IF NOT EXISTS vacancy_configurations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        crystal_id INTEGER NOT NULL,
        analysis_id INTEGER NOT NULL,
        num_vacancies INTEGER NOT NULL,
        vacancy_positions TEXT NOT NULL,
        energy REAL,
        is_stable BOOLEAN,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (crystal_id) REFERENCES crystal_structures (id) ON DELETE CASCADE,
        FOREIGN KEY (analysis_id) REFERENCES symmetry_analyses (id) ON DELETE CASCADE
    )
    """
    )

    # Commit the changes
    db_conn.commit()


class CrystalStructure:
    """
    Class for interacting with crystal_structures table.

    This class provides static methods for creating, retrieving, and deleting
    crystal structure records in the database.
    """

    @staticmethod
    def create(
        db_conn: DatabaseConnection,
        name: str,
        source: str,
        lattice_parameters: Union[str, List[float], Tuple[float, ...]],
        cod_id: Optional[int] = None,
        file_path: Optional[str] = None,
        space_group: Optional[str] = None,
        formula: Optional[str] = None,
    ) -> int:
        """
        Create a new crystal structure record.

        Args:
            db_conn: Database connection
            name: Crystal name
            source: Source of the crystal data (e.g., 'COD', 'CIF')
            lattice_parameters: Lattice parameters (a, b, c, alpha, beta, gamma)
            cod_id: Crystallography Open Database ID
            file_path: Path to the CIF file
            space_group: Space group symbol
            formula: Chemical formula

        Returns:
            ID of the created record
        """
        # Convert lattice parameters to JSON if needed
        if isinstance(lattice_parameters, (list, tuple)):
            lattice_parameters = json.dumps(list(lattice_parameters))

        db_conn.execute(
            """
            INSERT INTO crystal_structures
            (name, source, cod_id, file_path, lattice_parameters, space_group, formula)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (name, source, cod_id, file_path, lattice_parameters, space_group, formula),
        )

        # Get the ID of the inserted record
        db_conn.execute("SELECT last_insert_rowid()")
        result = db_conn.fetchone()
        db_conn.commit()

        return result["last_insert_rowid()"]

    @staticmethod
    def get_by_id(
        db_conn: DatabaseConnection, crystal_id: int
    ) -> Optional[Dict[str, Any]]:
        """
        Get a crystal structure by ID.

        Args:
            db_conn: Database connection
            crystal_id: Crystal structure ID

        Returns:
            Crystal structure record as a dictionary, or None if not found
        """
        db_conn.execute("SELECT * FROM crystal_structures WHERE id = ?", (crystal_id,))
        return db_conn.fetchone()

    @staticmethod
    def get_by_cod_id(
        db_conn: DatabaseConnection, cod_id: int
    ) -> Optional[Dict[str, Any]]:
        """
        Get a crystal structure by COD ID.

        Args:
            db_conn: Database connection
            cod_id: Crystallography Open Database ID

        Returns:
            Crystal structure record as a dictionary, or None if not found
        """
        db_conn.execute("SELECT * FROM crystal_structures WHERE cod_id = ?", (cod_id,))
        return db_conn.fetchone()

    @staticmethod
    def get_all(db_conn: DatabaseConnection) -> List[Dict[str, Any]]:
        """
        Get all crystal structures.

        Args:
            db_conn: Database connection

        Returns:
            List of crystal structure records
        """
        db_conn.execute("SELECT * FROM crystal_structures ORDER BY created_at DESC")
        return db_conn.fetchall()

    @staticmethod
    def delete(db_conn: DatabaseConnection, crystal_id: int) -> bool:
        """
        Delete a crystal structure.

        Args:
            db_conn: Database connection
            crystal_id: Crystal structure ID

        Returns:
            True if successful, False otherwise
        """
        db_conn.execute("DELETE FROM crystal_structures WHERE id = ?", (crystal_id,))
        db_conn.commit()
        return True


class SymmetryAnalysis:
    """
    Class for interacting with symmetry_analyses table.

    This class provides static methods for creating, retrieving, and managing
    symmetry analysis records in the database.
    """

    @staticmethod
    def create(
        db_conn: DatabaseConnection,
        crystal_id: int,
        supercell_size: int,
        symmetry_operations: Union[str, Dict[str, Any], List[Dict[str, Any]]],
        point_group: Optional[str] = None,
    ) -> int:
        """
        Create a new symmetry analysis record.

        Args:
            db_conn: Database connection
            crystal_id: Crystal structure ID
            supercell_size: Size of the supercell
            symmetry_operations: Symmetry operations as JSON or dictionary
            point_group: Point group symbol

        Returns:
            ID of the created record
        """
        # Convert symmetry operations to JSON if needed
        if isinstance(symmetry_operations, (dict, list)):
            symmetry_operations = json.dumps(symmetry_operations)

        db_conn.execute(
            """
            INSERT INTO symmetry_analyses
            (crystal_id, supercell_size, symmetry_operations, point_group)
            VALUES (?, ?, ?, ?)
            """,
            (crystal_id, supercell_size, symmetry_operations, point_group),
        )

        # Get the ID of the inserted record
        db_conn.execute("SELECT last_insert_rowid()")
        result = db_conn.fetchone()
        db_conn.commit()

        return result["last_insert_rowid()"]

    @staticmethod
    def get_by_id(
        db_conn: DatabaseConnection, analysis_id: int
    ) -> Optional[Dict[str, Any]]:
        """
        Get a symmetry analysis by ID.

        Args:
            db_conn: Database connection
            analysis_id: Symmetry analysis ID

        Returns:
            Symmetry analysis record as a dictionary, or None if not found
        """
        db_conn.execute("SELECT * FROM symmetry_analyses WHERE id = ?", (analysis_id,))
        return db_conn.fetchone()

    @staticmethod
    def get_by_crystal_id(
        db_conn: DatabaseConnection, crystal_id: int
    ) -> List[Dict[str, Any]]:
        """
        Get all symmetry analyses for a crystal.

        Args:
            db_conn: Database connection
            crystal_id: Crystal structure ID

        Returns:
            List of symmetry analysis records
        """
        db_conn.execute(
            "SELECT * FROM symmetry_analyses WHERE crystal_id = ? ORDER BY analysis_date DESC",
            (crystal_id,),
        )
        return db_conn.fetchall()


class VacancyConfiguration:
    """
    Class for interacting with vacancy_configurations table.

    This class provides static methods for creating, retrieving, and managing
    vacancy configuration records in the database.
    """

    @staticmethod
    def create(
        db_conn: DatabaseConnection,
        crystal_id: int,
        analysis_id: int,
        num_vacancies: int,
        vacancy_positions: Union[str, List[Tuple[float, float, float]]],
        energy: Optional[float] = None,
        is_stable: Optional[bool] = None,
    ) -> int:
        """
        Create a new vacancy configuration record.

        Args:
            db_conn: Database connection
            crystal_id: Crystal structure ID
            analysis_id: Symmetry analysis ID
            num_vacancies: Number of vacancies
            vacancy_positions: Positions of vacancies as JSON or list of tuples
            energy: Energy of the configuration
            is_stable: Whether the configuration is stable

        Returns:
            ID of the created record
        """
        # Convert vacancy positions to JSON if needed
        if isinstance(vacancy_positions, list):
            vacancy_positions = json.dumps(vacancy_positions)

        db_conn.execute(
            """
            INSERT INTO vacancy_configurations
            (crystal_id, analysis_id, num_vacancies, vacancy_positions, energy, is_stable)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                crystal_id,
                analysis_id,
                num_vacancies,
                vacancy_positions,
                energy,
                is_stable,
            ),
        )

        # Get the ID of the inserted record
        db_conn.execute("SELECT last_insert_rowid()")
        result = db_conn.fetchone()
        db_conn.commit()

        return result["last_insert_rowid()"]

    @staticmethod
    def get_by_id(
        db_conn: DatabaseConnection, config_id: int
    ) -> Optional[Dict[str, Any]]:
        """
        Get a vacancy configuration by ID.

        Args:
            db_conn: Database connection
            config_id: Vacancy configuration ID

        Returns:
            Vacancy configuration record as a dictionary, or None if not found
        """
        db_conn.execute(
            "SELECT * FROM vacancy_configurations WHERE id = ?", (config_id,)
        )
        return db_conn.fetchone()

    @staticmethod
    def get_by_crystal_id(
        db_conn: DatabaseConnection, crystal_id: int
    ) -> List[Dict[str, Any]]:
        """
        Get all vacancy configurations for a crystal.

        Args:
            db_conn: Database connection
            crystal_id: Crystal structure ID

        Returns:
            List of vacancy configuration records
        """
        db_conn.execute(
            """
            SELECT * FROM vacancy_configurations
            WHERE crystal_id = ?
            ORDER BY created_at DESC
            """,
            (crystal_id,),
        )
        return db_conn.fetchall()

    @staticmethod
    def get_by_analysis_id(
        db_conn: DatabaseConnection, analysis_id: int
    ) -> List[Dict[str, Any]]:
        """
        Get all vacancy configurations for a symmetry analysis.

        Args:
            db_conn: Database connection
            analysis_id: Symmetry analysis ID

        Returns:
            List of vacancy configuration records
        """
        db_conn.execute(
            """
            SELECT * FROM vacancy_configurations
            WHERE analysis_id = ?
            ORDER BY created_at DESC
            """,
            (analysis_id,),
        )
        return db_conn.fetchall()
