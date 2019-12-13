from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
print(dir(Keys))
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org/")
time.sleep(2)

act = ActionChains(driver)

## To do Arrow DOWN operation
act.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(4)
act.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(4)
act.send_keys(Keys.ARROW_DOWN).perform()


## To do Arrow UP operation
time.sleep(4)
act.send_keys(Keys.ARROW_UP).perform()


## To do F5 operation
time.sleep(4)
act.send_keys(Keys.F5).perform()
time.sleep(2)