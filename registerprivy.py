from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get("https://oauth.privy.id/login?response_type=code&client_id=xCfTZ_MHwbwQ7XsbByIqvmVC5f7Y1C2aprBHfh1uqUs&redirect_uri=https%3A%2F%2Fapp.privy.id%2Fauth%2Fcallback&state=%7B%7D&scope=public%20read%20write%20manage&register=true")


driver.find_element_by("").click()