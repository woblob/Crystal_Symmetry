#!/usr/bin/env python3
"""
Update all Task Master tasks from markdown files.

This script updates all tasks in tasks.json based on markdown files in the tasks/docs/ directory.
It can be used to ensure that all task details are consistent with their markdown documentation.

Features:
- Updates all tasks at once (or a specified range of tasks)
- Provides detailed logging of changes
- Includes test mode to verify functionality without making changes
- Compatible with existing task management scripts

Usage:
    python update_all_tasks.py [options]

Options:
    --start-id <id>    Start updating from this task ID (inclusive)
    --end-id <id>      Stop updating at this task ID (inclusive)
    --test             Run in test mode without making changes
    --verbose          Show detailed logging
    --help             Show this help message

Example:
    python update_all_tasks.py
    python update_all_tasks.py --start-id 3 --end-id 5
    python update_all_tasks.py --test --verbose
"""

import json
import logging
import re
import sys
from pathlib import Path
from typing import Any, Dict, Optional, Set, Tuple

import click

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def setup_logging(verbose: bool) -> None:
    """Configure logging level based on verbosity."""
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)


def read_markdown_file(file_path: Path) -> Optional[str]:
    """Read content from a markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")
        return None


def extract_markdown_content(
    content: str, section_name: str = "Details"
) -> Optional[str]:
    """Extract content from a specific section in markdown."""
    if not content:
        return None

    try:
        # Find the section
        pattern = rf"^## {section_name}\s*$(.*?)(?:^##\s|\Z)"
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

        if match:
            return match.group(1).strip()
        return None
    except Exception as e:
        logger.error(f"Error extracting markdown content: {e}")
        return None


def extract_task_info(content: str) -> Dict[str, Any]:
    """Extract basic task information from markdown content."""
    info = {}

    try:
        # Extract title
        title_match = re.search(r"^# (Task \d+: .+)$", content, re.MULTILINE)
        if title_match:
            info["title"] = re.sub(r"^Task \d+: ", "", title_match.group(1))

        # Extract status
        status_match = re.search(r"\*\*Status:\*\* (\w+)", content)
        if status_match:
            info["status"] = status_match.group(1).lower()

        # Extract description
        desc_match = re.search(
            r"\*\*Description:\*\* (.+?)(?:\n\n|\Z)", content, re.DOTALL
        )
        if desc_match:
            info["description"] = desc_match.group(1).strip()

        return info
    except Exception as e:
        logger.error(f"Error extracting task info: {e}")
        return {}


def extract_subtask_info(content: str) -> Dict[str, Any]:
    """Extract subtask information from markdown content."""
    info: Dict[str, Any] = {}

    try:
        # Extract title
        title_match = re.search(
            r"^# (Subtask \d+\.\d+: .+)$", content, re.MULTILINE
        )
        if title_match:
            info["title"] = re.sub(
                r"^Subtask \d+\.\d+: ", "", title_match.group(1)
            )

        # Extract status
        status_match = re.search(r"\*\*Status:\*\* (\w+)", content)
        if status_match:
            info["status"] = status_match.group(1).lower()

        # Extract dependencies
        deps_match = re.search(
            r"\*\*Dependencies:\*\* (.+?)(?:\n\n|\Z)", content
        )
        if deps_match:
            deps_text = deps_match.group(1).strip()
            if deps_text.lower() == "none":
                info["dependencies"] = []
            else:
                info["dependencies"] = [
                    dep.strip() for dep in deps_text.split(",")
                ]

        # Extract description
        desc_match = re.search(
            r"\*\*Description:\*\* (.+?)(?:\n\n|\Z)", content, re.DOTALL
        )
        if desc_match:
            info["description"] = desc_match.group(1).strip()

        return info
    except Exception as e:
        logger.error(f"Error extracting subtask info: {e}")
        return {}


def clean_details(details: str) -> str:
    """Remove timestamp tags from details content."""
    if not details:
        return details

    try:
        # Check if the details contain timestamp tags
        if "<info added on" in details and "</info added on" in details:
            # Extract the content between the tags
            pattern = r"<info added on[^>]*>(.*?)</info added on[^>]*>"
            matches = re.findall(pattern, details, re.DOTALL)

            if matches:
                # Join all content between tags
                content = "\n\n".join(match.strip() for match in matches)
                return content

        return details
    except Exception as e:
        logger.error(f"Error cleaning details: {e}")
        return details


def load_tasks_json() -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """Load tasks.json file."""
    tasks_json_path = Path("tasks/tasks.json")

    if not tasks_json_path.exists():
        error_msg = f"Error: File {tasks_json_path} does not exist."
        logger.error(error_msg)
        return None, error_msg

    try:
        with open(tasks_json_path, "r", encoding="utf-8") as f:
            tasks_data = json.load(f)
        return tasks_data, None
    except Exception as e:
        error_msg = f"Error loading tasks.json: {e}"
        logger.error(error_msg)
        return None, error_msg


def save_tasks_json(
    tasks_data: Dict[str, Any], test_mode: bool = False
) -> Tuple[bool, Optional[str]]:
    """Save tasks.json file."""
    tasks_json_path = Path("tasks/tasks.json")

    if test_mode:
        logger.info("Test mode: Not saving changes to tasks.json")
        return True, None

    try:
        with open(tasks_json_path, "w", encoding="utf-8") as f:
            json.dump(tasks_data, f, indent=2)
        logger.info("Successfully saved tasks.json")
        return True, None
    except Exception as e:
        error_msg = f"Error saving tasks.json: {e}"
        logger.error(error_msg)
        return False, error_msg


def update_task_details(
    task: Dict[str, Any],
    task_id: int,
    details_content: Optional[str],
    test_mode: bool,
    updated_fields: Set[str],
) -> None:
    """Update task details if they've changed."""
    if not details_content:
        return

    if test_mode or task.get("details") != details_content:
        if not test_mode:
            task["details"] = details_content
        updated_fields.add("details")
        logger.debug(f"Updated details for task {task_id}")


def update_task_info(
    task: Dict[str, Any],
    task_id: int,
    task_info: Dict[str, Any],
    test_mode: bool,
    updated_fields: Set[str],
) -> None:
    """Update task info fields if they've changed."""
    for key, value in task_info.items():
        if not value:
            continue

        if test_mode or task.get(key) != value:
            if not test_mode:
                task[key] = value
            updated_fields.add(key)
            logger.debug(f"Updated {key} for task {task_id}")


def update_subtask_details(
    subtask: Dict[str, Any],
    task_id: int,
    subtask_id: int,
    details_content: Optional[str],
    test_mode: bool,
    updated_fields: Set[str],
) -> None:
    """Update subtask details if they've changed."""
    if not details_content:
        return

    if test_mode or subtask.get("details") != details_content:
        if not test_mode:
            subtask["details"] = details_content
        updated_fields.add(f"subtask_{subtask_id}.details")
        logger.debug(f"Updated details for subtask {task_id}.{subtask_id}")


def update_subtask_info(
    subtask: Dict[str, Any],
    task_id: int,
    subtask_id: int,
    subtask_info: Dict[str, Any],
    test_mode: bool,
    updated_fields: Set[str],
) -> None:
    """Update subtask info fields if they've changed."""
    for key, value in subtask_info.items():
        if not value:
            continue

        if test_mode or subtask.get(key) != value:
            if not test_mode:
                subtask[key] = value
            updated_fields.add(f"subtask_{subtask_id}.{key}")
            logger.debug(f"Updated {key} for subtask {task_id}.{subtask_id}")


def clean_subtask_details(
    subtask: Dict[str, Any],
    task_id: int,
    subtask_id: int,
    test_mode: bool,
    updated_fields: Set[str],
) -> None:
    """Clean timestamp tags from subtask details."""
    original_details = subtask.get("details", "")
    cleaned_details = clean_details(original_details)

    if cleaned_details == original_details:
        return

    if not test_mode:
        subtask["details"] = cleaned_details
    updated_fields.add(f"subtask_{subtask_id}.details")
    logger.debug(f"Cleaned details for subtask {task_id}.{subtask_id}")


def process_subtask(
    subtask: Dict[str, Any],
    task_id: int,
    task_dir: Path,
    test_mode: bool,
    updated_fields: Set[str],
) -> None:
    """Process a single subtask."""
    subtask_id = subtask.get("id")
    if subtask_id is None:
        return

    subtask_path = task_dir / f"subtask_{subtask_id:03d}.md"
    if not subtask_path.exists():
        clean_subtask_details(
            subtask, task_id, subtask_id, test_mode, updated_fields
        )
        return

    subtask_content = read_markdown_file(subtask_path)
    if not subtask_content:
        clean_subtask_details(
            subtask, task_id, subtask_id, test_mode, updated_fields
        )
        return

    # Process subtask content
    subtask_info = extract_subtask_info(subtask_content)
    details_content = extract_markdown_content(subtask_content)

    update_subtask_details(
        subtask,
        task_id,
        subtask_id,
        details_content,
        test_mode,
        updated_fields,
    )
    update_subtask_info(
        subtask, task_id, subtask_id, subtask_info, test_mode, updated_fields
    )


def update_task(
    task: Dict[str, Any], task_id: int, test_mode: bool = False
) -> Tuple[bool, Set[str]]:
    """Update a task and its subtasks from markdown files."""
    task_dir = Path(f"tasks/docs/task_{task_id:03d}")
    updated_fields: Set[str] = set()

    if not task_dir.exists():
        logger.warning(
            f"Directory {task_dir} does not exist. Skipping task {task_id}."
        )
        return False, updated_fields

    # Process overview.md if it exists
    overview_path = task_dir / "overview.md"
    if overview_path.exists():
        overview_content = read_markdown_file(overview_path)
        if overview_content:
            task_info = extract_task_info(overview_content)
            details_content = extract_markdown_content(overview_content)

            update_task_details(
                task, task_id, details_content, test_mode, updated_fields
            )
            update_task_info(
                task, task_id, task_info, test_mode, updated_fields
            )

    # Process all subtasks
    for subtask in task.get("subtasks", []):
        process_subtask(subtask, task_id, task_dir, test_mode, updated_fields)

    return len(updated_fields) > 0, updated_fields


def update_all_tasks(
    start_id: int = 1, end_id: int = 999, test_mode: bool = False
) -> Tuple[bool, Dict[int, Set[str]]]:
    """Update all tasks in the specified range."""
    tasks_data, error = load_tasks_json()
    if not tasks_data:
        return False, {}

    updated_tasks = {}
    tasks_updated = False

    # Process each task in the specified range
    for task in tasks_data.get("tasks", []):
        task_id = task.get("id")
        if task_id is None or not (start_id <= task_id <= end_id):
            continue

        logger.info(f"Processing task {task_id}...")
        updated, updated_fields = update_task(task, task_id, test_mode)

        if not updated:
            logger.info(f"No updates needed for task {task_id}")
            continue

        updated_tasks[task_id] = updated_fields
        tasks_updated = True
        logger.info(f"Task {task_id} updated: {', '.join(updated_fields)}")

    # Save changes if needed
    if not tasks_updated or test_mode:
        return True, updated_tasks

    success, error = save_tasks_json(tasks_data, test_mode)
    if not success:
        return False, updated_tasks

    return True, updated_tasks


def run_tests() -> bool:
    """Run tests to verify script functionality."""
    logger.info("Running tests...")
    all_tests_passed = True

    # Test 1: Load tasks.json
    logger.info("Test 1: Loading tasks.json")
    tasks_data, error = load_tasks_json()
    if not tasks_data:
        logger.error("Test 1 failed: Could not load tasks.json")
        return False
    logger.info("Test 1 passed: Successfully loaded tasks.json")

    # Test 2: Extract markdown content
    logger.info("Test 2: Extracting markdown content")
    test_content = """# Test Task

## Details

This is the details section.

## Another Section

This is another section.
"""
    details = extract_markdown_content(test_content)
    if details != "This is the details section.":
        logger.error(
            f"Test 2 failed: Extracted content does not match expected. Got: {details}"
        )
        all_tests_passed = False
    else:
        logger.info("Test 2 passed: Successfully extracted markdown content")

    # Test 3: Clean details
    logger.info("Test 3: Cleaning details")
    test_details = """<info added on 2025-04-16T18:49:35.663Z>
This is the content.
</info added on 2025-04-16T18:49:35.663Z>"""
    cleaned = clean_details(test_details)
    if cleaned != "This is the content.":
        logger.error(
            f"Test 3 failed: Cleaned content does not match expected. Got: {cleaned}"
        )
        all_tests_passed = False
    else:
        logger.info("Test 3 passed: Successfully cleaned details")

    # Test 4: Extract task info
    logger.info("Test 4: Extracting task info")
    test_task_content = """# Task 1: Test Task

**Status:** pending

**Description:** This is a test task.

## Details

Task details here.
"""
    task_info = extract_task_info(test_task_content)
    expected_info = {
        "title": "Test Task",
        "status": "pending",
        "description": "This is a test task.",
    }
    if task_info != expected_info:
        logger.error(
            f"Test 4 failed: Extracted task info does not match expected. Got: {task_info}"
        )
        all_tests_passed = False
    else:
        logger.info("Test 4 passed: Successfully extracted task info")

    # Test 5: Extract subtask info
    logger.info("Test 5: Extracting subtask info")
    test_subtask_content = """# Subtask 1.1: Test Subtask

**Status:** pending

**Dependencies:** 1, 2

**Description:** This is a test subtask.

## Details

Subtask details here.
"""
    subtask_info = extract_subtask_info(test_subtask_content)
    expected_subtask_info: Dict[str, Any] = {
        "title": "Test Subtask",
        "status": "pending",
        "dependencies": ["1", "2"],
        "description": "This is a test subtask.",
    }
    if subtask_info != expected_subtask_info:
        logger.error(
            f"Test 5 failed: Extracted subtask info does not match expected. Got: {subtask_info}. Expected: {expected_subtask_info}"
        )
        all_tests_passed = False
    else:
        logger.info("Test 5 passed: Successfully extracted subtask info")

    # Test 6: Test mode update
    logger.info("Test 6: Testing update in test mode")
    success, updated_tasks = update_all_tasks(test_mode=True)
    if not success:
        logger.error("Test 6 failed: Update in test mode failed")
        all_tests_passed = False
    else:
        logger.info(
            f"Test 6 passed: Successfully tested update in test mode. Would update: {updated_tasks}"
        )

    if all_tests_passed:
        logger.info("All tests passed!")
    else:
        logger.error("Some tests failed!")

    return all_tests_passed


@click.command()
@click.option(
    "--start-id",
    type=int,
    default=1,
    help="Start updating from this task ID (inclusive)",
)
@click.option(
    "--end-id",
    type=int,
    default=999,
    help="Stop updating at this task ID (inclusive)",
)
@click.option(
    "--test",
    is_flag=True,
    help="Run in test mode without making changes",
)
@click.option(
    "--verbose",
    is_flag=True,
    help="Show detailed logging",
)
def main(start_id: int, end_id: int, test: bool, verbose: bool) -> None:
    """Update all Task Master tasks from markdown files.

    This script updates all tasks in tasks.json based on markdown files in the tasks/docs/ directory.
    It can be used to ensure that all task details are consistent with their markdown documentation.
    """
    setup_logging(verbose)

    if test:
        click.echo("Running in test mode - no changes will be made")
        run_tests()
        success, updated_tasks = update_all_tasks(
            start_id, end_id, test_mode=True
        )
        if success:
            if updated_tasks:
                click.echo(
                    f"Test successful. Would update {len(updated_tasks)} tasks:"
                )
                for task_id, fields in updated_tasks.items():
                    click.echo(f"  Task {task_id}: {', '.join(fields)}")
            else:
                click.echo("Test successful. No tasks would be updated.")
        else:
            click.echo("Test failed. See above for errors.", err=True)
            sys.exit(1)
    else:
        success, updated_tasks = update_all_tasks(start_id, end_id)
        if success:
            if updated_tasks:
                click.echo(f"Successfully updated {len(updated_tasks)} tasks:")
                for task_id, fields in updated_tasks.items():
                    click.echo(f"  Task {task_id}: {', '.join(fields)}")
            else:
                click.echo("No tasks needed updating.")
        else:
            click.echo("Update failed. See above for errors.", err=True)
            sys.exit(1)


if __name__ == "__main__":
    main(
        start_id=1,
        end_id=999,
        test=False,
        verbose=False,
    )
