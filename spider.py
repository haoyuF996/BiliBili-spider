#载入selenium和urllib（request）--浏览器、网页操作
from selenium import webdriver
from urllib import request
from selenium.webdriver.common.by import By


#driver.implicitly_wait(10)

#载入xlrd、xlwt、xlutils--excel文件操作
import xlrd
import xlwt
from xlutils.copy import copy
import os

#Filename = 'C:\Users\haoyu\Desktop\CS python\Final1.xls'
#创建excel文件
#book = xlwt.Workbook(encoding='utf-8', style_compression=0)
#生成表格
#sheet = book.add_sheet('test', cell_overwrite_ok=True)
#写入表头
#sheet.write(0, 0, 'av号') 
#sheet.write(0, 1, '投硬币枚数') 
#sheet.write(0, 2, '点赞数') 
#sheet.write(0, 3, '收藏人数') 
#sheet.write(0, 4, '总播放数') 
#sheet.write(0, 5, '历史累计弹幕数')
#保存excell文件
#book.save(r'C:\Users\haoyu\Desktop\CS python\Final1.xls')
#打开包含可用av号的T_list.txt文件并转为列表储存
with open('T_list.txt',"r") as f:
    pre_T_list = f.read()
T_list = []
T_list = pre_T_list.split('av')
del T_list[0]
#载入time--延时
import time

#设置函数处理数据
def get_coin(a):
    if coin == '投硬币枚数':
        coin = 0
    else:
        coin = eval(coin[5:])


#遍历所以可以av号
count = 5904
for avid in T_list:
    print(avid)
    #打开浏览器driver（Edge）
    driver=webdriver.Edge()
    #根据av号生成对应url
    url = 'https://www.bilibili.com/video/av'+str(avid)
    #访问该url并初步获取数据
    driver.get(url)
    #定位元素：播放数量
    #time.sleep(0.1)
    view = driver.find_element_by_class_name("view").get_attribute("title")
    waited = 0
    #通过播放数量检查网页是否初步加载完毕
    while True: #view == '总播放数--':
        try:
            coin = driver.find_element_by_class_name("coin").get_attribute("title")
            like = driver.find_element_by_class_name("like").get_attribute("title")
            collect = driver.find_element_by_class_name("collect").get_attribute("title")
            view = driver.find_element_by_class_name("view").get_attribute("title")
            dm = driver.find_element_by_class_name("dm").get_attribute("title")
            
            #初步处理得到数值
            if coin == '投硬币枚数':
                coin = 0
            else:
                coin = eval(coin[5:])
            
            if like == '点赞数':
                like = 0
            else:
                like = eval(like[3:])
                
            if collect == '收藏人数':
                collect = 0
            else:
                collect = eval(collect[4:])
                
            if view == '总播放数':
                view = 0
            else:
                view = eval(view[4:])
                
            if dm == '历史累计弹幕数':
                dm = 0
            else:
                dm = eval(dm[7:])
                
            driver.quit()
            break
            
        except Exception:
            time.sleep(0.05)
            waited+=1
        #view = driver.find_element_by_class_name("view").get_attribute("title")
        #time.sleep(0.05)#未加载完毕则等待
        #waited+=1
        #若等待时间超过3秒，则刷新网页
        if waited >=60:
            #while True:
            #driver.quit()
            #driver.get(url)
            driver.refresh()
            #view = driver.find_element_by_class_name("view").get_attribute("title")
            waited = 0
    #初步获取数据
    '''coin = driver.find_element_by_class_name("coin").get_attribute("title")
    like = driver.find_element_by_class_name("like").get_attribute("title")
    collect = driver.find_element_by_class_name("collect").get_attribute("title")
    view = driver.find_element_by_class_name("view").get_attribute("title")
    dm = driver.find_element_by_class_name("dm").get_attribute("title")
    driver.quit()
    #初步处理得到数值
    if coin == '投硬币枚数':
        coin = 0
    else:
        coin = eval(coin[5:])
    
    if like == '点赞数':
        like = 0
    else:
        like = eval(like[3:])
    
    if collect == '收藏人数':
        collect = 0
    else:
        collect = eval(collect[4:])
    
    if view == '总播放数':
        view = 0
    else:
        view = eval(view[4:])
    
    if dm == '历史累计弹幕数':
        dm = 0
    else:
        dm = eval(dm[7:])'''
    #将数值写入现有excel文件中
    owb = xlrd.open_workbook(r"c:\Users\haoyu\Desktop\CS python\Final1.xls")
    nwb = copy(owb)
    sheet = nwb.get_sheet(0)
    sheet.write(count, 0,avid)
    sheet.write(count, 1,coin)
    sheet.write(count, 2,like)
    sheet.write(count, 3,collect)
    sheet.write(count, 4,view)
    sheet.write(count, 5,dm)
    os.remove(r"c:\Users\haoyu\Desktop\CS python\Final1.xls")
    nwb.save(r"c:\Users\haoyu\Desktop\CS python\Final1.xls")

    count+=1
    #显示完成度
    print(str(count/6443*100)+'%')
    print(str((count-5904)/len(T_list)*100)+'%')
#book.save(r'C:\Users\haoyu\Desktop\CS python\Final1.xls')

#av8221075\27895289\19306956\14670200在爬取过程中失效
#因为是电视剧无法获取数据av4498050
#1重复
