from urllib import request
import json
import gzip

headers = {
    'Accept':' */*',
    'Accept-Encoding':' gzip, deflate',
    'Accept-Language':' zh-CN,zh;q=0.9',
    'Cache-Control':' no-cache',
    'Connection':' keep-alive',
    # 'Content-Length':' 250',
    'Content-Type':' text/plain;charset=UTF-8',
    'Host':' www.izuiyou.com',
    'Origin: http':'//www.izuiyou.com',
    'Pragma':' no-cache',
    'Referer: http':'//www.izuiyou.com/',
    'User-Agent':' Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 SE 2.X MetaSr 1.0',
}

data = {
    'ctn': 200,
    'direction': 'up',
    'filter': 'all',
    'h_av': '3.0',
    'h_ch': 'web_app',
    'h_dt': 9,
    'h_nt': 9,
    'offset': 0,
    'tab': 'rec',
    'ua': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

# json对象传输 request payload
# 如果是form data用parse.urlencode
data = json.dumps(data)

url = 'http://www.izuiyou.com/api/index/webrecommend'

req = request.Request(url=url, data=bytes(data, encoding='utf-8'), headers=headers)

response = request.urlopen(req)

f = gzip.GzipFile(fileobj=response)

res = f.read().decode('utf-8')

res = json.loads(res)['data']['list']

titleArray = []
for var in res:
    titleArray.append(var['content'])
print(titleArray)