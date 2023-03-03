# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post请求
# cname: 北京
# pid: 
# pageIndex: x
# pageSize: 10

import urllib.parse
import urllib.request
# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    
    data = {
        'cname': '北京',
        'pid':'',
        'pageIndex': page,
        'pageSize': '10'
    }
    
    data = urllib.parse.urlencode(data).encode('utf-8')
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    
    request = urllib.request.Request(url=base_url,headers=headers,data=data)
    
    return request
    

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('kfc_' + str(page) + '.json','w',encoding='utf-8') as fp:
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