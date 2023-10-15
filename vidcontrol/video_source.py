import logging as log
from typing import Optional

import cv2
import imageio
import numpy as np

from .video_platform import video_platform

DEFAULT_RESOLUTION = (1280, 720)
DEFAULT_FPS = 30


class VideoSource:
    """
    A class representing a video source.

    Args:
        camera_id (int): The ID of the camera to use as the video source.
        resolution (tuple): The resolution of the video source, in pixels, as a tuple of (width, height).
        fps (int): The frames per second of the video source.
    """

    def __init__(self, camera_id: int, resolution: tuple, fps: int):
        self.fps = fps
        self.resolution = resolution
        self._camera_id = camera_id

        device_name = video_platform._get_ffmpeg_device_name(camera_id)
        log.debug(f"Using device name {device_name} for camera {camera_id}")

        input_params = self._build_ffmpeg_input_params()

        # create reader for video stream
        try:
            self.reader = imageio.get_reader(
                device_name,
                size=resolution,
                input_params=input_params,
            )
        except Exception as e:
            log.error(f"Could not create reader for device {device_name} with resolution {resolution} and fps {fps}")
            log.error(e)
            self.reader = None
            raise Exception(f"Could not create reader for device {device_name}")
        else:
            log.info(f"Created reader for device {device_name} with resolution {resolution} and fps {fps}")

        # default settings
        self.flip_frame_vertical = True
        self.flip_frame_horizontal = False
        self.color_format = "rgb"

    def _build_ffmpeg_input_params(self):
        input_params = []

        # append framerate to input params
        input_params += ["-framerate", f"{self.fps}"]

        # append platform specific options to input params
        input_params += video_platform._get_platform_specific_ffmpeg_options()
        return input_params

    def __iter__(self):
        return self

    def __next__(self) -> np.array:
        if not self.reader:
            return

        frame = self.reader.get_next_data()

        if self.flip_frame_vertical:
            frame = cv2.flip(frame, 1)

        if self.flip_frame_horizontal:
            frame = cv2.flip(frame, 0)

        if self.color_format == "bgr":
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        return frame

    def set_mirror_frame(self, flip_frame: bool):
        """
        Sets whether or not to flip the frame vertically.
        """
        self.flip_frame_vertical = flip_frame

    def set_flip_frame_horizontal(self, flip_frame: bool):
        """
        Set whether to flip the video frame horizontally.
        """
        self.flip_frame_horizontal = flip_frame

    def set_color_format(self, color_format: str):
        """
        Sets the color format for the video source.
        """
        self.color_format = color_format

    def set_config(self, config: dict):
        """
        Set the configuration for the video source.

        Args:
            config (dict): A dictionary containing the configuration options. The following keys are supported:
                - "mirror_frame": Whether to flip the frame vertically.
                - "flip_frame_horizontal": Whether to flip the frame horizontally.
                - "color_format": The color format to use for the video source.
        """
        if "mirror_frame" in config:
            self.set_mirror_frame(config["mirror_frame"])

        if "flip_frame_horizontal" in config:
            self.set_flip_frame_horizontal(config["flip_frame_horizontal"])

        if "color_format" in config:
            self.set_color_format(config["color_format"])
