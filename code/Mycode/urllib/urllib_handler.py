# 用handler访问百度，获取网页源码
# 使用handler是一个反爬虫手段

import urllib.request
# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

# 原来是： response = urllib.request.urlopen(request)

# handler build_opener  open

# 1 获取hanlder对象
handler = urllib.request.HTTPHandler()

# 2 通过handler获取oponer对象
opener = urllib.request.build_opener(handler)

# 3 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)