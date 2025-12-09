# Copilot Vibe Agentic Coding Study

This repository contains coding tasks for a study comparing two modes of GitHub Copilot: Vibe Coding (Ask Mode) and Agentic Coding (Agent Mode).

## Participant Groups

- **Group 1 (GAIA-inspired Tasks):** Data analysis and CSV processing tasks using Python's standard library.
  - Assigned tasks: `task_group_1/task_1a/` and `task_group_1/task_1b/`.
- **Group 2 (SWE-inspired Tasks):** Bug-fixing tasks in Python configuration parsers.
  - Assigned tasks: `task_group_2/task_2a/` and `task_group_2/task_2b/`.

You will be assigned to one group based on the study design.

## Repository Contents

- `task_group_1/`: Data Analysis Tasks (Group 1)
  - `task_1a/`: **GAIA-a - Invasive Species Research**: Analyze USGS CSV data to find unique ZIP codes where clownfish (from *Finding Nemo*) was observed as nonnative before 2020. Filter by species name, data source, and observation year. Return sorted list of 5-digit ZIP codes.
  - `task_1b/`: **GAIA-b - British Museum Mollusk Shell & Bead Age**: Analyze research articles CSV to find the minimum age of beads made from a specific mollusk species linked to British Museum object "2012,5015.17". Filter by journal (Science Advances), publication year (2021), and return minimum age in thousands of years.

- `task_group_2/`: Software Engineering Bug-Fixing Tasks (Group 2)
  - `task_2a/`: **CSV Parser Case Sensitivity Bug**: Fix a CSV configuration parser that crashes on lowercase commands. The parser reads special command lines (like `#SKIP` or `#DELIMITER`) but only recognizes UPPERCASE versions. Make command parsing case-insensitive so `#skip`, `#Skip`, and `#SKIP` all work.
  - `task_2b/`: **JSON Config Validation Bug**: Fix a configuration validator that fails to handle boolean values represented as strings. Add support for converting string representations (`"true"`, `"false"`, `"1"`, `"0"`) to proper boolean types, similar to existing int/float conversion.

- Each task folder has its own README with detailed instructions, starter code, tests, and data files (for Group 1).

## Experiment Process (Step-by-Step)

The study takes 60 minutes total. Follow these steps in order:

1. **Phase 1: Onboarding & Consent (10 minutes)**
   - Arrive and review the study procedure.
   - Sign consent form.
   - Complete a background survey (experience with AI tools, programming).

2. **Phase 2: Task 1 Coding Session (15 minutes)**
   - The researcher assigns you a Copilot mode (Vibe or Agentic) for this task.
   - Navigate to your assigned task folder (based on your group).
   - Read the task README and implement the code using the assigned mode.
   - Screen recording and time tracking will occur.

3. **Phase 3: Post-Task Survey 1 (5 minutes)**
   - Complete a short survey rating the mode you just used.
   - Sample questions (Likert scale: 1-5, Strongly Disagree to Strongly Agree):
     - "I trusted the AI suggestions."
     - "The mode aligned with my workflow."
     - "I felt in control of the coding process."
   - Write a brief reflection (e.g., "What was frustrating?").

4. **Phase 4: Task 2 Coding Session (15 minutes)**
   - Switch to the other Copilot mode.
   - Work on the second task in your group.
   - Screen recording continues.

5. **Phase 5: Post-Task Survey 2 (5 minutes)**
   - Rate the second mode with similar Likert questions.
   - Write a brief reflection.

6. **Phase 6: Comparative Interview (10 minutes)**
   - Discuss your experiences with both modes.
   - Answer comparative questions (e.g., "Which mode was more efficient?").

**Important:** Stick to the time limits. Do not switch modes mid-task. The researcher will guide you through each phase.
