import requests

searchName = {
    "kw": 'ip'
}

urlBase = "https://www.baidu.com/s?"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"
}

proxy = {
    'http': '123.163.97.61:9999'
}

res = requests.get(url=urlBase, headers=headers, params=searchName, proxies=proxy)

res.encoding = 'utf-8'

print(res.text)

with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(res.text)