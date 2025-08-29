# def find_min_max(*args):
#   min_num = float("-inf") # smallest possible number in python
#   max_num = float("inf") # largest possible number in python
  
#   return (min_num, max_num)

# TODO: write test cases and pass them to the function. Print the results
# TODO: write test cases and pass them to the function. Print the results

import math

def find_min_max(*args):
    min_num = float("inf")   
    max_num = float("-inf")  

    for num in args:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return (min_num, max_num)

print(find_min_max(4, 7, 2, 9, 0, 3))             # answer (0, 9)
print(find_min_max(-9, -12, 38, 489, 38, 2, -2)) # answer (-12, 489)
print(find_min_max(3903, 28, math.e, -90))       # answer (-90, 3903)

