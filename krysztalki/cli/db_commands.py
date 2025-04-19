"""
Database CLI commands for Crystal Symmetry project.

This module provides CLI commands for interacting with the database.
"""

import json
from pathlib import Path

import click
from tabulate import tabulate

from krysztalki.db.connection import DatabaseConnection
from krysztalki.db.models import (
    CrystalStructure,
)
from krysztalki.db.utils import (
    get_default_db_path,
    init_database,
    store_crystal,
    list_all_crystals,
    get_crystal_with_analyses,
)
from krysztalki.io.cif import read_cif


@click.group(name="db", help="Database operations")
@click.option(
    "--db-path",
    type=click.Path(),
    help="Path to the database file (default: ~/.krysztalki/crystal_symmetry.db)",
)
@click.pass_context
def db_commands(ctx, db_path):
    """Database operations for crystal structures."""
    # Use default path if not specified
    if db_path is None:
        db_path = get_default_db_path()

    # Store database path in context
    ctx.ensure_object(dict)
    ctx.obj["db_path"] = db_path


@db_commands.command(name="init")
@click.pass_context
def init_db(ctx):
    """Initialize the database."""
    db_path = ctx.obj["db_path"]

    # Check if database already exists
    if Path(db_path).exists():
        if not click.confirm(f"Database already exists at {db_path}. Reinitialize?"):
            return

    # Initialize database
    db_conn = init_database(db_path)
    db_conn.close()

    click.echo(f"Database initialized at {db_path}")


@db_commands.command(name="import")
@click.argument("file", type=str)
@click.option("--name", type=str, help="Name for the crystal structure")
@click.pass_context
def import_crystal(ctx, file, name):
    """
    Import a crystal structure from a CIF file or COD ID.

    FILE can be either a path to a CIF file or a Crystallography Open
    Database (COD) ID.
    """
    db_path = ctx.obj["db_path"]

    # Process file path
    try:
        cod_id = int(file)
        file_path = None
        source = "COD"
        if name is None:
            name = f"COD-{cod_id}"
    except ValueError:
        cod_id = None
        file_path = file
        source = "CIF"
        if name is None:
            name = Path(file).stem

    # Load crystal
    click.echo(
        f"Loading crystal from {'COD ID: ' + file if cod_id else 'file: ' + file}"
    )
    crystal = read_cif(file)

    # Store in database
    db_conn = DatabaseConnection(db_path).connect()
    try:
        crystal_id = store_crystal(
            crystal,
            name=name,
            source=source,
            cod_id=cod_id,
            file_path=file_path,
            db_conn=db_conn,
        )
        click.echo(f"Crystal structure imported with ID: {crystal_id}")
    finally:
        db_conn.close()


@db_commands.command(name="list")
@click.pass_context
def list_crystals(ctx):
    """List all crystal structures in the database."""
    db_path = ctx.obj["db_path"]

    # Get all crystal structures
    db_conn = DatabaseConnection(db_path).connect()
    try:
        crystals = list_all_crystals(db_conn)

        if not crystals:
            click.echo("No crystal structures found in the database.")
            return

        # Format as table
        table_data = []
        for crystal in crystals:
            # Parse created_at
            created_at = crystal["created_at"].split(".")[0]  # Remove microseconds

            # Add to table
            table_data.append(
                [
                    crystal["id"],
                    crystal["name"],
                    crystal["source"],
                    crystal["cod_id"] or "N/A",
                    crystal["space_group"] or "N/A",
                    crystal["formula"] or "N/A",
                    created_at,
                ]
            )

        # Print table
        click.echo(
            tabulate(
                table_data,
                headers=[
                    "ID",
                    "Name",
                    "Source",
                    "COD ID",
                    "Space Group",
                    "Formula",
                    "Created At",
                ],
                tablefmt="grid",
            )
        )
    finally:
        db_conn.close()


@db_commands.command(name="show")
@click.argument("crystal_id", type=int)
@click.option("--json", "output_json", is_flag=True, help="Output as JSON")
@click.pass_context
def show_crystal(ctx, crystal_id, output_json):
    """Show details of a crystal structure."""
    db_path = ctx.obj["db_path"]

    # Get crystal structure
    db_conn = DatabaseConnection(db_path).connect()
    try:
        crystal = get_crystal_with_analyses(crystal_id, db_conn)

        if not crystal:
            click.echo(f"Crystal structure with ID {crystal_id} not found.")
            return

        if output_json:
            # Output as JSON
            click.echo(json.dumps(crystal, indent=2))
        else:
            # Output as formatted text
            click.echo(f"Crystal Structure: {crystal['name']}")
            click.echo(f"ID: {crystal['id']}")
            click.echo(f"Source: {crystal['source']}")
            click.echo(f"COD ID: {crystal['cod_id'] or 'N/A'}")
            click.echo(f"Space Group: {crystal['space_group'] or 'N/A'}")
            click.echo(f"Formula: {crystal['formula'] or 'N/A'}")
            click.echo(f"Created At: {crystal['created_at']}")

            # Parse lattice parameters
            lattice_params = json.loads(crystal["lattice_parameters"])
            click.echo("\nLattice Parameters:")
            click.echo(f"  a: {lattice_params[0]:.4f} Å")
            click.echo(f"  b: {lattice_params[1]:.4f} Å")
            click.echo(f"  c: {lattice_params[2]:.4f} Å")
            click.echo(f"  α: {lattice_params[3]:.2f}°")
            click.echo(f"  β: {lattice_params[4]:.2f}°")
            click.echo(f"  γ: {lattice_params[5]:.2f}°")

            # Show atoms
            click.echo(f"\nAtoms ({len(crystal['atoms'])}):")
            atom_table = []
            for i, atom in enumerate(crystal["atoms"][:10]):  # Show first 10 atoms
                atom_table.append(
                    [
                        i + 1,
                        atom["element"],
                        atom["atomic_number"],
                        f"{atom['x']:.4f}",
                        f"{atom['y']:.4f}",
                        f"{atom['z']:.4f}",
                    ]
                )

            click.echo(
                tabulate(
                    atom_table,
                    headers=["#", "Element", "Z", "x", "y", "z"],
                    tablefmt="simple",
                )
            )

            if len(crystal["atoms"]) > 10:
                click.echo(f"... and {len(crystal['atoms']) - 10} more atoms")

            # Show analyses
            if crystal["analyses"]:
                click.echo(f"\nSymmetry Analyses ({len(crystal['analyses'])}):")
                for analysis in crystal["analyses"]:
                    click.echo(f"  Analysis ID: {analysis['id']}")
                    click.echo(f"  Supercell Size: {analysis['supercell_size']}")
                    click.echo(f"  Point Group: {analysis['point_group'] or 'N/A'}")
                    click.echo(f"  Date: {analysis['analysis_date']}")

                    # Show vacancy configurations
                    if analysis.get("vacancy_configurations"):
                        click.echo(
                            f"  Vacancy Configurations ({len(analysis['vacancy_configurations'])}):"
                        )
                        for config in analysis["vacancy_configurations"]:
                            click.echo(f"    Config ID: {config['id']}")
                            click.echo(f"    Vacancies: {config['num_vacancies']}")
                            click.echo(f"    Energy: {config['energy'] or 'N/A'}")
                            click.echo(f"    Stable: {config['is_stable'] or 'N/A'}")
                            click.echo("")
            else:
                click.echo("\nNo symmetry analyses found for this crystal.")
    finally:
        db_conn.close()


@db_commands.command(name="delete")
@click.argument("crystal_id", type=int)
@click.option("--force", is_flag=True, help="Force deletion without confirmation")
@click.pass_context
def delete_crystal(ctx, crystal_id, force):
    """Delete a crystal structure from the database."""
    db_path = ctx.obj["db_path"]

    # Get crystal structure
    db_conn = DatabaseConnection(db_path).connect()
    try:
        crystal = CrystalStructure.get_by_id(db_conn, crystal_id)

        if not crystal:
            click.echo(f"Crystal structure with ID {crystal_id} not found.")
            return

        # Confirm deletion
        if not force and not click.confirm(
            f"Are you sure you want to delete crystal '{crystal['name']}' (ID: {crystal_id})?"
        ):
            return

        # Delete crystal
        CrystalStructure.delete(db_conn, crystal_id)
        click.echo(f"Crystal structure with ID {crystal_id} deleted.")
    finally:
        db_conn.close()
