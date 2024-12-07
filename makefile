init:
	rm -rf env
	python3.9 -m venv env
	env/bin/pip install -U pip
	env/bin/pip install -e .
