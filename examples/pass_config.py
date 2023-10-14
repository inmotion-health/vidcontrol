from vidcontrol import VideoManager

import cv2

manager = VideoManager()

manager_config = {
    "preferred_height": 480,
    "preferred_fps": 30,
}

manager.set_config(manager_config)

source_config = {
    "mirror_frame": True,
    "flip_frame_horizontal": True,
    "color_format": "bgr",
}

source = manager.get_video_source(0)
source.set_config(source_config)

# iterate over the frames and display them
for frame in source:
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)  # Wait for 1 millisecond
    if key == 27:  # Exit loop on 'Esc' key press
        break

cv2.destroyAllWindows()
