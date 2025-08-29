# Write a function that finds the min and max number in a list of numbers

# Your function should:

# 1. Take several inputs as arguments find_min_max(arg1, arg2, arg3, …, argn)
# 2. Finds the minimum and maximum number
# 3. Returns both of them as a tuple (minimum, maximum)

# Write a few cases to verify that it works:
# [4, 7, 2, 9, 0, 3]
# [-9, -12, 38, 489, 38, 2, -2]
# [3903, 28, math.e, -90]
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
print(find_min_max(4, 7, 2, 9, 0, 3))
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))
print(find_min_max(3903, 28, math.e, -90))
