
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(-10,10,100)
circle = plt.Circle((3, -6), 6.0, color='blue', fill=False,label='x² + y² - 6x + 12y + 9 = 0')
fig=plt.gcf()
ax=fig.gca()# (or if you have an existing figure)

ax.add_patch(circle)
ax.axis('equal')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x, 2*x+10, '-b', label='y=2x+10')
plt.plot(x, -1/2*x-4.5,'-.g', label='y=-1/2x-4.5')

plt.legend(loc='upper left')
plt.show()

