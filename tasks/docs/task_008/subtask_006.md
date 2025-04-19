# Subtask 8.6: Measure and improve test coverage

**Status:** pending

**Dependencies:** 8.5

**Description:** Measure code coverage, identify gaps, and implement targeted tests to improve coverage.

## Details

# Test Coverage Implementation Plan

## Coverage Measurement Tools
- Configure pytest-cov to measure code coverage
- Set up coverage reports in HTML and XML formats
- Integrate with CI pipeline for automated coverage tracking
- Use coverage.py to generate detailed reports

## Coverage Goals
- Aim for minimum 90% overall code coverage
- Require 100% coverage for critical components:
  - Core crystallographic algorithms
  - File parsers
  - Public API functions
- Establish coverage thresholds for CI pipeline

## Implementation Process

### Configuration Setup
```ini
# .coveragerc
[run]
source = crystal_symmetry
omit = 
    */tests/*
    */__init__.py
    */setup.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise NotImplementedError
    if __name__ == .__main__.:
    pass
    raise ImportError
```

### Integration with pytest
```bash
# Running tests with coverage
pytest --cov=crystal_symmetry --cov-report=html:coverage_html --cov-report=xml:coverage.xml
```

### CI Pipeline Integration
```yaml
# GitHub Actions example
- name: Run tests with coverage
  run: pytest --cov=crystal_symmetry --cov-report=xml:coverage.xml
  
- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    files: ./coverage.xml
    flags: unittests
    fail_ci_if_error: true
```

## Coverage Analysis Process
1. Run baseline coverage measurement
2. Identify modules with low coverage
3. Analyze uncovered lines and branches
4. Prioritize critical components
5. Implement targeted tests for gaps
6. Verify coverage improvements

## Targeted Testing Strategy
- Focus on complex conditional logic
- Ensure all branches are tested
- Add tests for exception handlers
- Create tests for rarely used options
- Test defensive programming checks

## Example Coverage Analysis Script
```python
"""Script to analyze coverage data and identify testing gaps."""
import json
import os
from pathlib import Path
import sys

def parse_coverage_data(coverage_file):
    """Parse coverage data and return uncovered lines by file."""
    with open(coverage_file, 'r') as f:
        coverage_data = json.load(f)
    
    results = {}
    for file_path, file_data in coverage_data['files'].items():
        # Skip test files
        if '/tests/' in file_path:
            continue
            
        uncovered_lines = sorted(file_data['missing_lines'])
        if uncovered_lines:
            results[file_path] = {
                'uncovered_lines': uncovered_lines,
                'coverage_percent': file_data['summary']['percent_covered'],
                'num_statements': file_data['summary']['num_statements'],
                'missing_branches': file_data.get('missing_branches', [])
            }
    
    return results

def main():
    """Generate a report of files with coverage below threshold."""
    if len(sys.argv) < 2:
        print("Usage: python analyze_coverage.py <coverage.json>")
        return 1
        
    coverage_file = sys.argv[1]
    coverage_data = parse_coverage_data(coverage_file)
    
    # Sort by coverage percentage
    sorted_files = sorted(
        coverage_data.items(), 
        key=lambda x: x[1]['coverage_percent']
    )
    
    print("Files with lowest coverage:")
    for file_path, data in sorted_files[:10]:
        print(f"{file_path}: {data['coverage_percent']:.1f}% covered")
        print(f"  Missing lines: {data['uncovered_lines']}")
        if data['missing_branches']:
            print(f"  Missing branches: {data['missing_branches']}")
        print()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

## Reporting and Documentation
- Generate visual coverage reports for review
- Document areas with intentionally low coverage
- Include coverage badges in README
- Track coverage trends over time
- Set up alerts for coverage regressions


## Navigation
- [Back to Task Overview](overview.md)
- [Previous Subtask](subtask_005.md)

