import math

def find_min_max(*numbers):
    if not numbers:
        return None 

    min_num = max_num = numbers[0]
    for num in numbers[1:]:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    return (min_num, max_num)

# Test Cases
print(find_min_max(4, 7, 2, 9, 0, 3))  # (0, 9)
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))  # (-12, 489)
print(find_min_max(3903, 28, math.e, -90))  # (-90, 3903)
