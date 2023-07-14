import cv2
import numpy as np

 
img = cv2.imread("rov.JPG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

 
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#الارقام اللي هتعمل بيها العمليات الحسابيه 
square_count = 0
triangle_count = 0
circle_count = 0
x_count = 0

 
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    if len(approx) == 3:
        triangle_count += 1
        cv2.drawContours(img, [contour], 0, (0, 0, 255), 3)
    elif len(approx) == 4:
        square_count += 1
        cv2.drawContours(img, [contour], 0, (0, 255, 0), 3)
    elif len(approx) > 12:
        (x, y, w, h) = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
            circle_count += 1
            cv2.drawContours(img, [contour], 0, (255, 0, 0), 3)
    else:
        x_count += 1
        cv2.drawContours(img, [contour], 0, (255, 255, 0), 3)

 
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Squares: ", square_count)
print("Triangles: ", triangle_count)
print("X : ", x_count)
print("Circles: ", circle_count)
 
total_circle_count = circle_count*20
total_x_count = x_count*5
total_triangle_count = triangle_count*10
total_square_count = square_count*15 

total = total_x_count + total_circle_count + total_square_count + total_triangle_count
print("Total = ", total)