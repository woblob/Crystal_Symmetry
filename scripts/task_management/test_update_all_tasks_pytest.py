#!/usr/bin/env python3
"""
Test script for update_all_tasks.py using pytest.

This script runs comprehensive tests on the update_all_tasks.py script
to verify its functionality. It creates temporary test files and directories,
runs the script in test mode, and verifies the results.

Usage:
    pytest test_update_all_tasks_pytest.py
"""

import json
import os
import shutil
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch
import update_all_tasks  # type: ignore

import pytest
from click.testing import CliRunner

# Add the parent directory to sys.path to import the module
sys.path.insert(0, str(Path(__file__).parent))


@pytest.fixture
def temp_test_env():
    """Create a temporary test environment with necessary files and directories."""
    # Create temporary directory
    temp_dir = tempfile.mkdtemp()
    tasks_dir = Path(temp_dir) / "tasks"
    docs_dir = tasks_dir / "docs"

    # Create directory structure
    tasks_dir.mkdir(exist_ok=True)
    docs_dir.mkdir(exist_ok=True)

    # Create test task directories
    (docs_dir / "task_001").mkdir(exist_ok=True)
    (docs_dir / "task_002").mkdir(exist_ok=True)

    # Save original working directory
    original_dir = os.getcwd()

    # Change to temporary directory
    os.chdir(temp_dir)

    # Create test files
    _create_tasks_json(tasks_dir)
    _create_task1_files(docs_dir)
    _create_task2_files(docs_dir)

    # Yield the test environment
    yield {
        "temp_dir": temp_dir,
        "tasks_dir": tasks_dir,
        "docs_dir": docs_dir,
        "original_dir": original_dir,
    }

    # Clean up after tests
    os.chdir(original_dir)
    shutil.rmtree(temp_dir)


def _create_tasks_json(tasks_dir):
    """Create tasks.json test file."""
    tasks_json = {
        "tasks": [
            {
                "id": 1,
                "title": "Original Task 1",
                "status": "pending",
                "description": "Original description 1",
                "details": "<info added on 2025-04-16T18:49:35.663Z>\nOriginal details 1\n</info added on 2025-04-16T18:49:35.663Z>",
                "subtasks": [
                    {
                        "id": 1,
                        "title": "Original Subtask 1.1",
                        "status": "pending",
                        "description": "Original subtask description 1.1",
                        "details": "<info added on 2025-04-16T18:49:35.663Z>\nOriginal subtask details 1.1\n</info added on 2025-04-16T18:49:35.663Z>",
                    }
                ],
            },
            {
                "id": 2,
                "title": "Original Task 2",
                "status": "pending",
                "description": "Original description 2",
                "details": "Original details 2",
                "subtasks": [
                    {
                        "id": 1,
                        "title": "Original Subtask 2.1",
                        "status": "pending",
                        "description": "Original subtask description 2.1",
                        "details": "Original subtask details 2.1",
                    }
                ],
            },
        ]
    }

    with open(tasks_dir / "tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks_json, f, indent=2)


def _create_task1_files(docs_dir):
    """Create markdown files for task 1."""
    # Create overview.md for task 1
    overview_content = """# Task 1: Updated Task 1

**Status:** done

**Description:** Updated description 1

## Details

Updated details 1
"""
    with open(
        docs_dir / "task_001" / "overview.md", "w", encoding="utf-8"
    ) as f:
        f.write(overview_content)

    # Create subtask_001.md for task 1
    subtask_content = """# Subtask 1.1: Updated Subtask 1.1

**Status:** done

**Dependencies:** None

**Description:** Updated subtask description 1.1

## Details

Updated subtask details 1.1
"""
    with open(
        docs_dir / "task_001" / "subtask_001.md", "w", encoding="utf-8"
    ) as f:
        f.write(subtask_content)


def _create_task2_files(docs_dir):
    """Create markdown files for task 2."""
    # Create overview.md for task 2 (no changes)
    overview_content = """# Task 2: Original Task 2

**Status:** pending

**Description:** Original description 2

## Details

Original details 2
"""
    with open(
        docs_dir / "task_002" / "overview.md", "w", encoding="utf-8"
    ) as f:
        f.write(overview_content)


def test_extract_markdown_content():
    """Test extract_markdown_content function."""
    test_content = """# Test Task

## Details

This is the details section.

## Another Section

This is another section.
"""
    details = update_all_tasks.extract_markdown_content(test_content)
    assert details == "This is the details section."


def test_clean_details():
    """Test clean_details function."""
    test_details = """<info added on 2025-04-16T18:49:35.663Z>
This is the content.
</info added on 2025-04-16T18:49:35.663Z>"""
    cleaned = update_all_tasks.clean_details(test_details)
    assert cleaned == "This is the content."


def test_extract_task_info():
    """Test extract_task_info function."""
    test_task_content = """# Task 1: Test Task

**Status:** pending

**Description:** This is a test task.

## Details

Task details here.
"""
    task_info = update_all_tasks.extract_task_info(test_task_content)
    expected_info = {
        "title": "Test Task",
        "status": "pending",
        "description": "This is a test task.",
    }
    assert task_info == expected_info


def test_extract_subtask_info():
    """Test extract_subtask_info function."""
    test_subtask_content = """# Subtask 1.1: Test Subtask

**Status:** pending

**Dependencies:** 1, 2

**Description:** This is a test subtask.

## Details

Subtask details here.
"""
    subtask_info = update_all_tasks.extract_subtask_info(test_subtask_content)
    expected_info = {
        "title": "Test Subtask",
        "status": "pending",
        "dependencies": ["1", "2"],
        "description": "This is a test subtask.",
    }
    assert subtask_info == expected_info


def test_load_tasks_json(temp_test_env):
    """Test load_tasks_json function."""
    tasks_data, error = update_all_tasks.load_tasks_json()
    assert tasks_data is not None
    assert error is None
    assert len(tasks_data["tasks"]) == 2


def test_update_task_test_mode(temp_test_env):
    """Test update_task function in test mode."""
    tasks_data, error = update_all_tasks.load_tasks_json()
    assert tasks_data is not None, f"Failed to load tasks.json: {error}"

    task = tasks_data["tasks"][0]
    updated, updated_fields = update_all_tasks.update_task(
        task, 1, test_mode=True
    )

    assert updated is True
    assert "title" in updated_fields
    assert "status" in updated_fields
    assert "description" in updated_fields
    assert "details" in updated_fields
    assert "subtask_1.title" in updated_fields
    assert "subtask_1.status" in updated_fields
    assert "subtask_1.description" in updated_fields
    assert "subtask_1.details" in updated_fields

    # Verify no changes were made in test mode
    assert task["title"] == "Original Task 1"
    assert task["status"] == "pending"


def test_update_task_real_mode(temp_test_env):
    """Test update_task function in real mode."""
    tasks_data, error = update_all_tasks.load_tasks_json()
    assert tasks_data is not None, f"Failed to load tasks.json: {error}"

    task = tasks_data["tasks"][0]
    updated, updated_fields = update_all_tasks.update_task(
        task, 1, test_mode=False
    )

    assert updated is True
    assert "title" in updated_fields
    assert "status" in updated_fields
    assert "description" in updated_fields
    assert "details" in updated_fields

    # Verify changes were made in real mode
    assert task["title"] == "Updated Task 1"
    assert task["status"] == "done"
    assert task["description"] == "Updated description 1"
    assert task["details"] == "Updated details 1"

    # Verify subtask changes
    subtask = task["subtasks"][0]
    assert subtask["title"] == "Updated Subtask 1.1"
    assert subtask["status"] == "done"
    assert subtask["description"] == "Updated subtask description 1.1"
    assert subtask["details"] == "Updated subtask details 1.1"


def test_update_all_tasks_test_mode(temp_test_env):
    """Test update_all_tasks function in test mode."""
    # First verify tasks.json exists and is valid
    tasks_data, error = update_all_tasks.load_tasks_json()
    assert tasks_data is not None, f"Failed to load tasks.json: {error}"

    success, updated_tasks = update_all_tasks.update_all_tasks(test_mode=True)

    assert success is True
    # The number of updated tasks may vary depending on the test environment
    assert len(updated_tasks) >= 1  # At least task 1 should be updated
    assert 1 in updated_tasks

    # Verify no changes were made to tasks.json
    with open(
        temp_test_env["tasks_dir"] / "tasks.json", "r", encoding="utf-8"
    ) as f:
        tasks_data = json.load(f)

    task = tasks_data["tasks"][0]
    assert task["title"] == "Original Task 1"
    assert task["status"] == "pending"


def test_update_all_tasks_real_mode(temp_test_env):
    """Test update_all_tasks function in real mode."""
    # First verify tasks.json exists and is valid
    tasks_data, error = update_all_tasks.load_tasks_json()
    assert tasks_data is not None, f"Failed to load tasks.json: {error}"

    success, updated_tasks = update_all_tasks.update_all_tasks()

    assert success is True
    assert len(updated_tasks) == 1  # Only task 1 should be updated
    assert 1 in updated_tasks

    # Verify changes were made to tasks.json
    with open(
        temp_test_env["tasks_dir"] / "tasks.json", "r", encoding="utf-8"
    ) as f:
        tasks_data = json.load(f)

    task = tasks_data["tasks"][0]
    assert task["title"] == "Updated Task 1"
    assert task["status"] == "done"
    assert task["description"] == "Updated description 1"
    assert task["details"] == "Updated details 1"

    # Verify task 2 was not changed
    task2 = tasks_data["tasks"][1]
    assert task2["title"] == "Original Task 2"
    assert task2["status"] == "pending"


def test_update_with_range(temp_test_env):
    """Test update_all_tasks function with a specific range."""
    # First verify tasks.json exists and is valid
    tasks_data, error = update_all_tasks.load_tasks_json()
    assert tasks_data is not None, f"Failed to load tasks.json: {error}"

    # Update only task 2
    success, updated_tasks = update_all_tasks.update_all_tasks(
        start_id=2, end_id=2
    )

    assert success is True
    assert len(updated_tasks) == 0  # Task 2 has no changes

    # Verify task 1 was not processed
    with open(
        temp_test_env["tasks_dir"] / "tasks.json", "r", encoding="utf-8"
    ) as f:
        tasks_data = json.load(f)

    task = tasks_data["tasks"][0]
    assert task["title"] == "Original Task 1"
    assert task["status"] == "pending"


def test_click_interface():
    """Test the Click command-line interface."""
    runner = CliRunner()

    # Test help output
    result = runner.invoke(update_all_tasks.main, ["--help"])
    assert result.exit_code == 0
    assert "Update all Task Master tasks from markdown files" in result.output

    # Test with test mode
    with patch("update_all_tasks.run_tests") as mock_run_tests, patch(
        "update_all_tasks.update_all_tasks"
    ) as mock_update_all_tasks:
        mock_update_all_tasks.return_value = (True, {1: {"details"}})

        result = runner.invoke(update_all_tasks.main, ["--test"])
        assert result.exit_code == 0
        mock_run_tests.assert_called_once()
        mock_update_all_tasks.assert_called_once_with(1, 999, test_mode=True)

    # Test with start-id and end-id
    with patch("update_all_tasks.update_all_tasks") as mock_update_all_tasks:
        mock_update_all_tasks.return_value = (
            True,
            {3: {"details"}, 4: {"title"}},
        )

        result = runner.invoke(
            update_all_tasks.main, ["--start-id", "3", "--end-id", "4"]
        )
        assert result.exit_code == 0
        mock_update_all_tasks.assert_called_once_with(3, 4)


def test_nonexistent_task_directory():
    """Test handling of non-existent task directory."""
    with patch("update_all_tasks.logger") as mock_logger:
        updated, _ = update_all_tasks.update_task({}, 999, test_mode=True)

        assert updated is False
        assert mock_logger.warning.called

        # Use a more flexible assertion that works with different path separators
        warning_msg = mock_logger.warning.call_args[0][0]
        assert "Directory" in warning_msg
        assert "task_999" in warning_msg
        assert "does not exist" in warning_msg


def test_invalid_tasks_json(temp_test_env):
    """Test handling of invalid tasks.json file."""
    # Create invalid JSON file
    with open(
        temp_test_env["tasks_dir"] / "tasks.json", "w", encoding="utf-8"
    ) as f:
        f.write("Invalid JSON")

    tasks_data, error = update_all_tasks.load_tasks_json()

    assert tasks_data is None
    assert error is not None
    assert "Error loading tasks.json" in error
