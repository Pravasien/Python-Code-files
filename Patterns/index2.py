User_Row=int(input("Enter the amount of rows you want: "))
num=1
for i in range(1,User_Row+1):
    for j in range(1,i+1):
        print(num,end="")
        num=num+1
    print()