# Task Group 2: SWE-inspired Tasks

## Steps to Complete Task Group 2

1. Install Python
   - Download and install Python 3.6+ from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`
   - Ensure pip is available: `pip --version`
     - If not, install via `python get-pip.py` (download from bootstrap.pypa.io) or `python -m ensurepip --upgrade`

2. Set up the project environment
   - Navigate to the task directory: `cd task_group_2/task_2a/`
   - (Optional) Create a virtual environment for isolation: `python -m venv venv` then activate it
   - Install dependencies: `python -m pip install matplotlib numpy`

3. Implement the solution
   - Read the task description below
   - Edit `src/solution.py` to implement the required functions

4. Run and validate the solution
   - Execute tests: `python -m pytest` (from `task_2a/` directory)
   - Or run the demo: `python src/demo.py`

---

# Task 2a: Add Smooth Transitions Between Plots in Matplotlib

## Objective

Implement a new functionality that enables smooth animations/transitions between different states of a plot in Matplotlib.

## Requirements

### 1. Create `smooth_transition()` function

```python
def smooth_transition(from_data, to_data, duration=1.0, fps=30, **kwargs):
    """
    Create a smooth animation transitioning between data states.
    
    Parameters:
    - from_data: Initial data state
    - to_data: Final data state
    - duration: Transition duration in seconds (default: 1.0)
    - fps: Frames per second (default: 30)
    - **kwargs: Additional options (easing, plot_type, etc.)
    
    Returns:
    - Animation object
    """
    ...
```

The function should:
- Take initial and final data states
- Create a smooth animation transitioning between the states
- Support different plot types (line, scatter, bar, etc.)
- Allow customization of transition duration and frames per second
- Support transitions of various plot properties:
  - Data values (y-values in line plots, heights in bar charts, etc.)
  - Colors
  - Sizes/widths
  - Positions
- Provide options for different easing functions (linear, ease-in, ease-out, etc.)

### 2. Create `transition_plot_state()` function

```python
def transition_plot_state(fig_from, fig_to, duration=1.0, fps=30):
    """
    Transition between two completely different figure states.
    
    Parameters:
    - fig_from: Initial figure state
    - fig_to: Final figure state
    - duration: Transition duration in seconds
    - fps: Frames per second
    
    Returns:
    - Animation object
    """
    ...
```

### 3. Create a demo

Create `src/demo.py` showcasing various transition types.

## Files Structure

```
.
├─ README.md                # This file
├─ src/
│  ├─ solution.py           # Implement your functions here
│  └─ demo.py               # Demo script
└─ tests/
   └─ test_solution.py      # Automated tests
```

## Constraints

- Python 3, use matplotlib and numpy.
- Do not modify test files.

## Hints

- Use `matplotlib.animation.FuncAnimation` for animations.
- Implement easing functions for smooth transitions.
- Consider using numpy for interpolation between data states.
