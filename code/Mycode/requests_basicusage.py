# requests库用起来更方便

import requests


url = 'http://www.baidu.com'

response = requests.get(url=url)

# 一个类型和六个属性
# Response类型
print(type(response))
print('*'*50)

# 设置响应的编码格式
response.encoding = 'utf-8'
print('*'*50)

# 以字符串的形式来返回了网页的源码
print(response.text)
print('*'*50)

# 返回一个url地址
print(response.url)
print('*'*50)

# 返回的是二进制的数据
print(response.content)
print('*'*50)

# 返回响应的状态码
print(response.status_code)
print('*'*50)

# 返回的是响应头
print(response.headers)