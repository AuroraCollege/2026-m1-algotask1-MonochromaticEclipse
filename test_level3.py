from test_common import get_fn


class TestLevel3:
    """Level 3: Divide and Conquer — Binary Search"""

    NUMBERS = [3, 7, 12, 19, 25, 31, 44, 58, 67, 90]

    def test_3a_finds_element_in_middle(self):
        """binary_search finds a value near the middle of the list"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 25) == 4, (
            "binary_search([3,7,12,19,25,31,44,58,67,90], 25) should return 4"
        )

    def test_3a_finds_first_element(self):
        """binary_search finds the first element"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 3) == 0, (
            "binary_search should return 0 for the first element"
        )

    def test_3a_finds_last_element(self):
        """binary_search finds the last element"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 90) == 9, (
            "binary_search should return 9 for the last element (90)"
        )

    def test_3a_returns_negative_one_when_missing(self):
        """binary_search returns -1 when target is not in the list"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 10) == -1, (
            "binary_search should return -1 when target is not found"
        )

    def test_3a_returns_negative_one_below_range(self):
        """binary_search returns -1 for a value below the list range"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 1) == -1

    def test_3a_returns_negative_one_above_range(self):
        """binary_search returns -1 for a value above the list range"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 999) == -1

    def test_3a_single_element_found(self):
        """binary_search works on a single-element list when target is present"""
        fn = get_fn("binary_search")
        assert fn([42], 42) == 0

    def test_3a_single_element_not_found(self):
        """binary_search works on a single-element list when target is absent"""
        fn = get_fn("binary_search")
        assert fn([42], 7) == -1

    def test_3a_two_elements_first(self):
        """binary_search finds the first of two elements"""
        fn = get_fn("binary_search")
        assert fn([10, 20], 10) == 0

    def test_3a_two_elements_second(self):
        """binary_search finds the second of two elements"""
        fn = get_fn("binary_search")
        assert fn([10, 20], 20) == 1

    def test_3a_returns_an_index_not_the_value(self):
        """binary_search returns the INDEX, not the value itself"""
        fn = get_fn("binary_search")
        result = fn(self.NUMBERS, 31)
        assert result == 5, (
            f"binary_search should return index 5 for value 31, got {result}. "
            "Make sure you're returning the index, not the value."
        )
