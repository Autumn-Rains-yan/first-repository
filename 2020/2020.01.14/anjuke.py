from urllib import request
from bs4 import BeautifulSoup
import json

page = 1

url = 'https://gl.fang.anjuke.com/loupan/all/p%d/'%page

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
}

response = request.Request(url=url, headers=headers)

res = request.urlopen(response).read().decode('utf-8')

html = BeautifulSoup(res, 'lxml')

infoList = html.select('.item-mod')

infoArray = []
for var in infoList:
    if var.select('.infos .lp-name span'):
        title = var.select('.infos .lp-name span')[0].get_text()
        address = var.select('.address .list-map')[0].get_text().replace('\xa0', '')
        infoTemp = {
            'title': title,
            'address': address
        }
        infoArray.append(infoTemp)

print(infoArray)

json.dump(infoArray, open('HouseInfo.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
