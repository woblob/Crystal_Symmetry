"""
Database connection module for Crystal Symmetry project.

This module provides a class for managing SQLite database connections
and executing queries.
"""

import os
import sqlite3
from pathlib import Path
from typing import Optional, List, Dict, Any, Union, Tuple


class DatabaseConnection:
    """
    SQLite database connection manager for Crystal Symmetry project.

    This class provides methods for connecting to a SQLite database,
    executing queries, and managing transactions.
    """

    db_path: Path
    _connection: Optional[sqlite3.Connection]
    _cursor: Optional[sqlite3.Cursor]

    def __init__(self, db_path: Union[str, Path]):
        """
        Initialize a database connection.

        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = Path(db_path)
        self._connection = None
        self._cursor = None

    def __enter__(self) -> "DatabaseConnection":
        """Context manager entry point."""
        self.connect()
        return self

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[Exception],
        exc_tb: Optional[object],
    ) -> None:
        """Context manager exit point."""
        self.close()

    def connect(self) -> "DatabaseConnection":
        """
        Connect to the database.

        Returns:
            Self for method chaining
        """
        # Create directory if it doesn't exist
        os.makedirs(self.db_path.parent, exist_ok=True)

        self._connection = sqlite3.connect(self.db_path)
        # Enable foreign keys
        self._connection.execute("PRAGMA foreign_keys = ON")
        # Return rows as dictionaries
        self._connection.row_factory = sqlite3.Row
        self._cursor = self._connection.cursor()

        return self

    def close(self) -> None:
        """Close the database connection."""
        if self._connection:
            self._connection.close()
            self._connection = None
            self._cursor = None

    def commit(self) -> None:
        """Commit the current transaction."""
        if self._connection:
            self._connection.commit()

    def rollback(self) -> None:
        """Roll back the current transaction."""
        if self._connection:
            self._connection.rollback()

    def execute(self, query: str, parameters: Optional[Tuple] = None) -> sqlite3.Cursor:
        """
        Execute a SQL query.

        Args:
            query: SQL query string
            parameters: Query parameters

        Returns:
            Cursor object for fetching results

        Raises:
            sqlite3.Error: If the query fails
        """
        if not self._cursor:
            self.connect()

        if parameters:
            return self._cursor.execute(query, parameters)
        return self._cursor.execute(query)

    def executemany(self, query: str, parameters_list: List[Tuple]) -> sqlite3.Cursor:
        """
        Execute a SQL query with multiple parameter sets.

        Args:
            query: SQL query string
            parameters_list: List of parameter tuples

        Returns:
            Cursor object for fetching results

        Raises:
            sqlite3.Error: If the query fails
        """
        if not self._cursor:
            self.connect()

        return self._cursor.executemany(query, parameters_list)

    def fetchone(self) -> Optional[Dict[str, Any]]:
        """
        Fetch a single row from the last query.

        Returns:
            Row as a dictionary, or None if no more rows
        """
        if not self._cursor:
            return None

        row = self._cursor.fetchone()
        if row:
            return dict(row)
        return None

    def fetchall(self) -> List[Dict[str, Any]]:
        """
        Fetch all rows from the last query.

        Returns:
            List of rows as dictionaries
        """
        if not self._cursor:
            return []

        return [dict(row) for row in self._cursor.fetchall()]

    def table_exists(self, table_name: str) -> bool:
        """
        Check if a table exists in the database.

        Args:
            table_name: Name of the table to check

        Returns:
            True if the table exists, False otherwise
        """
        self.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (table_name,),
        )
        return bool(self.fetchone())
