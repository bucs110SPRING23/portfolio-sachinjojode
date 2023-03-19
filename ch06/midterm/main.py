import turtle

#main function
def main():
    xpos, ypos = make_a_circle(20,-40,135,'black','brown')
    make_a_circle(20,xpos-(2*xpos),ypos,'black','brown')
    make_a_circle(50,0,75,'black','brown')
    vertoval(100,35,-75,'black','brown')
    heading(0)
    xpos, ypos = make_a_circle(30,45,-125,'black','brown')
    make_a_circle(30,xpos-(2*xpos),ypos,'black','brown')
    xpos, ypos = make_a_circle(25,65,10,'black','brown')
    make_a_circle(25,xpos-(2*xpos),ypos,'black','brown')
    xpos, ypos = make_a_circle(10,15,125,'black','white')
    make_a_circle(10,xpos-(2*xpos),ypos,'black','white')
    xpos, ypos = make_a_circle(7,15,125,'black','black')
    make_a_circle(7,xpos-(2*xpos),ypos,'black','black')
    make_a_circle(5,0,112,'black','black')
    jack.penup()
    jack.setpos(-16,105)
    jack.pendown()
    heading(270)
    smile(16,180)
    jack.hideturtle()

#make circles
def make_a_circle(radius,position_x,position_y,pen_color,fill_color):
    jack.pen(fillcolor = fill_color, pencolor = pen_color)
    jack.begin_fill()
    jack.penup()
    jack.setpos(position_x,position_y)
    jack.pendown()
    jack.circle(radius)
    jack.end_fill()
    x_pos, y_pos = jack.position()
    return x_pos, y_pos
    
#make vertical ovals
def vertoval(radius,position_x,position_y,pen_color,fill_color):
    jack.pen(fillcolor = fill_color, pencolor = pen_color)
    jack.begin_fill()
    jack.penup()
    jack.setpos(position_x,position_y)
    jack.pendown()
    jack.left(45)
    for i in range(2):
        jack.circle(radius,90)
        jack.circle(radius/2,90)
    jack.end_fill()    

#set heading
def heading(number):
    jack.setheading(number)
    
#make smile/arc
def smile(rad,arcdegree):
    jack.circle(rad,arcdegree)
    
#initialize turtle
window = turtle.Screen()
window.bgcolor("light blue")

jack = turtle.Turtle()
jack.color("blue")
jack.shape("turtle")
jack.pensize(2)
jack.speed(0)

main()

window.exitonclick()

