# Write a function that finds the min and max number in a list of numbers

import math

# The import math library helps to evaluate the math.e element which equals 2.17

def find_min_max(*args):
    min_num = float("inf") 
    max_num = float("-inf") 
  
    for num in args:
      if num < min_num:
          min_num = num
      if num > max_num:
          max_num = num

    return (min_num, max_num)

# TODO: write test cases and pass them to the function. Print the results
# --- Test Cases ---

print("Test Cases:")
print(f"find_min_max(4, 7, 2, 9, 0, 3) = {find_min_max(4, 7, 2, 9, 0, 3)}")
print(f"find_min_max(-9, -12, 38, 489, 38, 2, -2) = {find_min_max(-9, -12, 38, 489, 38, 2, -2)}")
print(f"find_min_max(3903, 28, math.e, -90) = {find_min_max(3903, 28, math.e, -90)}")
