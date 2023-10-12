from vidcontrol.video_platform import video_platform
from vidcontrol.video_source import VideoSource

import logging as log


class VideoManager:
    _readers = {}

    preferred_height = 480

    def create_source(self, camera_id: int):
        resolution, fps = video_platform.get_resolution_for(camera_id, self.preferred_height)
        log.debug(f"Using resolution {resolution} and fps {fps} for camera {camera_id}")

        VideoManager._readers = {camera_id: VideoSource(camera_id, resolution, fps)}

        log.info(f"Created reader for camera {camera_id}")

    def get_video_source(self, camera_id) -> VideoSource:
        # Check if the reader already exists
        if camera_id in VideoManager._readers:
            return VideoManager._readers[camera_id]

        # Create the reader
        self.create_source(camera_id)

        return VideoManager._readers[camera_id]

    def list_available_cameras(self):
        return video_platform.list_video_devices()

    def set_preferred_height(self, height: int):
        self.preferred_height = height
