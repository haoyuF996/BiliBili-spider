#载入selenium和urllib（request）--浏览器、网页操作
from selenium import webdriver
from urllib import request
from selenium.webdriver.common.by import By

import time

#载入xlrd、xlwt、xlutils--excel文件操作
import xlrd
import xlwt
from xlutils.copy import copy
import os

#print('Welcome! input avid please!')
avid = eval(input('Welcome! input avid please!'))
#print('How long is you want to be?(hours)')
t = eval(input('How long is you want to be?(hours)'))*3600
#print('What about the frequency?(>=30s)')
fr = eval(input('What about the frequency?(>=30s)'))

timeStrat = time.time()
tS = round(timeStrat,5)


#创建excel文件
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
#生成表格
sheet = book.add_sheet('test', cell_overwrite_ok=True)
#写入表头
sheet.write(0, 0, '时间') 
sheet.write(0, 1, '时间戳') 
sheet.write(0, 2, '实时观看人数') 
#保存excell文件
book.save(rf'C:\Users\haoyu\Desktop\CS python\Watch\Watch av{avid} {tS}.xls')

watching_list = []
tCostList = []
53437058
#打开浏览器driver（Edge）
driver = webdriver.Edge()

count = 1
while t > 0:
    t_start = time.time()
    #根据av号生成对应url
    url = 'https://www.bilibili.com/video/av'+str(avid)
    #访问该url并初步获取数据
    driver.get(url)
    time.sleep(2)
    #定位实时观看人数
    watching = driver.find_element_by_class_name("bilibili-player-video-info-people-number").text

    print(watching)
    #将观看人数及其时间加入列表
    timeArray = time.localtime(t_start)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    watching_list.append([otherStyleTime,t_start,watching])
    time.sleep(fr-9)
    driver.refresh()
    t_end = time.time()
    t_cost = t_end - t_start
    t -= int(t_cost)
    tCostList.append(t_cost)
    owb = xlrd.open_workbook(rf'C:\Users\haoyu\Desktop\CS python\Watch\Watch av{avid} {tS}.xls')
    nwb = copy(owb)
    sheet = nwb.get_sheet(0)
    sheet.write(count, 0,otherStyleTime)
    sheet.write(count, 1,t_start)
    sheet.write(count, 2,watching)
    os.remove(rf'C:\Users\haoyu\Desktop\CS python\Watch\Watch av{avid} {tS}.xls')
    nwb.save(rf'C:\Users\haoyu\Desktop\CS python\Watch\Watch av{avid} {tS}.xls')
    count +=1

#关闭Edge
driver.close()
#输出实际平均耗时
print('Actual time consumed every watch on average: ',sum(tCostList)/len(tCostList))
#Excel写入
for i,v in enumerate(watching_list):
    print(v)
