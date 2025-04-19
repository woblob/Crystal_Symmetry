#!/usr/bin/env python3
"""
Regenerate Task Master task files.

This script regenerates task files from tasks.json using Task Master's generate command.
It can be used after updating tasks.json to ensure all task files are in sync.

Usage:
    python regenerate_tasks.py

This script requires Task Master to be installed and configured.
"""

import os
import sys
import json
from pathlib import Path


def regenerate_task_files():
    """Regenerate task files using Task Master API."""
    try:
        # Get the project root directory
        project_root = Path.cwd().resolve()
        tasks_json_path = project_root / "tasks" / "tasks.json"

        # Check if tasks.json exists
        if not tasks_json_path.exists():
            print(f"Error: {tasks_json_path} does not exist.")
            return False

        # Load tasks.json
        with open(tasks_json_path, "r", encoding="utf-8") as f:
            tasks_data = json.load(f)

        # Generate individual task files
        tasks_dir = project_root / "tasks"
        for task in tasks_data.get("tasks", []):
            task_id = task.get("id")
            if task_id is not None:
                task_file_path = tasks_dir / f"task_{task_id:03d}.txt"

                # Generate task file content
                content = generate_task_file_content(task)

                # Write to file
                with open(task_file_path, "w", encoding="utf-8") as f:
                    f.write(content)

                print(f"Generated task file: {task_file_path}")

        print("Successfully regenerated all task files.")
        return True
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def generate_task_file_content(task):
    """Generate content for a task file."""
    content = []

    # Add task header
    content.append(f"# Task ID: {task.get('id')}")
    content.append(f"# Title: {task.get('title')}")
    content.append(f"# Status: {task.get('status')}")

    # Add dependencies
    deps = task.get("dependencies", [])
    if deps:
        content.append(f"# Dependencies: {', '.join(str(d) for d in deps)}")
    else:
        content.append("# Dependencies: None")

    # Add priority
    if "priority" in task:
        content.append(f"# Priority: {task.get('priority')}")

    # Add description
    if "description" in task:
        content.append(f"# Description: {task.get('description')}")

    # Add details
    if "details" in task:
        content.append("# Details:")
        content.append(task.get("details"))

    # Add test strategy
    if "testStrategy" in task:
        content.append("# Test Strategy:")
        content.append(task.get("testStrategy"))

    # Add subtasks
    subtasks = task.get("subtasks", [])
    if subtasks:
        content.append("# Subtasks:")
        for subtask in subtasks:
            subtask_id = subtask.get("id")
            subtask_title = subtask.get("title")
            subtask_status = subtask.get("status")

            content.append(f"## {subtask_id}. {subtask_title} [{subtask_status}]")

            # Add subtask dependencies
            subtask_deps = subtask.get("dependencies", [])
            if subtask_deps:
                content.append(
                    f"### Dependencies: {', '.join(str(d) for d in subtask_deps)}"
                )
            else:
                content.append("### Dependencies: None")

            # Add subtask description
            if "description" in subtask:
                content.append(f"### Description: {subtask.get('description')}")

            # Add subtask details
            if "details" in subtask:
                content.append("### Details:")
                content.append(subtask.get("details"))

    return "\n\n".join(content)


def main():
    """Main function to regenerate task files."""
    success = regenerate_task_files()
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
