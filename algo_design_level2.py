"""
=============================================================
  LEVEL 2 — Top-Down Design: Building a Report System
  Apply structure-chart thinking in real code.
=============================================================

In this level you'll build a simple student report program
using TOP-DOWN DESIGN. The structure looks like this:

        run_report_system()
        /         |         \
get_student()  calculate_stats()  display_report()
                   /       \
           find_highest()  find_average()

You'll write each subroutine separately, then connect them.
"""

from algo_design_level1 import calculate_grade


# ----------------------------------------------------------
# TASK 2A: Write the "leaf" subroutines first (bottom level)
# ----------------------------------------------------------

def find_average(scores):
    """
    INPUT:  a list of numbers (scores)
    OUTPUT: the average as a float
    Hint: sum(scores) gives you the total; len(scores) gives the count.
    """
    # YOUR CODE HERE
    pass


def find_highest(scores):
    """
    INPUT:  a list of numbers (scores)
    OUTPUT: the single highest score
    Hint: Python has a built-in max() function.
    """
    # YOUR CODE HERE
    pass


# Quick tests (uncomment to check):
# print(find_average([80, 90, 70]))   # Expected: 80.0
# print(find_highest([80, 90, 70]))   # Expected: 90


# ----------------------------------------------------------
# TASK 2B: Write the mid-level subroutine
# ----------------------------------------------------------

def calculate_stats(scores):
    """
    INPUT:  a list of scores
    OUTPUT: a dictionary with keys "average" and "highest"

    This function CALLS find_average() and find_highest().
    It combines their results into one package (a dictionary).

    Example return value: {"average": 80.0, "highest": 90}
    """
    # YOUR CODE HERE
    pass


# ----------------------------------------------------------
# TASK 2C: Write the display procedure
# ----------------------------------------------------------

def display_report(name, scores, stats):
    """
    PROCEDURE — no return value.
    Prints a formatted student report showing:
      - Student name
      - Their scores
      - Their average (from stats dictionary)
      - Their highest score (from stats dictionary)
      - Their overall grade (using calculate_grade from Level 1)
    """
    # YOUR CODE HERE
    pass


# ----------------------------------------------------------
# TASK 2D: Write the top-level function that ties it all together
# ----------------------------------------------------------

def run_report_system():
    """
    The "root" of the structure chart.

    1. Create a list of at least 3 students, each with a name and
       a list of scores. (You can hardcode this data for now.)
    2. For each student:
       a. Call calculate_stats() with their scores
       b. Call display_report() with their name, scores, and stats

    Example student data:
    students = [
        {"name": "Alex", "scores": [85, 90, 78]},
        {"name": "Sam",  "scores": [55, 60, 48]},
    ]
    """
    # YOUR CODE HERE
    pass


# Uncomment to run when all subroutines above are complete:
# run_report_system()
