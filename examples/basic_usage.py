from vidcontrol import VideoManager

manager = VideoManager()

# list available webcams
webcams = manager.list_available_cameras()
print(webcams)

# set the height of the video capture
manager.set_preferred_height(480)

# get a video source and start capturing
source = manager.get_video_source(0)
for frame in source:
    # do something with the frame
    pass
