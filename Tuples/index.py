"""Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple
"""
Tuple_Mix=(1,"Banana",3.14159,True,-45,"a","Hello world")
print("Tuples with dfferent datatypes:",Tuple_Mix)

Tuple_Int=(1,2,3,4,5,4,5,6,7,8,9,0)
print("Tuple of integers: ",Tuple_Int)

Tuple_Add_9=Tuple_Mix+(9,)
print("New tuple after adding 9:",Tuple_Add_9)

Count_Element=Tuple_Int.count(4)
print("Count of elements in the tuple:",Count_Element)

Tuple_Slicing=Tuple_Int[2:7]
print("Slicing the tuple from index notation 2 to 7:",Tuple_Slicing)