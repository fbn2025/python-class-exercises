def find_min_max(*args):
    if not args:
        return None  

    min_num = float("inf")   
    max_num = float("-inf")  

    for num in args:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return (min_num, max_num)


print(find_min_max(5, 8, 4, 6, 0, 3))                 
print(find_min_max(-6, -10, 35, 314, 35, 2, -2))     
import math
print(find_min_max(3504, 28, math.e, -80))          

