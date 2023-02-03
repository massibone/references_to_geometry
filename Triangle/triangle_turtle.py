from turtle import *
import random

import turtle
import random

window=turtle.Screen()

def gen_triangle_points():
    vertices=[]
    for i in range (3):
        x = random.randint(0,300)
        y = random.randint(0,300)
        vertices.append((x,y))
    return vertices

def draw_shape_from_points(vertices):
    pen=turtle.Turtle()
    pen.penup()
    pen.goto(vertices[0])
    pen.pendown()
    for point in vertices[1:]:
        pen.goto(point)
    pen.goto(vertices[0])

vertices=gen_triangle_points()

draw_shape_from_points(vertices)

window.exitonclick()

