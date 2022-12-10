from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.implicitly_wait(10)

driver.find_element_by_class_name("gLFyf").send_keys("privyid")
print("input search google sukses")


driver.find_element_by_class_name("gNO89b").click()
print("succses search")


driver.find_element_by_class_name("sVXRqc").click()
print("succes direct to link")


driver.find_element_by_link_text("Masuk").click()
print("succes klik masuk")



driver.find_element_by_name("user[privyId]").send_keys("KH0329")
print("succes input username")


driver.find_element_by_id("tag-lg001").click()
print("succes klik continue")

driver.find_element_by_name("user[secret]").send_keys("tai")
print("succes input psswd")


driver.find_element_by_id("tag-lg001").click()
print("succes klik continue")




time.sleep(10)
driver.quit()



