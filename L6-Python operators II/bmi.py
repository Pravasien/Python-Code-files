User_Weight=float(input("Enter your weight in kg: "))
User_Height=float(input("Enter your height in meters: "))
User_BMI=User_Weight/(User_Height**2)
if User_BMI<18.4:
    print("Your BMI is ",User_BMI,"which means you are underweight.")
elif User_BMI<24.9:
    print("Your BMI is ",User_BMI,"which means you have a normal weight.")
elif User_BMI<29.9:
    print("Your BMI is ",User_BMI,"which means you are overweight.")
elif User_BMI<34.9:
    print("Your BMI is ",User_BMI,"which means you are obese.")
elif User_BMI<39.9:
    print("Your BMI is ",User_BMI,"which means you are severely obese.")
else:
    print("Your BMI is ",User_BMI,"WHich means you are severely obese , you are going to die , go meet a doctor now!!!")