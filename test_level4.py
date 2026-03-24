import copy

from test_common import get_fn


class TestLevel4:
    """Level 4: Backtracking — Maze Solver (provided code integrity check)"""

    SOLVABLE_MAZE = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
    ]

    UNSOLVABLE_MAZE = [
        [0, 1],
        [1, 0],
    ]

    def _fresh_maze(self, template):
        return copy.deepcopy(template)

    def test_4a_solvable_maze_returns_true(self):
        """solve_maze returns True for a solvable maze"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.SOLVABLE_MAZE)
        result = fn(maze, 0, 0, [])
        assert result is True, "solve_maze should return True for a solvable maze"

    def test_4a_path_is_populated(self):
        """solve_maze populates the path list when a solution is found"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.SOLVABLE_MAZE)
        path = []
        fn(maze, 0, 0, path)
        assert len(path) > 0, "path list should contain cells after solving"

    def test_4a_path_starts_at_origin(self):
        """Path starts at (0, 0)"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.SOLVABLE_MAZE)
        path = []
        fn(maze, 0, 0, path)
        assert path[0] == (0, 0), f"Path should start at (0,0), started at {path[0]}"

    def test_4a_path_ends_at_goal(self):
        """Path ends at the bottom-right corner"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.SOLVABLE_MAZE)
        rows, cols = len(maze), len(maze[0])
        path = []
        fn(maze, 0, 0, path)
        assert path[-1] == (rows - 1, cols - 1), (
            f"Path should end at ({rows-1},{cols-1}), ended at {path[-1]}"
        )

    def test_4a_path_only_visits_open_cells(self):
        """Path only steps through originally open cells (no walls)"""
        fn = get_fn("solve_maze")
        original = self._fresh_maze(self.SOLVABLE_MAZE)
        maze = self._fresh_maze(self.SOLVABLE_MAZE)
        path = []
        fn(maze, 0, 0, path)
        for r, c in path:
            assert original[r][c] == 0, (
                f"Path stepped through a wall at ({r},{c})"
            )

    def test_4a_unsolvable_maze_returns_false(self):
        """solve_maze returns False for an unsolvable maze"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.UNSOLVABLE_MAZE)
        result = fn(maze, 0, 0, [])
        assert result is False, "solve_maze should return False for an unsolvable maze"

    def test_4a_unsolvable_maze_path_is_empty(self):
        """Path list remains empty when no solution exists"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.UNSOLVABLE_MAZE)
        path = []
        fn(maze, 0, 0, path)
        assert path == [], (
            f"Path should be empty for unsolvable maze, got {path}"
        )
