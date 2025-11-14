n=int(input("Enter the amount of rows you want * to be printed:"))
for i in range(n):
    for h in range(i+1):
        print("*",end="  ")
    print()