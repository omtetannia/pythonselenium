from selenium import webdriver
import time 

#melakukan klik oada notif atau alert

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")
time.sleep(2)

driver.find_element_by_id("alertButton").click()
time.sleep(2)

driver.switch_to.alert.accept()