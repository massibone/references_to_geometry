import turtle
import random
colors=['blue' , 'red', 'orange', 'green']
 
def cpolygon(n, size, colors):
    angle = 360/n
    for i in range(n):
        turtle.pencolor(random.choice(colors)) #chooses a random element in the given list 'colors'
        turtle.forward(100)
        turtle.left(angle)
    turtle.mainloop()
 
cpolygon(12, 100, colors)