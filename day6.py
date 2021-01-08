# python3

# Write a program to get unique values from a list

my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)

------------------------------------------------------

# Write a  program to check whether two lists are circularly identical.

A=[]
n=int(input("length of list:"))
print("elements of first list:")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)

B=[]
n1=int(input("length of list:"))
print("Element of the Second List:")
for i in range(int(n1)):
   k=int(input(""))
   B.append(k)
if ' '.join(map(str, B)) in ' '.join(map(str, A * 2)):
   print("lists are circularly identical")
else:
    print("lists are not circularly identical")

--------------------------------------------

# Write a  program to find the second smallest number in a list
   
   list1 = [1,100,200,2000,6000]

list1.sort()

print("Second smallest element is:", list1[1])



--------------------

