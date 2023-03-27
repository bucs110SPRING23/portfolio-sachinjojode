#import json

#def main():
    #filename = ".blank"
    #fptr = open(filename, "r")
    #accumulator = 0
    #for ch in fptr.read():
        #if ch.isalnum():
            #accumulator +=1
    #fptr.close()
    #return accumulator 

#result = main()
#print(result)

# protocols
# ---http
# ---xml
# ---json - javascript object notation
#    -string formats, not file formats

#3/23/2023
# managing complexities - advanced programming just manages complexity
# Unix - 10000 SLOC (source lines of code)
# Chrome - 10,000,000 SLOC
# OS X - 100,000,000 SLOC

# Complex Objects
# - primitives: int, str, float, lists, dict, tuple
# - turtle: x(int), y(int), color(color), heading(int), speed(int), pensize(int), shape(str)

# bundle data and functions together
# - state: the current values of the data in the object
# behavior: the functions that operate on the data in the object

# Point
# - object should do one thing
# state: x,y, color
# behavior: draw, move, rotate, scale, change_color

# Classes == Type
        #import turtle

        #t = turtle.Turtle()
        #print(type(t)) #complex
        #print(type(1)) #primitive

# class are blueprints for objects
# - functions are stored algorithms
# - classes as a stored data type
# - classes are not executable
# - don't put executable code in global scope, definitions are fine

# Point class
# - instance: an object created from a specific class
#    - t = turtle.Turtle() is an instance of the Turtle class
# - instance variable: an internal variable that is part of an instance
#     - t.x, t.pos, # x and pos are instance variables
# - interface: the functions and variables of an object
#    - t.forward, t.x, t.pos, t.color, t.shape, t.speed, t.pensize part of interface of turtle
# dunders: double underscore on both sides of name
# adding self.var ties the scope of var to the object scope

#class Point:
    #def __init__(self): #self is the instance being created
        #self.x = 0 # dot operator accesses instance variables of an object
        #self.y = 0
        #self.color = "red"

### main.py
#import point # it's just an example, that's why it doesn't work 

#p1 = point.Point() #p1 is an instance of the Point class
#p1.x = 10

#p2 = point.Point() #p2 is an instance of the Point class
#p2.x = 5

# state of p1(x=10, y=0, color="red") and p2(x=5, y=0, color="red")

class ColorPoint:
    def __init__(self): #self is the instance being created
        self.x = 0 # dot operator accesses instance variables of an object
        self.y = 0
        self.color = "red"