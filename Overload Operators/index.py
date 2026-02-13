"""
Write a program to overload the less than (<) and equal to (==) operators. For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively. You can additionally create more objects to try different values.
"""
class A:
    def __init__ (self,a):
        self.a=a
    def __lt__(self,other):
        if self.a<other.a:
            return "obj1 is lesser than obj2"
        elif self.a>other.a:
            return "obj2 is lesser than obj1"
        else:
            return "Both may have the same value "
    def __eq__ (self,other):
        if self.a==other.a:
            return "Both are equal"
        else:
            return "Both are unequal"
obj1=A(6)
obj2=A(6)
print("The passed values are",obj1.a,"and",obj2.a)
print(obj1<obj2)
print(obj1==obj2)
