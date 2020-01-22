from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
from urllib import request
import time

# 使用Chrome无头浏览器
# 创建一个参数对象，用来控制chrome以无界面方式打开
chrome_options = Options()
# 固定写法
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=python'

path = 'chromedriver.exe'

driver = webdriver.Chrome(executable_path=path, options=chrome_options)

driver.get(url)

for var in range(0, 3):
    driver.execute_script('scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)

res = driver.page_source

html = etree.HTML(res)

urlList = html.xpath('//li[@class="imgitem"]/@data-objurl')

print(urlList)
for var in urlList:
    name = var.split('/')[-1]
    print('图片%s正在下载中...'%name)
    try:
        request.urlretrieve(var, './images/' + name)
    except:
        print('图片%s下载错误'%name)



time.sleep(10)
driver.quit()