import math
def find_min_max(*args):
  # min_num = float("-inf") # smallest possible number in python
  # max_num = float("inf") # largest possible number in python
  if not args:
    return "None" "None"
  min_num = min(args)
  max_num = max(args)
  
  return (min_num, max_num)

# TODO: write test cases and pass them to the function. Print the results

print(find_min_max(4, 7, 2, 9, 0, 3))
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))
print(find_min_max(3903, 28, math.e, -90))
