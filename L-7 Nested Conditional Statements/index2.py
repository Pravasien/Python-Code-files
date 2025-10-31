"""
Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.
"""
User_Units=float(input("Enter the number of electricity units consumed: "))
if User_Units<=50:
    Unit_Cost=2.60
    Tax_Units=25
    Total_Cost= (User_Units*Unit_Cost)+Tax_Units
elif User_Units>50 and User_Units<=100:
    Unit_Cost=3.25
    Tax_Units=35
    Total_Cost=(User_Units*Unit_Cost)+Tax_Units
elif User_Units>100 and User_Units<=200:
    Unit_Cost=5.26
    Tax_Units=45
    Total_Cost=(User_Units*Unit_Cost)+Tax_Units
else:
    Unit_Cost=8.45
    Tax_Units=75
    Total_Cost=(User_Units*Unit_Cost)+Tax_Units
print("Your final electricity bill will sum up to a grand total of: $",Total_Cost)