from vidcontrol import VideoManager
import cv2

manager = VideoManager()

# list available webcams
webcams = manager.list_available_cameras()
print(webcams)

# configure the manager
manager.set_preferred_height(480)

# get a video source and check for errors
try:
    source = manager.get_video_source(0)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

# configure the video source
source.set_color_format("bgr")  # openCV uses BGR instead of RGB

# iterate over the frames and display them
for frame in source:
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)  # Wait for 1 millisecond
    if key == 27:  # Exit loop on 'Esc' key press
        break

cv2.destroyAllWindows()
