"""
=============================================================
  LEVEL 4 — Backtracking: Maze Solver  (Extension)
  A classic backtracking algorithm.
=============================================================

A maze is represented as a grid of 0s (open) and 1s (walls).
The solver starts at (0,0) and tries to reach the bottom-right.

Backtracking strategy:
  - Try moving RIGHT first
  - If that fails, try DOWN
  - If both fail → BACKTRACK (return False to caller)
  - Mark visited cells to avoid loops
"""


def solve_maze(maze, row, col, path):
    """
    INPUT:
      maze  — 2D list (0=open, 1=wall)
      row, col — current position
      path  — list of (row, col) tuples showing the route so far
    OUTPUT:
      True if a solution was found (and path is updated),
      False if this direction leads to a dead end.
    """
    rows = len(maze)
    cols = len(maze[0])

    # --- BASE CASES ---
    # Out of bounds
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False
    # Hit a wall or already visited (marked as 2)
    if maze[row][col] != 0:
        return False
    # Reached the goal (bottom-right corner)
    if row == rows - 1 and col == cols - 1:
        path.append((row, col))
        return True

    # Mark this cell as visited
    maze[row][col] = 2
    path.append((row, col))

    # --- RECURSIVE EXPLORATION ---
    # Try RIGHT, then DOWN, then LEFT, then UP
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if solve_maze(maze, row + dr, col + dc, path):
            return True  # This direction worked!

    # --- BACKTRACK ---
    # No direction worked — undo this step
    path.pop()
    maze[row][col] = 0   # Unmark so other paths can try this cell
    return False


def print_maze(maze):
    """Prints the maze in a readable grid format."""
    icons = {0: "·", 1: "█", 2: "★"}
    for row in maze:
        print("  " + " ".join(icons.get(cell, str(cell)) for cell in row))
    print()


# ----------------------------------------------------------
# TASK 4A: Run the maze solver and observe the output
# ----------------------------------------------------------

maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
]

# Uncomment to run:
# path = []
# print("Original maze:")
# print_maze([row[:] for row in maze])   # Print a copy
#
# if solve_maze(maze, 0, 0, path):
#     print(f"Solution found! Path taken: {path}")
#     print("\nMaze with path marked (★):")
#     print_maze(maze)
# else:
#     print("No solution exists.")


# ----------------------------------------------------------
# TASK 4B: Experiment (choose one or more)
# ----------------------------------------------------------
# 1. Create your own 5x5 maze (using 0s and 1s) and solve it.
# 2. Modify the solver to count how many cells it BACKTRACKS from.
# 3. Change the exploration order (try UP first, then LEFT) — does
#    it find a different path? Why or why not?
# 4. Can you create a maze with NO solution? What does the solver output?

# YOUR CODE HERE:


"""
=============================================================
  REFLECTION (answer in comments)
=============================================================

1. Which subroutines in your Level 2 report system are PROCEDURES
   and which are FUNCTIONS? How did you decide?

   YOUR ANSWER:

2. In binary search (Level 3), how many comparisons did your
   desk check take to find the target? How does this compare
   to checking every element one by one?

   YOUR ANSWER:

3. In the maze solver (Level 4), what makes this algorithm
   a "backtracking" approach? At what point does it backtrack?

   YOUR ANSWER:

4. How does the structure of your Level 2 code relate to the
   structure chart concept from Worksheet 1?

   YOUR ANSWER:
"""
