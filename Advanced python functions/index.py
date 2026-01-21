num1=[1,3,5]
num2=[2,4,6]
result=map(lambda x,y:x+y,num1,num2)
print("Addition of two lists: ")
print(list(result))

num_square=[1,2,3,4,5]
def square(n):
    return n*n
squared_result=list(map(square,num_square))
print("Square of number in the list: ",squared_result)