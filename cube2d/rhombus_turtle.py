from turtle import Screen, Turtle
from random import randint

def draw_art_cube(x, y):
    screen.onscreenclick(None)  # type: ignore # Disable handler inside handler

    pen.up()
    pen.setposition(x, y)
    pen.down()

    width = randint(25, 100)
    draw_triangle(width)

    screen.onscreenclick(draw_art_cube)  # Reenable handler on exit

def draw_triangle(short):

    long = short * 2**0.5

    pen.setheading(0)

    for _ in range(4):
        pen.forward(short)
        pen.left(135)
        pen.forward(long)
        pen.left(135)
        pen.forward(short)

        pen.left(180)

screen = Screen()
screen.setup(575, 575)

pen = Turtle()
pen.hideturtle()
pen.speed('fastest')
pen.pensize(2)

screen.onscreenclick(draw_art_cube(150,100))
screen.onscreenclick(draw_triangle(100))
screen.mainloop()