try:
    num_1,num_2=eval(input("Enter two numbers seperated by commas: "))
    output=num_1/num_2
    print("The result is:",output)
except ZeroDivisionError as e:
    print(e)
except SyntaxError as e:
    print(e)
except:
    print("An error has occured")
finally:
    print("Try in multiple exceptions have been executed.")