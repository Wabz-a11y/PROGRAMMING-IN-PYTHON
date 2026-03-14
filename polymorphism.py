
"""
Polymorphism : 
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    def display_info(self):
        print("The employee name is: ", self.__name)
        print("Salary is: ", self.__salary)
    
    def display_salary(self):
        return self.__salary
    
    @abstractmethod
    def calculate_salary(self):
        pass

    
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        fulltime = super().display_salary()
        return fulltime

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        parttime = super().display_salary()* 0.5
        return parttime

employeeInfo = Employee("Smith", 55462)
employeeInfo.display_info()

fullTime = FullTimeEmployee("Smith", 55462)
print(fullTime.calculate_salary())

partTime = PartTimeEmployee("Smith", 55462)
print(partTime.calculate_salary())