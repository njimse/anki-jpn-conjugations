init: clean
	python3.9 -m venv env
	env/bin/pip install -U pip setuptools
	env/bin/pip install -e .[test]
	echo "to activate default venv:\n\tsource env/bin/activate"

clean:
	rm -rf env
	rm -rf *.egg-info
	- find . -name "__pycache__" -type d -exec rm -r "{}" \;
	- find . -type f -name "*.pyc" -delete

test:
	env/bin/pytest tests

clone_cached_property:
	mkdir -p dependencies
	git clone git@github.com:pydanny/cached-property.git dependencies/cached_property
	pushd dependencies/cached_property

update_addon:
	rm -rf myaddon/*
	cp -r anki_jpn myaddon/
	cp -r addon/* myaddon/
	- find myaddon/ -name "__pycache__" -type d -exec rm -r "{}" \;
	- find myaddon/ -type d -name "*egg-info" -exec rm -r "{}" \;
	- find myaddon/ -type f -name "*.pyc" -delete