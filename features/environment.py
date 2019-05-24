from behave import fixture, use_fixture
from selenium import webdriver

import os
from utils import get_ip
import settings
from pages.ip_info_page import IpInfoPage


@fixture()
def setup_driver(context):
    context.browser = webdriver.Chrome(executable_path=settings.CHROME_DRIVER_PATH)
    yield context.browser
    context.browser.quit()


@fixture()
def setup_app(context):
    context.ip_info_page = IpInfoPage(context.browser)


@fixture()
def get_my_ip(context):
    context.my_ip = get_ip()


def before_all(context):
    use_fixture(setup_driver, context)
    use_fixture(setup_app, context)
    use_fixture(get_my_ip, context)
