- python3
## write a program to get a list sorted in increasing order by the last elemenet
   in each tuple from a given  list of non-empty tuples
    def last(n):
    return n[-1]

   def sort_list(tuples):
  return sorted(tuples, key=last)
   print (([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
   print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
