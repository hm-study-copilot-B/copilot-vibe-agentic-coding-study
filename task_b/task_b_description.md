# Task B – Debugging Recurring Task & Overdue Logic

**Please read the README first before beginning this task.**

---

## Overview

Task B is about a small Python system that takes care of repeating tasks — the
kind of tasks that come back every day, week, or month. Imagine a simple to-do
app that needs to know:

- when a repeating task should happen next,
- whether something is overdue,
- and which tasks should be ignored because they’re already marked “done.”

Right now, this logic doesn’t work correctly. Some tasks don’t get the right
next due date, some are marked overdue when they shouldn’t be, and some
repeating rules don’t behave as expected.

Your job is to fix these problems so the system behaves like a proper task
manager again and the tests pass.

---

## What You Need To Do

1. Open the `task_b` folder in VS Code.
2. Open a terminal at the location of the `task_b` folder.
3. Run the tests using:

   ```sh
   pytest
   ```

4. Look at which tests fail and what behavior they expect.
5. Use only the Copilot mode assigned to you to fix the code in this folder.
6. Re-run `pytest` to check your progress as you make changes.
7. The researcher will track the 20-minute time limit and notify you when time
   is over.
8. Read the tests to understand the expected behavior.
9. Continue fixing the issues using only your assigned Copilot mode.
10. Re-run the tests until they pass or the time limit ends.

---

## Notes

- Manual editing is allowed.
- You may read any file inside `task_b`.
- The logic requires careful reading, especially around dates and recurrence
  rules.
- Stop after 20 minutes, even if the task is not finished.
- The task will be followed by a questionnaire as soon as time is over.
