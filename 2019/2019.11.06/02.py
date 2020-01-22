from urllib import request, parse
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
}

urlBase = 'https://movie.douban.com/j/search_subjects'
data = {
    'type': 'movie',
    'tag': '热门',
    'sort': 'recommend',
    'page_start': 0,
    'page_limit': 20
}

data = parse.urlencode(data)

res = request.urlopen(request.Request(urlBase, bytes(data, encoding='utf-8'), headers))
resp = json.loads(res.read().decode('utf-8'))['subjects']

for item in resp:
    print(item['cover'])
    print(item['title'])
    request.urlretrieve(item['cover'], './images/02/%s.jpg'%item['title'])

json.dump(resp, open('douban.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)