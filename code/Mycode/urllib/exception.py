import urllib.request
import urllib.error
# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# url = 'https://blog.csdn.net/csdngeeknews/article/details/129313834' http error 通常为找不到页面

url = 'http://www.goudan666.com' # url error 通常是url写错

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

try:
    request = urllib.request.Request(url=url,headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级')
except urllib.error.URLError:
    print('都说了系统正在升级')