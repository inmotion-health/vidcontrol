from setuptools import setup, find_packages
import os


THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# Get version and docstring
__version__ = None
initFile = os.path.join(THIS_DIR, "vidcontrol", "__init__.py")
for line in open(initFile).readlines():
    if line.startswith("__version__"):
        exec(line.strip())

setup(
    name="vidcontrol",
    version=__version__,
    description="Cross platform multi-webcam video capture utility.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Fabian S. Klinke",
    author_email="fabian.s.klinke@inmotion.health",
    url="https://github.com/inmotion-health/vidcontrol",
    project_urls={
        "Bug Tracker": "https://github.com/inmotion-health/vidcontrol/issues",
        "Source Code": "https://github.com/inmotion-health/vidcontrol",
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "imageio",
        "opencv-python",
        "imageio-ffmpeg",
        "pygrabber",
    ],
    include_package_data=True,
    zip_safe=False,
)
