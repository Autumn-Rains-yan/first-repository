from urllib import request, parse
# 搜索名称
searchName = parse.urlencode({
    "kw": 'python'
})
# 定义基础地址
urlBase = "http://tieba.baidu.com/f?" + searchName

# 构造请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"
}

# response = request.urlopen(url)

def getData(url, header):
    res = request.urlopen(request.Request(url, headers=header))
    print(res.getcode())

for pages in range(1, 6):
    url = urlBase + "&pn=%d" % (int((pages-1) * 50))
    res = getData(url, headers)



