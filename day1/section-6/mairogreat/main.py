#TODO: write test cases and pass them to the function. Print the results


import math

def find_min_max(*args):
    """Finds the minimum and maximum number among the arguments."""
    if not args:  # handle empty input
        return None, None
    
    minimum = min(args)
    maximum = max(args)
    return (minimum, maximum)


# Test cases
print(find_min_max(4, 7, 2, 9, 0, 3))           # (0, 9)
print(find_min_max(-9, -12, 38, 489, 38, 2, -2)) # (-12, 489)
print(find_min_max(3903, 28, math.e, -90))       # (-90, 3903)
