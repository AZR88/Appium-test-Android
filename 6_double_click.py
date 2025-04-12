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
driver.find_element(By.XPATH, '//*[@content-desc="Add"]').click()
driver.find_element(By.XPATH, '//*[@text = "Text"]').click()

#============== INPUT TEXT ==================#
notes1 = "Test Notes 1"
driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/edit_note").send_keys(notes1)

#============== BACK ==================#
driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/back_btn").click()
driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/back_btn").click()
title1 = driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/title").click()

#============== DOUBLE CLICK ==================#
element_dbClick = driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/view_note")
ActionChains(driver).move_to_element(element_dbClick).click().pause(0.2).click().perform()


#========================================= QUIT DRIVER ==============================================#

time.sleep(5)
driver.quit()
print("success running appium server")