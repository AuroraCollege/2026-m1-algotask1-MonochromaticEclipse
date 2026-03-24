"""
=============================================================
  LEVEL 3 — Divide and Conquer: Binary Search
  Understand and implement a classic D&C algorithm.
=============================================================

Binary search works by DIVIDING the problem in half each time:
  - Look at the MIDDLE element of a sorted list
  - If it's the target → found it!
  - If target is SMALLER → search the LEFT half
  - If target is LARGER  → search the RIGHT half
  - Repeat until found or the list is empty

This is classic divide and conquer: each step halves the problem.
"""


# ----------------------------------------------------------
# TASK 3A: Complete the binary search function
# ----------------------------------------------------------

def binary_search(sorted_list, target):
    """
    INPUT:  a sorted list of numbers, and a target to find
    OUTPUT: the INDEX of the target, or -1 if not found

    Fill in the missing parts marked MISSING
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2        # Integer division to find middle index
        middle_value = sorted_list[mid]

        if middle_value == target:
            return mid                  # Found it!
        elif target < middle_value:
            high = MISSING                  # Search LEFT half — update high
        else:
            low = MISSING                   # Search RIGHT half — update low

    return -1  # Target not in list


# Test cases (uncomment when ready):
# numbers = [3, 7, 12, 19, 25, 31, 44, 58, 67, 90]
# print(binary_search(numbers, 25))   # Expected: 4 (index of 25)
# print(binary_search(numbers, 10))   # Expected: -1 (not in list)
# print(binary_search(numbers, 90))   # Expected: 9


# ----------------------------------------------------------
# TASK 3B: Desk check (trace) your binary search
# ----------------------------------------------------------
# On paper (or in comments below), trace binary_search([3,7,12,19,25], 19):
#
# Step | low | high | mid | sorted_list[mid] | Action
# -----|-----|-------|-----|------------------|--------
#  1   |  0  |   4   |  2  |       12         | 19 > 12, set low = mid+1
#  2   |  ?  |   ?   |  ?  |        ?         | ?
#  3   |  ?  |   ?   |  ?  |        ?         | ?
#
# Complete the table above as a comment.
