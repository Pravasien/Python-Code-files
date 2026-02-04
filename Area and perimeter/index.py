class circle:
    def __init__ (self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
radius = float(input("Enter radius: "))
circ_Rad = circle(radius)
print(circ_Rad.area())
print(circ_Rad.perimeter())