import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv(verbose=True)


driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("http://www.google.com")
search = driver.find_element_by_name("q")
search.send_keys("riot games api")
search.send_keys(Keys.RETURN)

driver.implicitly_wait(2)
riot = driver.find_element_by_css_selector(".LC20lb")
riot.click()
riot_login = driver.find_element_by_css_selector(".navbar-avatar")
riot_login.click()
driver.implicitly_wait(2)
username = driver.find_element_by_name("username")
username.send_keys(os.getenv("USERNAME"))
password = driver.find_element_by_name("password")
password.send_keys(os.getenv("PASSWORD"))
enter = driver.find_element_by_css_selector(".mobile-button")
enter.click()
driver.implicitly_wait(5)
regenerate = driver.find_element_by_name("confirm_action")
regenerate.click()
copy_api = driver.find_element_by_id("apikey_copy")
copy_api.click()