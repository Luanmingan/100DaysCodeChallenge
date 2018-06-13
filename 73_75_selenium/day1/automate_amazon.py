from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://www.amazon.com")
assert "Amazon" in driver.title
elem = driver.find_element_by_id("twotabsearchtextbox")
elem.clear()
elem.send_keys("raspberry pi")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
