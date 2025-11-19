import turtle
turtle.Screen().setup(600,600)
turtle.Screen().bgcolor("orange")
polygon=turtle.Turtle()
num_Sides=6
side_Angle=360/num_Sides
for i in range(num_Sides):
    polygon.forward(100)
    polygon.right(side_Angle)
turtle.done()
    