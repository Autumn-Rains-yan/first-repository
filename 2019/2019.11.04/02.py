from urllib import request, parse

name = input('请输入贴吧名')
searchName = {
    'kw': name
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"
}

urlBase = 'http://tieba.baidu.com/f?' + parse.urlencode(searchName)

for i in range(0,5):
    res = request.urlopen(request.Request(urlBase + '&pn=%s'%(i * 50), headers=headers))
    with open('./第%s章.html'%i, 'w', encoding='utf-8') as f:
        f.write(res.read().decode('utf-8'))




