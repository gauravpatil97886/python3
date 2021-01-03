- python3
#write a program to get a list sorted in increasing order by the last elemenet
 #  in each tuple from a given  list of non-empty tuples
#   Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
   
   def last(n):
    return n[-1]

   def sort_list(tuples):
  return sorted(tuples, key=last)
   print (([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
   print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

   
   
##   Write a  program to remove duplicates elements from a list.
   
   a = [10,10,10,20,20]

list1 = set()
l11 = []
for x in a:
    if x not in list1:
         l11.append(x)
        list1.add(x)

print(list1)



