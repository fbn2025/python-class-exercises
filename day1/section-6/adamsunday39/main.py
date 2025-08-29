def find_min_max(*args):
    if not args:
        return None, None  # handle empty input

    min_num = float("inf")   # start with largest possible number for min
    max_num = float("-inf")  # start with smallest possible number for max

    for num in args:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return (min_num, max_num)


# Test cases
print(find_min_max(4, 7, 1, 9, 0))     # (0, 9)
print(find_min_max(-5, -1, -10, -3))   # (-10, -1)
print(find_min_max(100))               # (100, 100)
print(find_min_max())                  # (None, None)
print(find_min_max(3.5, 2.1, 4.8, 0.0)) # (0.0, 4.8) 
