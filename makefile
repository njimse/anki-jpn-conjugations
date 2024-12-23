init: clean
	python3.8 -m venv env
	env/bin/pip install -U "pip<24" "setuptools<66"
	env/bin/pip install -e .[test]
	echo "to activate default venv:\n\tsource env/bin/activate"

clean:
	rm -rf env
	rm -rf *.egg-info
	- find . -name "__pycache__" -type d -exec rm -r "{}" \;
	- find . -type f -name "*.pyc" -delete

test:
	env/bin/pytest tests

update_addon:
	rm -rf myaddon/*
	- find addon -name "__pycache__" -type d -exec rm -r "{}" \;
	- find addon -type f -name "*.pyc" -delete
	cp -r addon/* myaddon/
