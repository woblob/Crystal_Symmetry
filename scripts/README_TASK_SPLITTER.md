# Task Splitter

This script parses a `tasks.json` file and splits it into individual files for each task and subtask, creating a more manageable directory structure.

## Overview

The Task Splitter script takes a monolithic `tasks.json` file and creates a directory structure with separate JSON files for:
- Project metadata
- Individual tasks
- Individual subtasks organized by parent task

This makes it easier to:
- Navigate and find specific tasks
- Edit individual tasks without affecting others
- Track changes to specific tasks in version control
- Implement task-specific functionality

## Directory Structure

The script creates the following directory structure:

```
tasks_split/
├── metadata.json                # Project metadata
├── tasks/                       # Directory for all tasks
│   ├── task_001.json            # Task 1
│   ├── task_002.json            # Task 2
│   └── ...
└── subtasks/                    # Directory for all subtasks
    ├── task_001/                # Subtasks for task 1
    │   ├── subtask_001.json
    │   ├── subtask_002.json
    │   └── ...
    ├── task_002/                # Subtasks for task 2
    │   └── ...
    └── ...
```

## Usage

```bash
python task_splitter.py [--input INPUT] [--output OUTPUT]
```

### Arguments

- `--input INPUT`: Path to the tasks.json file (default: tasks/tasks.json)
- `--output OUTPUT`: Path to the output directory (default: tasks_split)

### Examples

```bash
# Use default paths
python task_splitter.py

# Specify custom input and output paths
python task_splitter.py --input my_tasks.json --output my_split_tasks

# Run from any directory
python /path/to/task_splitter.py --input /path/to/tasks.json --output /path/to/output
```

## File Format

### Task File (task_XXX.json)

Each task file contains all the task properties except for the subtasks array, which is replaced with a `subtask_ids` array containing references to the subtask IDs.

```json
{
  "id": 1,
  "title": "Task Title",
  "description": "Task description",
  "status": "pending",
  "priority": "high",
  "dependencies": [2, 3],
  "details": "Task details...",
  "testStrategy": "Test strategy...",
  "subtask_ids": [1, 2, 3]
}
```

### Subtask File (subtask_XXX.json)

Each subtask file contains all the properties of the subtask, including the parent task ID.

```json
{
  "id": 1,
  "title": "Subtask Title",
  "description": "Subtask description",
  "status": "pending",
  "dependencies": [2],
  "parentTaskId": 1,
  "details": "Subtask details..."
}
```

### Metadata File (metadata.json)

The metadata file contains project-level information.

```json
{
  "projectName": "Project Name",
  "projectVersion": "1.0.0",
  "description": "Project description",
  "author": "Author Name",
  "dateCreated": "2023-01-01",
  "dateUpdated": "2023-01-15"
}
```

## Notes

- The script preserves all original data from the tasks.json file
- Task and subtask IDs are used in filenames with zero-padding (e.g., task_001.json)
- The original tasks.json file is not modified
- If a task or subtask is missing an ID, it will be skipped with a warning
