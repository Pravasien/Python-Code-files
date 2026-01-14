Student_Database={
    "Student_1":{"Name":["Pranav"],"Class":[8],"Subjects":["Maths","Science","English"]},
    "Student_2":{"Name":["Arnav"],"Class":[7],"Subjects":["Geography","History","English"]},
    "Student_3":{"Name":["Adhvik"],"Class":[9],"Subjects":["Maths","Biology","Chemistry"]},
    "Student_4":{"Name":["Pranav"],"Class":[8],"Subjects":["Maths","Science","English"]}
}
Student_Duplication={}
for key,value in Student_Database.items():
    if value not in Student_Duplication.values():
        Student_Duplication[key]=value
print(Student_Duplication)

