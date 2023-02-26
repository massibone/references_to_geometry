import numpy as np
import cv2
 
coords = np.array([[12,43], [200,400], [170,170], [260,170], [23,90],[200,323], [154,300], [254, 89]])
 
def sort_coordinates(list_of_xy_coords):
    cx, cy = list_of_xy_coords.mean(0)
    x, y = list_of_xy_coords.T
    angles = np.arctan2(x-cx, y-cy)
    indices = np.argsort(angles)
    return list_of_xy_coords[indices]
 
unsorted = coords
sorted = sort_coordinates(coords)
 
print("unsorted")
print(str(coords))
print("sorted")
print(str(sorted))
 
image = np.full((700, 800, 3), (255,255,255), dtype=np.uint8)
cc_x, cc_y = coords.mean(0)
cv2.circle(image, (int(cc_x), int(cc_y)), 2, (0,0,255), 5)
 
for i in range(len(sorted)):
    cv2.circle(image, (sorted[i][0], sorted[i][1]), 2, (255,0,0), 2)
    image = cv2.putText(image, str(i), (sorted[i][0], sorted[i][1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0), 1, cv2.LINE_AA)
    if i < len(sorted) - 1:
        cv2.line(image, (sorted[i][0], sorted[i][1]), (sorted[i+1][0], sorted[i+1][1]), (0,0,255), 1)
    cv2.line(image, (sorted[0][0], sorted[0][1]), (sorted[len(sorted) - 1][0], sorted[len(sorted) - 1][1]), (0,0,255), 1)
 
unimage = np.full((400, 800, 3), (255,255,255), dtype=np.uint8)
cv2.circle(unimage, (int(cc_x), int(cc_y)), 2, (0,0,255), 5)
 
for i in range(len(unsorted)):
    cv2.circle(unimage, (unsorted[i][0], unsorted[i][1]), 2, (255,0,0), 2)
    cv2.putText(unimage, str(i), (unsorted[i][0], unsorted[i][1]), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0), 1, cv2.LINE_AA)
    if i < len(unsorted) - 1:
        cv2.line(unimage, (unsorted[i][0], unsorted[i][1]), (unsorted[i+1][0], unsorted[i+1][1]), (0,0,255), 1)
    cv2.line(unimage, (unsorted[0][0], unsorted[0][1]), (unsorted[len(unsorted) - 1][0], unsorted[len(unsorted) - 1][1]), (0,0,255), 1)
 
 
cv2.imshow('Sorted Coordinates',image)
cv2.waitKey(0)


