from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/l/21345040031/ref=s9_acss_bw_cg_LFENPC_4a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=HPA7YMHC02GATQZ1TXZQ&pf_rd_t=101&pf_rd_p=ca1b5b37-3779-492f-89c5-f3e9eb7eb329&pf_rd_i=14591169031')
listoflinks = []
condition = True
while condition:
    link = driver.find_elements_by_css_selector('#mainResults ul li .s-item-container .a-row.a-spacing-mini .a-row.a-spacing-none.sx-line-clamp-4')
    for el in link:
        atag = el.find_element_by_tag_name('a').get_property('href')
        listoflinks.append(atag)
    try:
        driver.find_element_by_xpath('//*[@id="pagnNextString"]').click()
    except:
        condition = False
# print(listoflinks)
linkstable = pd.DataFrame(listoflinks)
linkstable.rename(index=str, columns={0:'new_column_name'})
# print(linkstable)
linkstable.to_csv('list.csv')