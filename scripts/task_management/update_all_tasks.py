#!/usr/bin/env python3

"""
Update all Task Master tasks from markdown files.

This script updates all tasks in tasks.json based on markdown files in the
tasks/docs/ directory. It ensures task details are consistent with their
markdown documentation.

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
from dataclasses import dataclass
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
    level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(level)


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
        if "<info added on" not in details or "</info added on" not in details:
            return details

        # Extract the content between the tags
        pattern = r"<info added on[^>]*>(.*?)</info added on[^>]*>"
        matches = re.findall(pattern, details, re.DOTALL)

        if not matches:
            return details

        # Join all content between tags
        content = "\n\n".join(match.strip() for match in matches)
        return content
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
    if test_mode:
        logger.info("Test mode: Not saving changes to tasks.json")
        return True, None

    tasks_json_path = Path("tasks/tasks.json")
    try:
        with open(tasks_json_path, "w", encoding="utf-8") as f:
            json.dump(tasks_data, f, indent=2)
        logger.info("Successfully saved tasks.json")
        return True, None
    except Exception as e:
        error_msg = f"Error saving tasks.json: {e}"
        logger.error(error_msg)
        return False, error_msg


@dataclass
class UpdateContext:
    """Context for update operations."""

    test_mode: bool
    updated_fields: Set[str]


def update_field(
    obj: Dict[str, Any],
    field_name: str,
    new_value: Any,
    field_id: str,
    ctx: UpdateContext,
) -> None:
    """Update a field if it's changed."""
    if not new_value:
        return

    if ctx.test_mode or obj.get(field_name) != new_value:
        if not ctx.test_mode:
            obj[field_name] = new_value
        ctx.updated_fields.add(field_id)
        logger.debug(f"Updated {field_id}")


def update_task_details(
    task: Dict[str, Any],
    task_id: int,
    details_content: Optional[str],
    ctx: UpdateContext,
) -> None:
    """Update task details if they've changed."""
    if not details_content:
        return

    field_id = f"task_{task_id}.details"
    update_field(task, "details", details_content, field_id, ctx)


def update_task_info(
    task: Dict[str, Any],
    task_id: int,
    task_info: Dict[str, Any],
    ctx: UpdateContext,
) -> None:
    """Update task info fields if they've changed."""
    for key, value in task_info.items():
        field_id = f"task_{task_id}.{key}"
        update_field(task, key, value, field_id, ctx)


def update_subtask_details(
    subtask: Dict[str, Any],
    subtask_id: int,
    details_content: Optional[str],
    ctx: UpdateContext,
) -> None:
    """Update subtask details if they've changed."""
    if not details_content:
        return

    field_id = f"subtask_{subtask_id}.details"
    update_field(subtask, "details", details_content, field_id, ctx)


def update_subtask_info(
    subtask: Dict[str, Any],
    subtask_id: int,
    subtask_info: Dict[str, Any],
    ctx: UpdateContext,
) -> None:
    """Update subtask info fields if they've changed."""
    for key, value in subtask_info.items():
        field_id = f"subtask_{subtask_id}.{key}"
        update_field(subtask, key, value, field_id, ctx)


def clean_subtask_details(
    subtask: Dict[str, Any], task_id: int, subtask_id: int, ctx: UpdateContext
) -> None:
    """Clean timestamp tags from subtask details."""
    original_details = subtask.get("details", "")
    cleaned_details = clean_details(original_details)

    if cleaned_details == original_details:
        return

    if not ctx.test_mode:
        subtask["details"] = cleaned_details
    ctx.updated_fields.add(f"subtask_{subtask_id}.details")
    logger.debug(f"Cleaned details for subtask {task_id}.{subtask_id}")


def process_subtask(
    subtask: Dict[str, Any], task_id: int, task_dir: Path, ctx: UpdateContext
) -> None:
    """Process a single subtask."""
    subtask_id = subtask.get("id")
    if subtask_id is None:
        return

    subtask_path = task_dir / f"subtask_{subtask_id:03d}.md"
    if not subtask_path.exists():
        clean_subtask_details(subtask, task_id, subtask_id, ctx)
        return

    subtask_content = read_markdown_file(subtask_path)
    if not subtask_content:
        clean_subtask_details(subtask, task_id, subtask_id, ctx)
        return

    # Process subtask content
    subtask_info = extract_subtask_info(subtask_content)
    details_content = extract_markdown_content(subtask_content)

    update_subtask_details(subtask, subtask_id, details_content, ctx)
    update_subtask_info(subtask, subtask_id, subtask_info, ctx)


def update_task(
    task: Dict[str, Any], task_id: int, test_mode: bool = False
) -> Tuple[bool, Set[str]]:
    """Update a task and its subtasks from markdown files."""
    task_dir = Path(f"tasks/docs/task_{task_id:03d}")
    ctx = UpdateContext(test_mode=test_mode, updated_fields=set())

    if not task_dir.exists():
        logger.warning(
            f"Directory {task_dir} does not exist. Skipping task {task_id}."
        )
        return False, ctx.updated_fields

    # Process overview.md if it exists
    overview_path = task_dir / "overview.md"
    if overview_path.exists():
        overview_content = read_markdown_file(overview_path)
        if overview_content:
            task_info = extract_task_info(overview_content)
            details_content = extract_markdown_content(overview_content)

            update_task_details(task, task_id, details_content, ctx)
            update_task_info(task, task_id, task_info, ctx)

    # Process all subtasks
    for subtask in task.get("subtasks", []):
        process_subtask(subtask, task_id, task_dir, ctx)

    return len(ctx.updated_fields) > 0, ctx.updated_fields


def update_all_tasks(
    start_id: int = 1, end_id: int = 999, test_mode: bool = False
) -> Tuple[bool, Dict[int, Set[str]]]:
    """Update all tasks in the specified range."""
    tasks_data, _ = load_tasks_json()
    if not tasks_data:
        return False, {}

    updated_tasks = {}
    tasks_updated = False

    # Process each task in the specified range
    for task in tasks_data.get("tasks", []):
        task_id = task.get("id")
        if task_id is None or not start_id <= task_id <= end_id:
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

    success, _ = save_tasks_json(tasks_data, test_mode)
    if not success:
        return False, updated_tasks

    return True, updated_tasks


def run_test_extract_markdown() -> bool:
    """Test extracting markdown content."""
    logger.info("Testing markdown content extraction")
    test_content = """# Test Task

## Details

This is the details section.

## Another Section

This is another section.
"""
    details = extract_markdown_content(test_content)
    if details != "This is the details section.":
        logger.error(
            "Failed: Extracted content does not match expected. "
            f"Got: {details}"
        )
        return False

    logger.info("Passed: Successfully extracted markdown content")
    return True


def run_test_clean_details() -> bool:
    """Test cleaning details."""
    logger.info("Testing details cleaning")
    test_details = """<info added on 2025-04-16T18:49:35.663Z>
This is the content.
</info added on 2025-04-16T18:49:35.663Z>"""
    cleaned = clean_details(test_details)
    if cleaned != "This is the content.":
        logger.error(
            f"Failed: Cleaned content does not match expected. Got: {cleaned}"
        )
        return False

    logger.info("Passed: Successfully cleaned details")
    return True


def run_test_extract_task_info() -> bool:
    """Test extracting task info."""
    logger.info("Testing task info extraction")
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
            "Failed: Extracted task info does not match expected. "
            f"Got: {task_info}"
        )
        return False

    logger.info("Passed: Successfully extracted task info")
    return True


def run_test_extract_subtask_info() -> bool:
    """Test extracting subtask info."""
    logger.info("Testing subtask info extraction")
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
            "Failed: Extracted subtask info does not match expected. "
            f"Got: {subtask_info}. Expected: {expected_subtask_info}"
        )
        return False

    logger.info("Passed: Successfully extracted subtask info")
    return True


def run_test_update_mode() -> bool:
    """Test update in test mode."""
    logger.info("Testing update in test mode")
    success, updated_tasks = update_all_tasks(test_mode=True)
    if not success:
        logger.error("Failed: Update in test mode failed")
        return False

    logger.info(
        "Passed: Successfully tested update in test mode. "
        f"Would update: {updated_tasks}"
    )
    return True


def run_tests() -> bool:
    """Run tests to verify script functionality."""
    logger.info("Running tests...")

    # Test 1: Load tasks.json
    logger.info("Test 1: Loading tasks.json")
    tasks_data, _ = load_tasks_json()
    if not tasks_data:
        logger.error("Test 1 failed: Could not load tasks.json")
        return False
    logger.info("Test 1 passed: Successfully loaded tasks.json")

    # Run individual test functions
    tests = [
        run_test_extract_markdown,
        run_test_clean_details,
        run_test_extract_task_info,
        run_test_extract_subtask_info,
        run_test_update_mode,
    ]

    test_results = [test() for test in tests]
    all_passed = all(test_results)

    if all_passed:
        logger.info("All tests passed!")
    else:
        logger.error("Some tests failed!")

    return all_passed


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

    This script updates tasks in tasks.json based on markdown files in the
    tasks/docs/ directory. It ensures task details are consistent with their
    markdown documentation.
    """
    setup_logging(verbose)

    if test:
        click.echo("Running in test mode - no changes will be made")
        run_tests()
        success, updated_tasks = update_all_tasks(
            start_id, end_id, test_mode=True
        )

        if not success:
            click.echo("Test failed. See above for errors.", err=True)
            sys.exit(1)

        if updated_tasks:
            click.echo(
                f"Test successful. Would update {len(updated_tasks)} tasks:"
            )
            for task_id, fields in updated_tasks.items():
                click.echo(f"  Task {task_id}: {', '.join(fields)}")
        else:
            click.echo("Test successful. No tasks would be updated.")
    else:
        success, updated_tasks = update_all_tasks(start_id, end_id)

        if not success:
            click.echo("Update failed. See above for errors.", err=True)
            sys.exit(1)

        if updated_tasks:
            click.echo(f"Successfully updated {len(updated_tasks)} tasks:")
            for task_id, fields in updated_tasks.items():
                click.echo(f"  Task {task_id}: {', '.join(fields)}")
        else:
            click.echo("No tasks needed updating.")


if __name__ == "__main__":
    # Use Click's command-line parsing
    main()  # pylint: disable=no-value-for-parameter
