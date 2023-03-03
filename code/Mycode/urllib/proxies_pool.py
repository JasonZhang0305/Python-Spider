# 代理池, 装一堆高密的ip地址，防止被反爬

proxies_pool = [
    {'http1':''},
    {'http2':''},
    {'httpN':''}
]

import random

proxies = random.choice(proxies_pool)

print(proxies)