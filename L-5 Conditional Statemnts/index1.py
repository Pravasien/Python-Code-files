a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if a>=b:
    print(a,"is the largest number")
else:
    print(b,"is the largest number")

c=input("Enter a string: ")
d=input("Enter another string: ")
if len(c)>len(d):
    print(c,"is longer than",d)
else:
    print(d,"is longer than",c)