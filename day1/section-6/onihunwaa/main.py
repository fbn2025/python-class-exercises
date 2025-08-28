import math

def find_min_max(*args):
    if not args:
        raise ValueError("At least one number is required")
    return (min(args), max(args))

print(find_min_max(4, 7, 2, 9, 0, 3))                 
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))      
print(find_min_max(3903, 28, math.e, -90))            
