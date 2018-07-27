PYTHON=python2.7

ENV_DIR=.env_$(PYTHON)

ifeq ($(OS),Windows_NT)
	IN_ENV=. $(ENV_DIR)/Scripts/activate && setx LOCAL_ENV "True" &&
else
	IN_ENV=. $(ENV_DIR)/bin/activate && export LOCAL_ENV="True" &&
endif

all: test

env: $(ENV_DIR)
	$(IN_ENV) pip install -U pip

$(ENV_DIR):
	virtualenv -p $(PYTHON) $(ENV_DIR)

geckodriver:
ifeq (, $(shell which geckodriver))
	$(info No geckodriver in path, attempting to install it.)
	wget https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz
	sudo mkdir -p /opt/geckodriver/
	sudo tar -xvzf geckodriver-v0.20.1-linux64.tar.gz -C /opt/geckodriver/
	sudo ln -s /opt/geckodriver/geckodriver /usr/bin/geckodriver
	rm geckodriver-v0.20.1-linux64.tar.gz
else
	$(info GeckoDriver found. Using $(shell which geckodriver))
endif

test_reqs: env
	$(IN_ENV) pip install -r requirements.txt

test:
	$(IN_ENV) export environment=UAT && export suite=smoke && $(MAKE) runtests

headless:
	$(IN_ENV) export environment=UAT && export suite=smoke && $(MAKE) runheadless

freeze: env
	- $(IN_ENV) pip freeze

shell: env
	- $(IN_ENV) $(PYTHON)

clean:
	- find -name '*.pyc' -delete
	- find -name '*.pyo' -delete
	- find -name '*.pyd' -delete

env_clean: clean
	- @rm -rf .env
	- @rm -rf $(ENV_DIR)

runtests: test_reqs geckodriver
	$(IN_ENV) export env=$(environment) && behave -D BEHAVE_DEBUG_ON_ERROR=yes --tags=$(suite)

runheadless: test_reqs geckodriver
	export headless=1 && $(MAKE) runtests