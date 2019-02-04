from turtle import *

pu()

setworldcoordinates(-100, -100, 100, 100)

goto(0, -100)

pensize(5)

'This is a note'

bgcolor('black')

pd()
color('blue','gold')
begin_fill()
goto(100, 0)
goto(0, 100)
goto(-100, 0)
goto(0, -100)
end_fill()

pu()

goto(50, 50)

pd()
color('navy', 'blue')
begin_fill()
goto(0, 75)
goto(-50, 50)
goto(-75, 0)
goto(-50, -50,)
goto(0, -75)
goto(50, -50)
goto(75, 0)
goto(50, 50)
end_fill()

pu()
goto(50, 0)
setheading(90)
pd()

color('black', 'red')
begin_fill()
circle(50)
end_fill()

pensize(3)

pu()
goto(-5, 55)

pd()
color('black', 'red')
begin_fill()
goto(-5, 100)
goto(-10, 100)
goto(-10, 55)
goto(-5, 55)
end_fill()

pu()
goto(-23, 45)

pd()
color('black', 'red')
begin_fill()
goto(-23, 90)
goto(-28, 90)
goto(-28, 45)
goto(-23, 45)
end_fill()

pu()
goto(5, 55)

pd()
color('black', 'red')
begin_fill()
goto(5, 100)
goto(10, 100)
goto(10, 55)
goto(5, 55)
end_fill()

pu()
goto(23, 45)

pd()
color('black', 'red')
begin_fill()
goto(23, 90)
goto(28, 90)
goto(28, 45)
goto(23, 45)
end_fill()

#Bottom Portion

pu()
goto(5, -55)

pd()
color('black', 'red')
begin_fill()
goto(5, -100)
goto(10, -100)
goto(10, -55)
goto(5, -55)
end_fill()

pu()
goto(23, -45)

pd()
color('black', 'red')
begin_fill()
goto(23, -90)
goto(28, -90)
goto(28, -45)
goto(23, -45)
end_fill()

pu()
goto(-5, -55)

pd()
color('black', 'red')
begin_fill()
goto(-5, -100)
goto(-10, -100)
goto(-10, -55)
goto(-5, -55)
end_fill()

pu()
goto(-23, -45)

pd()
color('black', 'red')
begin_fill()
goto(-23, -90)
goto(-28, -90)
goto(-28, -45)
goto(-23, -45)
end_fill()

#Sides (bottom)

pu()
goto(55, -5)

pd()
color('black', 'red')
begin_fill()
goto(100, -5)
goto(100, -10)
goto(55, -10)
goto(55, -5)
end_fill()

pu()
goto(45, -23)

pd()
color('black', 'red')
begin_fill()
goto(90, -23)
goto(90, -28)
goto(45, -28)
goto(45, -23)
end_fill()

pu()
goto(-55, -5)

pd()
color('black', 'red')
begin_fill()
goto(-100, -5)
goto(-100, -10)
goto(-55, -10)
goto(-55, -5)
end_fill()

pu()
goto(-45, -23)

pd()
color('black', 'red')
begin_fill()
goto(-90, -23)
goto(-90, -28)
goto(-45, -28)
goto(-45, -23)
end_fill()

#Sides (top)

pu()
goto(55, 5)

pd()
color('black', 'red')
begin_fill()
goto(100, 5)
goto(100, 10)
goto(55, 10)
goto(55, 5)
end_fill()

pu()
goto(45, 23)

pd()
color('black', 'red')
begin_fill()
goto(90, 23)
goto(90, 28)
goto(45, 28)
goto(45, 23)
end_fill()

pu()
goto(-55, 5)

pd()
color('black', 'red')
begin_fill()
goto(-100, 5)
goto(-100, 10)
goto(-55, 10)
goto(-55, 5)
end_fill()

pu()
goto(-45, 23)

pd()
color('black', 'red')
begin_fill()
goto(-90, 23)
goto(-90, 28)
goto(-45, 28)
goto(-45, 23)
end_fill()

pu()
goto(-25, -15)

color('black')
pensize(7)
pd()

goto(-25, 15)
goto(-10, -15)
goto(-10, 15)

pu()
goto(10, -15)
pd()

goto(10, 15)
goto(17.5, -15)
goto(25, 15)
goto(25, -15)

ht()

done()



