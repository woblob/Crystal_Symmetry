# Task Management Scripts

This directory contains scripts for managing Task Master tasks, particularly for synchronizing tasks with markdown documentation and ensuring consistent formatting.

## Scripts

### update_tasks.py

The main script that combines all functionality. It updates a task from markdown files, regenerates task files, and fixes encoding issues in a single operation.

**Features:**

- Combines the functionality of all other scripts in this directory
- Performs a complete workflow for updating tasks
- Ensures consistency between markdown documentation and Task Master files

**Usage:**

```bash
python update_tasks.py <task_id>
```

**Example:**

```bash
python update_tasks.py 4
```

### update_task_from_md.py

Updates a task and its subtasks in `tasks.json` based on markdown files in the `tasks/docs/task_XXX/` directory.

**Usage:**

```bash
python update_task_from_md.py <task_id>
```

**Example:**

```bash
python update_task_from_md.py 4
```

### regenerate_tasks.py

Regenerates task files from `tasks.json` using Task Master's generate command.

**Usage:**

```bash
python regenerate_tasks.py
```

### fix_encoding.py

Fixes encoding issues in task files, particularly replacing Unicode box-drawing characters with ASCII alternatives. It also handles special cases like the project directory tree structure.

**Features:**

- Replaces problematic Unicode box-drawing characters with ASCII alternatives
- Automatically detects and fixes the project directory tree structure
- Can fix a specific task file or all task files

**Usage:**

```bash
python fix_encoding.py [task_id]
```

If `task_id` is provided, only that task file will be fixed. If no `task_id` is provided, all task files will be fixed.

**Examples:**

```bash
python fix_encoding.py 1
python fix_encoding.py
```

## Workflow

The typical workflow for updating tasks is:

1. Edit markdown files in `tasks/docs/task_XXX/` directory
   - Update `overview.md` for the main task details
   - Update `subtask_XXX.md` files for each subtask
2. Run `update_tasks.py <task_id>` to update the task in `tasks.json`, regenerate task files, and fix encoding issues

For more granular control, you can run the individual scripts separately:

1. `update_task_from_md.py <task_id>` - Update task details from markdown files
2. `regenerate_tasks.py` - Regenerate task files
3. `fix_encoding.py [task_id]` - Fix encoding issues in task files

## Requirements

- Python 3.6+
- Task Master installed and configured
