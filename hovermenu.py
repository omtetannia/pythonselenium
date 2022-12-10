from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

#melihat menu yang tanpa di klik

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://privy.id/")

ActionChains(driver).move_to_element(driver.find_element_by_link_text("Resources")).perform()



print("END")