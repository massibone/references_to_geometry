from math import *
import math

print("First Traingle")
a = float(input("enter the value for height: "))
b = float(input("enter the value for b: "))
c = float(input("enter the value for c: "))
print("Enter value for second Triangle:")
a1 = float(input("enter the value for height: "))
b1 = float(input("enter the value for b: "))
c1 = float(input("enter the value for c: "))
if (a + b >= c) and (b + c >= a) and (c + a >= b):
    print("it's a triangle")

    A = degrees(acos((b**2 + c**2 - a**2)/(2*b*c)))
    B = degrees(acos((c**2 + a**2 - b**2)/(2*c*a)))
    C = degrees(acos((a**2 + b**2 - c**2)/(2*a*b)))
else:
    print("it's not a triangle")


if (a1 + b1 >= c1) and (b1 + c1 >= a1) and (c1 + a1 >= b1):
    print("This second data is a triangle")

    A1 = degrees(acos((b**2 + c**2 - a**2)/(2*b*c)))
    B1 = degrees(acos((c**2 + a**2 - b**2)/(2*c*a)))
    C1 = degrees(acos((a**2 + b**2 - c**2)/(2*a*b)))
else:
    print("This is not a triangle")





def side_side_side(sides_one, sides_two):
   # sorting same pace
   sides_one.sort()
   sides_two.sort()
   # checking the conditions
   if sides_one[0] / sides_two[0] == sides_one[1] / sides_two[1] \
      and sides_one[1] / sides_two[1] == sides_one[2] / sides_two[2] \
      and sides_one[2] / sides_two[2] == sides_one[0] / sides_two[0]:
      return True
   return False
def side_angle_side(sides_one, sides_two, angles_one, angles_two):
   # sorting same pace
   sides_one.sort()
   sides_one.sort()
   angles_one.sort()
   angles_one.sort()
   # checking conding 1
   if sides_one[0] / sides_two[0] == sides_one[1] / sides_two[1]:
      if angles_one[0] == angles_two[0]:
         return True
   # checking conding 2
   if sides_one[1] / sides_two[1] == sides_one[2] / sides_two[2]:
      if angles_one[1] == angles_two[1]:
         return True
   # checking conding 3
   if sides_one[2] / sides_two[2] == sides_one[0] / sides_two[0]:
      if angles_one[2] == angles_two[2]:
         return True
   # return False if any of the above conditions are not satisfied
      return False
def angle_angle_angle(angles_one, angles_two):
   # sorting same pace
   angles_one.sort()
   angles_two.sort()
   # checking the conditions
   if angles_one[0] == angles_two[0] \
      or angles_one[1] == angles_two[1] \
      or angles_one[2] == angles_two[2]:
      return True
   return False
   
if __name__ == '__main__':
  # initialzing the sides
      sides_one = [a, b, c]
      sides_two = [a1, b1, c1]
      # initialzing the angles
      angles_one = [80.0, 60.0, 40.0]
      angles_two = [40.0, 60.0, 80.0]
      # checking the printing the respective property
      print("Triangles are similar by:", end=' ')
      if side_side_side(sides_one, sides_two):
         print("SSS", end=' ')
      if side_angle_side(sides_one, sides_two, angles_one, angles_two):
         print("SAS", end=' ')
      if angle_angle_angle(angles_one, angles_two):
         print("AAA", end='')

import numpy as np
import matplotlib.pyplot as plt

def calc_angles(a,b,c):
    alpha = np.arccos(  (b**2 + c**2 - a**2) /(2.*b*c) )
    beta = np.arccos(  (-b**2 + c**2 + a**2) /(2.*a*c) )
    gamma = np.pi-alpha-beta
    return alpha, beta, gamma

def calc_point(alpha, beta, c):
    x = (c*np.tan(beta) )/( np.tan(alpha)+np.tan(beta) )
    y = x * np.tan(alpha)
    return (x,y)

def get_triangle(a,b,c):
    z = np.array([a,b,c])
    while z[-1] != z.max():
        z = z[[2,0,1]] # make sure last entry is largest
    alpha, beta, _ = calc_angles(*z)
    x,y = calc_point(alpha, beta, z[-1])
    return [(0,0), (z[-1],0), (x,y)]


fig, ax = plt.subplots()
ax.set_aspect("auto")

dreieck = plt.Polygon(get_triangle(a,b,c))
dreieck1 = plt.Polygon(get_triangle(a1,b1,c1),color='yellow')

ax.add_patch(dreieck)
ax.add_patch(dreieck1)
ax.relim()
ax.autoscale_view()
plt.show()