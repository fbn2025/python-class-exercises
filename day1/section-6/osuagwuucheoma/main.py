def find_min_max(*args):
  min_num = float("inf") # largest possible number in python
  max_num = float("-inf") # smallest possible number in python
  for n in args:
      if n < min_num:
          min_num = n
      if n > max_num:
          max_num = n
  return (min_num, max_num)
      
print (find_min_max(4, 7, 2, 9, 0, 3))
print (find_min_max(-9, -12, 38, 489, 38, 2, -2))

# TODO: write test cases and pass them to the function. Print the results

