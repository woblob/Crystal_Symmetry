"""
Type definitions for utility modules.

This module defines custom type aliases and annotations for utility modules
used throughout the codebase.
"""
from typing import Dict, List, Any, Union, Optional

# Task management types
TaskID = Union[str, int]
TaskDict = Dict[str, Any]
TaskList = List[TaskDict]

# File path types
FilePath = Union[str, bytes, int]  # Can be a string path, bytes path, or COD ID
