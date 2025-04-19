# Subtask 9.4: Implement end-to-end workflow tests

**Status:** pending

**Dependencies:** 9.1, 9.2, 9.3

**Description:** Create tests that verify complete processing pipelines from input to final output.

## Details

# End-to-End Workflow Tests Implementation Plan

## Test Objectives
- Validate complete processing pipelines
- Test realistic user workflows from input to output
- Verify data consistency across component boundaries
- Test performance and resource usage in full workflows

## Workflow Test Categories
1. **Structure Analysis Pipeline**
   - CIF file parsing
   - Structure validation and normalization
   - Symmetry analysis
   - Property calculation
   - Result output generation

2. **Transformation Workflows**
   - Structure manipulation
   - Symmetry preservation/breaking
   - Export to various formats
   - Visualization pipeline

3. **Database Integration Workflows**
   - Structure lookup
   - Search and filter operations
   - Structure comparison
   - Batch processing

## Implementation Example
```python
import pytest
from pathlib import Path
from crystal_symmetry.workflows import StructureAnalysisWorkflow
from crystal_symmetry.io import OutputFormatter

def test_structure_analysis_workflow(sample_cif_files, isolated_test_dir):
    """Test a complete structure analysis workflow."""
    # Set up input and output paths
    input_file = sample_cif_files["complex_zeolite"]
    output_dir = isolated_test_dir / "results"
    output_dir.mkdir()
    
    # Configure the workflow
    workflow = StructureAnalysisWorkflow(
        input_file=input_file,
        output_dir=output_dir,
        calculate_properties=["volume", "symmetry", "pore_size"],
        output_formats=["json", "cif", "report"]
    )
    
    # Execute the workflow
    results = workflow.run()
    
    # Verify workflow completion
    assert results["status"] == "success"
    
    # Check output files were generated
    assert (output_dir / "structure.json").exists()
    assert (output_dir / "modified.cif").exists()
    assert (output_dir / "analysis_report.html").exists()
    
    # Validate output content
    with open(output_dir / "structure.json") as f:
        import json
        data = json.load(f)
        
    # Verify key results
    assert "unit_cell_volume" in data
    assert "space_group" in data
    assert "symmetry_operations_count" in data
    assert "pore_diameter_angstrom" in data
    
    # Check consistency between input and output
    assert data["original_source"] == input_file.name
    assert data["chemical_formula"] is not None

def test_batch_processing_workflow(sample_cif_files, isolated_test_dir):
    """Test batch processing of multiple structures."""
    from crystal_symmetry.workflows import BatchProcessor
    
    # Create a batch processor
    processor = BatchProcessor(
        output_dir=isolated_test_dir / "batch_results",
        parallel_jobs=2
    )
    
    # Add multiple files for processing
    input_files = [
        sample_cif_files["simple_cubic"],
        sample_cif_files["complex_zeolite"],
        sample_cif_files["molecule_crystal"]
    ]
    
    for f in input_files:
        processor.add_file(f)
    
    # Run the batch job
    results = processor.process_all()
    
    # Verify all files were processed
    assert len(results) == len(input_files)
    assert all(r["status"] == "success" for r in results)
    
    # Check summary report
    summary = processor.generate_summary()
    assert len(summary["processed_files"]) == len(input_files)
    assert "total_processing_time" in summary
    assert "average_structure_volume" in summary
```

## Validation Strategy
- Compare workflow outputs with pre-computed reference results
- Measure performance metrics (execution time, memory usage)
- Validate logging and error reporting
- Test workflow resumption after interruption

## Command-Line Interface Testing
- Test CLI commands for executing workflows
- Verify parameter handling and validation
- Test various input/output scenarios
- Validate interactive mode behavior

## Visualization Testing
- Verify structure visualization outputs
- Test interactive visualization components
- Validate vector/raster output formats


## Navigation
- [Back to Task Overview](overview.md)
- [Previous Subtask](subtask_003.md)
- [Next Subtask](subtask_005.md)

