from selenium import webdriver
import time

#digunakan untuk alert atau notif yang ada pilihan yes/no

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")
time.sleep(2)

#untuk ok/yes
driver.find_element_by_id("confirmButton").click()
time.sleep(2)

driver.switch_to.alert.accept()
time.sleep(2)

#untuk cancel
driver.find_element_by_id("confirmButton").click()
time.sleep(2)

driver.switch_to.alert.dismiss()
time.sleep(2)

