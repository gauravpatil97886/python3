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


# Write a  program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
lst = []
n = int(input("length of a list: "))
print("Enter list elements: ")
count = 0;
for i in range(n):
    l1 = input()
    lst += [l1]
    if len(l1) > 1 and l1[0] == l1[-1]:
        count = count + 1
print("Given list is : ",lst)
print("number of strings having same first and last character in a list : ",count)



