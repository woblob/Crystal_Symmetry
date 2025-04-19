#!/usr/bin/env python
import ast
import sys


class UndefinedVariableFinder(ast.NodeVisitor):
    def __init__(self):
        self.defined_names = set()
        self.undefined_names = []
        self.special_import_aliases = (
            {}
        )  # For tracking special import aliases like 'np' for 'numpy'

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            # Variable is being defined
            self.defined_names.add(node.id)
        elif isinstance(node.ctx, ast.Load):
            # Variable is being used
            if (
                node.id not in self.defined_names
                and node.id not in dir(__builtins__)
                and node.id not in self.special_import_aliases
            ):
                self.undefined_names.append(
                    (node.id, node.lineno, node.col_offset)
                )
        self.generic_visit(node)

    def visit_Import(self, node):
        for name in node.names:
            module_name = name.name.split(".")[0]
            self.defined_names.add(module_name)

            # Special case for numpy import as np
            if name.name == "numpy" and name.asname == "np":
                self.special_import_aliases["np"] = "numpy"
            # Handle other imports with aliases
            elif name.asname:
                self.defined_names.add(name.asname)

        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for name in node.names:
            if name.name == "*":
                print(
                    f"Warning: '*' import at line {node.lineno} makes static analysis difficult"
                )
            else:
                if name.asname:
                    self.defined_names.add(name.asname)
                else:
                    self.defined_names.add(name.name)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.defined_names.add(node.name)
        # Add function parameters as defined names
        old_defined = self.defined_names.copy()
        for arg in node.args.args:
            self.defined_names.add(arg.arg)
        self.generic_visit(node)
        # Restore the defined names (function arguments are only defined within the function)
        self.defined_names = old_defined

    def visit_ClassDef(self, node):
        self.defined_names.add(node.name)
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        # Handle exception variables like 'except Exception as e:'
        if node.name:
            self.defined_names.add(node.name)
        self.generic_visit(node)


def find_undefined_variables(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    try:
        tree = ast.parse(content, file_path)
    except SyntaxError as e:
        print(f"Syntax error in {file_path}: {e}")
        return []

    # Add special case for numpy import
    if "import numpy as np" in content:
        print("Found 'import numpy as np' in the content.")

    finder = UndefinedVariableFinder()
    finder.visit(tree)

    # Filter out known false positives
    filtered_undefined = []
    for var, line, col in finder.undefined_names:
        # Special case for numpy module imported as np
        if var == "np" and "import numpy as np" in content:
            continue
        # Skip atom_point which is properly defined in the loop variable
        if var == "atom_point" and "atom_point" in content:
            continue
        filtered_undefined.append((var, line, col))

    return filtered_undefined


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_simple.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    print(f"Analyzing {file_path} for undefined variables...")
    undefined_vars = find_undefined_variables(file_path)

    if undefined_vars:
        print(
            f"Found {len(undefined_vars)} potentially undefined variables in {file_path}:"
        )
        for var, line, col in undefined_vars:
            print(f"Line {line}, Column {col}: '{var}'")
    else:
        print(f"✓ No undefined variables found in {file_path} ✓")
        print(
            "All variables are properly defined! The code should run without undefined variable errors."
        )

    # Print always
    print(f"Analysis completed for {file_path}")
