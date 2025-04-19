#!/usr/bin/env python3
"""
Run pytest tests for the update_all_tasks module.

This script runs the pytest tests for the update_all_tasks module
and displays the results in a readable format.

Usage:
    python run_pytest.py
"""

import os
import subprocess
import sys
from pathlib import Path


def run_tests():
    """Run pytest tests for the update_all_tasks module."""
    # Get the directory of this script
    script_dir = Path(__file__).parent.absolute()

    # Change to the script directory
    os.chdir(script_dir)

    # Run pytest with verbose output
    try:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "test_update_all_tasks_pytest.py",
                "-v",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        print(result.stdout)

        # Check if any tests failed
        if "failed" in result.stdout:
            print("\nSome tests failed. Please check the output above.")
            return False
        else:
            print("\nAll tests passed successfully!")
            return True
    except subprocess.CalledProcessError as e:
        print(f"Error running tests: {e}")
        print(e.stdout)
        print(e.stderr)
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
