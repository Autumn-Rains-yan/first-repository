from urllib import request, parse
import json

urlBase = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
}

data = {
    'cname': '北京',
    'pid': '',
    'pageIndex': 1,
    'pageSize': 10,
    }

jsonList = []

i = 1
for list in range(0, 1000):
    print('正在获取第%s页'%i)
    data['pageIndex'] = i
    dataEncode = parse.urlencode(data)
    res = request.urlopen(request.Request(urlBase, bytes(dataEncode, encoding='utf-8'), headers))
    jsonInfo = json.loads(res.read().decode('utf-8'))['Table1']
    i = i + 1
    if len(jsonInfo) == 0:
        break
    for jsonTemp in jsonInfo:
        jsonList.append(jsonTemp)

json.dump(jsonList, open('kfc.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)