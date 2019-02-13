# Python Turtle Week 5 Luke Perrine

# Imports
import turtle as garbo
import random as r

# Makes the initial drawing window
width = 600
height = 600
garbo.setup(width+2, height+2, None, None)
garbo.screensize(width, height)
garbo.setworldcoordinates(9, 9, width, height)

# Turtle Initial Setup
garbo.speed(0)
garbo.pensize(8)
garbo.hideturtle()


# Sets the vertex positions in order to create the cube.
pos = [[100, 300],
       [300, 300],
       [100, 100],
       [300, 100],
       [200, 400],
       [400, 400],
       [200, 200],
       [400, 200]]

# draw the vertices
for v in pos:
    garbo.pu()
    garbo.goto(v[0], v[1])
    garbo.pd()
    garbo.dot(30, "green")

# initialize a graph matrix
mat = [[0, 1, 1, 0, 1, 0, 0, 0],
       [1, 0, 0, 1, 0, 1, 0, 0],
       [1, 0, 0, 1, 0, 0, 1, 0],
       [0, 1, 1, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 1, 1, 0],
       [0, 1, 0, 0, 1, 0, 0, 1],
       [0, 0, 1, 0, 1, 0, 0, 1],
       [0, 0, 0, 1, 0, 1, 1, 0],]

# This part makes the edge drawings between the nodes.
for row in range(len(mat)):
    for col in range(len(mat[row])):
        if mat[row][col]:
            garbo.pu()
            garbo.goto(pos[row][0], pos[row][1])
            garbo.pd()
            garbo.goto(pos[col][0], pos[col][1])
# To keep the program open
garbo.done()
        
    
    






