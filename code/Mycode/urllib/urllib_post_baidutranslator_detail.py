import urllib.request
import json
# 全局取消ssl证书验证 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    # 'Acs-Token': '1677740549023_1677740549107_zytqGG/D1sONq4uKb8nNWTBtHeQa9mWQcd5NXM6vcotKpQrmgjvsNma/qRSjcpYEAnHKj7c92gLg3fVsRiFQqnbEHfOhqmOhT/tgsus3g2YrGUmVnlx1uNn07f6bn7hJm0Kg7eJCN71vYXBSdQY0IL8bkDi7JvyiLyg6jDF+X00eAs799Xi7HpqNG4zTloN/47tuzZDKhn1MFu6vtUBl/fuLu7CVh+8AbwR7TS3aGsvnqg24JdQ7WB89sNrpRpKJOXfGZrJcqRajiNXWjSXXb07H9JW65Ye59EZVrjr55ABV+bjAYX45scNGARQUU5xlGEspKdO36c3GCFVTvz+SFQb3O1SEyU1UlCOFVNDWbbw=',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '116',
    # 反爬设在cookie
    'Cookie': 'BIDUPSID=446566B2EEF4A1CA5F870EB4C0FDEE07; PSTM=1666940855; BAIDUID=9EF376D3ADD4A9F930C9B56AD7E92B9D:FG=1; newlogin=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=WhJVVQwRmo1MGJoam1qckhPNURSUktiNzJtOEZ3N0NidnlyRHNPN2QtVkdtaVprSVFBQUFBJCQAAAAAAQAAAAEAAADV-3I-0q7SrtKuMDAxMTkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEYN~2NGDf9jS; BDUSS_BFESS=WhJVVQwRmo1MGJoam1qckhPNURSUktiNzJtOEZ3N0NidnlyRHNPN2QtVkdtaVprSVFBQUFBJCQAAAAAAQAAAAEAAADV-3I-0q7SrtKuMDAxMTkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEYN~2NGDf9jS; BA_HECTOR=208ga5aga500812g2k0g80c41i00d341n; BAIDUID_BFESS=9EF376D3ADD4A9F930C9B56AD7E92B9D:FG=1; delPer=0; PSINO=7; ZFY=YI8wVMOv1SL0yAUCYGMu70NWrLPCTH4CyqLhMjGqKzE:C; BDRCVFR[feWj1Vr5u3D]=JMnxQfpB2B6fZu1uy7zmv6; BDRCVFR[C0p6oIjvx-c]=rJZwba6_rOCfAF9pywd; H_PS_PSSID=38186_36559_37551_38126_37907_38148_38267_38170_38233_36804_38034_37932_38041_26350_37958_38281_37881; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1677739134; ab_sr=1.0.1_ZmFjMDIyNmM1Yzc1ZjE1YzcxN2U5OWEzMjZjOWNlNDE1YjVjYjVlYjExMDQwNDhiMGQ4YTVjYWYyODYwN2UzMmQ0N2FjMDc4NGQzY2VmMzg3ZjBlZjVjMzc3OWQwODcwMTE0YzY0Njk3NmU0YzA4MmM1OGYyYjE0M2NiN2Y5YTNkNGQ0OTZlYmQzNmJkZThmMGY4ODZmOWVlMzU5YTU3M2Y0OWYzMGNhYzFmNjg3NDYwOTE4M2JhY2FkOTg3NWM4; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1677740549'
}

data = {
    'from':'en',
    'to':'zh',
    'query':'love',
    'simple_means_flag':'3',
    'sign':'198772.518981',
    'token':'6d8e01abcdfbe04f458a5b5ff1fe302d',
    'domain':'common'
}

data = urllib.parse.urlencode(data).encode('utf-8')

request  = urllib.request.Request(url=url,data=data,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)

print(obj)