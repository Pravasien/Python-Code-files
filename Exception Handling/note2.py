try:
    age = int(input('Enter your age: '))
    if age<=18:
        raise ValueError
except:
    print('You are not allowed to vote')
finally:
    print(age)