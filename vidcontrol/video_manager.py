import vidcontrol.video_platform as video_platform
from vidcontrol.video_source import VideoSource


class VideoManager:
    _readers = {}

    preferred_height = 480

    def __init__(self):
        self.platform = video_platform.get_platform()

    def create_readers(self):
        webcam_list = self.platform.list_video_devices()
        cam_ids = [cam.id for cam in webcam_list]

        for cam_id in cam_ids:
            print("Creating reader for cam_id: " + cam_id)

    def get_video_source(self, cam_id) -> VideoSource:
        raise NotImplementedError("get_video_source is not implemented")

    def list_available_cameras(self):
        return self.platform.list_video_devices()

    def set_preferred_height(self, height: int):
        self.preferred_height = height
