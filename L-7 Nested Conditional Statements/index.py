"""
Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
"""
User_Input_Medical_Email=input("Do you have a medical certificate to present (Y/N): ")
if User_Input_Medical_Email not in ["Y","N"]:
    print("Invalid Input, please enter either Y or N.")
    exit()
else:
    if User_Input_Medical_Email=="Y":
        print("You are allowed to take the exam.")
    else:
        User_Input_Attendance=float(input("Enter your attendance percentage: "))
        if User_Input_Attendance>75:
            print("You are allowed to take the exam.")
        else:
            print("You are not allowed to take the exam.")
