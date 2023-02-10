from matplotlib.patches import Polygon
import matplotlib.pyplot as plt


import math
def get_angle(a, b, c):
   angle = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
   return angle + 360 if angle < 0 else angle

def solve(points):
   n = len(points)
   for i in range(len(points)):
      p1 = points[i-2]
      p2 = points[i-1]
      p3 = points[i]
      if get_angle(p1, p2, p3) > 180:
         return False
   return True

points = [(3,4), (4,7),(7,9),(8,9),(12,7),(10,1),(5,2)]
print(solve(points))

polygon1 = Polygon([(3,4), (4,7),(7,9),(8,9),(12,7),(10,1),(5,2),])


fig, ax = plt.subplots(1,1)

ax.add_patch(polygon1)


plt.ylim(0,16)
plt.xlim(0,16)
plt.show()