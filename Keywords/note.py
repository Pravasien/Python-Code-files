User_Input=str(input("Enter a word to check the presence of the letter a: ")).lower()
for i in User_Input:
    if (i=="a"):
        print("A is present in the word")
        break
else:
    print("A is not found in the word entered")