from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)

## To create ActionChains object
act = ActionChains(driver)


driver.find_element_by_xpath('//input[@id="email"]').send_keys('srikumar')
time.sleep(4)
## To do TAB operation
act.send_keys(Keys.TAB).perform()
time.sleep(4)


## To do right click operation
act.context_click().perform()

