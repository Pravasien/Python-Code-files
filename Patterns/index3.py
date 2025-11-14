User_Row=int(input("Enter the nuber of rows you want for your diamond: "))
if User_Row%2==0:
    Half_Diamond=int(User_Row/2)
else:
    Half_Diamond=int(User_Row/2)+1
space=Half_Diamond-1
for i in range(1,Half_Diamond+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()
space=1
for i in range(1,Half_Diamond):
    for j in range(1,space+1):
        print("",end=" ")
    space=space+1
    num=1
    for j in range (1,2*(Half_Diamond-i)):
        print(end=str(num))
        num=num+1
    print()