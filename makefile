init: clean
	python3.9 -m venv env
	env/bin/pip install -U pip setuptools
	env/bin/pip install -e .[test,dev]
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
	cp -r anki_jpn myaddon/
	cp -r addon/* myaddon/
	cp doc/config.md myaddon/
	- find myaddon/ -name "__pycache__" -type d -exec rm -r "{}" \;
	- find myaddon/ -type d -name "*egg-info" -exec rm -r "{}" \;
	- find myaddon/ -type f -name "*.pyc" -delete

create_addon:
	rm -rf ../japanese_conjugation
	mkdir -p ../japanese_conjugation
	cp -r anki_jpn ../japanese_conjugation/
	cp -r addon/* ../japanese_conjugation/
	cp doc/config.md japanese_conjugation/
	- find ../japanese_conjugation/ -name "__pycache__" -type d -exec rm -r "{}" \;
	- find ../japanese_conjugation/ -type d -name "*egg-info" -exec rm -r "{}" \;
	- find ../japanese_conjugation/ -type f -name "*.pyc" -delete
