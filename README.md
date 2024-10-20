# Object Detection & Tracking Using OpenCV

This project demonstrates object detection using template matching and OpenCV. A template image of an object is compared against each frame of the video to detect the object, and the video pauses momentarily when the object is detected.

## Features
- Real-time object detection and tracking
- Pauses the video upon detecting the object
- Detects object using a pre-specified template image
- Highlights the detected object using a bounding rectangle

## Requirements
To run the project, you need the following Python libraries:
- OpenCV
- NumPy

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/dsp-object-detection.git
    cd dsp-object-detection
    ```

2. Install the required libraries:
    ```bash
    pip install opencv-python
    pip install numpy
    ```

### Usage

1. Place the template image (`template_image.jpg`) in the project folder.
2. Replace the video path with the video you want to use for detection.
3. Run the Python file:
    ```bash
    python object_detection.py
    ```

### Example Code Snippet
Here’s an example from the project for detecting objects:

```python
import cv2
import numpy as np

# Load template and video
template = cv2.imread('template_image.jpg', 0)
video = cv2.VideoCapture('video_file.mp4')

# Process each frame for object detection
# ...
