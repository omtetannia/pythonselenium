from selenium import webdriver
import time

#digunakan untuk alert/notif yang membutuhkan value

driver = webdriver.Chrome()

#untuk mengasih jeda waktu untuk menemukan element
driver.implicitly_wait(10)


driver.get("https://demoqa.com/alerts")

driver.find_element_by_id("promtButton").click()


driver.switch_to.alert.send_keys("tai")


driver.switch_to.alert.accept()


