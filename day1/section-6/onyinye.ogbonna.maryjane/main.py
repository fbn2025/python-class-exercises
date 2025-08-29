import math

def find_min_max(*args):
  
  try:
    return (min(args), max(args))
  except ValueError:
    print(("At least one number is required"))
   

print(find_min_max(4, 7, 2, 9, 0, 3))
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))
print(find_min_max(3903, 28, math.e, -90))

# TODO: write test cases and pass them to the function. Print the results

# TODO: write test cases and pass them to the function. Print the results

