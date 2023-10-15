import importlib

from .platforms.linux import LinuxVideoPlatform
from .platforms.mac import MacVideoPlatform
from .platforms.win import WindowsVideoPlatform

std_platform = importlib.import_module("platform")


def get_platform():
    """
    Returns an instance of the appropriate video platform class based on the current operating system.
    """
    system = std_platform.system()
    if system == "Darwin":
        return MacVideoPlatform()
    elif system == "Windows":
        return WindowsVideoPlatform()
    elif system == "Linux":
        return LinuxVideoPlatform()
    else:
        raise Exception("Unsupported platform")


video_platform = get_platform()
