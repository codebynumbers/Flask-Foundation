.PHONY: docs test

help:
	@echo "  env                             create a development environment using virtualenv"
	@echo "  deps                            install dependencies using pip"
	@echo "  clean                           remove unwanted files like .pyc's"
	@echo "  lint                            check style with flake8"
	@echo "  test                            run all your tests using py.test"
	@echo "  rename appname=<new_name>       rename app"

env:
	sudo easy_install pip && \
	pip install virtualenv && \
	virtualenv env && \
	. env/bin/activate && \
	make deps

deps:
	pip install -r requirements.txt

clean:
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;

lint:
	flake8 --exclude=env .

test:
	py.test tests

rename:
	echo "renaming appname to $(appname)"
	find . -type f | grep -v '/env/' | xargs replace appname $(appname) -- {}
	mv appname $(appname)
