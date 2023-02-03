import turtle
import matplotlib.path as mplP

t1 = turtle.Turtle()

polygon_points = [[0, 0],
        [100, 0],
        [100, 100],
        [0, 100],
        ]
  
t1.penup()
t1.speed(0)
t1.hideturtle()
  
for point in polygon_points:
    t1.setposition(point)
    t1.pendown()

t1.home()
t1.penup()

poly_path = mplP.Path(polygon_points)
point = (20, 20)
t1.setposition(point)
string1 = str(point) + " in polygon: " + str(poly_path.contains_point(point))
t1.write(string1)

point = (90, 35)
t1.setposition(point)
string1 = str(point) + " in polygon: " + str(poly_path.contains_point(point))
t1.write(string1)

turtle.done()