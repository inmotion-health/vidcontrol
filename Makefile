build:
	python -m build

install:
	pip install .

basic-example: install
	python examples/basic_usage.py