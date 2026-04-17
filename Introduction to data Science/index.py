import numpy as np
Student_Data_Type=[("Name","S15"),("Class",int),("Height",float)]
Student_Info=[("Michael",8,1.65),("Sam",6,1.5),("Chris",4,1.2)]
array_Students=np.array(Student_Info,dtype=Student_Data_Type)
print("Orriginal array: ",Student_Info)
print("Sorted Array: ",np.sort(array_Students,order="Height"))