init: clean
	python3.9 -m venv env
	env/bin/pip install -U pip
	env/bin/pip install -e .
	echo "to activate default venv:\n\tsource env/bin/activate"

clean:
	rm -rf env
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyc" -delete