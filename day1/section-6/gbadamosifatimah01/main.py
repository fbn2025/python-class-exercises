def find_min_max(*args):
  min_num = float("-inf") # smallest possible number in python
  max_num = float("inf") # largest possible number in python
  
  return (min_num, max_num)
  

# TODO: write test cases and pass them to the function. Print the results

import math
def find_min_max(*numbers):
  min_num = float("-inf") # smallest possible number in python
  max_num = float("inf") # largest possible number in python
  
  for i in range(len(numbers)):
    for num in numbers:
      if numbers[i] == num:
        pass
      elif numbers[i] < num:
        min_num = numbers[i]
        max_num = num
        
      elif numbers[i] > num:
        min_num = num
        max_num = numbers[i]
        break

    for num in numbers:
      if min_num > num:
        min_num = num
      if max_num < num:
        max_num = num        

  return (min_num, max_num)

# TODO: write test cases and pass them to the function. Print the results

print(find_min_max(4, 7, 2, 9, 0, 3))
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))
print(find_min_max(3903, 28, math.e, -90))

print("My samples cases:")
print(find_min_max(2, 3, 28, 927, -1087, -2, 0, 91, -365))
print(find_min_max(-2, 0, 2, -8, 57, 34, 75, 1, -21, 32, -1))




