import pytest
import time
from appium import webdriver
from helper.config import *

@pytest.fixture()
def open_driver():
    caps = {
        "platformName": "Android",
        "appium:udid": my_udid,
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": appPackage,
        "appium:appActivity": appActivity,
        "appium:autoGrantPermissions": True,
        "appium:noReset": False,
        "appium:ignoreHiddenApiPolicyError": True,
        "appium:disableAnimations": True,
        "appium:disableIdLocatorAutocompletions": True
    }
    direct = True
    driver =webdriver.Remote(appium_url, caps, direct_connection=direct)
    return driver

@pytest.fixture(scope='function', autouse=True)
def hook(request, open_driver):
    print("before test")
    open_driver.implicitly_wait(3)
    time.sleep(3)
    yield 
    open_driver.quit()
    print("after test")


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    print("before suite")
    yield
    print("after suite")

