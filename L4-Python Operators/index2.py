amount=int(input("Enter the amout you want to withdraw:"))
dollar_100_notes=amount//100
dollar_50_notes=(amount%100)//50
dollar_10_notes=((amount%100)%50)//10
print("Number of $100 notes: ",dollar_100_notes)
print("Number of $50 notes: ",dollar_50_notes)
print("Number of $10 notes: ",dollar_10_notes)