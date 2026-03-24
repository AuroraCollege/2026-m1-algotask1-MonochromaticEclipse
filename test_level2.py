import pytest

from test_common import get_fn


class TestLevel2:
    """Level 2: Top-Down Design — Report System"""

    def test_2a_find_average_basic(self):
        """find_average returns correct average for a simple list"""
        fn = get_fn("find_average")
        result = fn([80, 90, 70])
        assert result == pytest.approx(80.0), (
            f"find_average([80, 90, 70]) should be 80.0, got {result}"
        )

    def test_2a_find_average_returns_float(self):
        """find_average returns a number (int or float), not None"""
        fn = get_fn("find_average")
        result = fn([50, 100])
        assert result is not None, "find_average returned None — did you forget 'return'?"
        assert isinstance(result, (int, float)), (
            f"find_average should return a number, got {type(result)}"
        )

    def test_2a_find_average_single(self):
        """find_average works with a single-element list"""
        fn = get_fn("find_average")
        assert fn([77]) == pytest.approx(77.0)

    def test_2a_find_average_decimals(self):
        """find_average handles non-whole averages"""
        fn = get_fn("find_average")
        result = fn([70, 71])
        assert result == pytest.approx(70.5), (
            f"find_average([70, 71]) should be 70.5, got {result}"
        )

    def test_2a_find_highest_basic(self):
        """find_highest returns the maximum value"""
        fn = get_fn("find_highest")
        assert fn([80, 90, 70]) == 90, (
            "find_highest([80, 90, 70]) should return 90"
        )

    def test_2a_find_highest_returns_value(self):
        """find_highest returns a value, not None"""
        fn = get_fn("find_highest")
        result = fn([55, 72, 88])
        assert result is not None, "find_highest returned None — did you forget 'return'?"

    def test_2a_find_highest_single(self):
        """find_highest works with a single-element list"""
        fn = get_fn("find_highest")
        assert fn([42]) == 42

    def test_2a_find_highest_all_same(self):
        """find_highest works when all scores are equal"""
        fn = get_fn("find_highest")
        assert fn([70, 70, 70]) == 70

    def test_2b_calculate_stats_structure(self):
        """calculate_stats returns a dict with 'average' and 'highest' keys"""
        fn = get_fn("calculate_stats")
        result = fn([80, 90, 70])
        assert result is not None, "calculate_stats returned None — did you forget 'return'?"
        assert isinstance(result, dict), (
            f"calculate_stats should return a dict, got {type(result)}"
        )
        assert "average" in result, "Result dict missing key 'average'"
        assert "highest" in result, "Result dict missing key 'highest'"

    def test_2b_calculate_stats_values(self):
        """calculate_stats returns correct average and highest"""
        fn = get_fn("calculate_stats")
        result = fn([80, 90, 70])
        assert result["average"] == pytest.approx(80.0), (
            f"Expected average 80.0, got {result.get('average')}"
        )
        assert result["highest"] == 90, (
            f"Expected highest 90, got {result.get('highest')}"
        )

    def test_2b_calculate_stats_calls_helpers(self):
        """calculate_stats delegates to find_average and find_highest (not reimplemented inline)"""
        calc = get_fn("calculate_stats")
        avg_fn = get_fn("find_average")
        hi_fn = get_fn("find_highest")
        scores = [55, 72, 88, 61]
        result = calc(scores)
        assert result is not None
        assert result.get("average") == pytest.approx(avg_fn(scores)), (
            "calculate_stats average doesn't match find_average — are you calling it?"
        )
        assert result.get("highest") == hi_fn(scores), (
            "calculate_stats highest doesn't match find_highest — are you calling it?"
        )

    def test_2c_display_report_runs_without_error(self, capsys):
        """display_report runs without raising an exception"""
        fn = get_fn("display_report")
        calc = get_fn("calculate_stats")
        scores = [85, 90, 78]
        stats = calc(scores) if calc(scores) is not None else {"average": 84.3, "highest": 90}
        fn("Alex", scores, stats)

    def test_2c_display_report_prints_something(self, capsys):
        """display_report actually prints output"""
        fn = get_fn("display_report")
        calc = get_fn("calculate_stats")
        scores = [85, 90, 78]
        stats = calc(scores) or {"average": 84.3, "highest": 90}
        fn("Alex", scores, stats)
        captured = capsys.readouterr()
        assert captured.out.strip() != "", (
            "display_report produced no output — did you forget to print anything?"
        )

    def test_2c_display_report_includes_name(self, capsys):
        """display_report output includes the student's name"""
        fn = get_fn("display_report")
        calc = get_fn("calculate_stats")
        scores = [85, 90, 78]
        stats = calc(scores) or {"average": 84.3, "highest": 90}
        fn("Jordan", scores, stats)
        captured = capsys.readouterr()
        assert "Jordan" in captured.out, (
            "display_report output doesn't include the student's name"
        )

    def test_2c_display_report_includes_grade(self, capsys):
        """display_report output includes a grade letter"""
        fn = get_fn("display_report")
        calc = get_fn("calculate_stats")
        scores = [85, 90, 78]
        stats = calc(scores) or {"average": 84.3, "highest": 90}
        fn("Alex", scores, stats)
        captured = capsys.readouterr()
        assert any(g in captured.out for g in ["A", "B", "C", "F"]), (
            "display_report output doesn't include a grade letter (A/B/C/F)"
        )

    def test_2d_run_report_system_runs(self, capsys):
        """run_report_system runs without raising an exception"""
        fn = get_fn("run_report_system")
        fn()

    def test_2d_run_report_system_prints_multiple_students(self, capsys):
        """run_report_system prints output for at least 2 students"""
        fn = get_fn("run_report_system")
        fn()
        captured = capsys.readouterr()
        lines = [l for l in captured.out.strip().splitlines() if l.strip()]
        assert len(lines) >= 2, (
            f"run_report_system printed {len(lines)} line(s) — expected output for at least 2 students"
        )
