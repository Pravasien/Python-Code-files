def Addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
def Multiplication(a,b):
    return a*b
def Division(a,b):
    return a/b
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
option=int(input("Enter which operation you want to perform 1. Addition 2. Subtraction 3. Multiplication 4. Division:"))
if option==1:
    print("THe addition of two numbers is: ",Addition(x,y))
elif option==2:
    print("The subtraction of two numbers is: ",Subtraction(x,y))
elif option==3:
    print("The multiplication of two numbers is: ",Multiplication(x,y))
elif option==4:
    print("The division of two numbers is: ",Division(x,y))
else:
    print("Invalid option")