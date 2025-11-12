string=input("Enter a string: ").lower()
char=input("Enter a character to find its frequency in the string you have inputed (in lowercase): ").lower()
i=0
count=0
while i<len(string):
    if string[i]==char:
        count=count+1
    i=i+1
print("The frequency of the character",char,"in the string is: ",count)