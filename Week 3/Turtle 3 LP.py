# Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.

import turtle
import random
from random import randint

# Initial Turtle Setup
chad = turtle.Turtle()
turtle.setworldcoordinates(-500, -500, 500, 500)
chad.pu()
chad.ht()
chad.home()
chad.pd()
chad.speed(0)
turtle.Screen().bgcolor("PaleVioletRed1")
chad.pensize(3)

# Color Bank
Colors = ["darkblue", "darkcyan", "royalblue", "cyan", "purple", "navy", "mediumvioletred", "cadetblue", "magenta2",
          "midnightblue", "turquoise"]

# Initial Random Color Choice
chad.color((random.choice(Colors)), (random.choice(Colors)))

# Uses Randint to choose shape
count = 0
while count < 20:

    shape = randint(1, 3)

    if shape == 1:

        # Standard Snowflake
        chad.begin_fill()
        for i in range(10):
            for j in range(2):
                chad.forward(100)
                chad.right(60)
                chad.forward(100)
                chad.right(120)
            chad.right(40)
        chad.end_fill()

    elif shape == 2:

        # Medium Snowflake
        chad.begin_fill()
        for i in range(10):
            for j in range(3):
                chad.forward(80)
                chad.left(50)
                chad.forward(80)
                chad.left(130)
            chad.left(40)
        chad.end_fill()

    else:

        # Small Snowflake
        chad.begin_fill()
        for i in range(10):
            for j in range(3):
                chad.forward(60)
                chad.left(80)
                chad.forward(60)
                chad.left(100)
            chad.left(40)
        chad.end_fill()

    count = count + 1
    chad.pu()
    chad.goto((random.randrange(-475, 475, 1)), (random.randrange(-475, 475, 1)))
    chad.rt(random.randrange(45, 180, 5))
    chad.color((random.choice(Colors)), (random.choice(Colors)))
    chad.pd()

