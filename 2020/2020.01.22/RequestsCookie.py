import requests

session = requests.Session()

url = 'https://www.kuaidaili.com/login/'

data = {
    'next': '',
    'kf5_return_to': '',
    'username': '237977800@qq.com',
    'passwd': '123456'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
}

session.get(url=url, data=data, headers=headers)



