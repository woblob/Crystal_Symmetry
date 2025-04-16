#!/usr/bin/env python
import ast
import sys

class UndefinedVariableFinder(ast.NodeVisitor):
    def __init__(self):
        self.defined_names = set()
        self.undefined_names = []
        self.scope_stack = []

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            # Variable is being defined
            self.defined_names.add(node.id)
            print(f"Defined: {node.id} at line {node.lineno}")
        elif isinstance(node.ctx, ast.Load):
            # Variable is being used
            if node.id not in self.defined_names and node.id not in dir(__builtins__):
                self.undefined_names.append((node.id, node.lineno, node.col_offset))
                print(f"Undefined: {node.id} at line {node.lineno}")
        self.generic_visit(node)

    def visit_Import(self, node):
        for name in node.names:
            imported_name = name.name.split('.')[0]
            self.defined_names.add(imported_name)
            print(f"Imported: {imported_name} at line {node.lineno}")
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for name in node.names:
            if name.name == '*':
                # Can't track * imports statically
                print(f"Warning: '*' import at line {node.lineno} makes static analysis difficult")
            else:
                self.defined_names.add(name.name)
                print(f"Imported from: {name.name} at line {node.lineno}")
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.defined_names.add(node.name)
        print(f"Function: {node.name} at line {node.lineno}")
        # Add function parameters as defined names
        old_defined = self.defined_names.copy()
        for arg in node.args.args:
            self.defined_names.add(arg.arg)
            print(f"Param: {arg.arg} at line {node.lineno}")
        self.generic_visit(node)
        # Restore the defined names (function arguments are only defined within the function)
        self.defined_names = old_defined

    def visit_ClassDef(self, node):
        self.defined_names.add(node.name)
        print(f"Class: {node.name} at line {node.lineno}")
        self.generic_visit(node)

def find_undefined_variables(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    try:
        tree = ast.parse(content, file_path)
    except SyntaxError as e:
        print(f"Syntax error in {file_path}: {e}")
        return []

    finder = UndefinedVariableFinder()
    finder.visit(tree)

    print(f"DEBUG: Defined names: {sorted(finder.defined_names)}")
    return finder.undefined_names

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_undefined_vars.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    print(f"Analyzing {file_path} for undefined variables...")
    undefined_vars = find_undefined_variables(file_path)

    if undefined_vars:
        print(f"Found {len(undefined_vars)} potentially undefined variables in {file_path}:")
        for var, line, col in undefined_vars:
            print(f"Line {line}, Column {col}: '{var}'")
    else:
        print(f"✓ No undefined variables found in {file_path} ✓")
        print("All variables are properly defined! The code should run without undefined variable errors.") 