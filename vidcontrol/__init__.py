__version__ = "0.1.0"

from .video_source import VideoSource
from .video_manager import VideoManager
from .video_platform import video_platform as VideoPlatform

__all__ = ["VideoSource", "VideoManager", "VideoPlatform"]
