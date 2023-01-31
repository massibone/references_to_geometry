

def dist(x1, y1, x2, y2, r):
    print("The shortest distance between a point and a circle is ",((((x2 - x1)** 2) + ((y2 - y1)** 2))**(1/2)) - r);
 
  
# Driver code
#x1,y1 is the centre of the circle
x1 = 2
y1 = 3
#point A(30,40)
x2 = 20
y2 = 30
r = 5
print(dist(x1, y1, x2, y2, r))





