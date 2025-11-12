User_Lower=int(input("Enter the lower range: "))
User_Upper=int(input("Enter The upper range: "))
print("The prime numbers between the range",User_Lower,"and",User_Upper,"are: ")
for num in range(User_Lower,User_Upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)