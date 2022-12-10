from selenium import webdriver
import pyautogui
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://gofile.io/uploadFiles")

driver.find_element_by_id("rowUploadButton").click()

time.sleep(5)

pyautogui.write(r"C:\Users\KH0329\Downloads\chromedriver_win32.zip")
pyautogui.press("Enter")

