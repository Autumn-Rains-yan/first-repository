import requests
import json

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'python'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"
}

res = requests.post(url=url, data=data, headers=headers)

res = res.json()

print(res)
