#!/usr/bin/env python3
"""
Test script for update_all_tasks.py.

This script runs comprehensive tests on the update_all_tasks.py script
to verify its functionality. It creates temporary test files and directories,
runs the script in test mode, and verifies the results.

Usage:
    python test_update_all_tasks.py
"""

import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from click.testing import CliRunner

# Add the parent directory to sys.path to import the module
sys.path.insert(0, str(Path(__file__).parent))

# Import the module to test
import update_all_tasks  # type: ignore


class TestUpdateAllTasks(unittest.TestCase):
    """Test cases for update_all_tasks.py."""

    def setUp(self):
        """Set up test environment."""
        # Create temporary directory
        self.temp_dir = tempfile.mkdtemp()
        self.tasks_dir = Path(self.temp_dir) / "tasks"
        self.docs_dir = self.tasks_dir / "docs"

        # Create directory structure
        self.tasks_dir.mkdir(exist_ok=True)
        self.docs_dir.mkdir(exist_ok=True)

        # Create test task directories
        (self.docs_dir / "task_001").mkdir(exist_ok=True)
        (self.docs_dir / "task_002").mkdir(exist_ok=True)

        # Create test files
        self._create_test_files()

        # Save original working directory
        self.original_dir = os.getcwd()

        # Change to temporary directory
        os.chdir(self.temp_dir)

    def tearDown(self):
        """Clean up after tests."""
        # Change back to original directory
        os.chdir(self.original_dir)

        # Remove temporary directory
        shutil.rmtree(self.temp_dir)

    def _create_tasks_json(self):
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

        with open(self.tasks_dir / "tasks.json", "w", encoding="utf-8") as f:
            json.dump(tasks_json, f, indent=2)

    def _create_task1_files(self):
        """Create markdown files for task 1."""
        # Create overview.md for task 1
        overview_content = """# Task 1: Updated Task 1

**Status:** done

**Description:** Updated description 1

## Details

Updated details 1
"""
        with open(
            self.docs_dir / "task_001" / "overview.md", "w", encoding="utf-8"
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
            self.docs_dir / "task_001" / "subtask_001.md",
            "w",
            encoding="utf-8",
        ) as f:
            f.write(subtask_content)

    def _create_task2_files(self):
        """Create markdown files for task 2."""
        # Create overview.md for task 2 (no changes)
        overview_content = """# Task 2: Original Task 2

**Status:** pending

**Description:** Original description 2

## Details

Original details 2
"""
        with open(
            self.docs_dir / "task_002" / "overview.md", "w", encoding="utf-8"
        ) as f:
            f.write(overview_content)

    def _create_test_files(self):
        """Create test files for testing."""
        self._create_tasks_json()
        self._create_task1_files()
        self._create_task2_files()

    def test_extract_markdown_content(self):
        """Test extract_markdown_content function."""
        test_content = """# Test Task

## Details

This is the details section.

## Another Section

This is another section.
"""
        details = update_all_tasks.extract_markdown_content(test_content)
        self.assertEqual(details, "This is the details section.")

    def test_clean_details(self):
        """Test clean_details function."""
        test_details = """<info added on 2025-04-16T18:49:35.663Z>
This is the content.
</info added on 2025-04-16T18:49:35.663Z>"""
        cleaned = update_all_tasks.clean_details(test_details)
        self.assertEqual(cleaned, "This is the content.")

    def test_extract_task_info(self):
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
        self.assertEqual(task_info, expected_info)

    def test_extract_subtask_info(self):
        """Test extract_subtask_info function."""
        test_subtask_content = """# Subtask 1.1: Test Subtask

**Status:** pending

**Dependencies:** 1, 2

**Description:** This is a test subtask.

## Details

Subtask details here.
"""
        subtask_info = update_all_tasks.extract_subtask_info(
            test_subtask_content
        )
        expected_info = {
            "title": "Test Subtask",
            "status": "pending",
            "dependencies": ["1", "2"],
            "description": "This is a test subtask.",
        }
        self.assertEqual(subtask_info, expected_info)

    def test_load_tasks_json(self):
        """Test load_tasks_json function."""
        tasks_data, error = update_all_tasks.load_tasks_json()
        self.assertIsNotNone(tasks_data)
        self.assertIsNone(error)
        self.assertEqual(len(tasks_data["tasks"]), 2)

    def test_update_task_test_mode(self):
        """Test update_task function in test mode."""
        tasks_data, _ = update_all_tasks.load_tasks_json()
        task = tasks_data["tasks"][0]
        updated, updated_fields = update_all_tasks.update_task(
            task, 1, test_mode=True
        )

        self.assertTrue(updated)
        self.assertIn("title", updated_fields)
        self.assertIn("status", updated_fields)
        self.assertIn("description", updated_fields)
        self.assertIn("details", updated_fields)
        self.assertIn("subtask_1.title", updated_fields)
        self.assertIn("subtask_1.status", updated_fields)
        self.assertIn("subtask_1.description", updated_fields)
        self.assertIn("subtask_1.details", updated_fields)

        # Verify no changes were made in test mode
        self.assertEqual(task["title"], "Original Task 1")
        self.assertEqual(task["status"], "pending")

    def test_update_task_real_mode(self):
        """Test update_task function in real mode."""
        tasks_data, _ = update_all_tasks.load_tasks_json()
        task = tasks_data["tasks"][0]
        updated, updated_fields = update_all_tasks.update_task(
            task, 1, test_mode=False
        )

        self.assertTrue(updated)
        self.assertIn("title", updated_fields)
        self.assertIn("status", updated_fields)
        self.assertIn("description", updated_fields)
        self.assertIn("details", updated_fields)

        # Verify changes were made in real mode
        self.assertEqual(task["title"], "Updated Task 1")
        self.assertEqual(task["status"], "done")
        self.assertEqual(task["description"], "Updated description 1")
        self.assertEqual(task["details"], "Updated details 1")

        # Verify subtask changes
        subtask = task["subtasks"][0]
        self.assertEqual(subtask["title"], "Updated Subtask 1.1")
        self.assertEqual(subtask["status"], "done")
        self.assertEqual(
            subtask["description"], "Updated subtask description 1.1"
        )
        self.assertEqual(subtask["details"], "Updated subtask details 1.1")

    def test_update_all_tasks_test_mode(self):
        """Test update_all_tasks function in test mode."""
        success, updated_tasks = update_all_tasks.update_all_tasks(
            test_mode=True
        )

        self.assertTrue(success)
        # The number of updated tasks may vary depending on the test environment
        self.assertGreaterEqual(
            len(updated_tasks), 1
        )  # At least task 1 should be updated
        self.assertIn(1, updated_tasks)

        # Verify no changes were made to tasks.json
        with open(self.tasks_dir / "tasks.json", "r", encoding="utf-8") as f:
            tasks_data = json.load(f)

        task = tasks_data["tasks"][0]
        self.assertEqual(task["title"], "Original Task 1")
        self.assertEqual(task["status"], "pending")

    def test_update_all_tasks_real_mode(self):
        """Test update_all_tasks function in real mode."""
        success, updated_tasks = update_all_tasks.update_all_tasks()

        self.assertTrue(success)
        self.assertEqual(
            len(updated_tasks), 1
        )  # Only task 1 should be updated
        self.assertIn(1, updated_tasks)

        # Verify changes were made to tasks.json
        with open(self.tasks_dir / "tasks.json", "r", encoding="utf-8") as f:
            tasks_data = json.load(f)

        task = tasks_data["tasks"][0]
        self.assertEqual(task["title"], "Updated Task 1")
        self.assertEqual(task["status"], "done")
        self.assertEqual(task["description"], "Updated description 1")
        self.assertEqual(task["details"], "Updated details 1")

        # Verify task 2 was not changed
        task2 = tasks_data["tasks"][1]
        self.assertEqual(task2["title"], "Original Task 2")
        self.assertEqual(task2["status"], "pending")

    def test_update_with_range(self):
        """Test update_all_tasks function with a specific range."""
        # Update only task 2
        success, updated_tasks = update_all_tasks.update_all_tasks(
            start_id=2, end_id=2
        )

        self.assertTrue(success)
        self.assertEqual(len(updated_tasks), 0)  # Task 2 has no changes

        # Verify task 1 was not processed
        with open(self.tasks_dir / "tasks.json", "r", encoding="utf-8") as f:
            tasks_data = json.load(f)

        task = tasks_data["tasks"][0]
        self.assertEqual(task["title"], "Original Task 1")
        self.assertEqual(task["status"], "pending")

    def test_click_interface(self):
        """Test the Click command-line interface."""
        runner = CliRunner()

        # Test help output
        result = runner.invoke(update_all_tasks.main, ["--help"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(
            "Update all Task Master tasks from markdown files", result.output
        )

        # Test with test mode
        with patch("update_all_tasks.run_tests") as mock_run_tests, patch(
            "update_all_tasks.update_all_tasks"
        ) as mock_update_all_tasks:
            mock_update_all_tasks.return_value = (True, {1: {"details"}})

            result = runner.invoke(update_all_tasks.main, ["--test"])
            self.assertEqual(result.exit_code, 0)
            mock_run_tests.assert_called_once()
            mock_update_all_tasks.assert_called_once_with(
                1, 999, test_mode=True
            )

        # Test with start-id and end-id
        with patch(
            "update_all_tasks.update_all_tasks"
        ) as mock_update_all_tasks:
            mock_update_all_tasks.return_value = (
                True,
                {3: {"details"}, 4: {"title"}},
            )

            result = runner.invoke(
                update_all_tasks.main, ["--start-id", "3", "--end-id", "4"]
            )
            self.assertEqual(result.exit_code, 0)
            mock_update_all_tasks.assert_called_once_with(3, 4)

    def test_nonexistent_task_directory(self):
        """Test handling of non-existent task directory."""
        with patch("update_all_tasks.logger") as mock_logger:
            updated, _ = update_all_tasks.update_task({}, 999, test_mode=True)

            self.assertFalse(updated)
            self.assertTrue(mock_logger.warning.called)

            # Use a more flexible assertion that works with different path separators
            warning_msg = mock_logger.warning.call_args[0][0]
            self.assertIn("Directory", warning_msg)
            self.assertIn("task_999", warning_msg)
            self.assertIn("does not exist", warning_msg)

    def test_invalid_tasks_json(self):
        """Test handling of invalid tasks.json file."""
        # Create invalid JSON file
        with open(self.tasks_dir / "tasks.json", "w", encoding="utf-8") as f:
            f.write("Invalid JSON")

        tasks_data, error = update_all_tasks.load_tasks_json()

        self.assertIsNone(tasks_data)
        self.assertIsNotNone(error)
        self.assertIn("Error loading tasks.json", error)


if __name__ == "__main__":
    unittest.main()
