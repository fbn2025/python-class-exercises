import math
def find_min_max(*args):
  min_num = float("-inf") # smallest possible number in python
  max_num = float("inf") # largest possible number in python

  for i in args:
    if i > min_num:
       min_num = i
    if i < max_num:
       max_num = i

  min_num, max_num = max_num, min_num     

  return (min_num, max_num)

print(find_min_max(-1, -5, -3, -4))
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))
print(find_min_max(3903, 28, math.e, -90))
