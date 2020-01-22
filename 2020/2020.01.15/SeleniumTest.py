from selenium import webdriver
import time

path = 'chromedriver.exe'

driver = webdriver.Chrome(path)

url = 'http://www.baidu.com'

driver.get(url)

driver.find_element_by_id('kw').send_keys('python')

driver.find_element_by_id('su').click()

res = driver.page_source

print(res)

# time.sleep(3)
# driver.quit()
