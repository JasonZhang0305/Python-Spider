# https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&ie=utf-8&word=%E4%BC%97%E6%B3%B0%E6%B1%BD%E8%BD%A6&x_bfe_rqs=032000000000000000000000000000000000000000000008&x_bfe_tjscore=0.080000&tngroupname=organic_news&newVideo=12&goods_entry_switch=1&rsv_dl=news_b_pn&pn=0

# https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&ie=utf-8&word=%E4%BC%97%E6%B3%B0%E6%B1%BD%E8%BD%A6&x_bfe_
# rqs=032000000000000000000000000000000000000000000008&x_bfe_tjscore=0.080000&tngroupname=organic_news&newVideo=12&
# goods_entry_switch=1&rsv_dl=news_b_pn&pn=10

# https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&ie=utf-8&word=%E4%BC%97%E6%B3%B0%E6%B1%BD%E8%BD%A6&x_bfe_
# rqs=032000000000000000000000000000000000000000000008&x_bfe_tjscore=0.080000&tngroupname=organic_news&newVideo=12&
# goods_entry_switch=1&rsv_dl=news_b_pn&pn=20

# 请求方式：get
# 换页：pn=。。。

import urllib.request

# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url ='https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&ie=utf-8&word=%E4%BC%97%E6%B3%B0%E6%B1%BD%E8%BD%A6&x_bfe_rqs=032000000000000000000000000000000000000000000008&x_bfe_tjscore=0.080000&tngroupname=organic_news&newVideo=12&goods_entry_switch=1&rsv_dl=news_b_pn&pn=20'

response  = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

with open('zt_news.html','w',encoding='utf-8') as fp:
        fp.write(content)
