import cv2

# Try to open the video file
cap = cv2.VideoCapture(r'C:\object_detect\test_video.mp4')

# Print True if successful, False if not
print("Video Opened:", cap.isOpened())

# Release the capture object
cap.release()
