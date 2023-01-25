from sympy import Polygon, pi
p1, p2, p3, p4, p5 = [(0, 0), (1, 0), (5, 1), (0, 1), (3, 0)]
poly1=Polygon(p1, p2, p3, p4)
Polygon(p1, p2)
Polygon(p1, p2, p5)


print ("area of polygon is: ",poly1.area)