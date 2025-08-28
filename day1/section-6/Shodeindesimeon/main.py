# Write a function that finds the min and max number in a list of numbers

import unittest
import math

def find_min_max(*args):
    min_num = float("inf") # smallest possible number in python
    max_num = float("-inf") # largest possible number in python
  
    for num in args:
      if num < min_num:
          min_num = num
      if num > max_num:
          max_num = num

    return (min_num, max_num)

# TO DO: Write test cases and pass them to the function.

# Manual test cases
print("Manual Test Cases:")
print(f"find_min_max(4, 7, 2, 9, 0, 3) = {find_min_max(4, 7, 2, 9, 0, 3)}")
print(f"find_min_max(-9, -12, 38, 489, 38, 2, -2) = {find_min_max(-9, -12, 38, 489, 38, 2, -2)}")
print(f"find_min_max(3903, 28, math.e, -90) = {find_min_max(3903, 28, math.e, -90)}")

# Unit tests
class TestToFindMinMax(unittest.TestCase):
    def test_case_first(self):
        self.assertEqual(find_min_max(4, 7, 2, 9, 0, 3), (0, 9))
  
    def test_case_second(self):
        self.assertEqual(find_min_max(-9, -12, 38, 489, 38, 2, -2), (-12, 489))
  
    def test_case_third(self):
        self.assertEqual(find_min_max(3903, 28, math.e, -90), (-90, 3903))

if __name__ == '__main__':
    unittest.main()

