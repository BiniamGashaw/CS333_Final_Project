test:
	python3 -m unittest discover -s tests

integration-test:
	python3 -m unittest discover -s integration_tests

coverage:
	python3 -m coverage run -m unittest discover -s tests
	python3 -m coverage html
