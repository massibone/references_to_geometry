

def circumcenter():
    ax = float(input('What is x of point A?'))
    ay = float(input('What is y of point A?'))
    bx = float(input('What is x of point B?'))
    by = float(input('What is y of point B?'))
    cx = float(input('What is x of point C?'))
    cy = float(input('What is y of point C?'))
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by)
          * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by)
          * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return (ux, uy)


print("Midpoint of the triangle ABC is: ", circumcenter())
