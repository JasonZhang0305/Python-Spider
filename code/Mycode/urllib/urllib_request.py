# 使用urllib获取百度首页的源码
import urllib.request

# 1 定义一个url
url = 'http://www.baidu.com'

# 2 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 3 获取响应中的页面的源码
# read方法返回的是字节形式的二进制数据
# 二进制解码 -》 utf-8
content = response.read().decode('utf-8')

# 4 打印数据
print(content)
