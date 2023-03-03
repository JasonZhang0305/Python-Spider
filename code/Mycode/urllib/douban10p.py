# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=0&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=20&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=40&limit=20

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=60&limit=20

# page   1   2   3    4 
# start  0   20  40   60
# start = (page-1)*20

# 下载电影前十页的数据
# 1 请求对象的定制
# 2 获取响应的数据
# 3 下载数据
import urllib.parse
import urllib.request
# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start':(page-1)*20,
        'limit':20
    }
    
    data = urllib.parse.urlencode(data)
    
    url = base_url + data
    
    print(url)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    
    request = urllib.request.Request(url=url,headers=headers,data=data)

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('douban_' + str(page) + '.json','w',encoding='utf-8') as fp:
        fp.write(content)


# 程序入口
if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入起始的页码'))
    
    for page in range(start_page, end_page+1):
        # 每一页都有自己的请求对象定制
        request = create_request(page)
        # 获取响应数据
        content = get_content(request)
        # 下载
        down_load(page,content)
        
