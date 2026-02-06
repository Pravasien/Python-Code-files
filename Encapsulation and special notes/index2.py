"""
Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.
"""
class Computer:
    __max_price=1000
    def sell(self):
        print("The selling price is: ",self.__max_price)
    def setMaxPrice(self,price):
        self.__max_price=price
        print("Max price is updated to: ",self.__max_price)
obj=Computer()
obj.sell()
obj.setMaxPrice(2000)
obj.__max_price=2000
obj.sell()