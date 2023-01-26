n = int(input("Enter Number of Sides: "))

x_cords = list()
y_cords = list()
for k in range(n):
    x,y = map(int,input("Enter x,y co-ordinate separated by space: ").split(" "))
    x_cords.append(x)
    y_cords.append(y)

area = 0
for x in range(n-2):
    v1,v2,v3 = 0,x+1,x+2
    tr_area = abs(0.5*(x_cords[v1]*(y_cords[v2]-y_cords[v3])+
                   x_cords[v2]*(y_cords[v3]-y_cords[v1])+
                   x_cords[v3]*(y_cords[v1]-y_cords[v2])))

    area += tr_area

print ("Area of Polygon: ",area)
