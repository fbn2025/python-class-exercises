import math
def find_min_max(*args):
  min_num = float(1e309) # largest possible number in python
  max_num = float(-1e309) # smallest possible number in python
  for n in args:
      if n < min_num:
          min_num = n
      if n > max_num:
          max_num = n
  return (min_num, max_num)

# TODO: write test cases and pass them to the function. Print the results

case_1 = [4, 7, 2, 9, 0, 3]
case_2 = [-9, -12, 38, 489, 38, 2, -2]
case_3 = [3903, 28, math.e, -90]

print(find_min_max(*case_1))
print(find_min_max(*case_2))
print(find_min_max(*case_3))
