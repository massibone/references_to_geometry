def centroid():
    ax = float(input('What is x of point A?'))
    ay = float(input('What is y of point A?'))
    bx = float(input('What is x of point B?'))
    by = float(input('What is y of point B?'))
    cx = float(input('What is x of point C?'))
    cy = float(input('What is y of point C?'))
    x = round(((ax + bx + cy)/3), 1)
    y = round(((ay + by + cy)/3), 1)
    return (x, y)


print("The center of triangle is in point", centroid())
