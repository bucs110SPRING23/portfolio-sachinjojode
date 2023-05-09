import turtle
import random
import pygame
import math

screen = turtle.Screen()
g = turtle.Turtle()
h = turtle.Turtle()

g.penup()
h.penup()
g.goto(-100,20)
h.goto(-100,-20)
g.pendown()
h.pendown()

#Race 1
g.forward(random.randrange(1,100))
h.forward(random.randrange(1,100))
g.penup()
h.penup()
g.goto(-100,20)
h.goto(-100,-20)
g.pendown()
h.pendown()

#Race 2
for i in range(50):
    g.forward(random.randrange(1,10))
    h.forward(random.randrange(1,10))
g.penup()
h.penup()
g.goto(-100,20)
h.goto(-100,-20)
g.pendown()
h.pendown()

screen.exitonclick()

#Part B
pygame.init()
size = (600,600)
window = pygame.display.set_mode(size)
window.fill("white")

#triangle
points = []
num_sides = 3
side_length = 100
xpos = 300
ypos = 300
for i in range(num_sides):
    angle = 360 / num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    x=int(x)
    y = ypos + side_length * math.sin(radians)
    y=int(y)
    points.append((x,y))

pygame.draw.polygon(window, "red", points)
pygame.display.update()

pygame.time.wait(1000)
window.fill("black")
pygame.display.flip()

#square
points = []
num_sides = 4
side_length = 100
xpos = 300
ypos = 300
for i in range(num_sides):
    angle = 360 / num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    x=int(x)
    y = ypos + side_length * math.sin(radians)
    y=int(y)
    points.append((x,y))

pygame.draw.polygon(window, "white", points)
pygame.display.update()

pygame.time.wait(1000)
window.fill("white")
pygame.display.flip()

#hexagon
points = []
num_sides = 6
side_length = 100
xpos = 300
ypos = 300
for i in range(num_sides):
    angle = 360 / num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    x=int(x)
    y = ypos + side_length * math.sin(radians)
    y=int(y)
    points.append((x,y))

pygame.draw.polygon(window, "blue", points)
pygame.display.update()

pygame.time.wait(1000)
window.fill("gray")
pygame.display.flip()

#icosagon
points = []
num_sides = 20
side_length = 100
xpos = 300
ypos = 300
for i in range(num_sides):
    angle = 360 / num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    x=int(x)
    y = ypos + side_length * math.sin(radians)
    y=int(y)
    points.append((x,y))

pygame.draw.polygon(window, "pink", points)
pygame.display.update()

pygame.time.wait(1000)
window.fill("red")
pygame.display.flip()

#Hectagon
points = []
num_sides = 100
side_length = 200
xpos = 300
ypos = 300
for i in range(num_sides):
    angle = 360 / num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    x=int(x)
    y = ypos + side_length * math.sin(radians)
    y=int(y)
    points.append((x,y))

pygame.draw.polygon(window, "green", points)
pygame.display.update()

pygame.time.wait(1000)
window.fill("purple")
pygame.display.flip()

#Circle
points = []
num_sides = 360
side_length = 200
xpos = 300
ypos = 300
for i in range(num_sides):
    angle = 360 / num_sides
    radians = math.radians(angle * i)
    x = xpos + side_length * math.cos(radians)
    x=int(x)
    y = ypos + side_length * math.sin(radians)
    y=int(y)
    points.append((x,y))

pygame.draw.polygon(window, "orange", points)
pygame.display.update()

pygame.time.wait(1000)