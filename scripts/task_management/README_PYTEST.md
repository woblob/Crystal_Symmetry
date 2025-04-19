# Using pytest for Testing

This document explains how to use pytest for testing the task management scripts.

## Overview

We've converted the test suite from unittest to pytest to follow best practices and make tests more maintainable. Pytest offers several advantages:

1. Simpler test syntax with plain assert statements
2. Powerful fixtures for test setup and teardown
3. Better test discovery and organization
4. Rich plugin ecosystem
5. Detailed test reports

## Running Tests

### Option 1: Using the run_pytest.py script

The simplest way to run the tests is to use the provided script:

```bash
python run_pytest.py
```

This will run all the tests in the test_update_all_tasks_pytest.py file and display the results.

### Option 2: Using pytest directly

You can also run pytest directly:

```bash
# Run all tests
pytest test_update_all_tasks_pytest.py

# Run with verbose output
pytest test_update_all_tasks_pytest.py -v

# Run a specific test
pytest test_update_all_tasks_pytest.py::test_extract_markdown_content

# Run tests with coverage report
pytest test_update_all_tasks_pytest.py --cov=update_all_tasks
```

## Test Structure

The tests are organized as follows:

1. **Fixtures**: The `temp_test_env` fixture creates a temporary test environment with all necessary files and directories.
2. **Helper Functions**: Functions like `_create_tasks_json` help set up test data.
3. **Unit Tests**: Individual tests for specific functions.
4. **Integration Tests**: Tests that verify the interaction between components.

## Writing New Tests

When writing new tests, follow these guidelines:

1. Use descriptive test names that explain what is being tested
2. Use fixtures for test setup and teardown
3. Keep tests focused on a single functionality
4. Use plain assert statements instead of self.assert\* methods
5. Group related tests together
6. Always check for None before accessing dictionary keys to avoid Pylance "Object of type 'None' is not subscriptable" warnings

```python
# Good practice - check for None before accessing dictionary keys
tasks_data, error = update_all_tasks.load_tasks_json()
assert tasks_data is not None, f"Failed to load tasks.json: {error}"

# Now it's safe to access the dictionary
task = tasks_data["tasks"][0]
```

Example:

```python
def test_new_feature():
    """Test the new feature functionality."""
    # Setup
    input_data = "test input"

    # Execute
    result = my_function(input_data)

    # Assert
    assert result == "expected output"
    assert isinstance(result, str)
```

## Converting More Tests to pytest

To convert more unittest tests to pytest:

1. Replace `unittest.TestCase` classes with standalone test functions
2. Replace `setUp` and `tearDown` methods with fixtures
3. Replace `self.assert*` methods with plain `assert` statements
4. Replace `self.setUp()` with fixture setup code
5. Replace `self.tearDown()` with fixture teardown code

## Dependencies

Make sure you have pytest installed:

```bash
pip install pytest pytest-cov
```
