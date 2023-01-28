import math


def slope(x1, y1, x2, y2):  # Line slope given two points:
    return (y2-y1)/(x2-x1)


def angle(s1, s2):
    return math.degrees(math.atan((s2-s1)/(1+(s2*s1))))


lineA = ((1.6, 3.4), (1.4, 2.4))
lineB = ((3.6, 3), (2.5, 3.5))

slope1 = slope(lineA[0][0], lineA[0][1], lineA[1][0], lineA[1][1])
slope2 = slope(lineB[0][0], lineB[0][1], lineB[1][0], lineB[1][1])

ang = angle(slope1, slope2)
print('Angle in degrees = ', round(ang, 2))
