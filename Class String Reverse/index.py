n = int(input("Enter how many values you want to be reversed ?"))
my_list = []
for i in range(n):
    value = input("Enter value: ")
    my_list.append(value)
reversed_list = []
for value in my_list:
    reversed_list.append(value[::-1])
print("Reversed list:", reversed_list)