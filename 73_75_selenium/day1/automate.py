from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


user = os.environ.get("MOMO_USER")
password = os.environ.get("MOMO_PASS")

driver = webdriver.Chrome()
driver.get("https://web.immomo.com")

driver.find_element_by_id("user").send_keys(user)
driver.find_element_by_id("ie_login_pwd").send_keys(password + Keys.RETURN)


code = input("please input your validation code: ")
driver.find_element_by_name("code").send_keys(code + Keys.RETURN)

assert "No results found." not in driver.page_source
