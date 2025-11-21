def Circumference():
    from math import pi
    radius=int(input("Enter the radius of the circle: "))
    circumference = 2 * pi * radius
    print("The circumference of the circle is: ", circumference)
    return circumference
Circumference()