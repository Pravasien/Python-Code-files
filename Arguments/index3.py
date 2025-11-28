def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print("The factorial of 0:",factorial(0))
print("The factorial of 5:",factorial(1))
print("The factorial of 5:",factorial(4))
print("The factorial of 5:",factorial(5))
print("The factorial of 5:",factorial(10))