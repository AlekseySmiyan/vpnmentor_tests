from behave import fixture, use_fixture
from selenium import webdriver

import os
from utils import get_ip

# base dir project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# drivers path
DRIVERS_DIR = os.path.join(BASE_DIR, 'drivers')
CHROME_DRIVER_PATH = os.path.join(DRIVERS_DIR, 'chromedriver')


@fixture()
def setup_app(context):
    context.browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    yield context.browser
    context.browser.quit()


@fixture()
def get_my_ip(context):
    context.my_ip = get_ip()


def before_all(context):
    use_fixture(setup_app, context)
    use_fixture(get_my_ip, context)
