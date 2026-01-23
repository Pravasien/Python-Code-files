
n = int(input("Enter a number: "))
odd_numbers = [num for num in range(1, n)
                if num % 2 != 0]
print("Odd numbers:", odd_numbers)

fruits = ["apple", "banana", "guava","orange", "Mango"]
fruits_capitalized = [fruit.capitalize() for fruit in fruits]
print("Original fruits:", fruits)
print("Capitalized fruits:", fruits_capitalized)