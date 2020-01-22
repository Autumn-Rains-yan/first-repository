from urllib import request

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
}

http_handler = request.HTTPHandler()

openner = request.build_opener(http_handler)

req = request.Request(url=url, headers=headers)

response = openner.open(req)

print(response.read().decode('utf-8'))