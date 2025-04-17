"""Main module for crystal symmetry analysis and vacancy calculations."""

from itertools import combinations
from time import time
from typing import Set, Tuple, List, Dict, Any, Union

import click
import numpy as np

from krysztalki.core.symmetry import analyze_symmetry
from krysztalki.io.cif import read_cif, getSCell


def process_file_path(file_path_str: str) -> Union[str, int]:
    """Convert file path string to either a string path or integer COD ID."""
    try:
        return int(file_path_str)
    except ValueError:
        return file_path_str


@click.group(help="Crystal symmetry analysis toolkit")
def main():
    """Krysztalki - Crystal symmetry analysis toolkit.

    This tool provides commands for analyzing crystal structures,
    calculating symmetry operations, and studying vacancy configurations.
    """
    pass


@main.command()
@click.argument("file", type=str)
@click.option(
    "--supercell", "-s", type=int, default=1, help="Supercell size (default: 1)"
)
@click.option(
    "--vacancies",
    "-v",
    type=int,
    default=1,
    help="Number of vacancies to analyze (default: 1)",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(writable=True),
    default="OUTPUT.txt",
    help="Output file path (default: OUTPUT.txt)",
)
def analyze(file: str, supercell: int, vacancies: int, output: str) -> None:
    """Analyze crystal symmetry from a CIF file or COD ID.

    FILE can be either a path to a CIF file or a Crystallography Open Database (COD) ID.

    Examples:
        krysztalki analyze 1000041  # Analyze NaCl structure from COD
        krysztalki analyze path/to/file.cif  # Analyze structure from local file
    """
    # Process file path
    file_path = process_file_path(file)

    if isinstance(file_path, int):
        click.echo(f"Loading crystal from COD ID: {file_path}")
    else:
        click.echo(f"Loading crystal from file: {file_path}")

    click.echo(f"Using supercell size: {supercell}")
    click.echo(f"Analyzing with {vacancies} vacancies")

    start = time()

    # Run analysis using the proper module function
    result = analyze_symmetry(read_cif(file_path), vacancy_count=vacancies)

    click.echo(f"Analysis completed in {(time() - start):.2f} seconds")
    click.echo(f"Found {len(result['symmetry_operations'])} symmetry operations")
    click.echo(f"Writing results to {output}")

    # Write results to output file
    with open(output, "w") as f:
        f.write(f"Crystal file: {file_path}\n")
        f.write(f"Supercell size: {supercell}\n")
        f.write(f"Vacancy count: {vacancies}\n\n")
        f.write("Symmetry operations:\n")
        for sym_op in result["symmetry_operations"]:
            f.write(f"  {sym_op}\n")
        f.write("\nVacancy configurations:\n")
        for i, config in enumerate(result["vacancy_configs"]):
            f.write(f"Configuration {i+1}:\n")
            f.write(f"  Vacancies at: {config['positions']}\n")
            f.write(f"  Preserved symmetries: {config['symmetries']}\n")
            f.write("\n")


@main.command()
@click.argument("file", type=str)
@click.option("--verbose", "-v", is_flag=True, help="Show detailed crystal information")
def info(file: str, verbose: bool) -> None:
    """Display information about a crystal structure.

    FILE can be either a path to a CIF file or a Crystallography Open Database (COD) ID.

    Examples:
        krysztalki info 1000041  # Show info about NaCl structure from COD
        krysztalki info --verbose path/to/file.cif  # Show detailed info about local file
    """
    # Process file path
    file_path = process_file_path(file)

    if isinstance(file_path, int):
        click.echo(f"Loading crystal from COD ID: {file_path}")
    else:
        click.echo(f"Loading crystal from file: {file_path}")

    # Load the crystal structure
    crystal = read_cif(file_path)

    # Display basic information
    click.echo(f"\nCrystal Structure Information:")
    click.echo(f"---------------------------")
    click.echo(f"Formula: {crystal.composition}")
    click.echo(f"Space group: {crystal.symmetry()['international']}")
    click.echo(f"Number of atoms: {len(crystal)}")

    # Display detailed information if verbose flag is set
    if verbose:
        click.echo(f"\nDetailed Information:")
        click.echo(f"---------------------------")
        click.echo(f"Space group number: {crystal.symmetry()['international_number']}")
        click.echo(f"Lattice parameters:")
        click.echo(f"  a = {crystal.lattice_parameters[0]:.4f} Å")
        click.echo(f"  b = {crystal.lattice_parameters[1]:.4f} Å")
        click.echo(f"  c = {crystal.lattice_parameters[2]:.4f} Å")
        click.echo(f"  α = {crystal.lattice_parameters[3]:.2f}°")
        click.echo(f"  β = {crystal.lattice_parameters[4]:.2f}°")
        click.echo(f"  γ = {crystal.lattice_parameters[5]:.2f}°")
        click.echo(f"\nAtom types:")
        for element, count in crystal.chemical_composition.items():
            click.echo(f"  {element}: {count}")


if __name__ == "__main__":
    main()
