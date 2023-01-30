import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()
ax.scatter(1,5, 1.5)
cir = plt.Circle((1.5, 1.5), 1.20, color='b',fill=False)
ax.set_aspect('equal', adjustable='datalim')
ax.add_patch(cir)
plt.show()