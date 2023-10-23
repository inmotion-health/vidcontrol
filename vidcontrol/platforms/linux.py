import logging
from typing import Dict, List, Optional, Tuple

log = logging.getLogger(__name__)

import vidcontrol.platforms.base as base


class LinuxVideoPlatform(base.VideoPlatform):
    def get_video_format(self):
        return "v4l2"

    def list_video_devices(self) -> Dict[int, str]:
        pass

    def list_available_resolutions(self, device_id: int) -> Optional[Tuple[Tuple[int, int], int]]:
        pass

    def _get_platform_specific_ffmpeg_options(self) -> List[str]:
        return []
