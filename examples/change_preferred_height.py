from vidcontrol import VideoManager
import cv2

import logging as log

log.basicConfig(level=log.DEBUG)

manager = VideoManager()
manager.set_preferred_height(480)

source = manager.get_video_source(0)
source.set_color_format("bgr")  # openCV uses BGR instead of RGB

# iterate over the frames and display them
for frame in source:
    cv2.imshow("frame 480", frame)
    key = cv2.waitKey(1)  # Wait for 1 millisecond
    if key == 27:  # Exit loop on 'Esc' key press
        break

cv2.destroyAllWindows()

# now lets change the preferred height
manager.set_preferred_height(720)

# reconfigure the source
source = manager.get_video_source(0)
source.set_color_format("bgr")  # openCV uses BGR instead of RGB

# and lets display the next 100 frames
for frame in source:
    cv2.imshow("frame 720", frame)
    key = cv2.waitKey(1)  # Wait for 1 millisecond
    if key == 27:  # Exit loop on 'Esc' key press
        break

cv2.destroyAllWindows()
