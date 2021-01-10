## Python3

**Python Program to Print Hello world!**

 print('Hello, world!')
 
 -------------------------------------------------
 -----------------------------------------

# Python Program to find the area of triangle

a = 5
b = 6
c = 7

#### Uncomment below to take inputs from the user
#### a = float(input('Enter first side: '))
#### b = float(input('Enter second side: '))
#### c = float(input('Enter third side: '))

#### calculate the semi-perimeter
s = (a + b + c) / 2

#### calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

-----------------------------------------
------------------------------------------
-----------------------------------------

#### Python program to find the largest number among the three input numbers

#### change the values of num1, num2 and num3
#### for a different result
num1 = 10
num2 = 14
num3 = 12

#### uncomment following lines to take three numbers from user.

#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

------------------------------------
-----------------------------------

#### Python program to check if year is a leap year or not

year = 2000

#### To get year (integer input) from the user
#### year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
   
   
   -----------------------------------------------
 
 
