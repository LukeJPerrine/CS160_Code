'''
Week 7
Mondrian
'''

import turtle as t
import random as r

# function definitions
def line(x1, y1, x2, y2):
    t.pu()
    t.goto(x1, y1)
    t.pd()
    t.goto(x2, y2)
    return

def square(x1, y1, x2, y2, color):
    t.pu()
    # make x1, y1 the lower left corner of square and go there
    if x1 >= x2:
        temp = x1
        x1 = x2
        x2 = temp
    if y1 >= y2:
        temp = x1
        x1 = x2
        x2 = temp
    t.goto(x1, y1)

    # draw square
    t.seth(0)
    t.pd()
    t.color(color)
    t.begin_fill()
    t.fd(x2-x1)
    t.lt(90)
    t.fd(y2-y1)
    t.lt(90)
    t.fd(x2-x1)
    t.lt(90)
    t.fd(y2-y1)
    t.end_fill()
    return

def getcolor():
    rand = r.randint(0, 100)
    if rand < 10:
        return "red"
    elif rand < 20:
        return "blue"
    elif rand < 30:
        return "yellow"
    elif rand < 40:
        return "green"
    elif rand < 50:
        return "purple"
    elif rand < 60:
        return "teal"
    elif rand < 70:
        return "black"
    else:
        return "white"

def divide(x1, y1, x2, y2, depth):
    # base case
    if depth <= 0:
        color = getcolor()
        square(x1, y1, x2, y2, color)
        return

    # recursive case
    rand = r.randint(1, 100)
    if rand < 45:      # divide vertical 45% of the time
        # randomly pick line location (between 1/4 and 3/4)
        randx = x1 + r.randint(int((x2-x1)/4), int(3*(x2-x1)/4))
        
        # draw line (3 wide)
        t.color("black")
        t.width(3)
        line(randx, y1, randx, y2);
        t.width(1)
        
        # recurse
        divide(x1, y1, randx-2, y2, depth-1) # +-2 since line width is 3
        divide(randx+2, y1, x2, y2, depth-1)

    elif rand < 90: # divide horizontal 45% of the time
        # randomly pick line location (between 1/4 and 3/4)
        randy = y1 + r.randint(int((y2-y1)/4), int(3*(y2-y1)/4))
        
        # draw line (3 wide)
        t.color("black")
        t.width(3)
        line(x1, randy, x2, randy);
        t.width(1)
        
        # recurse
        divide(x1, y1, x2, randy-2, depth-1) # +-2 since line width is 3
        divide(x1, randy+2, x2, y2, depth-1)
        
    else:               # the rest of the time quit dividing early
        color = "white"
        square(x1, y1, x2, y2, color)

# make the drawing screen like the first quadrant of the xy-plane
width = 600
height = 600
t.setup(width+2, height+2, None, None) # resize window, +2 to avoid scroll bars
t.screensize(width, height) # resize canvas
t.setworldcoordinates(9, 9, width, height) # reset origin, 9 to avoid automatic border

# boilerplate for fastest drawing and coding
t.speed(0)
t.tracer(100, 1)
t.hideturtle()

def draw():
    # these first two clear the screen and draw a border
    square(5, 5, width-5, height-5, "black")
    square(10, 10, width-10, height-10, "white")
    divide(10, 10, width-10, height-10, 5)

t.onkey(draw, 'f')
t.listen()
