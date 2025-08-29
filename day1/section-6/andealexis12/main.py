import math

def find_min_max(*args):
   
    min_num = min(args)
    max_num = max(args)

    return min(args), max(args)

print(find_min_max(4, 7, 2, 9, 0, 3))         
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))  
print(find_min_max(3903, 28, math.e, -90)) 
