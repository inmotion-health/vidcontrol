from typing import Dict, Optional, Tuple, List
from abc import ABC, abstractmethod


class VideoPlatform(ABC):
    """
    Abstract base class for video platforms.

    Defines methods for getting video format, listing video devices, listing available resolutions for a device,
    getting the ffmpeg device name, and getting platform-specific ffmpeg options.
    """

    @abstractmethod
    def get_video_format(self) -> str:
        pass

    @abstractmethod
    def list_video_devices(self) -> Dict[int, str]:
        """
        Returns a dictionary of available video devices, where the keys are device IDs and the values are device names.

        For example, this method might return `{0: "Integrated Camera", 1: "USB Camera"}`.
        """
        pass

    @abstractmethod
    def list_available_resolutions(self, device_id: int) -> Optional[List[Tuple[Tuple[int, int], int]]]:
        """
        Returns a list of available resolutions for the specified device.

        Args:
            device_id (int): The ID of the device to retrieve resolutions for.

        Returns:
            Optional[List[Tuple[Tuple[int, int], int]]]: A list of tuples, where each tuple contains a resolution
            (represented as a tuple of width and height) and a refresh rate (in Hz). Returns None if the device is not
            found or if an error occurs while retrieving the resolutions.
            Example: `[((1280, 720), 30), ((640, 480), 60)]`
        """
        pass

    @abstractmethod
    def _get_ffmpeg_device_name(self, cam_id: int) -> str:
        pass

    @abstractmethod
    def _get_platform_specific_ffmpeg_options(self) -> List[str]:
        pass

    def get_resolution_for(
        self, camera_id: int, preferred_height: int, preferred_fps: int, next_best: bool = False
    ) -> Tuple[Tuple[int, int], int]:
        """
        Get the resolution for a given camera ID, preferred height, and preferred FPS.

        If `next_best` is True, find the closest match if no exact match is found.

        Raises an exception if no matching resolution is found.
        """
        resolutions = self.list_available_resolutions(camera_id)

        if not resolutions:
            raise Exception(f"No resolutions found for camera {camera_id}")

        # Filter by preferred height
        height_filtered = [res for res in resolutions if res[0][1] == preferred_height]

        # If preferred height is found
        if height_filtered:
            fps_filtered = [res for res in height_filtered if res[1] == preferred_fps]
            if fps_filtered:
                return fps_filtered[0]

        # If 'next_best' flag is True, find closest match
        if next_best:
            # If preferred height was not found, find closest height match
            if not height_filtered:
                closest_height = min(resolutions, key=lambda x: abs(x[0][1] - preferred_height))
                return closest_height

            # If preferred height was found but fps was not, find closest fps match in height_filtered
            closest_fps = min(height_filtered, key=lambda x: abs(x[1] - preferred_fps))
            return closest_fps

        # If 'next_best' is False and we haven't returned yet, raise error
        raise Exception(f"No matching resolution found for camera {camera_id}")
