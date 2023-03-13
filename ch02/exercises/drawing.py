import turtle

sides = int(input("Please enter the number of sides that you want: "))
length = int(input("Please enter the length that you want: "))


angle = 360/sides

s = turtle.Screen()
t = turtle.Turtle()
t.color("blue")

for i in range(sides):
    t.right(angle)
    t.forward(length)

s.exitonclick()