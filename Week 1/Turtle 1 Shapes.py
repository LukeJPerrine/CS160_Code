'''
Week 1
This code will draw some common shapes.
'''

# boilerplate
import turtle as t
t.speed(1)
t.tracer(1, 1)
t.ht()
#t.st()

# move to upper left corner
t.pu()
t.rt(180)
t.fd(150)
t.rt(90)
t.fd(50)
t.pd()

# triangle
t.fd(200)
t.lt(120)
t.fd(200)
t.lt(120)
t.fd(200)
t.lt(120)

# move down a bit
t.pu()
t.rt(180)
t.fd(50)
t.pd()

# square
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)

# move down an bit more
t.pu()
t.fd(150)
t.pd()

# pentagon
t.fd(100)
t.rt(72)
t.fd(100)
t.rt(72)
t.fd(100)
t.rt(72)
t.fd(100)
t.rt(72)
t.fd(100)
t.rt(72)

# go toward the middle
t.pu()
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(50)
t.rt(90)
t.pd()

# hexagon
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(60)

# go up a bit
t.pu()
t.lt(90)
t.fd(150)
t.rt(90)
t.pd()

# formula for any polygon?
# how about a circle?

# circle (36 segments)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)
t.fd(10)
t.rt(10)

# move up a bit
t.pu()
t.lt(90)
t.fd(50)
t.rt(90)
t.pd()

# circle command
t.circle(75)

# move to the right side
t.pu()
t.fd(200)
t.pd()

# rosette
t.circle(50)
t.rt(60)
t.circle(50)
t.rt(60)
t.circle(50)
t.rt(60)
t.circle(50)
t.rt(60)
t.circle(50)
t.rt(60)
t.circle(50)
t.rt(60)


# t.exitonclick() # mouse click ends the program 
# t.onkeypress(t.bye, 'f') # keypress ends the program
