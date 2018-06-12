SHELL:=/bin/bash
PYTHON=`pipenv --venv`
MANAGE:=`pipenv --venv`/bin/python manage.py

requirements:
	pipenv install

dev-requirements:
	pipenv install --dev

load-initial-data:
	$(MANAGE) loaddata main/fixtures/auth.User.json

run:
	$(MANAGE) runserver 0.0.0.0:8000

migrate:
	$(MANAGE) migrate

collectstatic:
	$(MANAGE) collectstatic --noinput

shell:
	$(MANAGE) shell

test:
	$(PYTHON)/bin/py.test

testd:
	$(PYTHON)/bin/ptw

coverage:
	$(PYTHON)/coverage run -m py.test

report:
	$(PYTHON)/coverage report

html:
	@coverage html
	@echo "Generated coverage HTML report at ./htmlcov"

clean:
	@rm -f .coverage
	@rm -rf htmlcov/
	@echo "Cleaned coverage report files"

pull:
	git pull origin

install: requirements migrate load-initial-data

dev-install: dev-requirements migrate load-initial-data

update:	pull install

dev-update:	pull dev-install
