# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 12:24:18 2019
@author: MartinTropse
"""

class Employee:
    
    raise_amt = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@email.com" 
        
    def fullname(self):
        return print(f"Full name of employee: {self.first} {self.last}")
    
    def salary_raise(self):
        self.pay = self.pay * self.raise_amt
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    @classmethod #An alternative __init__/constructor
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split(' ')
        return cls(first ,last, pay)

    @staticmethod
    def isWorkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.15    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #This collects functions from the parent class Employee
        self.prog_lang = prog_lang #And also sets the arguments to self
   
     
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
   
bitch_1 = Employee("Martin", "Andersson", 40000)
bitch_2 = Employee("Kerstin", "Kempe", 40000)

#Employee.set_raise_amt(1.2)

bitch_2.email
bitch_2.salary_raise()
bitch_2.pay
bitch_1.raise_amt = 1.10
bitch_1.salary_raise()
bitch_1.fullname()
bitch_1.pay
bitch_3 = Employee.from_str('Lili Li 48000')    
bitch_3.email

import datetime
myDate=datetime.date(2019,12,30)
Employee.isWorkday(myDate)

dev1 = Developer('Moritz', 'Buck', 50000, "Python")
dev2 = Developer('Boritz', 'Bucker', 50000, "Cython")


print(help(dev1)) #Show resolution order (order that python check for attributes) among other things
dev1.email
dev1.prog_lang

mng1 = Manager("Sophia", "Renes", 58200, [dev1])
mng1.add_emp(dev2)
mng1.remove_emp(dev1)

mng1.print_emps()




class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f"Fullname: {self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)    
    

myEmp1 = Employee("Martin", "Vanderval")

myEmp1.fullname = "My Man"
myEmp1.email
