import random
numbers = [0,1,2,3,4,5,6,7,8,9]
small_alphabets = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m",]
Capital_Alphabets=["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
symbols = ["!","@","#","$","%","^","&","*",",","-","_","=","+"]
password = ""

for i in range(10):
    choice = random.randint(1, 4)
    if choice == 1:
        password += str(random.choice(numbers))
    elif choice == 2:
        password += random.choice(small_alphabets)
    elif choice == 3:
        password += random.choice(Capital_Alphabets)
    else:
        password += random.choice(symbols)
print("Your password's:", password)