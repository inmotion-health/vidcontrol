from typing import Dict
from vidcontrol.video_platform import video_platform
from vidcontrol.video_source import VideoSource

import logging as log


class VideoManager:
    """
    A class that manages video sources for a video application.
    """

    _vid_sources: Dict[int, VideoSource] = {}

    preferred_height = 480
    preferred_fps = 30
    next_best = False

    def get_video_source(self, camera_id) -> VideoSource:
        """
        Returns a VideoSource object for the specified camera ID. If a VideoSource object for the specified camera ID
        already exists, it is returned. Otherwise, a new VideoSource object is created and returned.

        Args:
            camera_id (int): The ID of the camera to get the VideoSource for.

        Raises:
            Exception: If no VideoSource object could be created for the specified camera ID. This can happen if the
                camera ID is invalid or if no matching resolution could be found for the camera, and the 'next_best'
                flag is set to False.
        """
        # Check if the reader already exists
        if camera_id in VideoManager._vid_sources:
            return VideoManager._vid_sources[camera_id]

        # Create the reader
        self._create_source(camera_id)

        return VideoManager._vid_sources[camera_id]

    def list_available_cameras(self):
        """
        Returns a list of available video devices. The list contains tuples of the form `(camera_id, camera_name)`.
        """
        return video_platform.list_video_devices()

    def set_preferred_height(self, height: int):
        """
        Sets the preferred height for video sources managed by this VideoManager instance.
        """
        VideoManager.preferred_height = height
        self._recreate_existing_sources()

    def set_preferred_fps(self, fps: int):
        """
        Sets the preferred frames per second (fps) for the video manager.
        """
        VideoManager.preferred_fps = fps
        self._recreate_existing_sources()

    def set_next_best(self, next_best: bool):
        """
        Sets the value of the 'next_best' flag, which determines whether the video manager should automatically
        switch to the next best video source if the current one fails.
        """
        VideoManager.next_best = next_best

    def set_config(self, config: dict):
        """
        Sets the configuration for the video manager.

        Args:
            config (dict): A dictionary containing the configuration options.
                The following keys are supported:
                - "preferred_height": The preferred height of the video.
                - "preferred_fps": The preferred frames per second of the video.
                - "next_best": Whether to use the next best configuration if the
                  preferred configuration is not available.
        """
        if "preferred_height" in config:
            self.set_preferred_height(config["preferred_height"])

        if "preferred_fps" in config:
            self.set_preferred_fps(config["preferred_fps"])

        if "next_best" in config:
            self.set_next_best(config["next_best"])

    def _create_source(self, camera_id: int):
        resolution, fps = video_platform.get_resolution_for(
            camera_id,
            VideoManager.preferred_height,
            VideoManager.preferred_fps,
            next_best=VideoManager.next_best,
        )
        log.debug(f"Using resolution {resolution} and fps {fps} for camera {camera_id}")

        VideoManager._vid_sources = {camera_id: VideoSource(camera_id, resolution, fps)}

        log.info(f"Created reader for camera {camera_id}")

    def _recreate_existing_sources(self):
        for camera_id in VideoManager._vid_sources:
            self._create_source(camera_id)
