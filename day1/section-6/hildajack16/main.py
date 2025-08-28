import math

def find_min_max(*args):
    min_num = float("inf") #starts at the largest possible number in python
    max_num = float("-inf") #starts at the smallest possible number in python

    # Loop through the arguments
    for num in args:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return (min_num, max_num)
  
# Test cases
print(find_min_max(4, 7, 2, 9, 0, 3))
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))
print(find_min_max(3903, 28, math.e, -90))
