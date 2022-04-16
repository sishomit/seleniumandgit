from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.set_page_load_timeout(2)
driver.get('https://www.google.com')
driver.find_element_by_name('q').send_keys('shomit')
# driver.find_element_by_name('btnK').send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
