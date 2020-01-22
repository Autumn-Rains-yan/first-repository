from urllib import request,parse
import re

baseUrl = 'https://tieba.baidu.com/f?'

data = {
    'kw': '国产动画',
    'np': 0
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

http_handler = request.HTTPHandler

openner = request.build_opener(http_handler)

dataEncode = parse.urlencode(data)

res = request.Request(url=baseUrl, data=bytes(dataEncode, encoding='utf-8'), headers=header)

response = openner.open(res).read().decode('utf-8')
listInfo = re.findall(r'class="thumbnail vpic_wrap">(.*?)</a>', response)

i = 0
for subList in listInfo:
    # print(subList)
    url = re.search(r'data-original="(.*?)"', subList)
    request.urlretrieve(url[1], './image/01/%s.jpg'%i)
    print('图片%s下载完成'%(i+1))
    i = i+1