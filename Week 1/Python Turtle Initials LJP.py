

'''
Trying to draw my initials
'''

# boilerplate/definitions
import turtle as t
t.speed(1)
t.tracer(1, 1)
#t.ht()
t.st()


'''Setup for initial letter'''
t.pu()
t.bk(220)
t.left(90)
t.fd(240)
t.left(180)

'''L'''
t.pd()
t.fd(220)
t.left(90)
t.fd(120)

'''J'''
t.pu()
t.fd(160)
t.left(90)
t.fd(220)
t.left(90)
t.fd(70)
t.pd()
t.left(180)
t.fd(140)
t.left(180)
t.fd(70)
t.left(90)
t.fd(160)
for x in range(180):
    t.forward(1)
    t.right(1)

t.pu()
t.right(180)
t.fd(60)
t.left(90)

'''P'''
t.fd(240)
t.pd()
t.left(90)
t.fd(160)
for x in range(270):
    t.forward(1)
    t.right(1)
t.fd(58)

t.pu()
t.fd(180)
t.right(90)
t.fd(300)
t.left(90)
t.pd()
t.circle(350)

raw_input()

