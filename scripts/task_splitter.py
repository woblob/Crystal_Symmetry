#!/usr/bin/env python3

"""
Task Splitter

This script parses a tasks.json file and splits it into individual files
for each task and subtask. It creates a new directory structure.

Usage:
    python task_splitter.py [--input INPUT] [--output OUTPUT] \
    [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Arguments:
    --input INPUT      Path to the tasks.json file (default: tasks/tasks.json)
    --output OUTPUT    Path to the output directory (default: tasks_split)
    --log-level LEVEL  Set the logging level (default: INFO)
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Configure logger
logger = logging.getLogger(__name__)


def setup_logging(log_level: str = "INFO") -> None:
    """Set up logging configuration.

    Args:
        log_level: The logging level to use (default: INFO)
    """
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    # Configure logging with standard format including level name
    # Note: "levelname" is a standard logging placeholder, not a typo
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def parse_args() -> argparse.Namespace:
    """Parse command line arguments.

    Returns:
        Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description="Split tasks.json into individual files"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="tasks/tasks.json",
        help="Path to the tasks.json file (default: tasks/tasks.json)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="tasks_split",
        help="Path to the output directory (default: tasks_split)",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: INFO)",
    )
    return parser.parse_args()


def validate_file_path(file_path: str) -> bool:
    """Validate that a file exists and is readable.

    Args:
        file_path: Path to the file to validate

    Returns:
        True if the file exists and is readable, False otherwise
    """
    path = Path(file_path)
    if not path.exists():
        logger.error(f"File {file_path} does not exist")
        return False
    if not path.is_file():
        logger.error(f"{file_path} is not a file")
        return False
    try:
        # Check if file is readable
        with open(file_path, "r", encoding="utf-8") as _:
            pass
        return True
    except PermissionError:
        logger.error(f"No permission to read {file_path}")
        return False
    except Exception as e:
        logger.error(f"Error validating {file_path}: {e}")
        return False


def load_tasks_json(
    file_path: str,
) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """Load the tasks.json file.

    Args:
        file_path: Path to the tasks.json file

    Returns:
        A tuple containing the loaded JSON data and an error message if any
    """
    if not validate_file_path(file_path):
        return None, f"File {file_path} is not valid or accessible"

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data, None
    except json.JSONDecodeError as e:
        error_msg = f"File {file_path} is not valid JSON: {e}"
        logger.error(error_msg)
        return None, error_msg
    except Exception as e:
        error_msg = f"Error loading {file_path}: {e}"
        logger.error(error_msg)
        return None, error_msg


def create_directory_structure(
    output_dir: str,
) -> Tuple[Dict[str, Path], Optional[str]]:
    """Create the directory structure for the output.

    Args:
        output_dir: Path to the output directory

    Returns:
        A tuple containing a dictionary of paths and an error message if any
    """
    paths = {
        "root": Path(output_dir),
        "tasks": Path(output_dir) / "tasks",
        "subtasks": Path(output_dir) / "subtasks",
    }

    # Create directories
    try:
        for path in paths.values():
            path.mkdir(parents=True, exist_ok=True)
        return paths, None
    except PermissionError:
        error_msg = f"No permission to create directory {output_dir}"
        logger.error(error_msg)
        return {}, error_msg
    except Exception as e:
        error_msg = f"Error creating directory structure: {e}"
        logger.error(error_msg)
        return {}, error_msg


def save_json_file(data: Dict[str, Any], file_path: Path) -> Optional[str]:
    """Save data to a JSON file.

    Args:
        data: The data to save
        file_path: Path to the output file

    Returns:
        An error message if any, None otherwise
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return None
    except PermissionError:
        error_msg = f"No permission to write to {file_path}"
        logger.error(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"Error saving {file_path}: {e}"
        logger.error(error_msg)
        return error_msg


def process_subtasks(
    subtasks: List[Dict[str, Any]], task_id: int, subtask_dir: Path
) -> Tuple[int, List[str]]:
    """Process subtasks for a task.

    Args:
        subtasks: List of subtasks to process
        task_id: ID of the parent task
        subtask_dir: Directory to save subtask files

    Returns:
        A tuple with the number of subtasks processed and a list of errors
    """
    subtasks_processed = 0
    errors = []

    for subtask in subtasks:
        subtask_id = subtask.get("id")
        if subtask_id is None:
            logger.warning(
                f"Subtask without ID found in task {task_id}, skipping."
            )
            continue

        # Save subtask file
        subtask_file = subtask_dir / f"subtask_{subtask_id:03d}.json"
        error = save_json_file(subtask, subtask_file)
        if error:
            errors.append(error)
            continue

        subtasks_processed += 1
        logger.debug(f"Processed subtask {task_id}.{subtask_id}")

    return subtasks_processed, errors


def process_tasks(
    tasks_data: Dict[str, Any], paths: Dict[str, Path]
) -> Tuple[int, int, List[str]]:
    """Process tasks and subtasks, saving them to individual files.

    Args:
        tasks_data: The tasks data to process
        paths: Dictionary of paths for output files

    Returns:
        A tuple with (tasks_processed, subtasks_processed, errors)
    """
    errors = []
    tasks_processed = 0
    subtasks_processed = 0

    # Extract metadata
    metadata = tasks_data.get("metadata", {})
    if metadata:
        error = save_json_file(metadata, paths["root"] / "metadata.json")
        if error:
            errors.append(error)

    # Process tasks
    tasks = tasks_data.get("tasks", [])
    for task in tasks:
        task_id = task.get("id")
        if task_id is None:
            logger.warning("Task without ID found, skipping.")
            continue

        # Create a copy of the task without subtasks
        task_copy = task.copy()
        subtasks = task_copy.pop("subtasks", [])

        # Add subtask references
        task_copy["subtask_ids"] = [
            s.get("id") for s in subtasks if s.get("id") is not None
        ]

        # Save task file
        task_file = paths["tasks"] / f"task_{task_id:03d}.json"
        error = save_json_file(task_copy, task_file)
        if error:
            errors.append(error)
            continue

        tasks_processed += 1
        logger.debug(f"Processed task {task_id}")

        # Process subtasks
        if subtasks:
            try:
                subtask_dir = paths["subtasks"] / f"task_{task_id:03d}"
                subtask_dir.mkdir(exist_ok=True)

                subtasks_count, subtask_errors = process_subtasks(
                    subtasks, task_id, subtask_dir
                )

                subtasks_processed += subtasks_count
                errors.extend(subtask_errors)

            except Exception as e:
                error_msg = (
                    f"Error processing subtasks for task {task_id}: {e}"
                )
                logger.error(error_msg)
                errors.append(error_msg)

    return tasks_processed, subtasks_processed, errors


def main() -> int:
    """Main function.

    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        args = parse_args()
        setup_logging(args.log_level)

        logger.info(f"Loading tasks from {args.input}...")
        tasks_data, error = load_tasks_json(args.input)
        if error:
            logger.error(f"Failed to load tasks: {error}")
            return 1

        if not tasks_data:
            logger.error("No tasks data found")
            return 1

        logger.info(f"Creating directory structure in {args.output}...")
        paths, error = create_directory_structure(args.output)
        if error:
            logger.error(f"Failed to create directory structure: {error}")
            return 1

        logger.info("Processing tasks and subtasks...")
        tasks_processed, subtasks_processed, errors = process_tasks(
            tasks_data, paths
        )

        if errors:
            logger.warning(f"Completed with {len(errors)} errors")
            for error in errors:
                logger.warning(f"- {error}")

        logger.info(
            f"Done! Processed {tasks_processed} tasks and "
            f"{subtasks_processed} subtasks"
        )
        logger.info(f"Output directory: {args.output}")
        return 0
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
