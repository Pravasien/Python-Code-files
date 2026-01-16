"""Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array."""
first_array=[1,3,5,3,7,9,3]
occurunce_of_3_in_Array=first_array.count(3)
print("The number of occurence of 3 in the array is: ",occurunce_of_3_in_Array)
first_array.reverse()
print("The reversed array is: ",first_array)

Second_Array=["Pranav","Arnav","Adhvik","Pranav","Pran","Aadit","Pranav"]
occurence_of_Pranav_in_Second_Array=Second_Array.count("Pranav")
print("The number of occurence of pranav in the second array is: ",occurence_of_Pranav_in_Second_Array)
Second_Array.reverse()
print("The reversed second array is: ",Second_Array)
