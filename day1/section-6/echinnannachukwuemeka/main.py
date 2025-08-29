import math


def find_min_max(*args):
    if not args:
        return None, None
    min_val = min(args)
    max_val = max(args)
    return min_val, max_val

print(find_min_max())
print(find_min_max(4, 7, 2, 9, 0, 3))
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))
print(find_min_max(3903, 28, math.e, -90))
