from __future__ import print_function

from datetime import datetime
import logging
import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from helpers import get_project_root, setup_logger

setup_logger()


def before_scenario(context, scenario):
    logging.info("RUNNING: " + scenario.name)
    print("Browser Test starting.\n")

    options = Options()

    if 'headless' in os.environ and os.environ['headless'] == '1':
        options.headless = True

    context.driver = webdriver.Chrome(chrome_options=options)

    context.driver.maximize_window()

    context.current_action = ''


def after_step(context, step):
    if step.status == "failed":
        logging.info("STEP FAILED: " + step.name)

        project_root = get_project_root()

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        failure_screenshot_path = "{root}/screenshots/failures/FAIL-_{time}.png".format(root=project_root,
                                                                                             time=timestamp)

        context.driver.get_screenshot_as_file(failure_screenshot_path)
    else:
        logging.info(step.name)


def after_scenario(context, scenario):
    if scenario.status == "passed":
        logging.info("PASSED: " + scenario.name + "\n")
    elif scenario.status == "failed":
        logging.info("FAILED: " + scenario.name + "\n")

    context.driver.quit()
