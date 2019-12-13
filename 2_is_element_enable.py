'''
With text function, we can find the element with exact text match
'''
from selenium import webdriver
import time

# Open a Browser 
driver = webdriver.Chrome("chromedriver.exe")

# Open a URL
driver.get(r'C:\REAL_TIME_BATCH\3_Selenium\12_is_element_enable.html')
driver.maximize_window()
time.sleep(3)

## To find element based partial text
elem = driver.find_element_by_xpath("/html/body/form/input[2]")
print(' \n Text is :', elem.text)
#print(' \n Text is :', elem.is_enabled())

time.sleep(10)

# Close a browser
driver.close()


