"""
Tests for the type_checking module.
"""

import os
import unittest
from typing import List, Dict, Any, Optional

import pytest

from krysztalki.utils.type_checking import check_types, check_type, is_type_checking_enabled


# Enable type checking for tests
os.environ["KRYSZTALKI_ENABLE_TYPE_CHECKING"] = "1"


class TestTypeChecking(unittest.TestCase):
    """Test cases for the type_checking module."""
    
    def setUp(self):
        """Set up the test environment."""
        # Ensure type checking is enabled for tests
        os.environ["KRYSZTALKI_ENABLE_TYPE_CHECKING"] = "1"
    
    def test_is_type_checking_enabled(self):
        """Test that type checking can be enabled and disabled."""
        # Test enabled
        os.environ["KRYSZTALKI_ENABLE_TYPE_CHECKING"] = "1"
        self.assertTrue(is_type_checking_enabled())
        
        # Test disabled
        os.environ["KRYSZTALKI_ENABLE_TYPE_CHECKING"] = "0"
        self.assertFalse(is_type_checking_enabled())
        
        # Test other values
        os.environ["KRYSZTALKI_ENABLE_TYPE_CHECKING"] = "true"
        self.assertTrue(is_type_checking_enabled())
        
        os.environ["KRYSZTALKI_ENABLE_TYPE_CHECKING"] = "false"
        self.assertFalse(is_type_checking_enabled())
    
    def test_check_type_valid(self):
        """Test that check_type passes for valid types."""
        # Test simple types
        self.assertEqual(check_type(123, int), 123)
        self.assertEqual(check_type("hello", str), "hello")
        self.assertEqual(check_type(3.14, float), 3.14)
        self.assertEqual(check_type(True, bool), True)
        
        # Test complex types
        self.assertEqual(check_type([1, 2, 3], List[int]), [1, 2, 3])
        self.assertEqual(check_type({"a": 1, "b": 2}, Dict[str, int]), {"a": 1, "b": 2})
    
    def test_check_type_invalid(self):
        """Test that check_type raises TypeError for invalid types."""
        # Test simple types
        with pytest.raises(TypeError):
            check_type("123", int)
        
        with pytest.raises(TypeError):
            check_type(123, str)
        
        # Test complex types
        with pytest.raises(TypeError):
            check_type([1, "2", 3], List[int])
        
        with pytest.raises(TypeError):
            check_type({"a": 1, "b": "2"}, Dict[str, int])
    
    def test_check_types_decorator_valid(self):
        """Test that the check_types decorator passes for valid types."""
        @check_types
        def add(a: int, b: int) -> int:
            return a + b
        
        self.assertEqual(add(1, 2), 3)
    
    def test_check_types_decorator_invalid_args(self):
        """Test that the check_types decorator raises TypeError for invalid argument types."""
        @check_types
        def add(a: int, b: int) -> int:
            return a + b
        
        with pytest.raises(TypeError):
            add("1", 2)
        
        with pytest.raises(TypeError):
            add(1, "2")
    
    def test_check_types_decorator_invalid_return(self):
        """Test that the check_types decorator raises TypeError for invalid return types."""
        @check_types
        def add(a: int, b: int) -> str:
            return a + b  # This will return an int, not a str
        
        with pytest.raises(TypeError):
            add(1, 2)
    
    def test_check_types_with_optional(self):
        """Test that the check_types decorator works with Optional types."""
        @check_types
        def process_value(value: Optional[int]) -> Optional[str]:
            if value is None:
                return None
            return str(value)
        
        self.assertEqual(process_value(123), "123")
        self.assertIsNone(process_value(None))
    
    def test_check_types_with_complex_types(self):
        """Test that the check_types decorator works with complex types."""
        @check_types
        def process_data(data: Dict[str, List[int]]) -> List[int]:
            result = []
            for values in data.values():
                result.extend(values)
            return result
        
        data = {"a": [1, 2, 3], "b": [4, 5, 6]}
        self.assertEqual(process_data(data), [1, 2, 3, 4, 5, 6])
        
        with pytest.raises(TypeError):
            process_data({"a": [1, 2, 3], "b": ["4", 5, 6]})


if __name__ == "__main__":
    unittest.main()
