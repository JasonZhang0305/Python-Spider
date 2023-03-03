import urllib.request
import ssl
# 全局取消ssl证书验证 
ssl._create_default_https_context = ssl._create_unverified_context

# 下载网页
url_page = 'http://www.baidu.com'

# 参数包括url, filename
# urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载图片
url_img = 'https://img1.runjiapp.com/duoteimg/dtnew_newsup_img/202108/20210826111916_64092.jpeg'
urllib.request.urlretrieve(url_img, 'lisa.jpeg')

# 下载视频
url_video = 'https://vd2.bdstatic.com/mda-kfdj4pbp7azag1uj/hd/mda-kfdj4pbp7azag1uj.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1677732207-0-0-ac9ead5fcdfd3e7f5a7bb27f76f5eb6b&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=0807296020&vid=5676199735227290826&abtest=107346_2-107354_2&klogid=0807296020'
urllib.request.urlretrieve(url_video, 'sszzr.mp4')