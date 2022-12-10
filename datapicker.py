from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demoqa.com/date-picker")
driver.find_element_by_id("datePickerMonthYearInput").click()
pyautogui.press("backspace", presses=10)
time.sleep(3)
driver.find_element_by_id("datePickerMonthYearInput").send_keys("01/01/2022")
pyautogui.press("enter")
time.sleep(3)

driver.find_element_by_id("dateAndTimePickerInput").click()
pyautogui.press("bac#kspace", presses=30)
time.sleep(3)

driver.find_element_by_id("dateAndTimePickerInput").send_keys("Januari 1, 2021 2:50 AM")
pyautogui.press("enter")
time.sleep(3)

