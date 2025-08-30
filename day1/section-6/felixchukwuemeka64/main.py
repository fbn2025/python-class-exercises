import math
def find_min_max(*args):
    if not args:  # edge case: no input
        return None, None

    min_num = float("inf")   # largest possible number
    max_num = float("-inf")  # smallest possible number

    for num in args:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return min_num, max_num



print(find_min_max(-5, 0, 100, 20, -200))  

print(find_min_max(3, 5, 7, 2, 8))   

print(find_min_max (100, 6000, -78, 56000, -9000) )

print(find_min_max (3903, 28, math.e, -90))
