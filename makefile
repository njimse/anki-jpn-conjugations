init: clean
	python3.8 -m venv env
	env/bin/pip install -U pip
	env/bin/pip install -e .[test]
	echo "to activate default venv:\n\tsource env/bin/activate"

clean:
	rm -rf env
	rm -rf *.egg-info
	- find . -name "__pycache__" -type d -exec rm -r "{}" \;
	- find . -type f -name "*.pyc" -delete

test:
	env/bin/pytest tests