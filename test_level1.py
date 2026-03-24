from test_common import get_fn


class TestLevel1:
    """Level 1: Procedures and Functions"""

    def test_1c_grade_A(self):
        """calculate_grade returns 'A' for scores >= 90"""
        fn = get_fn("calculate_grade")
        assert fn(90) == "A", "Score of 90 should return 'A'"
        assert fn(95) == "A", "Score of 95 should return 'A'"
        assert fn(100) == "A", "Score of 100 should return 'A'"

    def test_1c_grade_B(self):
        """calculate_grade returns 'B' for scores 75–89"""
        fn = get_fn("calculate_grade")
        assert fn(75) == "B", "Score of 75 should return 'B'"
        assert fn(80) == "B", "Score of 80 should return 'B'"
        assert fn(89) == "B", "Score of 89 should return 'B'"

    def test_1c_grade_C(self):
        """calculate_grade returns 'C' for scores 60–74"""
        fn = get_fn("calculate_grade")
        assert fn(60) == "C", "Score of 60 should return 'C'"
        assert fn(62) == "C", "Score of 62 should return 'C'"
        assert fn(74) == "C", "Score of 74 should return 'C'"

    def test_1c_grade_F(self):
        """calculate_grade returns 'F' for scores below 60"""
        fn = get_fn("calculate_grade")
        assert fn(59) == "F", "Score of 59 should return 'F'"
        assert fn(40) == "F", "Score of 40 should return 'F'"
        assert fn(0) == "F", "Score of 0 should return 'F'"

    def test_1c_returns_a_value(self):
        """calculate_grade must return a value, not print it"""
        fn = get_fn("calculate_grade")
        result = fn(85)
        assert result is not None, (
            "calculate_grade returned None — did you use 'return' instead of 'print'?"
        )

    def test_1c_boundary_exactly_90(self):
        """Boundary check: score of exactly 90 is an A, not a B"""
        fn = get_fn("calculate_grade")
        assert fn(90) == "A", "Score of exactly 90 should be 'A' (>= 90)"

    def test_1c_boundary_exactly_75(self):
        """Boundary check: score of exactly 75 is a B, not a C"""
        fn = get_fn("calculate_grade")
        assert fn(75) == "B", "Score of exactly 75 should be 'B' (>= 75)"

    def test_1c_boundary_exactly_60(self):
        """Boundary check: score of exactly 60 is a C, not an F"""
        fn = get_fn("calculate_grade")
        assert fn(60) == "C", "Score of exactly 60 should be 'C' (>= 60)"
