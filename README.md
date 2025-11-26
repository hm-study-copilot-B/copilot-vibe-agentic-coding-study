# From Collaboration to Delegation

Evaluating Developer Efficiency and Perception in Vibe and Agentic Coding using
Github Copilot and Gemini 3 Pro.

## 🗂️ Repository Purpose

This repository contains two small debugging tasks for the research study. The
goal is to compare how developers work with two levels of AI autonomy in GitHub
Copilot:

- **Vibe Coding (Copilot Ask Mode)**
- **Agentic Coding (Copilot Agent Mode)**

Each task is done using only one mode, assigned by the researcher. If Task A is
completed with Agent Mode, Task B must be completed with Ask Mode — and the
other way around. Switching modes or models during a task is not allowed.

## 📁 Repository Structure

```
copilot-autonomy-study/
├── task_a/
│   ├── src/
│   ├── tests/
│   └── task_a_description.md
├── task_b/
│   ├── src/
│   ├── tests/
│   └── task_b_description.md
└── README.md
```

## 📝 Task Overview

- `task_a_description.md` / `task_b_description.md` → instructions for each task to have an overview.
- `tests/` → the tests you must make pass
- `src/` → the code base per Task

## 👩‍💻 What You Need To Do Before the Session

The steps below describe exactly what to do after receiving the study
instructions.

1. **Install Python (if you don’t have it already)**

   - You need Python 3.9 or higher.
   - Download from: https://www.python.org/downloads/
   - Windows users: Make sure to check “Add Python to PATH” during installation.

2. **Log into VS Code/ GitHub Copilot**

   - Before cloning the repository:
     - Open VS Code/Please download if not already there.
     - Sign in with the VS Code provided by the researcher. (Password
       will be regenerated.) You can keep yours if you already signed in.
     - Install the GitHub Copilot extension (if not installed)
     - Sign in with the GitHub account provided by the researcher. (Password
       will be regenerated)
     - Make sure Copilot is activated
     - You will use the mode assigned to you (Ask or Agent)

3. **Clone the repository**

   - You can clone it in two ways:
     - **Option A — Directly in VS Code (recommended)**
       - Open VS Code
       - Press Ctrl+Shift+P (or Cmd+Shift+P on Mac)
       - Type: Git: Clone
       - Paste the repository link
       - Choose a folder on your computer
       - VS Code will ask: “Open cloned repository?” → click Open
     - **Option B — From GitHub.com**
       - Go to the repository page
       - Click “Clone → HTTPS”
       - Copy the link
       - Open VS Code → Terminal →
         - `git clone <paste-link-here>`

4. **Open the project in VS Code and Create a new branch with develop/participant_id (given by the researcher)**

   - If VS Code has not already opened the repo:
     - Go to File → Open Folder
     - Select copilot-vibe-agentic-coding-study
     - VS Code loads the whole project structure
     - Then please create your own branch, you can ask for the instructions.

5. **Create a Python environment inside the project**

   - This makes sure everything works the same for every participant.
   - Open the terminal in project directory in VS Code:
     - **Windows:**
       - `python -m venv .venv`
     - **macOS / Linux:**
       - `python3 -m venv .venv`
   - You will now see a .venv folder inside the project.

6. **Activate the environment**

   - **Windows:**
     - `\.venv\Scripts\activate`
   - **macOS / Linux:**
     - `source .venv/bin/activate`
   - Your terminal should now show: (.venv) at the beginning of the line.

7. **Install pytest**

   - Inside the activated environment, run:
     - `pip install pytest`
   - This installs the test runner you will use.

8. **Start the assigned task**

   - You will be instructed which task to start with (A or B), as well as which
     Copilot mode to use.
   - For Task A:
     - `cd task_a`
     - `pytest`
   - For Task B:
     - `cd task_b`
     - `pytest`
   - Some tests will fail at the start — this is normal.

9. **Fix the code using ONLY your assigned Copilot mode**

   - Ask Mode → conversational help and suggestions
   - Agent Mode → multi-step autonomous actions
   - **Rules:**
     - Do not switch modes
     - Do not use external websites or tools
     - Manual editing is allowed
     - You may re-run pytest as much as needed

10. **Time Limit: 20 minutes per task**
    - When the time is up, stop immediately.
    - You will then proceed to the next step of the study.

Once you finish the assigned task(s), the experiment continues with
questionnaires and at the end of two tasks a short interview.
