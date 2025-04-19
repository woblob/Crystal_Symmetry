#!/usr/bin/env python3
"""
Update Task Master tasks from markdown files and fix encoding issues.

This script combines the functionality of update_task_from_md.py, regenerate_tasks.py,
and fix_encoding.py to provide a complete workflow for updating tasks. It performs the
following operations in sequence:

1. Updates a task and its subtasks in tasks.json based on markdown files
2. Regenerates task files from the updated tasks.json
3. Fixes encoding issues in the regenerated task files

This ensures that task details are consistent between the markdown documentation
and the Task Master task files, with proper formatting and no encoding issues.

Usage:
    python update_tasks.py <task_id>

Example:
    python update_tasks.py 4
"""

import sys
import subprocess
from pathlib import Path


def run_script(script_name, *args):
    """Run another script with the given arguments."""
    script_path = Path(__file__).parent / f"{script_name}.py"

    if not script_path.exists():
        print(f"Error: Script {script_path} not found.")
        return False

    try:
        cmd = [sys.executable, str(script_path)] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error: {e.stderr}")
        return False
    except Exception as e:
        print(f"Unexpected error running {script_name}: {e}")
        return False


def main():
    """Main function to update tasks, regenerate files, and fix encoding."""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <task_id>")
        sys.exit(1)

    try:
        task_id = sys.argv[1]
        int(task_id)  # Validate that task_id is a number
    except ValueError:
        print("Error: Task ID must be a number.")
        sys.exit(1)

    # Step 1: Update task from markdown
    print(f"Updating task {task_id} from markdown files...")
    if not run_script("update_task_from_md", task_id):
        sys.exit(1)

    # Step 2: Regenerate task files
    print("\nRegenerating task files...")
    if not run_script("regenerate_tasks"):
        sys.exit(1)

    # Step 3: Fix encoding issues
    print("\nFixing encoding issues...")
    if not run_script("fix_encoding", task_id):
        sys.exit(1)

    msg = f"\nTask {task_id} has been successfully updated."
    print(msg)


if __name__ == "__main__":
    main()
