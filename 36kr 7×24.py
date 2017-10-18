#coding:utf-8
import requests
import re
import json

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
}

# 请求
request = requests.get('http://36kr.com/newsflashes', headers=headers)

# 打印响应码
print(request.status_code)

# 返回响应数据
str_data = request.content.decode()

# 正则找到有用的部分
pattern = re.compile(r'<script>var props=({.*?})</script> ', re.S)
dict_data = pattern.findall(str_data)[0]
# with open('36kr1.json', 'w') as f:
#     f.write(dict_data)


# 过滤掉有问题的地方
dict_data = re.sub(',locationnal=.*', '', dict_data)
# with open('36kr2.json', 'w') as f:
#     f.write(dict_data)

# 转换数据
list_data = json.loads(dict_data)['newsflashList|newsflash']

with open('36kr3.txt', 'w') as f:
    for data2 in list_data:
        f.write(json.dumps(data2['description'], ensure_ascii=False))



