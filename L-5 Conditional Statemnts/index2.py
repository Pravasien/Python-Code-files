Cost_Price=int(input("Enter cost price: "))
Selling_Price=int(input("Enter selling price: "))
if Selling_Price>Cost_Price:
    Profit=Selling_Price-Cost_Price
    print("You have scammed the person of$",Profit)
else:
    Loss=Cost_Price-Selling_Price
    print("You have been scammed of$",Loss)