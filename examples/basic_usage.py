from vidcontrol import VideoManager

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
source.set_flip_frame(False)

for frame in source:
    # do something with the frame
    pass
