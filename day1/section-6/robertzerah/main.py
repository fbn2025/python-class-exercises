import math

def find_min_max(*args):
    if not args:
        raise ValueError("At least one number must be provided")
    min_num = float("inf")    # start with the largest possible value for min
    max_num = float("-inf")   # start with the smallest possible value for max
    for num in args:
        min_num = min(min_num, num)
        max_num = max(max_num, num)
    return (min_num, max_num)

test1 = [4, 7, 2, 9, 0, 3]
test2 = [-9, -12, 38, 489, 38, 2, -2]
test3 = [3903, 28, math.e, -90]

print(find_min_max(*test1))
print(find_min_max(*test2))
print(find_min_max(*test3))
