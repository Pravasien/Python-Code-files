n = int(input("Enter the amount of rows you want * to be printed: "))
if n <= 0:
	print("Please enter a positive integer greater than 0.")
else:
	for i in range(n):
		left = "* " * (i + 1)
		middle = "  " * (n - i - 1)
		right = left
		print(left + middle + right)