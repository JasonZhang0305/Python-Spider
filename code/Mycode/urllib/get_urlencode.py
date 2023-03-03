#urlencode应用场景：多个参数的时候
import urllib.request
# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

data = {
    'wd':'周杰伦',
    'sex':'男'
}

a = urllib.parse.urlencode(data)
print(a)

base_url = 'https://www.baidu.com/s?'

new_data = urllib.parse.urlencode(data)

# 请求资源路径
url = base_url + new_data

request = urllib.request.Request(url)

reponse = urllib.request.urlopen(request)

# 获取网页源码的数据
content = reponse.read().decode('utf-8')

print(content)
