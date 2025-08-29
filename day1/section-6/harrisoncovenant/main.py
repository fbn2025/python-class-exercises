def find_min_max(*args):
    if not args:
        return None  # case 1: no numbers given

    if len(args) == 1:
        # case 2: only one number, min and max are the same
        return (args[0], args[0])

    min_num = float("inf")   # start with the largest possible number
    max_num = float("-inf")  # start with the smallest possible number

    for num in args:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return (min_num, max_num)  # case 3: two or more numbers


# Test cases
print(find_min_max(4, 7, 2, 9, 0, 3))                 # (0, 9)
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))      # (-12, 489)
import math
print(find_min_max(3903, 28, math.e, -90))         
