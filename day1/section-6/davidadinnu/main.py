import math  

# The import math library helps to evaluate the math.e element which equals 2.17

def find_min_max(*args):
      min_num = min(args) # smallest possible number in python
      max_num = max(args) # largest possible number in python
      print((min_num, max_num))
     

find_min_max(4, 7, 2, 9, 0, 3)
find_min_max(-9, -12, 38, 489, 38, 2, -2)
find_min_max(3903, 28, math.e, -90)

