import json
import subprocess
from pathlib import Path
from typing import List, Dict, Optional, Any, Union, cast


class CrystalTaskManager:
    """Manages crystal analysis tasks using Task Master."""

    def __init__(self):
        """Initialize the task manager with project paths."""
        self.project_root = Path(__file__).parent.parent
        self.tasks_dir = self.project_root / "tasks"

    def create_task(
        self,
        title: str,
        description: str,
        priority: str = "medium"
    ) -> Dict[str, Any]:
        """Create a new task using Task Master.

        Args:
            title: Task title
            description: Detailed task description
            priority: Task priority level (high, medium, low)

        Returns:
            Dict containing task information including ID

        Raises:
            RuntimeError: If task creation fails
        """
        cmd = [
            "task-master", "add-task",
            "--title", title,
            "--description", description,
            "--priority", priority,
            "--json"
        ]
        try:
            result = subprocess.run(
                cmd,
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                check=True
            )
            return cast(Dict[str, Any], json.loads(result.stdout))
        except subprocess.CalledProcessError as error:
            raise RuntimeError(f"Failed to create task: {error.stderr}") from error

    def get_tasks(self, status: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get all tasks, optionally filtered by status.

        Args:
            status: Filter tasks by status (e.g., 'pending', 'done')

        Returns:
            List of task dictionaries

        Raises:
            RuntimeError: If fetching tasks fails
        """
        cmd = ["task-master", "list", "--json"]
        if status:
            cmd.extend(["--status", status])

        try:
            result = subprocess.run(
                cmd,
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                check=True
            )
            return cast(List[Dict[str, Any]], json.loads(result.stdout))
        except subprocess.CalledProcessError as error:
            raise RuntimeError(f"Failed to get tasks: {error.stderr}") from error

    def mark_task_done(self, task_id: Union[str, int]) -> None:
        """Mark a task as completed.

        Args:
            task_id: The ID of the task to mark as done

        Raises:
            RuntimeError: If marking task as done fails
        """
        cmd = [
            "task-master", "set-status",
            "--id", str(task_id),
            "--status", "done"
        ]
        try:
            subprocess.run(
                cmd,
                cwd=str(self.project_root),
                check=True,
                capture_output=True
            )
        except subprocess.CalledProcessError as error:
            raise RuntimeError(f"Failed to mark task as done: {error.stderr}") from error

    def add_crystal_analysis_task(self, cif_file: Union[str, int]) -> Optional[Dict[str, Any]]:
        """Create a task specifically for crystal analysis.

        Args:
            cif_file: Path to the CIF file to analyze or COD database number.

        Returns:
            Dict: Created task information including ID, or None if creation fails

        Raises:
            RuntimeError: If task creation fails
        """
        title = f"Analyze crystal structure: {Path(str(cif_file)).stem}"
        description = f"""
        Analyze crystal structure from CIF file: {cif_file}

        Tasks:
        1. Load and parse CIF file
        2. Extract symmetry operations
        3. Calculate crystal properties
        4. Generate visualization
        """
        return self.create_task(title, description, priority="high")


# Example usage
if __name__ == "__main__":
    # Initialize task manager
    task_manager = CrystalTaskManager()

    # Example: Create a task for analyzing a new crystal structure
    task = task_manager.add_crystal_analysis_task(
        "workDir/cif files/1000003.cif"
    )

    # Example: List all pending tasks
    pending_tasks = task_manager.get_tasks(status="pending")
    print("\nPending Tasks:")
    for task in pending_tasks:
        print(f"- {task['title']} (ID: {task['id']})")

    # Example: Mark a task as done
    # task_manager.mark_task_done(task['id']) 