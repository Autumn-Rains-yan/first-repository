from selenium import webdriver
import time

url = 'https://qzone.qq.com'

path = 'chromedriver.exe'

driver = webdriver.Chrome(path)

driver.get(url)

driver.switch_to.frame('login_frame')

driver.find_element_by_id('switcher_plogin').click()

driver.find_element_by_id('u').clear()

time.sleep(2)
driver.find_element_by_id('u').send_keys('123456789')
time.sleep(2)
driver.find_element_by_id('p').send_keys('123456')
time.sleep(2)
driver.find_element_by_id('login_button').click()

time.sleep(20)
driver.quit()