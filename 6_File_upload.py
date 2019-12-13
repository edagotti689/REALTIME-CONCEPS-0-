from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(2)

FILE = r'C:\REAL_TIME_BATCH\3_Selenium\4_ENTER_Operation.py'

## To upload file
driver.find_element_by_css_selector("input[id='file-upload']").send_keys(FILE)
time.sleep(3)
driver.find_element_by_css_selector(".button").click()