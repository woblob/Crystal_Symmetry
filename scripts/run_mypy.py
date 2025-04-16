"""Run mypy on the codebase."""
import subprocess
import sys
import os

def main():
    """Run mypy on the codebase."""
    # Change to the project root directory
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Run mypy on the core modules
    result = subprocess.run(
        ["mypy", "--config-file", "pyproject.toml", "krysztalki/core", "krysztalki/io"],
        capture_output=True,
        text=True,
    )
    
    # Print the output
    print(result.stdout)
    if result.stderr:
        print("Errors:", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
    
    # Return the exit code
    return result.returncode

if __name__ == "__main__":
    sys.exit(main())
