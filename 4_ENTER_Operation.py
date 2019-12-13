from selenium import webdriver
'''
1. We can do Enter operation using Keys.RETURN or Keys.ENTER
'''

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
#print(dir(Keys))
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(2)


## To enter text and enter on google search bar
driver.find_element_by_name('q').send_keys('python')
time.sleep(3)
driver.find_element_by_name('q').send_keys(Keys.RETURN)


## To enter text and enter on google search bar
#driver.find_element_by_name('q').send_keys('python'+Keys.ENTER)

