#try , except , raise and finally
try:
    a = 5
    b = 6
    print(a)
    print(b)
    z = a+b
    print(c)

except NameError as e: 
    print(e)

finally:
    print(z)
    print('The try and except is executed.')

