import cv2
import numpy as np


cap = cv2.VideoCapture("2.mp4")

while True:
    # Read a frame from the video stream
    ret, frame = cap.read() 

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply threshold to convert the image to binary
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize a flag to keep track of the largest contour
    largest_contour = None

    # Initialize a variable to store the area of the largest contour
    largest_area = 0

    for cnt in contours:
        # Approximate the contour with a rectangle or a polygon
        epsilon = 0.1 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True, cv2.CHAIN_APPROX_TC89_KCOS)

        # Check if the contour has 4 vertices 
        if len(approx) == 4:
            # Calculate the area of the contour
            area = cv2.contourArea(approx)

            # Check if the area of the current contour is larger than the largest area
            if area > largest_area:
                # Update the largest contour and the largest area
                largest_contour = approx
                largest_area = area

    # Check if the largest contour was found
    if largest_contour is not None:
        # Draw a rectangle around the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
         # point .....
        pointx = x + w // 2
        pointy = y + h // 2
        cv2.circle(frame, (pointx, pointy), 5, (0, 255, 0), -1)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
