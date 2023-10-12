from vidcontrol import VideoManager
import cv2

manager = VideoManager()

# list available webcams
webcams = manager.list_available_cameras()
print(webcams)

manager.set_preferred_height(480)

# lets create a video source for each webcam
sources = []
for cam in webcams:
    # configure the manager

    # get a video source and check for errors
    try:
        source = manager.get_video_source(cam)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

    # configure the video source
    source.set_color_format("bgr")  # openCV uses BGR instead of RGB

    sources.append(source)

# iterate over the frames and display them
while True:
    for source in sources:
        frame = next(source)
        cv2.imshow(f"frame {source._camera_id}", frame)

    key = cv2.waitKey(1)  # Wait for 1 millisecond
    if key == 27:  # Exit loop on 'Esc' key press
        break


cv2.destroyAllWindows()
