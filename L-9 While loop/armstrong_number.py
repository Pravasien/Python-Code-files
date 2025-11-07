User_Num=int(input("Enter a number: "))
sum=0
temporary_Number=User_Num
while temporary_Number>0:
    digit=temporary_Number%10
    print(digit)
    sum=sum+digit**3
    print(sum)
    temporary_Number=temporary_Number//10
    print(temporary_Number)
if sum==User_Num:
    print(User_Num,"Is an amstrong number")
else:
    print(User_Num,"Is not an amstrong number")