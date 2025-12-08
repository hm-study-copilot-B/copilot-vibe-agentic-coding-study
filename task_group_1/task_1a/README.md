# Task Group 1: Data Analysis Tasks

## Steps to Complete Task Group 1

1. Install Python
   - Download and install Python 3.6+ from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`
   - Ensure pip is available: `pip --version`
     - If not, install via `python get-pip.py` (download from bootstrap.pypa.io) or `python -m ensurepip --upgrade`

2. Set up the project environment
   - Navigate to the task directory: `cd task_group_1/task_1a/`
   - (Optional) Create a virtual environment for isolation: `python -m venv venv` then activate it
   - Install testing dependencies: `python -m pip install pytest` (use `python -m pip` instead of `pip` directly, as `pip` may not be in PATH)

3. Implement the solution
   - Read `task_1a/README.md` for details
   - Edit `task_1a/src/solution.py` to implement the required function

4. Run and validate the solution
   - Execute tests: `python -m pytest` (from `task_1a/` directory)
   - Ensure all tests pass

# GAIA-a – Invasive Species Research (Data Analysis Task)

## Task Overview

Analyze a CSV of USGS invasive species records for a pet fish from *Finding Nemo*. Find all unique 5-digit ZIP codes where this fish was observed as nonnative before 2020. Do not use web access or external APIs.

## Files and Structure

```
.
├─ README.md                # This file
├─ data/
│  └─ usgs_nemo_observations.csv
├─ src/
│  └─ solution.py           # Implement your solution here
└─ tests/
   └─ test_solution.py      # Automated tests
```

### data/usgs_nemo_observations.csv

CSV with columns: `species_common_name`, `data_source`, `observation_year`, `zip_code`, etc. Inspect header for exact names.

## What You Need to Implement

Implement in `src/solution.py`:

```python
from typing import List

def find_nonnative_zip_codes(csv_path: str = "data/usgs_nemo_observations.csv") -> List[str]:
    """
    Return unique 5-digit ZIP codes where the Nemo fish (clownfish) was observed as nonnative by USGS before 2020.
    Filter: data_source == "USGS", observation_year < 2020, species contains "clownfish" (case-insensitive).
    Return sorted list of strings.
    """
    ...
```

## Input / Output

- **Input:** CSV path (default: "data/usgs_nemo_observations.csv")
- **Output:** List[str] of unique ZIP codes, sorted ascending.

Example: ["33040", "60601", "96701", "96706", "96734"]

## Constraints

- Python 3, standard library only.
- Do not modify CSV or test files.

## Evaluation

Tests check correct filtering, unique/sorted ZIP codes, and match expected results.

## Hints

- Use `csv` module.
- Lowercase for species matching.
- ZIP codes as strings to preserve leading zeros.
- Use `set` for uniqueness, then sort.