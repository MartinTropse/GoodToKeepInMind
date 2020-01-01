# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 13:50:35 2019
@author: MartinTropse
"""
#https://www.youtube.com/watch?v=ZDa-Z5JzLYM #All videos in the series are listed below in the link

#Data and function associated with specific class, 
#called attributes and methods
#Method = a function associated with a class


"""
Python OOP Lesson 1:  

Shows how you can return functions from other functions as variables, by doing
this you can set one part of the function as "static" argument and vary the other one.
The variable that is saved as function
#Class is a blueprint for creating "instances"""

class Employee:
    
    def __init__(self,first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self): #Self needs to be in each method (i.e class function)  
        return print(f"Employee fullname {self.first} {self.last}")
        
"""the constructor / or initalization
This by default the argument to a class
and is by conventrion refered to as self"""

emp_1 = Employee("Martin", "Andersson", "50000000") #2 instances of the Employee Class
emp_2 = Employee("Lili", "Li", "10000000") #This is an instance

emp_1.fullname() #Here the instance argument self is passed from emp_1
Employee.fullname(emp_1) #This is identical, but we give the insantce argument as is "typically done"


#Lesson 2   
"""Difference between class variable and instance variables 
Class variables are constant through all instances while instance variables 
can be modified for each instance. 

Python first looks for variables within the instance, then within class or other 
classes it inheirited from. 
"""

class Employee:
    raise_amount = 1.05 
    
    def __init__(self,first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):  
        return print(f"Employee fullname {self.first} {self.last}")

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount #This creates the ability to change attribute
        #for an instance, since it will look there before checking if exists as a class variable 

#Employee.raise_amount

emp_1 = Employee("Martin", "Andersson", 5000) 
emp_2 = Employee("Lili", "Li", 10000)
  
emp_2.raise_amount = 1.50 

emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.pay)
print(emp_2.pay)


"""=============================================================================
Lesson 3: Classmethods and staticmethods
============================================================================="""
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))



"""=============================================================================
Lesson 4: Python OOP, Inheritance - Creating Subclasses

In this Python Object-Oriented Tutorial, we will be learning about inheritance and how
to create subclasses. Inheritance allows us to inherit attributes and methods from a 
parent class. This is useful because we can create subclasses and get all of the 
functionality of our parents class, and have the ability to overwrite or add completely 
new functionality without affecting the parents class in any ways.
============================================================================="""

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()


"""
OOP Lesson 5: Special (Magic/Dunder) Methods

In this Python Object-Oriented Tutorial, we will be learning about special methods. 
These are also called magic or dunder methods. These methods allow us to emulate built-in types 
or implement operator overloading. These can be extremely powerful if used correctly. 
We will start by writing a few special methods of our own and then look at how some of them 
are used in the Standard Library. Let's get started.

Dunder = double underscore  
"""
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay): #Init is the most common special method
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self): #This changes what the repr function does with the instance objects
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self): #This changes what the str function does with the instance objects
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other): #This changes what the "+" operator behaves with the instance objects
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname()) #We specify that len on the instance checks the length of the fullname by default


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1 + emp_2)


print(len(emp_1)) 
print(emp_1+emp_2)
print(str(emp_1))
print(repr(emp_1))

"""=============================================================================
Python OOP: Property Decorators - Getters, Setters, and Deleters

In this Python Object-Oriented Tutorial, we will be learning about the property decorator. 
The property decorator allows us to define Class methods that we can access like attributes. 
This allows us to implement getters, setters, and deleters. 
============================================================================="""
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname


"""=============================================================================
Example of first class functions. https://www.youtube.com/watch?v=kr0mpwqttM0 

Inherits its variable from the previous function.
Those variables are NOT defined outside of the function 

This particular function is creating html lines, either as anchor (p) or heading (h1)
============================================================================="""
def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1') 
#print(msg) #This will return an error since msg is not defined outside of the print_h1 function

print_h1('Test Headline!') #Notice 
print_h1('Another Headline!')

#print_p = html_tag('p') #This way you can change the "static" function  
#print_p('Test Paragraph!' )
"""=============================================================================
Closures 
============================================================================="""
"""
A closure is an inner function that has access to variables in it local scope which it 
was created, even after the outer function has fininshed excuting
"""

def outer_func():
    message = 'Hi' #This variable is local to the function
    
    def inner_func():
        print(message) #A free variable that is inherited from the outer function
        
    return inner_func() #Notice that it returns and exectured function

outer_func()



def outer_func(msg):
    message = msg
    
    def inner_func():
        print(message)
        
    return inner_func()

hi_unc = outer_func("Hi") #Becomes the inner_func since that is returned #Also the outerfunction will "stay" executed, i.e the message hi is stored in my_func
hello_unc = outer_func("Hello") #now there is two seperate msg variables and neither is global

"""Another Example of closures"""

import logging 
logging.basicConfig(filename='example.log', level=logging.INFO) #Creates a logfile

def logger(func):  #So the function takes another function as argument
    def log_func(*args): #This allows the function to have any number of arguments 
        logging.info(
            f'Running {func.__name__} with arguments {args}') #So the function used as argument will be in the func.__name__
        print(func(*args))
    return log_func

def add(x,y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add) #Keeps the name of the function in memory 
sub_logger = logger(sub)

add_logger(3,3)
add_logger(5,5)

sub_logger(10,7)
sub_logger(10,4)


"""=============================================================================
Decorator section
Can add new functionallity across many functions. This reduces risk of errors, 
since a small piece of code can then be implemented and edited to any function. 
============================================================================="""

def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function()
    return wrapper_function

def display():
    print('Display function ran')
    
decorated_display = decorator_function(display)
 
decorated_display() #So the wrapper function is returned. This is then executed, which in turn returns the executed display function 
# =============================================================================
#This will create identical results and is the standardized way of writing it 
def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function()
    return wrapper_function

@decorator_function
def display(): 
    print('Display function ran')

display()
 


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs) #Allows an unspecified amount of keyword and positional arguments 
    return wrapper_function

@decorator_function
def display(): 
    print('Display function ran')

@decorator_function
def display_info(name,age):
    print('Display_info ran with arguments ({}, {})'.format(name, age))

display()

display_info('Martin',77)


"""One of the most common usages for decorators in python is for logging, how many times 
was a function run and with which arguments. A timer is another one. """ 

# Decorators
from functools import wraps #Used this to wrap around the orig function, in order to preserve its information
#Becomes necessary when using multiple decorators, which returns functions to each other in succession.
#Here it would cause the time decorator to return wrapper rather then sending the display_info function to the 
#logger decorater. 

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)   



