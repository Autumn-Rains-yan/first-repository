import re

str = 'ssssssssssssssssssssssssss'

def isVail(strs):
    return re.search('^[a-zA-Z0-9_]\w{7,9}$', strs)

if isVail(str):
    print(isVail(str).group())
else:
    print('匹配失败')