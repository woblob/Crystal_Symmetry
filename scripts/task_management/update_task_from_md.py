#!/usr/bin/env python3
"""
Update Task Master tasks from markdown files.

This script reads markdown files from the tasks/docs/task_XXX/ directory
and updates the corresponding task in tasks.json to match the content.
It removes timestamp tags and ensures consistent formatting.

Usage:
    python update_task_from_md.py <task_id>

Example:
    python update_task_from_md.py 4
"""

import json
import os
import sys
import re
from pathlib import Path


def read_markdown_file(file_path):
    """Read content from a markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def extract_markdown_content(content, section_name="Details"):
    """Extract content from a specific section in markdown."""
    if not content:
        return None

    # Find the section
    pattern = rf"^## {section_name}\s*$(.*?)(?:^##\s|\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if match:
        return match.group(1).strip()
    return None


def extract_task_info(content):
    """Extract basic task information from markdown content."""
    info = {}

    # Extract title
    title_match = re.search(r"^# (Task \d+: .+)$", content, re.MULTILINE)
    if title_match:
        info["title"] = re.sub(r"^Task \d+: ", "", title_match.group(1))

    # Extract status
    status_match = re.search(r"\*\*Status:\*\* (\w+)", content)
    if status_match:
        info["status"] = status_match.group(1).lower()

    # Extract description
    desc_match = re.search(r"\*\*Description:\*\* (.+?)(?:\n\n|\Z)", content, re.DOTALL)
    if desc_match:
        info["description"] = desc_match.group(1).strip()

    return info


def extract_subtask_info(content):
    """Extract subtask information from markdown content."""
    info = {}

    # Extract title
    title_match = re.search(r"^# (Subtask \d+\.\d+: .+)$", content, re.MULTILINE)
    if title_match:
        info["title"] = re.sub(r"^Subtask \d+\.\d+: ", "", title_match.group(1))

    # Extract status
    status_match = re.search(r"\*\*Status:\*\* (\w+)", content)
    if status_match:
        info["status"] = status_match.group(1).lower()

    # Extract dependencies
    deps_match = re.search(r"\*\*Dependencies:\*\* (.+?)(?:\n\n|\Z)", content)
    if deps_match:
        deps_text = deps_match.group(1).strip()
        if deps_text.lower() == "none":
            info["dependencies"] = []
        else:
            info["dependencies"] = [dep.strip() for dep in deps_text.split(",")]

    # Extract description
    desc_match = re.search(r"\*\*Description:\*\* (.+?)(?:\n\n|\Z)", content, re.DOTALL)
    if desc_match:
        info["description"] = desc_match.group(1).strip()

    return info


def clean_details(details):
    """Remove timestamp tags from details content."""
    if not details:
        return details

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


def update_task_from_md(task_id):
    """Update a task and its subtasks from markdown files."""
    # Paths
    task_dir = Path(f"tasks/docs/task_{task_id:03d}")
    tasks_json_path = Path("tasks/tasks.json")

    # Check if directories and files exist
    if not task_dir.exists():
        print(f"Error: Directory {task_dir} does not exist.")
        return False

    if not tasks_json_path.exists():
        print(f"Error: File {tasks_json_path} does not exist.")
        return False

    # Load tasks.json
    try:
        with open(tasks_json_path, "r", encoding="utf-8") as f:
            tasks_data = json.load(f)
    except Exception as e:
        print(f"Error loading tasks.json: {e}")
        return False

    # Find the task in tasks.json
    task_found = False
    for task in tasks_data.get("tasks", []):
        if task.get("id") == int(task_id):
            task_found = True

            # Read overview.md
            overview_path = task_dir / "overview.md"
            if overview_path.exists():
                overview_content = read_markdown_file(overview_path)
                task_info = extract_task_info(overview_content)

                # Update task details
                details_content = extract_markdown_content(overview_content)
                if details_content:
                    task["details"] = details_content

                # Update other task info if available
                for key, value in task_info.items():
                    if value:
                        task[key] = value

            # Process subtasks
            for subtask in task.get("subtasks", []):
                subtask_id = subtask.get("id")
                if subtask_id is not None:
                    subtask_path = task_dir / f"subtask_{subtask_id:03d}.md"
                    if subtask_path.exists():
                        subtask_content = read_markdown_file(subtask_path)
                        subtask_info = extract_subtask_info(subtask_content)

                        # Update subtask details
                        details_content = extract_markdown_content(subtask_content)
                        if details_content:
                            subtask["details"] = details_content

                        # Update other subtask info if available
                        for key, value in subtask_info.items():
                            if value:
                                subtask[key] = value
                    else:
                        # Clean existing details by removing timestamp tags
                        subtask["details"] = clean_details(subtask.get("details", ""))

            break

    if not task_found:
        print(f"Error: Task with ID {task_id} not found in tasks.json.")
        return False

    # Save updated tasks.json
    try:
        with open(tasks_json_path, "w", encoding="utf-8") as f:
            json.dump(tasks_data, f, indent=2)
        print(f"Successfully updated task {task_id} from markdown files.")
        return True
    except Exception as e:
        print(f"Error saving tasks.json: {e}")
        return False


def main():
    """Main function to parse arguments and update tasks."""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <task_id>")
        sys.exit(1)

    try:
        task_id = int(sys.argv[1])
    except ValueError:
        print(f"Error: Task ID must be a number.")
        sys.exit(1)

    success = update_task_from_md(task_id)
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
