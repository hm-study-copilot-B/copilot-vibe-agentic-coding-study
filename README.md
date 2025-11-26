# From Collaboration to Delegation

## Evaluating Developer Efficiency and Perception in Vibe and Agentic Coding

---

### 🗂️ Repository Purpose

This repository contains two debugging tasks used in a research study comparing
two levels of AI autonomy in GitHub Copilot:

- **Vibe Coding (Copilot Ask Mode)**
- **Agentic Coding (Copilot Agent Mode)**

Each task corresponds to exactly one mode assigned by the researcher.
Participants cannot use both modes on the same task. If Task A uses Agent Mode,
then Task B uses Ask Mode, and vice versa.

---

### 📁 Repository Structure

```
copilot-autonomy-study/
├── task_a/
│   ├── src/
│   │   ├── models.py
│   │   ├── data_source.py
│   │   ├── query.py
│   │   ├── stats.py
│   │   └── utils.py
│   └── tests/
│       └── test_task_a.py
├── task_b/
│   ├── src/
│   │   ├── models.py
│   │   ├── data_source.py
│   │   ├── schedule.py
│   │   ├── overdue.py
│   │   └── utils.py
│   └── tests/
│       └── test_task_b.py
└── README.md
```

---

### 📝 Task Descriptions

**Task A**

- Focus: Filtering logic, querying, and statistics computation
- Bugs: Incorrect filter logic, case-sensitive search, missing priority
  filtering, improper statistics counting, mislabelling of status and assignee
  fields
- Tests: Validate filtering and statistical correctness

**Task B**

- Focus: Recurrence scheduling, overdue detection, and handling of
  recurring/completed tasks
- Bugs: Missing date parsing, incorrect recurrence intervals, incomplete monthly
  logic, improper overdue calculation, incorrect handling of done tasks
- Tests: Validate recurrence, overdue logic, and proper parsing

---

### 👩‍💻 How Participants Use the Repo

1. Clone the repository
2. Run `pytest` inside each task directory
3. Fix failing tests using the assigned Copilot mode
4. Use only the mode assigned by the researcher for each task
5. Do **not** switch modes or use external resources
6. Each task has a maximum time limit (20 minutes)
7. Work entirely inside VS Code with GitHub Copilot

---

### 🧑‍🔬 Modes

**Vibe Coding (Ask Mode):**

- Conversational prompting and iterative refinement

**Agentic Coding (Agent Mode):**

- Autonomous multi-step execution and planning

---

### 📜 Rules

- Only the assigned mode may be used per task
- No switching modes mid-task
- No external tools or internet
- Manual editing is allowed
- You may re-run prompts or agent steps
- Tasks are isolated; `task_a` and `task_b` must not be mixed

---

### 🎯 Goal of Each Task

Identify and fix all intentional bugs so that all tests pass. No need to
optimize or refactor beyond what the tests require.

---

### ⚙️ Technical Requirements

- Python 3 installed
- pytest installed
- VS Code with GitHub Copilot enabled

---

**End of Repo Info. Please check the task_a.md and task_b.md files in directories to see descriptions based on the task.**
