from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# Measure the time taken to load the page
# start_time = time()
# driver.get("http://www.python.org")
# load_time = time() - start_time
# print(f"Page loaded in {load_time:.2f} seconds")

time.sleep(5)  # Let the user actually see something!
driver.close()
