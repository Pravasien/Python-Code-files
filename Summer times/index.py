temp=float(input("Enter the temperature in °C: "))

if temp<10:
    print("Wear a coat.")
elif 10<=temp<=20:
    print("Wear a sweater.")
elif 21<=temp<=30:
    print("Wear light clothes.")
else:
    print("Range entered is wrong. Please enter a temperature between 10 and 30.")