from urllib import request, parse
import http.cookiejar
import json

urlBase = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019105940377'

headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

data = {
    'email':'15978042383',
    'icode': '',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': 1,
    'captcha_type': 'web_login',
    'password':'2546920b9d879794093a8c6b21956e9c35ad2b6c23863d0cb5b851940dde0da5',
    'rkey': 'b53cb58fddd7e22162b08f37d1e90142',
    'f': 'http%3A%2F%2Fwww.renren.com%2F972812037'
}

data = parse.urlencode(data)
# 创建一个cookie对象 可以帮助我们保存服务器向浏览器cookie重写入的内容
cookie = http.cookiejar.CookieJar()

http_handler = request.HTTPCookieProcessor(cookie)

opener = request.build_opener(http_handler)

res = request.Request(url=urlBase, data=bytes(data, encoding='utf-8'), headers=headers)

ress = json.loads(opener.open(res).read().decode('utf-8'))

if ress['code']:
    # 这里表示登录成功，进行登录完成处理
    # print(ress)
    urlUse = ress['homeUrl']
    resFinish = opener.open(urlUse).read().decode('utf-8')
    print(resFinish)
else:
    print('登录失败')


