'''
 

'''
from selenium import webdriver
import time

# Open a Browser 
driver = webdriver.Chrome()

# Open a URL
driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(3)

ele = driver.find_element_by_xpath('//*[@id="gbw"]/div/div/div[1]/div[1]/a')

## To get elealues of attrbutes
print(' LINK URL IS ', ele.get_attribute('href'))
print(' LINK URL IS ', ele.get_attribute('class'))
print(' LINK URL IS ', ele.get_attribute('data-pid'))

time.sleep(10)

a_elements = driver.find_elements_by_xpath('//a')


## To get all links in a page
for e in a_elements:
    time.sleep(1)
    print(' \n LINK : ', e.get_attribute('href'))

# Close a browser
driver.close()



