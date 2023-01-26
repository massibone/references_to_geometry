import matplotlib.pyplot as plt
import numpy as np

x=[-1 ,0.5 ,1,-0.5]
y=[ 0.5,  1, -0.5, -1]


#circle1 = plt.Circle((0, 0), 0.2, color='r')
circle2 = plt.Circle((0.5, 0.5), 0.2, color='blue')
#circle3 = plt.Circle((1, 1), 0.2, color='g', clip_on=False)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

#ax.add_patch(circle1)
ax.add_patch(circle2)

#ax.add_patch(circle3)

plt.axis('equal')
plt.show()