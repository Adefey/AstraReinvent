PYTHON_CODE=src/*.py test/*.py

all: install_env format check test_coverage

install_env: requirements.txt
	sudo pip install -r requirements.txt


format: $(PYTHON_CODE)
	black $(PYTHON_CODE) --line-length 79

check: $(PYTHON_CODE)
	#flake8 $(PYTHON_CODE)
	pylint $(PYTHON_CODE) --disable=missing-module-docstring,missing-function-docstring,missing-class-docstring,wrong-import-position

test_coverage: $(PYTHON_CODE)
	coverage run test/test.py -b
	coverage report -m --omit=/usr/lib/*,/usr/local/lib/*
	coverage html
