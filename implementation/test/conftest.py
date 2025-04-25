import pytest
import time
from appium import webdriver
from helper.config import *  
from appium.options.android import UiAutomator2Options

@pytest.fixture()
def open_driver():
    
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.udid = my_udid
    options.automation_name = "UiAutomator2"
    options.app_package = appPackage
    options.app_activity = appActivity
    options.auto_grant_permissions = True
    options.no_reset = False
    options.ignore_hidden_api_policy_error = True
    options.set_capability("disableAnimations", True)
    options.set_capability("disableIdLocatorAutocompletions", True)

    driver = webdriver.Remote(appium_url, options=options)
    return driver


@pytest.fixture(scope='function', autouse=True)
def hook(request, open_driver):
    print("before test")
    open_driver.implicitly_wait(3)
    time.sleep(3)
    yield 
    open_driver.quit()
    print("after test")

# Fixture untuk setup dan teardown pada level suite
@pytest.fixture(scope='session', autouse=True)
def suite(request):
    print("before suite")
    print("run suite")
    yield
    print("after suite")
