"""
Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.
"""
class myclass:
    __privateVar=100
    def __privMeth(self):
        print("This is a function inside the class namely myclass")
    def hello(self):
        print("The value of privateVar is: ",self.__privateVar)
obj=myclass()
obj.hello()
obj.__privMeth()