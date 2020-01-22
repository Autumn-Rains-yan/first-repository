from urllib import request
import re

url = "http://tieba.baidu.com/f?kw=%E6%89%8B%E6%9C%BA"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"
}

req = request.Request(url=url, headers=headers)

response = request.urlopen(req)

html = response.read().decode('utf-8')

imgList = re.findall(r'<img .*? bpic="(.*?)"', html)

for image in imgList:
    name = image.split("/")[-1][-15:]
    print("%s正在下载..." % name)
    request.urlretrieve(image, "./images/%s" % name)
