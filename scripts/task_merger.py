#!/usr/bin/env python3

"""
Task Merger

This script merges task and subtask files into a single tasks.json file.
It reverses the operation of task_splitter.py.

Usage:
    python task_merger.py [--input INPUT] [--output OUTPUT] \
    [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Arguments:
    --input INPUT      Directory with split task files (default: tasks_split)
    --output OUTPUT    Output file path (default: tasks/tasks_merged.json)
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
        description="Merge individual task files into tasks.json"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="tasks_split",
        help="Directory with split task files (default: tasks_split)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="tasks/tasks_merged.json",
        help="Path to the output file (default: tasks/tasks_merged.json)",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: INFO)",
    )
    return parser.parse_args()


def validate_file_path(file_path: Path) -> bool:
    """Validate that a file exists and is readable.

    Args:
        file_path: Path to the file to validate

    Returns:
        True if the file exists and is readable, False otherwise
    """
    if not file_path.exists():
        logger.error(f"File {file_path} does not exist")
        return False
    if not file_path.is_file():
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


def load_json_file(
    file_path: Path,
) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """Load a JSON file.

    Args:
        file_path: Path to the JSON file

    Returns:
        A tuple containing the loaded JSON data and an error message if any
    """
    if not file_path.exists():
        return {}, f"File {file_path} not found"

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f), None
    except json.JSONDecodeError as e:
        error_msg = f"File {file_path} is not valid JSON: {e}"
        logger.error(error_msg)
        return {}, error_msg
    except Exception as e:
        error_msg = f"Error loading {file_path}: {e}"
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
    # Create directory if it doesn't exist
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        error_msg = f"No permission to create directory {file_path.parent}"
        logger.error(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"Error creating directory {file_path.parent}: {e}"
        logger.error(error_msg)
        return error_msg

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


def validate_directory(dir_path: Path) -> bool:
    """Validate that a directory exists and is readable.

    Args:
        dir_path: Path to the directory to validate

    Returns:
        True if the directory exists and is readable, False otherwise
    """
    if not dir_path.exists():
        logger.error(f"Directory {dir_path} does not exist")
        return False
    if not dir_path.is_dir():
        logger.error(f"{dir_path} is not a directory")
        return False
    try:
        # Check if directory is readable by listing its contents
        next(dir_path.iterdir(), None)
        return True
    except PermissionError:
        logger.error(f"No permission to read directory {dir_path}")
        return False
    except Exception as e:
        logger.error(f"Error validating directory {dir_path}: {e}")
        return False


def process_subtasks(
    task_id: int, subtasks_dir: Path
) -> Tuple[List[Dict[str, Any]], int, List[str]]:
    """Process subtasks for a task.

    Args:
        task_id: ID of the parent task
        subtasks_dir: Directory containing subtask files

    Returns:
        A tuple with (subtasks, subtasks_processed, errors)
    """
    subtasks = []
    subtasks_processed = 0
    errors = []

    try:
        # Sort subtask files by ID
        subtask_files = sorted(
            list(subtasks_dir.glob("subtask_*.json")),
            key=lambda f: int(f.stem.split("_")[1]),
        )

        # Process each subtask file
        for subtask_file in subtask_files:
            subtask_data, error = load_json_file(subtask_file)
            if error:
                errors.append(
                    f"Error loading subtask file {subtask_file}: {error}"
                )
                continue

            if subtask_data:
                subtasks.append(subtask_data)
                subtasks_processed += 1
                subtask_id = subtask_data.get("id")
                logger.debug(f"Processed subtask {task_id}.{subtask_id}")
    except Exception as e:
        error_msg = f"Error processing subtasks for task {task_id}: {e}"
        logger.error(error_msg)
        errors.append(error_msg)

    return subtasks, subtasks_processed, errors


def load_metadata(
    input_path: Path,
) -> Tuple[Optional[Dict[str, Any]], List[str]]:
    """Load metadata from the input directory.

    Args:
        input_path: Path to the input directory

    Returns:
        A tuple containing the metadata and a list of errors
    """
    errors = []
    metadata = None

    metadata_path = input_path / "metadata.json"
    if metadata_path.exists():
        metadata_data, error = load_json_file(metadata_path)
        if error:
            errors.append(error)
        elif metadata_data and isinstance(metadata_data, dict):
            metadata = metadata_data

    return metadata, errors


def merge_tasks(input_dir: str) -> Tuple[Optional[Dict[str, Any]], List[str]]:
    """Merge task and subtask files into a single tasks.json structure.

    Args:
        input_dir: Directory containing split task files

    Returns:
        A tuple with (merged_data, errors)
    """
    errors = []
    input_path = Path(input_dir)

    # Initialize the result structure
    result: Dict[str, Any] = {"tasks": []}

    # Validate input directory
    if not validate_directory(input_path):
        errors.append(f"Input dir {input_dir} is invalid or inaccessible")
        return None, errors

    # Load metadata if it exists
    metadata, metadata_errors = load_metadata(input_path)
    if metadata_errors:
        errors.extend(metadata_errors)
    if metadata:
        result["metadata"] = metadata

    # Get all task files
    tasks_dir = input_path / "tasks"
    if not validate_directory(tasks_dir):
        errors.append(
            f"Tasks directory {tasks_dir} not found or not accessible"
        )
        return None, errors

    # Sort task files by ID (extracted from filename)
    try:
        task_files = sorted(
            list(tasks_dir.glob("task_*.json")),
            key=lambda f: int(f.stem.split("_")[1]),
        )
    except Exception as e:
        errors.append(f"Error sorting task files: {e}")
        return None, errors

    if not task_files:
        errors.append(f"No task files found in {tasks_dir}")
        return None, errors

    tasks_processed = 0
    subtasks_processed = 0

    # Process each task file
    for task_file in task_files:
        task_data, error = load_json_file(task_file)
        if error:
            errors.append(f"Error loading task file {task_file}: {error}")
            continue

        if not task_data:
            errors.append(f"Task file {task_file} is empty or invalid")
            continue

        # Extract task ID
        task_id = task_data.get("id")
        if task_id is None:
            errors.append(f"Task in {task_file} has no ID, skipping")
            continue

        # Remove subtask_ids field (we'll replace it with actual subtasks)
        task_data.pop("subtask_ids", [])

        # Initialize subtasks list
        task_data["subtasks"] = []

        # Load subtasks for this task
        subtasks_dir = input_path / "subtasks" / f"task_{task_id:03d}"
        if subtasks_dir.exists() and subtasks_dir.is_dir():
            subtasks, subtasks_count, subtask_errors = process_subtasks(
                task_id, subtasks_dir
            )

            task_data["subtasks"] = subtasks
            subtasks_processed += subtasks_count
            errors.extend(subtask_errors)

        # Add task to result
        result["tasks"].append(task_data)
        tasks_processed += 1
        logger.debug(f"Processed task {task_id}")

    logger.info(
        f"Processed {tasks_processed} tasks and {subtasks_processed} subtasks"
    )

    if not result["tasks"]:
        errors.append("No tasks were successfully processed")
        return None, errors

    return result, errors


def main() -> int:
    """Main function.

    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        args = parse_args()
        setup_logging(args.log_level)

        logger.info(f"Merging tasks from {args.input}...")
        merged_data, errors = merge_tasks(args.input)

        if errors:
            logger.warning(f"Encountered {len(errors)} errors during merging:")
            for error in errors:
                logger.warning(f"- {error}")

        if not merged_data:
            logger.error("Failed to merge tasks")
            return 1

        logger.info(f"Saving merged tasks to {args.output}...")
        save_error = save_json_file(merged_data, Path(args.output))
        if save_error:
            logger.error(f"Failed to save merged tasks: {save_error}")
            return 1

        logger.info(f"Done! Tasks have been merged into {args.output}")
        return 0
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
