import math

def find_min_max(*args):
    try:
      return f'In the list {args}, \n \t the minimum value is {min(args)}, and maximum value is {max(args)}'
    except ValueError:
        return "ValueError encountered: No value was supplied."

print(find_min_max())
print(find_min_max(4, 7, 2, 9, 0, 3))
print(find_min_max(-9, -12, 38, 489, 38, 2, -2))
print(find_min_max(3903, 28, math.e, -90))
