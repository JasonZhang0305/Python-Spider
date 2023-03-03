# post请求

import urllib.request
import urllib.parse
import json

# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw':'spider',
}

# post请求参数必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post请求参数不会凭借在url后面，而是要放在请求对象定制的参数中
request  =urllib.request.Request(url=url,data=data)

# print(request)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')

obj = json.loads(content)
print(obj)

 
