from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
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
driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/edit_note").send_keys("Test Notes 1")

#============== BACK ==================#
driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/back_btn").click()
driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/back_btn").click()
title1 = driver.find_element(By.ID, "com.socialnmobile.dictapps.notepad.color.note:id/title").text

print(title1)
#========================================= QUIT DRIVER ==============================================#

time.sleep(5)
driver.quit()