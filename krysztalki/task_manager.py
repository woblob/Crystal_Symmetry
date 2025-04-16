"""
Task management module for crystal analysis.
"""
from typing import Dict, Any, Optional, Union
import logging

logger = logging.getLogger(__name__)

class CrystalTaskManager:
    """
    Manages tasks related to crystal analysis.

    This class provides functionality to create, track, and update tasks during
    the crystal analysis process.
    """

    def __init__(self):
        self.tasks = []
        self.task_id_counter = 0

    def create_task(self, title: str, description: str, priority: str = "medium") -> Dict[str, Any]:
        """
        Create a new task.

        Args:
            title: Title of the task
            description: Detailed description of the task
            priority: Priority level ('high', 'medium', 'low')

        Returns:
            Dict containing task details
        """
        self.task_id_counter += 1
        task = {
            'id': self.task_id_counter,
            'title': title,
            'description': description,
            'status': 'pending',
            'priority': priority
        }
        self.tasks.append(task)
        logger.info(f"Created task: {title} (ID: {self.task_id_counter})")
        return task

    def mark_task_done(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id: ID of the task to mark as completed

        Returns:
            True if the task was found and updated, False otherwise
        """
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'done'
                logger.info(f"Marked task {task_id} as done")
                return True

        logger.warning(f"Could not find task with ID {task_id}")
        return False

    def add_crystal_analysis_task(self, file_name: Union[str, int]) -> Optional[Dict[str, Any]]:
        """
        Add a crystal analysis task.

        Args:
            file_name: Name of the CIF file or COD ID to analyze

        Returns:
            The created task dict or None if task creation failed
        """
        try:
            return self.create_task(
                f"Analyze crystal from {file_name}",
                f"Perform symmetry analysis on the crystal structure from {file_name}",
                "high"
            )
        except Exception as e:
            logger.error(f"Failed to create crystal analysis task: {str(e)}")
            return None

    def get_pending_tasks(self) -> list:
        """
        Get all pending tasks.

        Returns:
            List of task dictionaries with 'pending' status
        """
        return [task for task in self.tasks if task['status'] == 'pending'] 