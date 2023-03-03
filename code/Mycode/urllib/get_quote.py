# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6 -> 周杰伦的Unicode码
# 编码集演变：ASCII -> Unicode(统一所有语言的编码)
import urllib.request
# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#需求：获取周杰伦网页的源码

url = 'https://www.baidu.com/s?wd='

# 请求对象的定制，解决反爬问题
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
} 

# 将周杰伦三个字变成unicode编码格式
# 需要依赖于urllib.parse
name = urllib.parse.quote('周杰伦')
# 拼接一下就得到了完整的unicode编码
url = url + name

# print(name)

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers) #这里要明确参数名

# 发送请求
response = urllib.request.urlopen(url)

# 获取响应的内容
content = response.read().decode('utf-8')

print(content)