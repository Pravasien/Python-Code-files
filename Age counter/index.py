age=int(input("Enter your age: "))
if age<18:
    ValueError
    print("You must be at least 18 years old.")
else:
    print("Access granted.")

age2=int(input("Enter your age again: "))
if age%2==0:
    print("Your age is even.")
else:
    print("Your age is odd.")