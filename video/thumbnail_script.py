import cv2

# Set the path to the video file
video_path = "video/mstera_video.mp4"

# Create a VideoCapture object to read the video file
cap = cv2.VideoCapture(video_path)

# Check if the VideoCapture object was successfully created
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Set the frame position in seconds to capture the thumbnail from (e.g. 10 seconds)
time_sec = 5
cap.set(cv2.CAP_PROP_POS_MSEC, time_sec * 1000)

# Read the next frame from the video
success, frame = cap.read()

# Check if the frame was successfully read
if not success:
    print("Error: Could not read frame.")
    exit()

# Set the path and filename for the thumbnail image
thumbnail_path = f"{video_path}_thumbnail.jpg"

# Write the frame as a JPEG image to the specified path
cv2.imwrite(thumbnail_path, frame)

# Release the VideoCapture object and close the video file
cap.release()
cv2.destroyAllWindows()
