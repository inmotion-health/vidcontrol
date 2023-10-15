from abc import abstractmethod
from typing import Dict, Optional, Tuple, List


class VideoPlatform:
    @abstractmethod
    def get_video_format(self) -> str:
        pass

    @abstractmethod
    def list_video_devices(self) -> Dict[int, str]:
        pass

    @abstractmethod
    def list_available_resolutions(self, device_id: int) -> Optional[List[Tuple[Tuple[int, int], int]]]:
        pass

    @abstractmethod
    def get_ffmpeg_device_name(self, cam_id: int) -> str:
        pass

    @abstractmethod
    def get_platform_specific_ffmpeg_options(self) -> List[str]:
        pass

    def get_resolution_for(
        self, camera_id: int, preferred_height: int, preferred_fps: int, next_best: bool = False
    ) -> Tuple[Tuple[int, int], int]:
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
