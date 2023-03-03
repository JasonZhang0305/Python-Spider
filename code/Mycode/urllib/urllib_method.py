# urllib一个类型6个方法
import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# response是HTTPReponse的类型
print(type(response))

# 按照一个字节一个字节的读, read(n) 返回n个字节
content = response.read(5)
# 读一行
content = response.readline()
#一行一行地读
content = response.readlines()
# print(content)

# 状态码，如果是200证明逻辑没有错
print(response.getcode())

# 获取url
print(response.geturl())

# 获取响应头
print(response.getheaders())