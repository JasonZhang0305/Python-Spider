import urllib.request
# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://www.baidu.com/s?wd=ip%E5%9C%B0%E5%9D%80%E6%9F%A5%E8%AF%A2'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

# response = urllib.request.urlopen(request)

proxies = {
    'http':'61.216.156.222:60808'
}

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('proxy.html','w',encoding='utf-8') as fp:
    fp.write(content)