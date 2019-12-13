## How send a text into text box ?
    Using send_keys()  method

## How to do click operation ?
    using click() method

## How to do scrolldown operation ?
    Using execute_script we can do scrolldown operation
    
    # Example:-    d.execute_script("window.scrollTo(0, 200)")
    
## How to do double click operations ?
    Using ActionChains we can do double click operation
    
    #Example:-  
                actions = ActionChains(driver)
                obj = driver.find_element_by_xpath('//*[@id="authentication"]/button')
                actions.move_to_element(obj)
                actions.double_click()
                actions.perform()

## What are the element locators ?
    Below are methods to find a web element based on the locators in Selenium python bindings:

    find_element_by_id
    find_element_by_name
    find_element_by_xpath
    find_element_by_link_text
    find_element_by_partial_link_text
    find_element_by_tag_name
    find_element_by_class_name
    find_element_by_css_selector
    
    To find multiple elements (these methods will return a list):

    find_elements_by_name
    find_elements_by_xpath
    find_elements_by_link_text
    find_elements_by_partial_link_text
    find_elements_by_tag_name
    find_elements_by_class_name
    find_elements_by_css_selector

## How to handle popups(alerts) ?
    Using switch_to.alert 
    
    #example:- alert = d.switch_to.alert
    #          alert.accept()

## How switch window ?
    Using d.window_handles we can switch one window to another
    
    # example:- windows = d.window_handles
    #           d.switch_to.window(windows[1])

## How to get window title ?
    using driver.title()

## How to get text ?
    using text we can get text from element 
    # example:- text = driver.find_element_by_xpath('//*[@id="downloads"]/a').text

## How to refresh page ?
    using driver.refresh()

## What are the navigators ?
    driver.back() and driver.forward()

## How to know check box is selected or not ?
    By usong is_selected() method


## D/B Absolute xpath and relative xpath ?
    # Absolute XPath:
    1. It is the direct way to find the element, but the disadvantage of the absolute XPath is that if there are any changes made in the path of the element then that XPath gets failed.

    2. The key characteristic of XPath is that it begins with the single forward slash(/) ,which means you can select the element from the root node.
    # Example:- html/body/div[1]/section/div[1]/div/div/div[3]/div[1]/div/h4[1]/b

    # Relative xpath:
    1. For Relative Xpath the path starts from the middle of the HTML DOM structure. 
    2. It starts with the double forward slash (//), which means it can search the element anywhere at the webpage.
    3. You can start from the middle of the HTML DOM structure and no need to write long xpath.
    # Example:- //*[@class='featured-box']//*[text()='Testing']

## How to select drop down values and how many ways to select a drop down values ?
    We can can select drop dwon values by using select class
    
    Three ways to find dropdwon values
        1. select_by_visible_text
        2. select_by_value
        3. select_by_value
        
        example :-
            continents = Select(driver.find_element_by_id('continents'))
            continents.select_by_visible_text('North America')
            continents.select_by_value('NA')
            continents.select_by_index(3)

## What are the selenium exceptions ?
        • StaleElementReferenceException 
        • NoSuchElementException
        • ElementNotVisibleException
        • ElementNotInteractableException
        • TimeoutException

## How to do mouse operations ?
    Using Action Chains we can do mouse operations
    actions = ActionChains(driver)
    obj = driver.find_element_by_xpath('//*[@id="authentication"]/button')
    actions.move_to_element(obj)
    actions.perform()

## How to switch into iframe ?
    Using switch_to.frame we can switch into another frame
    d.switch_to.frame('alert_frame')

## How to select multiple check boxes at a time ?
    Using find_elements 
    
    cboxes = driver.find_elements_by_xpath('//input[contains(@id,"tool-")]')

    for c in cboxes:
        time.sleep(2)
        c.click()

## D/B find element and elements ?

    # FindElement() method
    1. We need to use findElement method frequently in our webdriver software test case because this is the only way to locate any element in webdriver software testing tool.
    2. findElement method is useful to locating targeted single element.
    3. If targeted element is not found on the page then it will throw NoSuchElementException.
    # FindElements() method
    1. We are using findElements method just occasionally.
    2. findElements method will return list of all the matching elements from current page as per given element locator mechanism.
    3. If not found any element on current page as per given element locator mechanism, it will return empty list.

## Waits in python selenium
    1. These days most of the web apps are using AJAX techniques and angular. 
    2. When a page is loaded by the browser, the elements within that page may load at different time intervals.
    3. This makes locating elements difficult if an element is not yet present in the DOM, a locate function will raise an ElementNotVisibleException exception.
    4. Using waits, we can solve this issue.

## Wait types:
    1. Implicitly Wait
    2. Explicity wait

## D/B implicity wait and explicity wiat ?
# Implicitly wait
    1. Implicitly wait is one of the way to request selenium not throw any exception until provided time.
    2. Default wait time of the selenium is 500 milli-seconds.
    3. Implicit wait tries to find the element in first go, if element is not present implicit wait tries to find the element after 500ms of first polling, if element is not available on second time also then implicit wait tries third time after 500 ms of second try and it goes on till the time reaches the given time.

# Explicity wait
    1. The explicit wait is used to tell the Web Driver to wait for certain conditions or the maximum time limit before throwing an Exception .
    2. We can reuse the WebdriverWait object once we create it.Explicit wait will be applicable for only one line, we have to use it with ExpectedConditions class.
    3. WebDriverWait by default calls the ExpectedCondition every 500 milliseconds until it returns successfully.

