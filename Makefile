test:
	python3 -m unittest discover -s tests

integration-test:
	python3 -m unittest discover -s integration_tests

coverage:
	coverage run -m unittest discover -s tests
	coverage report -m
	coverage html
