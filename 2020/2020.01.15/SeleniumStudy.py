from selenium import webdriver
import time

path = 'chromedriver.exe'

driver = webdriver.Chrome(path)

time.sleep(3)

driver.quit()