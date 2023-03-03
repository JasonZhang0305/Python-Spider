# 适用场景： 数据采集需要绕过登陆，然后进入到某个页面
# 会报UnicodeDecodeError 因为反爬手段会自动转跳到登陆页面
# 爬虫与反爬的博弈

import urllib.request
# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://st.uc.career-tasu.jp/topHeader/logo/?XWID=907b1ea807418a47bad1273d2d62cc39'

headers = {
    # cookie携带着登陆信息
    'cookie': 'WMONID=MW8nsJgfkJf; _gcl_au=1.1.65513442.1674791156; _ycl_1001164457_aw=GCL.1674791157.EAIaIQobChMI_u_Anuvm_AIVZ9OWCh0IPwtVEAAYASAAEgJMIPD_BwE; _ts_yjad=1674791156520; _fbp=fb.1.1674791156600.99458637; satori_id=327ebc45-d2f2-463e-b1a9-94f36e4e34e4; st_segs=2hw9,dqm,2zym,29ju,25u0,1mtt,1mtr,3w6,26hg,2jqe,2jqf,3uw,3ux,2ikc,26hd,3uz,2chy,2zrp,2dr8,2h03,1pby,286e,ovk,2h08,1pbt,2bb1,28ax,2zgq,1zj5,3v0,3v2,267z,285s,6tr,287s,46x,ih5,6xz,8rt,2taf; _ga_Q6ZYFV131Z=GS1.1.1674791156.1.0.1674791271.60.0.0; __uc_hash__=50b742a99f7a819738dcd271e79be850; XSID=52dhi3mkcca97a7ijpvig9mffgqeu3av; __uc_keep__=04653682264015b8102d612.09232274; _gid=GA1.2.1989049818.1677810562; _gat_uc=1; _ga_3KJ5NDKX76=GS1.1.1677810561.3.1.1677810663.43.0.0; _ga=GA1.1.1463511316.1674791156',
    # referer为当前路径的上一个路径
    'referer': 'https://st.uc.career-tasu.jp/menu/navi/?XWID=907b1ea807418a47bad1273d2d62cc39&XSMID=top'
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('shushoku.html','w',encoding='utf-8') as fp:
    fp.write(content)