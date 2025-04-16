"""Type stubs for Profiling module.

This module provides decorators for profiling function execution time.
"""

from typing import Any, Callable, TypeVar, cast

T = TypeVar('T', bound=Callable[..., Any])

def profiler(sortby: str) -> Callable[[T], T]:
    """Create a profiling decorator that sorts results by the specified key.
    
    Args:
        sortby: Key to sort profiling results by (e.g., "cumulative", "time")
        
    Returns:
        A decorator function that profiles the decorated function
    """
    ...

def profile_old(fnc: T) -> T:
    """A decorator that uses cProfile to profile a function.
    
    This decorator profiles the execution time of the decorated function
    and prints the results sorted by cumulative time.
    
    Args:
        fnc: The function to profile
        
    Returns:
        The decorated function
    """
    ...
