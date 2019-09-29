import time
from urllib import request
from bs4 import BeautifulSoup
import chardet

    #这是代理IP
proxy = {'http':'125.123.142.56:9999'}
    #创建ProxyHandler
proxy_support = request.ProxyHandler(proxy)
    #创建Opener
opener = request.build_opener(proxy_support)
    #添加User Angent
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
request.install_opener(opener)

from bs4 import BeautifulSoup
import urllib.request
import gzip
import io
import random

T=0
T_list=[]
F=0
F_list=[]
Tta = True_to_all = []

count = 0
for i in range(10000):
    avid = random.randint(200000,49110000)
    print(avid)
    pre_url = 'https://www.bilibili.com/video/av'+str(avid)
    #url = 'https://www.bilibili.com/video/av212109/'

    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.5',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'}


    req = urllib.request.Request(pre_url, headers=headers)
    while True:
        try:
            response = urllib.request.urlopen(req)
            break
        except Exception:
            time.sleep(0.05)

    if response.info().get('Content-Encoding') == 'gzip':
        pagedata = gzip.decompress(response.read())
    elif response.info().get('Content-Encoding') == 'deflate':
        pagedata = response.read()
    elif response.info().get('Content-Encoding'):
        print('Encoding type unknown')
    else:
        pagedata = response.read()

    soup = BeautifulSoup(pagedata,'lxml')

    title=soup.title

    title = soup.find("meta",  property="og:title")
    #print(title["content"] if title else "No meta title given")
    #print(soup.prettify())
    e = title["content"] if title else "No meta title given"

    if e =='视频去哪了呢？_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili':
        print('F')
        F_list.append(avid)
        F+=1
        Tta.append(0)
    else:
        print('T')
        T_list.append(avid)
        T+=1
        Tta.append(1)
    count+=1
    print(str(count/100)+'%')
    print(str(T/(T+F)*100)+'%')
    #Tta.append(T/(T+F)*100)
print(T)
print(F)
#T_list.append(43872244)

