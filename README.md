# vidcontrol

⚠️ This package is still under development and is not yet ready for production use. ⚠️

vidcontrol is a python package for managing multi-webcam video capture. It is designed to be cross platform and easy to use. Under the hood we use [imageio](https://imageio.github.io/) for video capture, which itself used [ffmpeg](https://ffmpeg.org/). This package offers various utility functions for listing and selecting available webcams, and for capturing video from multiple webcams simultaneously. We also provide an easy to use interface for resolving image resolutions and frame rates.

This package has been developed in conjunction with the [ctrlability](https://github.com/inmotion-health/ctrlability) together with the [Prototype Fund](https://prototypefund.de/).


| Platform | Status                  |                                    |
| -------- | ----------------------- | ---------------------------------- |
| MacOS    | full support            | tested and verified on macOS 12.0+ |
| Linux    | not yet, but planned    |                                    |
| Windows  | currently working on it | tested and verified on Windows 11  |

## Getting Started

```python
import vidcontrol as vc

manager = vc.VideoManager()

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

## Contributing and Issues

We welcome contributions and feedback. Please use GitHub issues to report bugs, discuss features, or ask questions. If you would like to contribute to the project, feel free to open a pull request. Please make sure to follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide.

Things we especially would appreciate help with:

- testing on different platforms and versions
- testing with different webcams

When contributing, please make sure to use conventional commits for your commit messages. This makes it easier to automatically generate a changelog. You can find more information about conventional commits [here](https://www.conventionalcommits.org/en/v1.0.0/).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
