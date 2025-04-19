# Subtask 5.5: Create linting workflow script

**Status:** pending

**Dependencies:** 5.1

**Description:** Create a script that implements a proper linting workflow: first run linters that check for code-breaking errors, fix errors immediately, then apply code formatters. The script should treat warnings as errors and stop the process if any issues are found.

## Implementation Details

### Script Overview

Create a Python script called `run_linters.py` in the `scripts` directory that implements a sequential linting workflow following these principles:
1. Run linters that check for code-breaking errors first
2. Stop immediately if any errors are found
3. Treat warnings as errors
4. Only apply code formatters after all errors are fixed

### Linting Order and Tools

The script should run linters in this specific order:

1. **mypy** - Type checking (most critical errors)
   - Command: `python -m mypy <target_files> --config-file=pyproject.toml`
   - Exit on any type errors

2. **pylint** - Code quality and logic errors
   - Command: `python -m pylint <target_files> --rcfile=.pylintrc`
   - Exit on any errors (treat warnings as errors)

3. **flake8** - PEP8 compliance and syntax errors
   - Command: `python -m flake8 <target_files> --config=.flake8`
   - Exit on any errors (treat warnings as errors)

4. **black** (check mode first) - Code formatting
   - Command: `python -m black --check <target_files>`
   - If check fails, suggest running black to format

5. **isort** (check mode first) - Import sorting
   - Command: `python -m isort --check <target_files> --profile=black`
   - If check fails, suggest running isort to format

### Script Features

1. **Command-line Arguments**:
   - `--path`: Path to file or directory to lint (default: entire package)
   - `--fix`: Automatically apply fixes for formatting issues (black/isort)
   - `--strict`: Treat all warnings as errors (default: True)
   - `--verbose`: Show detailed output from linters

2. **Error Handling**:
   - Capture and display linter output in a readable format
   - Provide clear error messages with file and line numbers
   - Show suggestions for fixing common errors
   - Exit with appropriate error codes

3. **Reporting**:
   - Display a summary of issues found by each linter
   - Show timing information for each linting step
   - Provide a final report with overall status

### Implementation Steps

1. Create the basic script structure with argument parsing
2. Implement functions to run each linter with proper error handling
3. Create a sequential workflow that respects the order of operations
4. Add reporting and summary functionality
5. Implement automatic fixing option for formatting tools
6. Add documentation and usage examples

### Example Usage

```bash
# Run all linters on the entire package
python scripts/run_linters.py

# Run linters on a specific file
python scripts/run_linters.py --path krysztalki/core/symmetry.py

# Run linters and automatically fix formatting issues
python scripts/run_linters.py --fix

# Run linters with detailed output
python scripts/run_linters.py --verbose
```

### Integration with Pre-commit

Add instructions for integrating the script with pre-commit hooks to ensure code quality before commits:

```yaml
# .pre-commit-config.yaml
repos:
-   repo: local
    hooks:
    -   id: linting-workflow
        name: Run linting workflow
        entry: python scripts/run_linters.py
        language: system
        pass_filenames: false
```
