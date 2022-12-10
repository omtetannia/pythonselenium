from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")

driver.find_element_by_id("promtButton").click()


driver.switch_to.alert.send_keys("tai")


driver.switch_to.alert.accept()