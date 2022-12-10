from selenium import webdriver
import time


driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/login")

driver.find_element_by_class_name("radius").click()
time.sleep(2)





