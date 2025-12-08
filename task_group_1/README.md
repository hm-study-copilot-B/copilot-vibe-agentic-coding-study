# Task Group 1: Data Analysis Tasks

## Steps to Complete Task Group 1

1. Install Python
   - Download and install Python 3.6+ from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`
   - Ensure pip is available: `pip --version`
     - If not, install via `python get-pip.py` (download from bootstrap.pypa.io) or `python -m ensurepip --upgrade`

2. Set up the project environment
   - Navigate to the task directory: `cd task_group_1/task_1a/` (for Task 1a) or `cd task_group_1/task_1b/` (for Task 1b)
   - (Optional) Create a virtual environment for isolation: `python -m venv venv` then activate it
   - Install testing dependencies: `python -m pip install pytest` (use `python -m pip` instead of `pip` directly, as `pip` may not be in PATH)

3. Implement the solution
   - Read `task_1a/README.md` for Task 1a (GAIA-a) or `task_1b/README.md` for Task 1b (GAIA-b)
   - Edit `src/solution.py` in the respective task directory to implement the required function

4. Run and validate the solution
   - Execute tests: `python -m pytest` (from the task directory)
   - Ensure all tests pass