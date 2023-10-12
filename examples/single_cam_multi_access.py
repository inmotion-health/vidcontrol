from vidcontrol import VideoManager
import cv2

import logging as log

log.basicConfig(level=log.DEBUG)

manager = VideoManager()

# get source for the first webcam but open it twice
source1 = manager.get_video_source(0)
source2 = manager.get_video_source(0)

source1.set_color_format("bgr")  # openCV uses BGR instead of RGB
source2.set_color_format("bgr")  # openCV uses BGR instead of RGB

# iterate over the frames and display them
while True:
    frame1 = next(source1)
    frame2 = next(source2)

    cv2.imshow("frame1", frame1)
    cv2.imshow("frame2", frame2)

    key = cv2.waitKey(1)  # Wait for 1 millisecond
    if key == 27:  # Exit loop on 'Esc' key press
        break

cv2.destroyAllWindows()
