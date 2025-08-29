# Write a function that finds the min and max number in a list of numbers

# Your function should:

# 1. Take several inputs as arguments find_min_max(arg1, arg2, arg3, …, argn)
# 2. Finds the minimum and maximum number
# 3. Returns both of them as a tuple (minimum, maximum)

# Write a few cases to verify that it works:
# [4, 7, 2, 9, 0, 3]
# [-9, -12, 38, 489, 38, 2, -2]
# [3903, 28, math.e, -90]
import unittest
import math


def find_min_max(*args):
  min_num = float("-inf") # smallest possible number in python
  max_num = float("inf") # largest possible number in python

  if not args:
     return (min_num, max_num)

  for number in args:
    if number > min_num:
      min_num = number
    if number < max_num:
      max_num = number

  min_num, max_num = max_num, min_num

  return (min_num, max_num)

# TODO: write test cases and pass them to the function. Print the results

# --- Test Cases ---
class TestMaxMin(unittest.TestCase):
    """Tests for the find_min_max function."""

    def test_no_argument(self):
        self.assertEqual(find_min_max(), (float("-inf"), float("inf")))

    def test_all_zero_arguments(self):
        self.assertEqual(find_min_max(0, 0, 0, 0, 0), (0, 0))

    def test_single_positive_argument(self):
        self.assertEqual(find_min_max(8), (8, 8))

    def test_single_negative_argument(self):
        self.assertEqual(find_min_max(-4), (-4, -4))

    def test_no_negative_arguments_with_zero(self):
        self.assertEqual(find_min_max(4, 7, 2, 9, 0, 3), (0, 9))

    def test_no_negative_arguments_without_zero(self):
        self.assertEqual(find_min_max(4, 7, 2, 9, 5, 3), (2, 9))

    def test_with_negative_arguments(self):
        self.assertEqual(find_min_max(-9, -12, 38, 489, 38, 2, -2), (-12, 489))

    def test_with_all_negative_arguments(self):
        self.assertEqual(find_min_max(-9, -12, -38, -489, -38, -2, -76), (-489, -2))

    def test_with_exponential_argument(self):
        self.assertEqual(find_min_max(3903, 28, math.e, -90), (-90, 3903))

# --- Test Runner ---
if __name__ == '__main__':
    unittest.main()
