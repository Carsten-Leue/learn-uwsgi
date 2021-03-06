files = learn_uwsgi test *.py

test:
	pytest -s -v test/test_*.py --doctest-modules --cov learn_uwsgi --cov-config=.coveragerc --cov-report term-missing

lint:
	flake8 $(files)

fix:
	autopep8 --in-place -r $(files)

install:
	pip install -r requirements.txt -r test-requirements.txt

report:
	codecov

build: learn_uwsgi
	rm -rf dist
	python setup.py sdist bdist_wheel

publish:
	make build
	twine upload --config-file ~/.pypirc -r pypi dist/*

.PHONY: test
