from urllib import request
from bs4 import BeautifulSoup
import chardet

#if __name__ == "__main__":
    #访问网址
url = 'http://ip.myhostadmin.net/'#'https://www.bilibili.com/video/av212109/'
    #这是代理IP
proxy = {'http':'125.123.139.44:9999'}
    #创建ProxyHandler
proxy_support = request.ProxyHandler(proxy)
    #创建Opener
opener = request.build_opener(proxy_support)
    #添加User Angent
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
request.install_opener(opener)
    #使用自己安装好的Opener
response = request.urlopen(url)
    #读取相应信息（-并解码
print(response)
'''html = response.read()#.decode("utf-8")
print(type(html))
print(html)
    #识别编码方式
charset = chardet.detect(html)
print(charset)
    #解码
html = html.decode('vary')
    #打印信息
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
print(soup.title)
print(soup.head)
print(soup.a)'''
