from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyautogui

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demoqa.com/select-menu")

# Select Value
driver.find_element_by_id("withOptGroup").click()
pyautogui.typewrite("A root option"),pyautogui.press("enter")


# Select One
driver.find_element_by_id("selectOne").click()
pyautogui.typewrite("Dr."), pyautogui.press("enter")
