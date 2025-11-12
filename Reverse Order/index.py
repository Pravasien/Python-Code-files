user_input = input("Enter text or number: ")
count = 0
for char in user_input:
    if char.isdigit():
        count = count + 1
print("Total digits:", count)