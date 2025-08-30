import math

def find_min_max(*args):
    min_num = float("inf")   
    max_num = float("-inf")  

    for num in args:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    
    return (min_num, max_num)
  
# TODO: write test cases and pass them to the function. Print the results  
print(find_min_max(4, 7, 2, 9, 0, 3))      

print(find_min_max(-9, -12, 38, 489, 38, 2, -2))  

print(find_min_max(3903, 28, math.e, -90))  

