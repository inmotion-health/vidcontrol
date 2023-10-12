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

    def get_resolution_for(self, camera_id: int, preferred_height: int) -> Optional[Tuple[Tuple[int, int], int]]:
        resolutions = self.list_available_resolutions(camera_id)

        if not resolutions:
            return None

        # Find 720p resolutions
        _720_resolutions = [res for res in resolutions if res[0][1] == preferred_height]

        if not _720_resolutions:
            return resolutions[0][0], resolutions[0][1]

        return _720_resolutions[0][0], _720_resolutions[0][1]
