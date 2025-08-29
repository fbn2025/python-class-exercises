# Write a function that finds the min and max number in a list of numbers

# Your function should:

# 1. Take several inputs as arguments find_min_max(arg1, arg2, arg3, …, argn)
# 2. Finds the minimum and maximum number
# 3. Returns both of them as a tuple (minimum, maximum)

# Write a few cases to verify that it works:
# [4, 7, 2, 9, 0, 3]
# [-9, -12, 38, 489, 38, 2, -2]
# [3903, 28, math.e, -90]

# TODO: write test cases and pass them to the function. Print the results

import math
def find_min_max(*args):
    if not args:
        raise ValueError("At least one number is required")
    min_num = float("inf")  # largest possible number in python
    max_num = float("-inf") # smallest possible number in python
    for x in args:
        if x < min_num:
            min_num = x
        if x > max_num:
            max_num = x
    return (min_num, max_num)

print(find_min_max(4, 7, 2, 9, 0, 3))                 # -> (0, 9)
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))      # -> (-12, 489)
print(find_min_max(3903, 28, math.e, -90))            # -> (-90, 3903)

