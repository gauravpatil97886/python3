

--------------------------------

1.  Write a program to create a dictionary from two lists without losing duplicate values.
Program:--



key_list = []
no = int(input("Enter the length of a key_list "))
print("Enter elements of key_list ")
for i in range(no):
 key_list.append(int(input()))
value_list = []
no = int(input("Enter the length of a value_list "))
print("Enter elements of value_list ")
for i in range(no):
 value_list.append(int(input()))
print ("Original key list is = " + str(key_list)) 
print ("Original value list is = " + str(value_list)) 
result = {} 
for key in key_list: 
    for value in value_list: 
        result[key] = value 
        value_list.remove(value) 
        break  
print ("Resultant dictionary is= " +  str(result))
Output:--
Enter the length of a key_list 4
Enter elements of key_list 
1
2
3
4
Enter the length of a value_list 4
Enter elements of value_list 
10
20
20
30
Original key list is = [1, 2, 3, 4]
Original value list is = [10, 20, 20, 30]
Resultant dictionary is= {1: 10, 2: 20, 3: 20, 4: 30}

---------
---------------

