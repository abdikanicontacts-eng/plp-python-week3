# PLP Python Week 3 Assignment

* `grade_reporter.py`: Evaluates a list of student scores to assign letter grades, computes pass/fail counts, and calculates the rounded average score.
* `bug_hunt.py`: Fixes syntax, type, and logic bugs in a summation script and documents each fix with clear explanatory comments.

### Bug Hunt Reflection
The hardest bug to find was the loop condition (`count < 5` instead of `count <= 5`), because it produced no error message and allowed the program to execute successfully. I knew something was wrong because the printed result was 10 instead of the expected 15, which immediately indicated a logical calculation error.