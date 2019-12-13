'''
1. Stale Element means an old element or no longer available element
2. Assume there is an element is present web page, If DOM changes due to after refresh page or part of page(Ajax calls) 
3. then element will get StaleElementReferenceException 
4. If you do page refresh then it will create new DOM structure 
5. To resolve this issue we should find element when we require, do not find early, or we need find element again or use try block 
'''

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException as SEE
import time

# Open a Browser 
driver = webdriver.Chrome()
time.sleep(3)
# To Maximize window
driver.maximize_window()
time.sleep(3)

# Open a URL
driver.get('https://accounts.google.com/')
time.sleep(3)

# To enter username in text box based on ID identifier
uname = driver.find_element_by_id('identifierId')
driver.refresh()
time.sleep(5)
try:
    uname.send_keys('sriram.python111')
except SEE as e:
    print(e)
    uname = driver.find_element_by_id('identifierId')
    uname.send_keys('sriram.python111')

time.sleep(10)

# Close a browser
#driver.close()

# DOM - Document Object Model