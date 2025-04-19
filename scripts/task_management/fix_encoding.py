#!/usr/bin/env python3
"""
Fix encoding issues in Task Master task files.

This script replaces problematic Unicode box-drawing characters with ASCII alternatives
in task files to ensure proper display across different environments.

Usage:
    python fix_encoding.py [task_id]

If task_id is provided, only that task file will be fixed.
If no task_id is provided, all task files will be fixed.

Example:
    python fix_encoding.py 1
    python fix_encoding.py
"""

import sys
import re
from pathlib import Path


# Define the replacements for the box-drawing characters
REPLACEMENTS = {
    # Problematic encodings
    'â"ś': "|--",  # ├──
    'â"‚': "|",  # │
    'â""': "`--",  # └──
    'â"€': "-",  # ─
    # Unicode box-drawing characters (for direct replacement)
    "├": "|--",
    "│": "|",
    "└": "`--",
    "─": "-",
}


def fix_file_encoding(file_path):
    """Replace problematic characters in a file with ASCII alternatives."""
    try:
        # Read the file content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if the file contains any of the problematic characters
        needs_fixing = any(bad_char in content for bad_char in REPLACEMENTS)
        if not needs_fixing:
            print(f"No encoding issues found in {file_path}")
            return True

        # Replace each problematic character
        for bad_char, good_char in REPLACEMENTS.items():
            content = content.replace(bad_char, good_char)

        # Fix tree structure formatting
        content = fix_tree_structure(content)

        # Write the fixed content back to the file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Fixed encoding in {file_path}")
        return True
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False


def fix_tree_structure(content):
    """Fix formatting issues in tree structures."""
    # Find code blocks containing tree structures
    tree_pattern = r"```\s*\n(.*?crystal_symmetry/.*?)```"
    matches = re.findall(tree_pattern, content, re.DOTALL)

    # Define the ASCII tree structure for the project
    ascii_tree = """  crystal_symmetry/
  |-- __init__.py          # Main package initialization
  |-- core/               # Core symmetry algorithms
  |   |-- __init__.py     # Core module exports
  |   |-- lattice.py      # Lattice operations
  |   `-- symmetry.py     # Symmetry operations
  |-- io/                 # Input/output operations
  |   |-- __init__.py     # IO module exports
  |   |-- cif.py          # CIF file parsing
  |   `-- exporters.py    # Data export functions
  |-- utils/              # Utility functions
  |   |-- __init__.py     # Utils module exports
  |   |-- math.py         # Math helpers
  |   `-- validation.py   # Data validation
  `-- visualization/      # Visualization components
      |-- __init__.py     # Visualization exports
      `-- plotting.py     # Plotting functions"""

    for match in matches:
        # Check if this is a tree structure that needs fixing
        if "crystal_symmetry/" in match and any(char in match for char in REPLACEMENTS):
            # If it's the main project structure, replace with the predefined ASCII tree
            if match.strip().startswith("crystal_symmetry/"):
                content = content.replace(match, ascii_tree)
            else:
                # For other tree structures, replace characters
                fixed_tree = match
                for bad_char, good_char in REPLACEMENTS.items():
                    fixed_tree = fixed_tree.replace(bad_char, good_char)

                # Fix spacing and alignment
                fixed_tree = re.sub(r"(\s+)`--", r"\1`--", fixed_tree)
                fixed_tree = re.sub(r"(\s+)\|--", r"\1|--", fixed_tree)

                # Replace the original tree with the fixed one
                content = content.replace(match, fixed_tree)

    return content


def fix_task_file(task_id):
    """Fix encoding issues in a specific task file."""
    tasks_dir = Path("tasks")
    file_path = tasks_dir / f"task_{task_id:03d}.txt"

    if not file_path.exists():
        print(f"Error: Task file {file_path} does not exist.")
        return False

    return fix_file_encoding(file_path)


def fix_all_task_files():
    """Fix encoding issues in all task files."""
    tasks_dir = Path("tasks")
    fixed_count = 0

    # Get all task files
    for file_path in tasks_dir.glob("task_*.txt"):
        if fix_file_encoding(file_path):
            fixed_count += 1

    print(f"Fixed encoding in {fixed_count} task files")
    return fixed_count > 0


def main():
    """Main function to parse arguments and fix encoding issues."""
    if len(sys.argv) > 2:
        print(f"Usage: {sys.argv[0]} [task_id]")
        sys.exit(1)

    if len(sys.argv) == 2:
        try:
            task_id = int(sys.argv[1])
            success = fix_task_file(task_id)
        except ValueError:
            print("Error: Task ID must be a number.")
            sys.exit(1)
    else:
        success = fix_all_task_files()

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
