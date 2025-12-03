try:
    User_Input=int(input("Enter a number: "))
    print("The number you entered is:",User_Input)
except ValueError as e:
    print(e)