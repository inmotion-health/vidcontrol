install:
	pip install .

ex_basic_usage: install
	python examples/basic_usage.py

ex_multi_webcam: install
	python examples/multi_webcam.py

ex_single_cam_multi_access: install
	python examples/single_cam_multi_access.py