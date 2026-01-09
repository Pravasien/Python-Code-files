user_input=int(input("Enter a number: "))
user_end=int(input("Enter the end number: "))
lst=[]
for i in range(user_input,user_end+1):
    r=i**2
    lst.append(r)
print("Squares:", lst)
el=[]
od=[]
for item in lst:
    if item%2==0:
        el.append(item)
    else:
        od.append(item)
print("Even squares:", el)
print("Odd squares:", od)