import vidcontrol.video_platform as video_platform


class VideoManager:
    _readers = {}

    def __init__(self):
        self.platform = video_platform.get_platform()
