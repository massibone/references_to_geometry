

from sympy import Eq, plot_implicit
from sympy.abc import x, y
import math
import matplotlib.pyplot as plt
from numpy import sin, cos, pi

r=9
po=plot_implicit(Eq(x ** 2 + y ** 2, r), aspect_ratio=(1, 1))
PI = 3.142
#sqrt(x**2+y**2)-r   ||  r=√(A/π) || A= π * r**2

#r=math.sqrt(A/PI)
A=PI * r**2
#point (3,4)
p1=3
p2=4
plt.plot(p1,p2, color = 'red', marker = 'o')
distance= math.sqrt(p1**2 + p2**2) - (math.sqrt(r))
po2 = plot_implicit(x**2, line_color='crimson', show=False)
po.append(po2[0])

print(distance)