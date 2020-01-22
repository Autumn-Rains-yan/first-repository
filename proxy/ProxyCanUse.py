import requests
from GetProxy import GetProxy
import re

'''
利用访问http://icanhazip.com/返回的IP进行测试
说明：利用的http://icanhazip.com/返回的IP进行校验，如返回的是代理池的IP，说明代理有效，否则实际代理无效
'''
# headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
}
# 地址
baseUrl = 'http://icanhazip.com/'
# 获取免费代理IP
value = GetProxy.getProxy(page=1)
# 代理ip池
ip_list = value

for var in ip_list:
    try:
        print('正在尝试代理：' + var)
        res = requests.get(url=baseUrl, headers=headers, proxies={'http': var})
        print(res.text)
    except:
        # 访问失败
        print(var + '代理无效')
    else:
        print(var + '代理可用')
