bill = float(input("Enter bill amount: $"))
paid = float(input("Enter payment received: $"))
due = bill - paid

if due > 0:
    print("Amount due: $",due)
    
elif due == 0:
    print("Payment complete!")
    pass
else:
    print("Refund: $",abs(due))