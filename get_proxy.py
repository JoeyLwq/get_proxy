#__author: Joey
#date:    2018/5/31
import requests
import re
import threading
import time
import os
file_path = os.path.join(os.path.abspath('.'),'proxy.text')

proxy_checked = []
def verify(proxy):
    try:
        if requests.get(url='http://www.baidu.com', proxies=proxy, timeout=3).status_code == 200:
            if proxy not in proxy_checked:
                proxy_checked.append(proxy.get('http'))
    except:
        pass
def get_proxies():
    for i in range(1,10):
        url = 'http://www.66ip.cn/areaindex_%d/1.html' %i
        page = requests.get(url=url).content.decode('gbk')
        pattern = re.compile('<td>(\d+\.\d+\.\d+\.\d+)</td><td>(\d+)</td>',re.S)
        proxies = re.findall(pattern,page)

        for i in proxies:
            proxy = {'http':'http://' + i[0] + ':' + i[1]}
            threading.Thread(target=verify,args=(proxy,)).start()
    while threading.active_count() > 1:
        time.sleep(0.5)

    with open(file_path,'w') as f:
        for i in proxy_checked:
            f.write(i + '\n')

if __name__ == '__main__':
    get_proxies()