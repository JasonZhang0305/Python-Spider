import urllib.request

# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://movie.douban.com/chart'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)