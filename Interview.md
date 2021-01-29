## INTERIEW PREPERATION


---------------------------------------

### [1. What are the key features of Python?]()


Python is an interpreted language. That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.
Python is well suited to **object orientated programming** in that it allows the definition of classes along with composition and inheritance. Python does not have access specifiers (like C++’s public, private).
In Python, functions are first-class objects. This means that they can be assigned to variables, returned from other functions and passed into functions. Classes are also first class objects
Writing Python code is quick but running it is often slower than compiled languages. Fortunately，Python allows the inclusion of C-based extensions so bottlenecks can be optimized away and often are. The numpy package is a good example of this, it’s really quite quick because a lot of the number-crunching it does isn’t actually done by Python
Python finds use in many spheres – web applications, automation, scientific modeling, big data applications and many more. It’s also often used as “glue” code to get other languages and components to play nice.



----------------------------------

[2.What type of language is python? Programming or scripting?]()


**Ans:** Python is capable of scripting, but in general sense, it is considered as a general-purpose programming language. To know more about Scripting, you can refer to the Python Scripting Tutorial.


-------------------

## [Q4.Python an interpreted language.]()

Ans: An interpreted language is any programming language which is not in machine-level code before runtime. Therefore, Python is an interpreted language.

Q5.What is pep 8?
Ans: PEP stands for Python Enhancement Proposal. It is a set of rules that specify how to format Python code for maximum readability.

## [Q6. How is memory managed in Python?]()
Ans: Memory is managed in Python in the following ways:

Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap.
The programmer does not have access to this private heap. The python interpreter takes care of this instead.
The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code.
Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.


-------------------------------

## [Q7. What is namespace in Python?]()

**Ans:** A namespace is a naming system used to make sure that names are unique to avoid naming conflicts.

----------------------

## [Q8. What is PYTHONPATH?]()

Ans: It is an environment variable which is used when a module is imported. Whenever a module is imported, PYTHONPATH is also looked up to check for the presence of the imported modules in various directories. The interpreter uses it to determine which module to load.

---------------

## [Q9. What are python modules? Name some commonly used built-in modules in Python?]()

Ans: Python modules are files containing Python code. This code can either be functions classes or variables. A Python module is a .py file containing executable code.

**Some of the commonly used built-in modules are:**

- os
- sys
- math
- random
- data time
- JSON

---------------

##  [What is PEP 8 and why is it important?]()

- PEP stands for Python Enhancement Proposal. A PEP is an official design document providing information to the Python Community, or describing a new feature for Python or its processes. PEP 8 is especially important since it documents the style guidelines for Python Code. Apparently contributing in the Python open-source community requires you to follow these style guidelines sincerely and strictly.

----------------------

##  [How is memory managed in Python?]()

- Memory management in Python is handled by the Python Memory Manager. The memory allocated by the manager is in form of a private heap space dedicated for Python. All Python objects are stored in this heap and being private, it is inaccessible to the programmer. Though, python does provide some core API functions to work upon the private heap space.
Additionally, Python has an in-built garbage collection to recycle the unused memory for the private heap space.

![](https://miro.medium.com/max/656/1*xIJgwPGI-6yjKCMogU152w.png)

---------------------

## [What are Python namespaces? Why are they used?]()


- A namespace in Python ensures that object names in a program are unique and can be used without any conflict. Python implements these namespaces as dictionaries with 'name as key' mapped to a corresponding 'object as value'. This allows for multiple namespaces to use the same name and map it to a separate object. A few examples of namespaces are as follows:

- Local Namespace includes local names inside a function. the namespace is temporarily created for a function call and gets cleared when the function returns.
Global Namespace includes names from various imported packages/ modules that is being used in the current project. This namespace is created when the package is imported in the script and lasts until the execution of the script.

- Built-in Namespace includes built-in functions of core Python and built-in names for various types of exceptions.
Lifecycle of a namespace depends upon the scope of objects they are mapped to. If the scope of an object ends, the lifecycle of that namespace comes to an end. Hence, it isn't possible to access inner namespace objects from an outer namespace.
![](https://assets.interviewbit.com/assets/skill_interview_questions/python/python-namespaces-4d66efcaf95c5b42452c3e14d90c4aa4873c577c8cf72e0f2d9a8bbec9ec5cba.png.gz)


--------------

##  [What is Scope in Python?]()

- Every object in Python functions within a scope. A scope is a block of code where an object in Python remains relevant. Namespaces uniquely identify all the objects inside a program. However, these namespaces also have a scope defined for them where you could use their objects without any prefix. A few examples of scope created during code execution in Python are as follows:

- A local scope refers to the local objects available in the current function.
- A global scope refers to the objects available throught the code execution since their inception.
- A module-level scope refers to the global objects of the current module accessible in the program.
- An outermost scope refers to all the built-in names callable in the program. The objects in this scope are searched last to find the name referenced.
**Note: Local scope objects can be synced with global scope objects using keywords such as global.**

---------------------






