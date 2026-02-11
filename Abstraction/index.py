"""
Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.
"""
from abc import ABC, abstractmethod
class Class_1(ABC):
    def print(self,x):
        print("The value is: ",x)
    @abstractmethod
    def display(self):
        print("This is an abstract method")
class Childclass(Class_1):
    def display(self):
        print("This is an implementation of abstract method in a child class")
obj=Childclass()
obj.print(100)
obj.display()