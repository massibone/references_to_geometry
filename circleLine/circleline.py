import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi, linspace


#draw a circle

angles = linspace(0 * pi, 2 * pi, 100 )
r = 1.5
xs = r * cos(angles)
ys = r * sin(angles)
plt.plot(xs, ys, color = 'green')
#draw line
r2 = 1.5
segment_angles = linspace(6/4 * 2* pi, 2 * pi, 80 )
segment_xs = r2 * cos(segment_angles)
segment_ys = r2 * sin(segment_angles)
#plt.plot(segment_xs, segment_ys, color = 'yellow')
plt.plot([4.5, -4], [-0.57, -2.5], color = 'red')
plt.gca().annotate('tangent', xy=(1, -2.8), xycoords='data', fontsize=15, rotation = 17)
seg_x_p1 = r2 * cos(2 * pi)


#draw daimeter
plt.plot(1.5, 0, marker = '.', color = 'blue')
plt.plot(-1.5, 0, marker = '.', color = 'blue')
plt.plot([1.5, -1.5], [0, 0])
plt.gca().annotate('Diameter', xy=(-0.5, -0.25), xycoords='data', fontsize=10)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.gca().set_aspect('equal')
plt.show()

