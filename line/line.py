import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x / 2 + 3

t = np.arange(-10, 10, 0.5)

def findPCSlope(m):
  
    return -1.0 / m
  
m = 2.0
p = np.arange(-10, 10, 0.5)

  


plt.plot(m,findPCSlope(m))
plt.plot(t, f(t))




plt.show()