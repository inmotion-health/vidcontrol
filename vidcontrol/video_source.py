import logging as log
from typing import Optional, Set

import cv2
import imageio
import numpy as np

from .video_platform import video_platform

DEFAULT_RESOLUTION = (1280, 720)
DEFAULT_FPS = 30


class VideoSource:
    def __init__(self, camera_id: int, resolution: tuple, fps: int):
        self.fps = fps
        self.resolution = resolution
        self._camera_id = camera_id

        device_name = video_platform.get_ffmpeg_device_name(camera_id)
        log.debug(f"Using device name {device_name} for camera {camera_id}")

        # create reader for video stream
        try:
            self.reader = imageio.get_reader(
                device_name,
                size=resolution,
                input_params=[
                    "-framerate",
                    f"{self.fps}",
                ],
            )
        except Exception as e:
            log.error(f"Could not create reader for device {device_name} with resolution {resolution} and fps {fps}")
            log.error(e)
            self.reader = None
            raise Exception("Could not create reader for device")

        # default settings
        self.flip_frame = True

    def __iter__(self):
        return self

    def __next__(self) -> np.array:
        if not self.reader:
            return

        frame = self.reader.get_next_data()

        if self.flip_frame:
            frame = self.flip(frame)

        return frame

    def set_flip_frame(self, flip_frame: bool):
        self.flip_frame = flip_frame

    @staticmethod
    def flip(frame: np.array) -> np.array:
        return cv2.flip(frame, 1)

    def get_probe_frame(self) -> Optional[np.array]:
        if not self.reader:
            log.error("probe frame: No reader found!")
            return None

        frame = self.reader.get_next_data()
        return self.flip(frame)
