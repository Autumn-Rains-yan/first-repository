from urllib import request
from lxml import etree
import re
import json

url = "https://tieba.baidu.com/f?kw=%E5%8A%A8%E7%94%BB"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"
}

requests = request.Request(url=url, headers=headers)

response = request.urlopen(requests)

res = response.read().decode('utf-8')

# 这里用replace替换也是可以的
res_new = re.sub('<!--', '', res)

html = etree.HTML(res_new)

infoList = html.xpath('//div[@class="t_con cleafix"]')

jsonInfo = []
for var in infoList:
    title = var.xpath('.//div[contains(@class, "threadlist_title")]/a/text()')[0]
    author = re.sub('主题作者: ', '', var.xpath('.//span[contains(@class, "tb_icon_author")]/@title')[0])
    contentTemp = var.xpath('.//div[contains(@class,"threadlist_abs")]/text()')
    if contentTemp:
        content = contentTemp[0].replace(' ', '').replace('\n', '')
    else:
        content = ''
    jsonTemp = {title: title, author: author, content: content}
    jsonInfo.append(jsonTemp)

json.dump(jsonInfo, open('tiebaJson.json', 'w', encoding="utf-8"), ensure_ascii=False, indent=4)
