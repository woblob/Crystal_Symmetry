# Subtask 6.4: Implement progress tracking for long-running operations

**Status:** pending

**Dependencies:** 6.2

**Description:** Create a system for tracking and reporting progress during lengthy computational operations.

## Details

# Progress Tracking Implementation

## Requirements Analysis
- Long-running operations in crystallography code include:
  - Large CIF file parsing
  - Symmetry operations on complex structures
  - Visualization rendering
  - Database search operations
  - Batch processing of multiple structures

## Design Approach
- Create a flexible callback-based system
- Implement both text-based and GUI progress indicators
- Support cancellation of operations
- Provide meaningful progress metrics (not just percentage)

## Core Progress Tracker Implementation
```python
from typing import Callable, Optional, Any
import time

class ProgressTracker:
    """Track progress of long-running operations with callback support."""
    
    def __init__(self, total_steps: int, 
                 description: str = "", 
                 callback: Optional[Callable[[float, str], Any]] = None):
        """Initialize progress tracker.
        
        Args:
            total_steps: Total number of steps in the operation
            description: Human-readable description of the operation
            callback: Function to call on progress updates, receives
                      (progress_fraction, status_message)
        """
        self.total_steps = total_steps
        self.current_step = 0
        self.description = description
        self.callback = callback
        self.start_time = time.time()
        self.cancelled = False
        
        # Initial progress report
        self._report_progress("Started")
    
    def update(self, steps: int = 1, status: Optional[str] = None) -> None:
        """Update progress by specified number of steps."""
        if self.cancelled:
            raise CancellationError("Operation was cancelled")
            
        self.current_step += steps
        self._report_progress(status or f"Step {self.current_step}/{self.total_steps}")
    
    def _report_progress(self, status_message: str) -> None:
        """Report progress to callback if available."""
        progress = min(1.0, self.current_step / self.total_steps) if self.total_steps > 0 else 0
        
        # Calculate ETA
        elapsed = time.time() - self.start_time
        if progress > 0:
            eta = elapsed * (1 - progress) / progress
            status_message = f"{status_message} (ETA: {self._format_time(eta)})"
        
        if self.callback:
            self.callback(progress, status_message)
    
    def _format_time(self, seconds: float) -> str:
        """Format time duration in human-readable format."""
        if seconds < 60:
            return f"{seconds:.1f}s"
        elif seconds < 3600:
            return f"{seconds/60:.1f}m"
        else:
            return f"{seconds/3600:.1f}h"
```

## Integration Examples

### CLI Progress Bar
```python
from tqdm import tqdm

def process_large_structure(filepath, progress_callback=None):
    # Estimate total operations
    file_size = os.path.getsize(filepath)
    estimated_steps = file_size // 1024  # Rough estimate
    
    # Create progress tracker with tqdm integration
    with tqdm(total=estimated_steps, desc="Processing structure") as pbar:
        def update_progress(fraction, message):
            if progress_callback:
                progress_callback(fraction, message)
            pbar.n = int(fraction * estimated_steps)
            pbar.set_description(message)
            pbar.refresh()
        
        tracker = ProgressTracker(estimated_steps, 
                                "Processing structure", 
                                update_progress)
        
        # Actual processing with periodic tracker.update() calls
        # ...
```

## Cancellation Support
```python
# In the worker thread
try:
    for i, item in enumerate(items):
        if tracker.cancelled:
            break
        process_item(item)
        tracker.update(1, f"Processed item {i+1}/{len(items)}")
 except Exception as e:
    logger.error("Processing failed", exc_info=True)
    return False
```

## Best Practices
- Update progress at appropriate granularity (not too frequent, not too sparse)
- Include meaningful status messages beyond just percentages
- Provide accurate total step estimates when possible
- Include time estimates for better user experience
- Support both determinate (known steps) and indeterminate progress
- Make progress tracking optional with clean fallbacks


## Navigation
- [Back to Task Overview](overview.md)
- [Previous Subtask](subtask_003.md)
- [Next Subtask](subtask_005.md)

