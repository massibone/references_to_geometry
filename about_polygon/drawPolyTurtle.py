from turtle import *
from random import randint

# l is lenght, s sides
def drawPoly(x,y,l,s,thickness=False):
    angle=180-(((s-2)*180)/s)
    pensize(thickness)
    up()
    goto(x,y)
    down()
    for i in range(s):
        fd(l)
        color('blue','green')
        rt(angle)
    mainloop()

(drawPoly(0,0,40,6,2))
