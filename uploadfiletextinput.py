from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://privy.id/pdf-verification")

driver.find_element_by_id("verify").send_keys("C:/Users/KH0329/Downloads/Logbook CCTV NVR Jogja-Imogiri Oktober 2022.pdf")

driver.find_element_by_css_selector("#verify-form > div:nth-child(2) > button").click()

