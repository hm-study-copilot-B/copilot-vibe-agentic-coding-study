# Task Group 2: SWE-inspired Tasks

## Steps to Complete Task Group 2

1. Install Python
   - Download and install Python 3.6+ from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`
   - Ensure pip is available: `pip --version`
     - If not, install via `python get-pip.py` (download from bootstrap.pypa.io) or `python -m ensurepip --upgrade`

2. Set up the project environment
   - Navigate to the task directory: `cd task_group_2/task_2b/`
   - (Optional) Create a virtual environment for isolation: `python -m venv venv` then activate it
   - Install dependencies: `python -m pip install matplotlib numpy`

3. Implement the solution
   - Read the task description below
   - Edit `src/solution.py` to implement the required functions

4. Run and validate the solution
   - Execute tests: `python -m pytest` (from `task_2b/` directory)
   - Or run the demo: `python src/demo.py`

---

# Task 2b: Add Dark Mode Toggle to Matplotlib

## Objective

Add a new functionality that allows users to toggle any existing plot to dark mode with a single function call.

## Requirements

### 1. Create `toggle_dark_mode()` function

```python
def toggle_dark_mode(ax=None, fig=None):
    """
    Toggle dark mode on a plot.
    
    Parameters:
    - ax: Specific axis to apply dark mode (optional)
    - fig: Figure to apply dark mode (optional)
    - If neither is specified, applies to current figure
    
    Returns:
    - None (modifies plot in place)
    """
    ...
```

The function should:
- Be applicable to either a specific axis, a figure, or the current figure if none is specified
- Convert the plot background to a dark color (e.g., #121212)
- Invert text colors from dark to light
- Adjust plot elements (grid lines, tick marks, etc.) to be visible on dark background
- Preserve the original colors of data elements (lines, points, bars) or provide an option to adjust them for better visibility

### 2. Make it reversible

Calling `toggle_dark_mode()` again should toggle back to light mode.

### 3. Create a demo

Create `src/demo.py` showing the functionality in action.

## Files Structure

```
.
├─ README.md                # This file
├─ src/
│  ├─ solution.py           # Implement your function here
│  └─ demo.py               # Demo script
└─ tests/
   └─ test_solution.py      # Automated tests
```

## Constraints

- Python 3, use matplotlib and numpy.
- Do not modify test files.

## Hints

- Store original colors to enable toggling back.
- Use `ax.set_facecolor()` for background.
- Modify `ax.spines`, `ax.tick_params`, and text elements.
- Consider using a global or figure-level state to track dark mode status.
