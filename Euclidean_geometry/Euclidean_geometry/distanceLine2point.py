import numpy as np
p1=np.array([0,0])
p2=np.array([10,10])
p3=np.array([5,7])
d=np.cross(p2-p1,p3-p1)/np.linalg.norm(p2-p1)
print(d)
