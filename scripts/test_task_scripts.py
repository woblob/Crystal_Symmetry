#!/usr/bin/env python3
"""
Test script for task_splitter.py and task_merger.py

This script tests the functionality of the task_splitter.py and task_merger.py scripts
by creating a temporary test environment, running the scripts, and verifying the results.

Usage:
    python test_task_scripts.py
"""

import json
import os
import shutil
import sys
import tempfile
from pathlib import Path
import logging
import pytest
from typing import Dict, Any, List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# Add the parent directory to sys.path to import the modules
sys.path.insert(0, str(Path(__file__).parent))

# Import the modules to test
import task_splitter
import task_merger


@pytest.fixture
def temp_test_env():
    """Create a temporary test environment with a sample tasks.json file."""
    # Create temporary directory
    temp_dir = tempfile.mkdtemp()
    tasks_dir = Path(temp_dir) / "tasks"
    tasks_dir.mkdir(exist_ok=True)
    
    # Create sample tasks.json file
    tasks_json = {
        "metadata": {
            "projectName": "Test Project",
            "projectVersion": "1.0.0",
            "description": "Test project for task scripts",
            "author": "Test Author",
            "dateCreated": "2023-01-01",
            "dateUpdated": "2023-01-15"
        },
        "tasks": [
            {
                "id": 1,
                "title": "Task 1",
                "description": "Description for task 1",
                "status": "pending",
                "priority": "high",
                "dependencies": [2],
                "details": "Details for task 1",
                "testStrategy": "Test strategy for task 1",
                "subtasks": [
                    {
                        "id": 1,
                        "title": "Subtask 1.1",
                        "description": "Description for subtask 1.1",
                        "status": "pending",
                        "dependencies": [],
                        "parentTaskId": 1,
                        "details": "Details for subtask 1.1"
                    },
                    {
                        "id": 2,
                        "title": "Subtask 1.2",
                        "description": "Description for subtask 1.2",
                        "status": "pending",
                        "dependencies": [1],
                        "parentTaskId": 1,
                        "details": "Details for subtask 1.2"
                    }
                ]
            },
            {
                "id": 2,
                "title": "Task 2",
                "description": "Description for task 2",
                "status": "done",
                "priority": "medium",
                "dependencies": [],
                "details": "Details for task 2",
                "testStrategy": "Test strategy for task 2",
                "subtasks": [
                    {
                        "id": 1,
                        "title": "Subtask 2.1",
                        "description": "Description for subtask 2.1",
                        "status": "done",
                        "dependencies": [],
                        "parentTaskId": 2,
                        "details": "Details for subtask 2.1"
                    }
                ]
            }
        ]
    }
    
    with open(tasks_dir / "tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks_json, f, indent=2)
    
    # Save original working directory
    original_dir = os.getcwd()
    
    # Change to temporary directory
    os.chdir(temp_dir)
    
    # Yield the test environment
    yield {
        "temp_dir": temp_dir,
        "tasks_dir": tasks_dir,
        "original_dir": original_dir,
        "tasks_json": tasks_json
    }
    
    # Clean up after tests
    os.chdir(original_dir)
    shutil.rmtree(temp_dir)


def compare_json_objects(obj1: Dict[str, Any], obj2: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Compare two JSON objects and return a list of differences."""
    differences = []
    
    # Check if both are dictionaries
    if not isinstance(obj1, dict) or not isinstance(obj2, dict):
        return False, ["Objects are not both dictionaries"]
    
    # Check keys
    keys1 = set(obj1.keys())
    keys2 = set(obj2.keys())
    
    if keys1 != keys2:
        missing_keys = keys1 - keys2
        extra_keys = keys2 - keys1
        if missing_keys:
            differences.append(f"Missing keys in second object: {missing_keys}")
        if extra_keys:
            differences.append(f"Extra keys in second object: {extra_keys}")
    
    # Check values for common keys
    for key in keys1.intersection(keys2):
        if isinstance(obj1[key], dict) and isinstance(obj2[key], dict):
            # Recursively compare dictionaries
            equal, sub_differences = compare_json_objects(obj1[key], obj2[key])
            if not equal:
                differences.extend([f"{key}.{diff}" for diff in sub_differences])
        elif isinstance(obj1[key], list) and isinstance(obj2[key], list):
            # Compare lists
            if len(obj1[key]) != len(obj2[key]):
                differences.append(f"List length mismatch for key '{key}': {len(obj1[key])} vs {len(obj2[key])}")
            else:
                for i, (item1, item2) in enumerate(zip(obj1[key], obj2[key])):
                    if isinstance(item1, dict) and isinstance(item2, dict):
                        equal, sub_differences = compare_json_objects(item1, item2)
                        if not equal:
                            differences.extend([f"{key}[{i}].{diff}" for diff in sub_differences])
                    elif item1 != item2:
                        differences.append(f"Value mismatch for key '{key}[{i}]': {item1} vs {item2}")
        elif obj1[key] != obj2[key]:
            differences.append(f"Value mismatch for key '{key}': {obj1[key]} vs {obj2[key]}")
    
    return len(differences) == 0, differences


def test_task_splitter(temp_test_env):
    """Test the task_splitter.py script."""
    # Set up test parameters
    input_file = temp_test_env["tasks_dir"] / "tasks.json"
    output_dir = "test_split"
    
    # Run task_splitter
    task_splitter.setup_logging("INFO")
    tasks_data, error = task_splitter.load_tasks_json(str(input_file))
    assert tasks_data is not None, f"Failed to load tasks.json: {error}"
    
    paths, error = task_splitter.create_directory_structure(output_dir)
    assert error is None, f"Failed to create directory structure: {error}"
    
    tasks_processed, subtasks_processed, errors = task_splitter.process_tasks(tasks_data, paths)
    
    # Verify results
    assert tasks_processed == 2, f"Expected 2 tasks processed, got {tasks_processed}"
    assert subtasks_processed == 3, f"Expected 3 subtasks processed, got {subtasks_processed}"
    assert len(errors) == 0, f"Expected no errors, got {errors}"
    
    # Check that files were created
    assert (Path(output_dir) / "metadata.json").exists(), "metadata.json not created"
    assert (Path(output_dir) / "tasks" / "task_001.json").exists(), "task_001.json not created"
    assert (Path(output_dir) / "tasks" / "task_002.json").exists(), "task_002.json not created"
    assert (Path(output_dir) / "subtasks" / "task_001" / "subtask_001.json").exists(), "subtask_001.json not created for task 1"
    assert (Path(output_dir) / "subtasks" / "task_001" / "subtask_002.json").exists(), "subtask_002.json not created for task 1"
    assert (Path(output_dir) / "subtasks" / "task_002" / "subtask_001.json").exists(), "subtask_001.json not created for task 2"
    
    # Check task content
    with open(Path(output_dir) / "tasks" / "task_001.json", "r", encoding="utf-8") as f:
        task1 = json.load(f)
    
    assert task1["id"] == 1, f"Expected task ID 1, got {task1['id']}"
    assert task1["title"] == "Task 1", f"Expected task title 'Task 1', got {task1['title']}"
    assert "subtasks" not in task1, "Task should not contain subtasks field"
    assert "subtask_ids" in task1, "Task should contain subtask_ids field"
    assert task1["subtask_ids"] == [1, 2], f"Expected subtask_ids [1, 2], got {task1['subtask_ids']}"
    
    logger.info("Task splitter test passed")


def test_task_merger(temp_test_env):
    """Test the task_merger.py script."""
    # First run task_splitter to create the split files
    input_file = temp_test_env["tasks_dir"] / "tasks.json"
    split_dir = "test_split"
    merged_file = "test_merged.json"
    
    # Run task_splitter
    task_splitter.setup_logging("INFO")
    tasks_data, error = task_splitter.load_tasks_json(str(input_file))
    assert tasks_data is not None, f"Failed to load tasks.json: {error}"
    
    paths, error = task_splitter.create_directory_structure(split_dir)
    assert error is None, f"Failed to create directory structure: {error}"
    
    tasks_processed, subtasks_processed, errors = task_splitter.process_tasks(tasks_data, paths)
    
    # Now run task_merger
    task_merger.setup_logging("INFO")
    merged_data, errors = task_merger.merge_tasks(split_dir)
    
    assert merged_data is not None, f"Failed to merge tasks: {errors}"
    assert len(errors) == 0, f"Expected no errors, got {errors}"
    
    # Save merged data
    error = task_merger.save_json_file(merged_data, Path(merged_file))
    assert error is None, f"Failed to save merged tasks: {error}"
    
    # Load original and merged data for comparison
    with open(input_file, "r", encoding="utf-8") as f:
        original_data = json.load(f)
    
    with open(merged_file, "r", encoding="utf-8") as f:
        final_data = json.load(f)
    
    # Compare original and merged data
    equal, differences = compare_json_objects(original_data, final_data)
    
    assert equal, f"Original and merged data are not equal: {differences}"
    
    logger.info("Task merger test passed")


def test_full_workflow(temp_test_env):
    """Test the full workflow of splitting and merging tasks."""
    # Set up test parameters
    input_file = temp_test_env["tasks_dir"] / "tasks.json"
    split_dir = "test_full_workflow_split"
    merged_file = "test_full_workflow_merged.json"
    
    # Run task_splitter
    sys.argv = ["task_splitter.py", "--input", str(input_file), "--output", split_dir, "--log-level", "INFO"]
    task_splitter.main()
    
    # Run task_merger
    sys.argv = ["task_merger.py", "--input", split_dir, "--output", merged_file, "--log-level", "INFO"]
    task_merger.main()
    
    # Load original and merged data for comparison
    with open(input_file, "r", encoding="utf-8") as f:
        original_data = json.load(f)
    
    with open(merged_file, "r", encoding="utf-8") as f:
        final_data = json.load(f)
    
    # Compare original and merged data
    equal, differences = compare_json_objects(original_data, final_data)
    
    assert equal, f"Original and merged data are not equal: {differences}"
    
    logger.info("Full workflow test passed")


def main():
    """Run the tests."""
    try:
        # Create a temporary test environment
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a tasks directory
            tasks_dir = Path(temp_dir) / "tasks"
            tasks_dir.mkdir(exist_ok=True)
            
            # Create a sample tasks.json file
            tasks_json = {
                "metadata": {
                    "projectName": "Test Project",
                    "projectVersion": "1.0.0",
                    "description": "Test project for task scripts",
                    "author": "Test Author",
                    "dateCreated": "2023-01-01",
                    "dateUpdated": "2023-01-15"
                },
                "tasks": [
                    {
                        "id": 1,
                        "title": "Task 1",
                        "description": "Description for task 1",
                        "status": "pending",
                        "priority": "high",
                        "dependencies": [2],
                        "details": "Details for task 1",
                        "testStrategy": "Test strategy for task 1",
                        "subtasks": [
                            {
                                "id": 1,
                                "title": "Subtask 1.1",
                                "description": "Description for subtask 1.1",
                                "status": "pending",
                                "dependencies": [],
                                "parentTaskId": 1,
                                "details": "Details for subtask 1.1"
                            },
                            {
                                "id": 2,
                                "title": "Subtask 1.2",
                                "description": "Description for subtask 1.2",
                                "status": "pending",
                                "dependencies": [1],
                                "parentTaskId": 1,
                                "details": "Details for subtask 1.2"
                            }
                        ]
                    },
                    {
                        "id": 2,
                        "title": "Task 2",
                        "description": "Description for task 2",
                        "status": "done",
                        "priority": "medium",
                        "dependencies": [],
                        "details": "Details for task 2",
                        "testStrategy": "Test strategy for task 2",
                        "subtasks": [
                            {
                                "id": 1,
                                "title": "Subtask 2.1",
                                "description": "Description for subtask 2.1",
                                "status": "done",
                                "dependencies": [],
                                "parentTaskId": 2,
                                "details": "Details for subtask 2.1"
                            }
                        ]
                    }
                ]
            }
            
            with open(tasks_dir / "tasks.json", "w", encoding="utf-8") as f:
                json.dump(tasks_json, f, indent=2)
            
            # Save original working directory
            original_dir = os.getcwd()
            
            # Change to temporary directory
            os.chdir(temp_dir)
            
            try:
                # Run the tests
                logger.info("Running task_splitter test...")
                test_env = {
                    "temp_dir": temp_dir,
                    "tasks_dir": tasks_dir,
                    "original_dir": original_dir,
                    "tasks_json": tasks_json
                }
                test_task_splitter(test_env)
                
                logger.info("Running task_merger test...")
                test_task_merger(test_env)
                
                logger.info("Running full workflow test...")
                test_full_workflow(test_env)
                
                logger.info("All tests passed!")
                return 0
            finally:
                # Change back to original directory
                os.chdir(original_dir)
    except Exception as e:
        logger.exception(f"Error running tests: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
