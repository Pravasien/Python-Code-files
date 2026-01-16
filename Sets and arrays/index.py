"""
Write a program to create a set and perform the following operations on that set- 1. Create a set with integer elements 2. Create a set with mixed data type elements 3. Create another set with elements - 1, 2, 3, 4, 3, 2 4. Create a set from a list with elements - [1, 2, 3, 2] 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]"""

Set_1={1,2,3,4,5}

Set_2={"Hello world",10,5.642,True}

Set_3={1,2,3,4,3,2,}

List_1=[1,2,3,2]

set_4={0,1,3,4,5}
set_4.remove(0)
print("Set without first element: ",set_4)