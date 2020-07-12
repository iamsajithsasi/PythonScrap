from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.cubdomain.com/domains-registered-by-date/2020-06-19/1')
link = driver.find_elements_by_css_selector('section.box.domains-by-date .row .col-md-4')
listoflinks = []
for el in link:
    atag = el.find_element_by_tag_name('a').get_property('href')
    listoflinks.append(atag)
# print(listoflinks)
linkstable = pd.DataFrame(listoflinks)
linkstable.rename(index=str, columns={0:'new_column_name'})
linkstable.to_csv('list2.csv')