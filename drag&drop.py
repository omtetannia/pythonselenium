from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://demoqa.com/droppable")
driver.implicitly_wait(20)

drag = driver.find_element_by_id("draggable")

drop = driver.find_element_by_id("droppable")

aksi = ActionChains(driver)

aksi.drag_and_drop(drag, drop).perform()