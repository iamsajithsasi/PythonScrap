from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
searchInputBox = driver.find_element_by_xpath('//input[@id="search"]')
searchInputBox.send_keys('gadget match')
searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()