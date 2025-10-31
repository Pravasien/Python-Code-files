"""
Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.
"""
User_Choice=input("Select you ride preference (BIKE/CAR): ").lower()
if User_Choice not in ["bike","car"]:
    print("Invalid Input, please enter either BIKE or CAR.")
    exit()
else:
    if User_Choice=="car":
        Car_Choice=input("Select your car preference (Y/N) clutch").lower()
        if Car_Choice=="y":
            print("You have selected a car with clutch.")
        else:
            print("You have chosen a car without clutch.")
    else:
        Bike_Choice=input ("Select your bike preference (Two/Three) wheeler: ").lower()
        if Bike_Choice=="two":
            print("You have selected a two-wheeler bike.")
        else:
            print("You have selected a three-wheeler bike.")