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
   ------------------------------------------------
   
#### Program to generate a random number between 0 and 9

#### importing the random module
import random

print(random.randint(0,9))

-------------------------------

#### Python program to shuffle a deck of card

#### importing modules
import itertools, random

#### make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

#### shuffle the cards
random.shuffle(deck)

#### draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
   
   ----------------------------------
   
#### Q2. What are the key features of Python?


Python is an interpreted language. That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.
Python is dynamically typed, this means that you don’t need to state the types of variables when you declare them or anything like that. You can do things like x=111 and then x="I'm a string" without error
Python is well suited to object orientated programming in that it allows the definition of classes along with composition and inheritance. Python does not have access specifiers (like C++’s public, private).
In Python, functions are first-class objects. This means that they can be assigned to variables, returned from other functions and passed into functions. Classes are also first class objects
Writing Python code is quick but running it is often slower than compiled languages. Fortunately，Python allows the inclusion of C-based extensions so bottlenecks can be optimized away and often are. The numpy package is a good example of this, it’s really quite quick because a lot of the number-crunching it does isn’t actually done by Python
Python finds use in many spheres – web applications, automation, scientific modeling, big data applications and many more. It’s also often used as “glue” code to get other languages and components to play nice.

---------------
#### Q3. What type of language is python? Programming or scripting?
Ans: Python is capable of scripting, but in general sense, it is considered as a general-purpose programming language. To know more about Scripting, you can refer to the Python Scripting Tutorial.

#### Q4.How is Python an interpreted language?
Ans: An interpreted language is any programming language which is not in machine-level code before runtime. Therefore, Python is an interpreted language.

Q5.What is pep 8?
Ans: PEP stands for Python Enhancement Proposal. It is a set of rules that specify how to format Python code for maximum readability.

Q6. How is memory managed in Python?
Ans: 

Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.
The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code.
Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.
Q7. What is namespace in Python?
Ans: A namespace is a naming system used to make sure that names are unique to avoid naming conflicts.

Q8. What is PYTHONPATH?
Ans: It is an environment variable which is used when a module is imported. Whenever a module is imported, PYTHONPATH is also looked up to check for the presence of the imported modules in various directories. The interpreter uses it to determine which module to load.

Q9. What are python modules? Name some commonly used built-in modules in Python?
Ans: Python modules are files containing Python code. This code can either be functions classes or variables. A Python module is a .py file containing executable code.

Some of the commonly used built-in modules are:

- os
- sys
- math
- random
- data time
- JSON

-------------
 
 
