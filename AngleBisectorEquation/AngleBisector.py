#A(-2,7) B(4,1) C(-3,0)
from sympy import *
y = Symbol('y')
x = Symbol('x')
def biFinder(p1x, p1y, p2x, p2y, p3x, p3y):
    """Finds the angle bisector when given the xy coordinates of three
    points on the angle, assuming point 1 as the vertex."""
    
    lenba = (p1x-p2x, p1y-p2x) 
    lenbc = (p3x-p2x, p3x-p2y) 
    lenbp = (x-y,y-1) 
    p= lenbp*lenba/(lenba)**0.5
    p1=lenbp*lenba/(lenbc)**0.5
    return (p,p1)

