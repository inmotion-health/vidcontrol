# vidcontrol

⚠️ This package is still under development and is not yet ready for production use. ⚠️

vidcontrol is a Python package for managing multi-webcam video capture. It is designed to be cross-platform and easy to use. Under the hood, we use [imageio](https://imageio.github.io/) for video capture, which itself uses [ffmpeg](https://ffmpeg.org/). This package offers various utility functions for listing and selecting available webcams, and for capturing video from multiple webcams simultaneously. We also provide an easy-to-use interface for resolving image resolutions and frame rates.

This package has been developed in conjunction with [ctrlability](https://github.com/inmotion-health/ctrlability) together with the [Prototype Fund](https://prototypefund.de/).

| Platform | Status               |                                    |
| -------- | -------------------- | ---------------------------------- |
| MacOS    | Full support         | Tested and verified on macOS 12.0+ |
| Linux    | Not yet, but planned |                                    |
| Windows  | Full support         | Tested and verified on Windows 11  |

## Getting Started

### Prerequisites

This package requires Python 3.8 or higher. We recommend using a virtual environment for development. You can create a virtual environment using [venv](https://docs.python.org/3/library/venv.html) or [conda](https://docs.conda.io/en/latest/).

Additionally, you will need to install [ffmpeg](https://ffmpeg.org/) on your system. On macOS, you can install ffmpeg using [Homebrew](https://brew.sh/):

```bash
brew install ffmpeg
```

### Installation

You can install the latest version of the package directly from this repository:

```bash
pip install git+https://github.com/inmotion-health/vidcontrol.git
```

Or install from source:

```bash
git clone https://github.com/inmotion-health/vidcontrol.git
cd vidcontrol
pip install .
```

### Basic Usage

Generally, this package is constructed around two main classes: `VideoManager` and `VideoSource`. The `VideoManager` is used to manage all available webcams and to create new `VideoSource` instances. The `VideoSource` is used to capture video from a single webcam. The following example shows how to use these classes to capture video from a single webcam:

```python
from vidcontrol import VideoManager

manager = VideoManager()

# List available webcams
manager.list_available_cameras()

# Set the height of the video capture
manager.set_preferred_height(480)

# Get a video source and start capturing
source = manager.get_video_source(0)
for frame in source:
    # Do something with the frame
    pass
```

To capture video from a webcam, you first need to request a `VideoSource` from the `VideoManager`. You can do this by calling `get_video_source` and passing the index of the webcam you want to use. The index is the same as the index returned by `list_available_cameras`. You can also pass a `preferred_height` and `preferred_fps` to `get_video_source` to set the height and frame rate of the video capture. If you do not pass these parameters, the VideoManager will use the default values.

The VideoManager will then try to find a webcam that supports the requested height and frame rate. If it cannot find a webcam that supports the requested height and frame rate, it will use the next best resolution and frame rate. By default, this fallback is disabled, but you can enable it by setting `next_best` to `True` when configuring the VideoManager.

If the VideoSource for a webcam is requested multiple times, the VideoManager will return the same VideoSource instance. This means that you can use the same VideoSource instance in multiple places in your code. This is useful if you want to capture video from a single webcam multiple times.

For more detailed examples, please see the [examples](examples) folder.

### Configuration

vidcontrol supports various options for configuring the video capture. You can set these options either when creating a new `VideoManager` or when creating a new `VideoSource`. The following table lists all available options:

| Parameter               | Description                                                                | Default Value |
| ----------------------- | -------------------------------------------------------------------------- | ------------- |
| **VideoManager**        |                                                                            |               |
| `preferred_height`      | The preferred height of the video capture.                                 | `480`         |
| `preferred_fps`         | The preferred frame rate of the video capture.                             | `30`          |
| `next_best`             | Whether to use the next best resolution if the preferred resolution fails. | `False`       |
| **VideoSource**         |                                                                            |               |
| `color_format`          | The color format of the video capture.                                     | `rgb`         |
|                         | Other options: `bgr`                                                       |
| `mirror_frame`          | Whether to mirror the frame vertically.                                    | `True`        |
| `flip_frame_horizontal` | Whether to flip the frame horizontally.                                    | `False`       |

These options are either passed as a dictionary to the `VideoManager` or `VideoSource` `set_config`, or via their respective functions in the form of `set_<option>`. See the [basic usage](/examples/basic_usage.py) or [pass config](/examples/pass_config.py) example to see how to use some of these options.

## Contributing and Issues

We welcome contributions and feedback. Please use GitHub issues to report bugs, discuss features, or ask questions. If you would like to contribute to the project, feel free to open a pull request. Please make sure to follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide.

Things we especially would appreciate help with:

- Testing on different platforms and versions
- Testing with different webcams

When contributing, please make sure to use conventional commits for your commit messages. This makes it easier to automatically generate a changelog. You can find more information about conventional commits [here](https://www.conventionalcommits.org/en/v1.0.0/).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
