import cv2
import numpy as np

# Load template image
template = cv2.imread('C:/Users/preet/OneDrive/Desktop/dsp_project/image.png', 0)  # Load in grayscale
w, h = template.shape[::-1]

# Load the video
video = cv2.VideoCapture( 'C:/Users/preet/OneDrive/Desktop/dsp_project/video.mp4')  # Replace 'video_file.mp4' with the path to your video

# Set the threshold for detection accuracy
threshold = 0.8

# Loop through the video frames
while video.isOpened():
    ret, frame = video.read()

    if not ret:
        print("End of video or error reading the video.")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # If the object is detected
    if max_val >= threshold:
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # Draw a rectangle around the detected object
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 3)

        # Pause the video and show the detection
        cv2.putText(frame, 'Object Detected', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print("Object detected")
    else:
        cv2.putText(frame, 'Object Not Detected', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        print("Object not detected")

    # Display the video frame with object detection (if found)
    cv2.imshow('Object Detection', frame)

    # Pause the video momentarily if the object is detected
    if max_val >= threshold:
        cv2.waitKey(3000)  # Pauses for 3 seconds when object is detected

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
video.release()
cv2.destroyAllWindows()
