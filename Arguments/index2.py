def cube(num):
    return num*num*num
def divisible_by_three(num):
    if num%3==0:
        return cube(num)
    else:
        return False
print(divisible_by_three(9))
print(divisible_by_three(3))