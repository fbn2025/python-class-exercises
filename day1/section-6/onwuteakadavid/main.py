import math 

def find_min_max(*args):
  min_num = float("inf") # smallest possible number in python
  max_num = float("-inf") # largest possible number in python
  
   # Loop through arguments
  for num in args:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    
  return (min_num, max_num)

# TODO: write test cases and pass them to the function. Print the results

list_of_numbers = [3903, 28, math.e, -90]
Min_max = find_min_max(*list_of_numbers)
print (Min_max)
