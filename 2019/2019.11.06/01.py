from urllib import request,parse
import json

urlBase = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
}

data = {
    'kw': 'python'
}

req = request.Request(urlBase, bytes(parse.urlencode(data), 'utf-8'), headers)
resp = request.urlopen(req).read().decode('utf-8')
print(json.loads(resp))
