from appium import webdriver
from appium.options.android import UiAutomator2Options
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


#========================================= Start Driver ==============================================#

options = UiAutomator2Options()
options.platformName= "Android"
options.udid = "emulator-5554"
options.automation_name = "UiAutomator2"
options.app_package = "com.socialnmobile.dictapps.notepad.color.note"
options.app_activity = "com.socialnmobile.colornote.activity.Main"
options.auto_grant_permissions = True
options.no_reset = False
options.ignore_hidden_api_policy_error = True
options.disableAnimations = True
options.disableIdLocatorautocompletions = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options, direct_connection=True)
driver.implicitly_wait(10)

#========================================= BODY TEST ==============================================#

driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/step1_next").click()
driver.find_element(By.CLASS_NAME, "android.widget.Button").click()

#========================================= Loops ==============================================#   
for i in range(1,16):
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@content-desc="Add"]').click()
    driver.find_element(By.XPATH, '//*[@text = "Text"]').click()
    driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/edit_note").send_keys("Test Notes " +   (i))
    driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/back_btn").click()
    driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/back_btn").click()

def scroll_to_element (driver, element, max_scroll=5):
    window_size = driver.get_window_size()
    width_center = window_size['width'] / 2
    height_start = window_size['height'] / 2
    height_end = window_size['height']*0.1
    count= 0

    while True:
        driver.swipe(width_center, height_start, width_center, height_end, 400)
        try:
            if driver.find_element(By.XPATH, element).is_displayed():
                break
        except:
            count += 1
            if max_scroll >= 0 and count >= max_scroll:
                break
    
scroll_to_element(driver, '//*[@text = "Test Notes 1"]')

#========================================= QUIT DRIVER ==============================================#

time.sleep(5)
driver.quit()
print("success running appium server")