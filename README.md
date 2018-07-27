Virtru Automation
==============

1. Run "make test_reqs"

2. Setup run configurations in PyCharm
	a) Select "Edit Configurations" next to the run symbol in the right corner of PyCharm.
	b) Click the '+' sign in top the left corner and select 'Behave'
	c) Name the configuration: "Virtru Automation"
	d) Feature files or folders: ~/Projects/Virtru_Automation/features
	e) Params: -D BEHAVE_DEBUG_ON_ERROR=yes --tags=local
	f) Python Interpreter: Python 2.7.12(/usr/bin/python2.7)
	g) Click 'OK'

3. Select the "Virtru Automation" run configuration and hit the 'Play' button.

Alternatively, you can run the full suite by running "make runtests" from the command line.
