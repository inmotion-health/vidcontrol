# vidcontrol

[![Upload Python Package](https://github.com/inmotion-health/vidcontrol/actions/workflows/python-publish.yml/badge.svg)](https://github.com/inmotion-health/vidcontrol/actions/workflows/python-publish.yml)
[![PyPI version](https://badge.fury.io/py/vidcontrol.svg)](https://badge.fury.io/py/vidcontrol)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vidcontrol)](https://pypi.org/project/vidcontrol/)
[![PyPI - License](https://img.shields.io/pypi/l/vidcontrol)

⚠️ This package is still under development and is not yet ready for production use. ⚠️

vidcontrol is a python package for managing multi-webcam video capture. It is designed to be cross platform and easy to use. Under the hood we use [imageio](https://imageio.github.io/) for video capture, which itself used [ffmpeg](https://ffmpeg.org/). This package offers various utility functions for listing and selecting available webcams, and for capturing video from multiple webcams simultaneously. We also provide an easy to use interface for resolving image resolutions and frame rates.

This package has been developed in conjunction with the [ctrlability](https://github.com/inmotion-health/ctrlability) together with the [Prototype Fund](https://prototypefund.de/).

| Platform | Status                  |                                    |
| -------- | ----------------------- | ---------------------------------- |
| MacOS    | full support            | tested and verified on macOS 12.0+ |
| Linux    | not yet, but planned    |                                    |
| Windows  | currently working on it | tested and verified on Windows 11  |

## Getting Started

### Prerequisites

This package requires Python 3.8 or higher. We recommend using a virtual environment for development. You can create a virtual environment using [venv](https://docs.python.org/3/library/venv.html) or [conda](https://docs.conda.io/en/latest/).

Additionally, you will need to install [ffmpeg](https://ffmpeg.org/) on your system. On macOS, you can install ffmpeg using [homebrew](https://brew.sh/):

```bash
brew install ffmpeg
```

### Installation

You can install the package from PyPI:

```bash
pip install vidcontrol
```

Or install from source:

```bash
git clone https://github.com/inmotion-health/vidcontrol.git
cd vidcontrol
pip install .
```

### Basic Usage

```python
from vidcontrol import VideoManager

manager = VideoManager()

# list available webcams
manager.list_available_cameras()

# set the height of the video capture
manager.set_preferred_height(480)

# get a video source and start capturing
source = manager.get_video_source(0)
for frame in source:
    # do something with the frame
    pass
```

For more detailed examples, please see the [examples](examples) folder.

### Configuration

#### VideoManager

```python
manager.set_preferred_height(height: int)   # default: 480
```

#### VideoSource

```python
source.set_flip_frame(flip: bool)           # default: True
source.set_color_format(color_format: str)  # default: 'rgb', other options: 'bgr'
```

## Contributing and Issues

We welcome contributions and feedback. Please use GitHub issues to report bugs, discuss features, or ask questions. If you would like to contribute to the project, feel free to open a pull request. Please make sure to follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide.

Things we especially would appreciate help with:

- testing on different platforms and versions
- testing with different webcams

When contributing, please make sure to use conventional commits for your commit messages. This makes it easier to automatically generate a changelog. You can find more information about conventional commits [here](https://www.conventionalcommits.org/en/v1.0.0/).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
