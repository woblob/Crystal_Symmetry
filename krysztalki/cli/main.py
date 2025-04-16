"""Main module for crystal symmetry analysis and vacancy calculations."""

import argparse
from itertools import combinations
from time import time
from typing import Set, Tuple, List, Dict, Any

import numpy as np

from krysztalki.core.symmetry import analyze_symmetry
from krysztalki.io.cif import read_cif, getSCell

def main() -> None:
    """
    Main entry point for the crystal symmetry CLI.

    This function parses command line arguments and runs the crystal symmetry analysis.
    """
    parser = argparse.ArgumentParser(description="Crystal symmetry analysis tool")
    parser.add_argument("file", help="CIF file path or COD ID")
    parser.add_argument(
        "--supercell", "-s", type=int, default=1, 
        help="Supercell size (default: 1)"
    )
    parser.add_argument(
        "--vacancies", "-v", type=int, default=1,
        help="Number of vacancies to analyze (default: 1)"
    )
    parser.add_argument(
        "--output", "-o", type=str, default="OUTPUT.txt",
        help="Output file path (default: OUTPUT.txt)"
    )

    args = parser.parse_args()

    print(f"Loading crystal from: {args.file}")
    print(f"Using supercell size: {args.supercell}")
    print(f"Analyzing with {args.vacancies} vacancies")

    start = time()

    # Run analysis using the proper module function
    result = analyze_symmetry(
        read_cif(args.file), 
        vacancy_count=args.vacancies
    )

    print(f"Analysis completed in {(time() - start):.2f} seconds")
    print(f"Found {len(result['symmetry_operations'])} symmetry operations")
    print(f"Writing results to {args.output}")

    # Write results to output file
    with open(args.output, "w") as f:
        f.write(f"Crystal file: {args.file}\n")
        f.write(f"Supercell size: {args.supercell}\n")
        f.write(f"Vacancy count: {args.vacancies}\n\n")
        f.write("Symmetry operations:\n")
        for sym_op in result["symmetry_operations"]:
            f.write(f"  {sym_op}\n")
        f.write("\nVacancy configurations:\n")
        for i, config in enumerate(result["vacancy_configs"]):
            f.write(f"Configuration {i+1}:\n")
            f.write(f"  Vacancies at: {config['positions']}\n")
            f.write(f"  Preserved symmetries: {config['symmetries']}\n")
            f.write("\n")

if __name__ == "__main__":
    main()
