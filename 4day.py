# python3 @python3

----------------------
-  #numbers of a specified list after removing even numbers from it. aGet input from user for every program
-------------------------
list1 = [10, 21, 4, 45, 66, 93,11,22,33,45,65,44,78,34,7,8] 
print(" numbers of a specified list after removing even numbers from it. aGet input from user for every program")  

for num in list1: 
      
   
    if num % 2 == 0:
      print(num, end = " ")
      
      

 ------------------------------     
 - #program to find the list of words that are longer than n from a given list of words     
 ------------------------------     
 str=input("enter strings : ")
a=str.split(" ")
b=[]
n=int(input("enter value of n "))
for i in a:
   if (len(i)> n) :
      b.append(i)
print("list of words : ",b)


-------------------------
- #check list is empty or not
--------------------------

l = [3,3,3,3]
if not l:
  print("List is empty")
else:
    print ("list is not empty")
      
      
      
      
      
