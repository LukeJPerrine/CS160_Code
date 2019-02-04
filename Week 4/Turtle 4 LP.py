# Turtle Assignment 4

# Making Spirals

import turtle
import random

# declaration
chadrino = turtle.Turtle()
stacy = turtle.Turtle()
velma = turtle.Turtle()
bixby = turtle.Turtle()

turtle.setworldcoordinates(-1000, -1000, 1000, 1000)

# chadrino set up
chadrino.pu()
chadrino.goto(-150, 600)
chadrino.pensize(20.1)
chadrino.pd()

# stacy set up
stacy.pu()
stacy.goto(-170, 580)
stacy.pensize(20.1)
stacy.pd()

# velma set up
velma.pu()
velma.goto(-190, 560)
velma.pensize(20.1)
velma.pd()

# bixby set up
bixby.pu()
bixby.goto(-210, 540)
bixby.pensize(20.1)
bixby.pd()

# Speeds
chadrino.speed(0)
stacy.speed(0)
velma.speed(0)
bixby.speed(0)

P = 20

R = random.random()
B = random.random()
G = random.random()

R = int(R)
B = int(B)
G = int(G)

stacy.color(R, G, B)
chadrino.color(R, G, B)
velma.color(R, G, B)
bixby.color(R, G, B)

count = 0
while count < 180:
    # move
    chadrino.fd(180 - count)
    chadrino.rt(15)
    stacy.fd(180 - count)
    stacy.rt(15)
    velma.fd(180 - count)
    velma.rt(15)
    bixby.fd(180 - count)
    bixby.rt(15)

    # Color Randomizing
    R = random.random()
    B = random.random()
    G = random.random()
    chadrino.color(R, G, B)
    chadrino.pensize(P)

    print(R, G, B)

    if R > .85 and B > .85 and G > .85:
        R2 = R - .05
        G2 = G - .05
        B2 = B - .05
        R3 = R - .1
        G3 = G - .1
        B3 = B - .1
        R4 = R - .15
        G4 = G - .15
        B4 = B - .15
        stacy.color(R2, G2, B2)
        stacy.pensize(P)
        velma.color(R3, G3, B3)
        velma.pensize(P)
        bixby.color(R4, G4, B4)
        bixby.pensize(P)

    elif R < .85 and B < .85 and G < .85:
        R2 = R + .05
        G2 = G + .05
        B2 = B + .05
        R3 = R + .1
        G3 = G + .1
        B3 = B + .1
        R4 = R + .15
        G4 = G + .15
        B4 = B + .15
        stacy.color(R2, G2, B2)
        stacy.pensize(P)
        velma.color(R3, G3, B3)
        velma.pensize(P)
        bixby.color(R4, G4, B4)
        bixby.pensize(P)

    else:
        stacy.color(R, G, B)
        stacy.pensize(P)
        velma.color(R, G, B)
        velma.pensize(P)
        bixby.color(R, G, B)
        bixby.pensize(P)
    P = P - .1
    count = count + 1

turtle.done()
