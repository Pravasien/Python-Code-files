test_dict = {'Math':'pranav','Sports':'pranav','Music':'rahul','Art':'pranav','Dance':'simran'}
print("The original dictionary : "+str(test_dict)) 
Key_Name='pranav'
res=0
for key in test_dict:
    if test_dict[key] == Key_Name:
        res=res + 1 
print("Frequency of Pranav is : "+str(res))
