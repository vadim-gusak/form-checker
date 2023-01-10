dev:
		poetry run flask --app form_checker:app --debug run
lint:
		poetry run flake8 form_checker | poetry run flake8 tests
