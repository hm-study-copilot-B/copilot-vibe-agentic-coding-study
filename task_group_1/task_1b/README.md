# Task Group 1: Data Analysis Tasks

## Steps to Complete Task Group 1

1. Install Python
   - Download and install Python 3.6+ from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`
   - Ensure pip is available: `pip --version`
     - If not, install via `python get-pip.py` (download from bootstrap.pypa.io) or `python -m ensurepip --upgrade`

2. Set up the project environment
   - Navigate to the task directory: `cd task_group_1/task_1b/`
   - (Optional) Create a virtual environment for isolation: `python -m venv venv` then activate it
   - Install testing dependencies: `python -m pip install pytest` (use `python -m pip` instead of `pip` directly, as `pip` may not be in PATH)

3. Implement the solution
   - Read the task description below
   - Edit `src/solution.py` to implement the required function

4. Run and validate the solution
   - Execute tests: `python -m pytest` (from `task_1b/` directory)
   - Ensure all tests pass




Below is the deeper explanation of 
# GAIA-b — British Museum Mollusk Shell & Bead Age (Data Analysis Task)

## Task Overview

Analyze a CSV of mollusk bead research articles to find the minimum age of beads made from a specific species' shells. The species is linked to a British Museum object.

Find the minimum "at least" age (in thousands of years) from 2021 *Science Advances* articles about that species.

## Files and Structure

```
.
├─ README.md                # This file
├─ data/
│  └─ mollusk_bead_articles.csv
├─ src/
│  └─ solution.py           # Implement your solution here
└─ tests/
   └─ test_solution.py      # Automated tests
```

### data/mollusk_bead_articles.csv

CSV with columns: `museum_number`, `accepted_species_name`, `journal`, `publication_year`, `min_age_thousand_years_at_least`, etc.

## What You Need to Implement

Implement in `src/solution.py`:

```python
def find_min_bead_age(csv_path: str = "data/mollusk_bead_articles.csv") -> int:
    """
    Find the minimum 'at least' age (in thousands of years) of beads made from the mollusk species
    linked to British Museum object '2012,5015.17', as reported in 2021 Science Advances articles.
    """
    ...
```

## Input / Output

- **Input:** CSV path (default: "data/mollusk_bead_articles.csv")
- **Output:** Integer of the minimum age.

## Constraints

- Python 3, standard library only.
- Do not modify CSV or test files.

## Evaluation

Tests check the correct minimum age is returned.

## Hints

- Use `csv` module.
- Find species from museum_number "2012,5015.17".
- Filter by species, journal "Science Advances", year 2021.
- Find min of `min_age_thousand_years_at_least`.