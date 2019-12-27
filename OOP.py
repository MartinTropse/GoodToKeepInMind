# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 13:50:35 2019
@author: MartinTropse
"""
#https://www.youtube.com/watch?v=ZDa-Z5JzLYM

#Data and function associated with specific class, 
#called attributes and methods
#Method = a function associated with a class

#Lesson 1

#Class is a blueprint for creating "instances",
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



"""
Example of first class functions. https://www.youtube.com/watch?v=kr0mpwqttM0

Shows how you can return functions from other functions as variables, by doing
this you can set one part of the function as "static" argument and vary the other one.
The variable that is saved as function inherits its variable from the previous function.
Those variables are NOT defined outside of the function 


This particular function is creating html "lines", either as anchor (p) or heading (h1)
"""
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
