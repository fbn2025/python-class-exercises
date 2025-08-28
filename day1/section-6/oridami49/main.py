def find_min_max(*args):
    if not args:
        return None  # handle case when no numbers are passed

    min_num = float("inf")   
    max_num = float("-inf")  

    for num in args:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return (min_num, max_num)


# Test cases
print(find_min_max(4, 7, 2, 9, 0, 3))                 # (0, 9)
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))      # (-12, 489)
import math
print(find_min_max(3903, 28, math.e, -90))            # (-90, 3903)
