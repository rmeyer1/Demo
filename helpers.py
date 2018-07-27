import datetime
import logging
import os


def get_project_root():
    return os.path.abspath(os.path.dirname(__file__))


def setup_logger():
    log_filename = 'Virtu-test-results-{time}.txt'.format(time=datetime.datetime.now().strftime('%Y%m%d-%H%M'))

    logging.basicConfig(filename=log_filename,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.FileHandler(log_filename, mode='w')
