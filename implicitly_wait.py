from selenium import webdriver
import time

#digunakan untuk alert/notif yang membutuhkan value

driver = webdriver.Chrome()

#untuk mengasih jeda waktu untuk menemukan semua element
driver.implicitly_wait(10)


driver.get("https://demoqa.com/alerts")

driver.find_element_by_id("promtButton").click()
time.sleep(2)


driver.switch_to.alert.send_keys("tai")
time.sleep(2)


driver.switch_to.alert.accept()
time.sleep(2)


