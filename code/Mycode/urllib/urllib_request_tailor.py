import urllib.request

# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url ='https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&ie=utf-8&word=%E4%BC%97%E6%B3%B0%E6%B1%BD%E8%BD%A6'

# url 组成:
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&rsv_spt=1&oq=%25E7%2599%25BE%25E5%25BA%25A6&rsv_pq=bf3f6a9500047340&rsv_t=28bcdTlLOPqPADMA%2FRHxK%2F5U%2BIeNRNOI75K668KXuebjdOhA5dlg%2FW7CLtiCpyDzubaB&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&rsv_sug3=19&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&inputT=2004&rsv_sug4=2004
#  协议 主机 端口号（80/443）路径（s）  参数   锚点

# 反扒机制 定义headers

response  = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)
