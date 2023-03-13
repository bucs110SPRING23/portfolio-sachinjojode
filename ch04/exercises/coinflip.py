import turtle
import random

s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.speed(0)

distance = 50
angle = 90
is_in_screen = True

while is_in_screen:
    coin = random.randint(0,1)
    if coin:
        t.right(angle)
    else:
        t.left(angle)
    t.forward(50)
    
    turtleX = t.xcor()
    turtleY = t.ycor()

    x_range = s.window_width() / 2
    y_range = s.window_height() / 2

    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        is_in_screen = False

s.exitonclick()