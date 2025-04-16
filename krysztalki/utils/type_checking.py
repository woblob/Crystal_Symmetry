"""
Runtime type checking utilities.

This module provides decorators and functions for runtime type checking
using the typeguard library. These utilities can be used to validate
function parameters and return values against their type annotations.
"""

import functools
import inspect
import logging
import os
import sys
from typing import Any, Callable, TypeVar, cast

# Import typeguard conditionally to avoid hard dependency
try:
    import typeguard
    TYPEGUARD_AVAILABLE = True
except ImportError:
    TYPEGUARD_AVAILABLE = False

# Set up logging
logger = logging.getLogger(__name__)

# Type variables for function signatures
F = TypeVar('F', bound=Callable[..., Any])
T = TypeVar('T')

# Environment variable to control type checking
TYPE_CHECKING_ENV_VAR = "KRYSZTALKI_ENABLE_TYPE_CHECKING"


def is_type_checking_enabled() -> bool:
    """
    Check if runtime type checking is enabled.
    
    Type checking is enabled if the KRYSZTALKI_ENABLE_TYPE_CHECKING
    environment variable is set to a truthy value (1, true, yes, on).
    
    Returns:
        bool: True if type checking is enabled, False otherwise
    """
    env_value = os.environ.get(TYPE_CHECKING_ENV_VAR, "").lower()
    return env_value in ("1", "true", "yes", "on")


def check_types(func: F) -> F:
    """
    Decorator that performs runtime type checking on function arguments and return value.
    
    This decorator uses typeguard to check that the arguments passed to the decorated
    function and its return value match the type annotations.
    
    Args:
        func: The function to decorate
        
    Returns:
        The decorated function with runtime type checking
        
    Example:
        >>> @check_types
        >>> def add(a: int, b: int) -> int:
        >>>     return a + b
        >>>
        >>> add(1, 2)  # OK
        >>> add("1", 2)  # Raises TypeError
    """
    if not TYPEGUARD_AVAILABLE:
        logger.warning(
            "typeguard is not installed. Runtime type checking is disabled. "
            "Install with: pip install typeguard"
        )
        return func
    
    if not is_type_checking_enabled():
        return func
    
    # Get the signature of the function
    sig = inspect.signature(func)
    
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Skip type checking in certain environments
        if not is_type_checking_enabled():
            return func(*args, **kwargs)
        
        # Bind the arguments to the signature
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Check the types of the arguments
        for param_name, param in sig.parameters.items():
            if param.annotation is not inspect.Parameter.empty:
                arg_value = bound_args.arguments[param_name]
                try:
                    typeguard.check_type(arg_value, param.annotation)
                except TypeError as e:
                    raise TypeError(
                        f"Argument '{param_name}' to {func.__name__} has invalid type: {e}"
                    ) from e
        
        # Call the function
        result = func(*args, **kwargs)
        
        # Check the return type
        if sig.return_annotation is not inspect.Signature.empty:
            try:
                typeguard.check_type(result, sig.return_annotation)
            except TypeError as e:
                raise TypeError(
                    f"Return value from {func.__name__} has invalid type: {e}"
                ) from e
        
        return result
    
    return cast(F, wrapper)


def check_type(value: T, expected_type: Any) -> T:
    """
    Check that a value matches an expected type.
    
    This function uses typeguard to check that the value matches the expected type.
    If type checking is disabled, the value is returned as-is.
    
    Args:
        value: The value to check
        expected_type: The expected type of the value
        
    Returns:
        The value, if it matches the expected type
        
    Raises:
        TypeError: If the value does not match the expected type
        
    Example:
        >>> x = check_type("hello", str)  # OK
        >>> y = check_type(123, str)  # Raises TypeError
    """
    if not TYPEGUARD_AVAILABLE or not is_type_checking_enabled():
        return value
    
    try:
        typeguard.check_type(value, expected_type)
        return value
    except TypeError as e:
        raise TypeError(f"Value has invalid type: {e}") from e
