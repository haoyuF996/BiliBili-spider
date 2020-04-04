#用于监视某up的粉丝数 播放量等等
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

def getData():
    while True:
        try:
            fans = driver.find_element_by_xpath("//div[@class='n-statistics']/a[2]").get_attribute("title")
            thumbs = driver.find_element_by_xpath("//div[@class='n-statistics']/div[1]").get_attribute("title")
            views = driver.find_element_by_xpath("//div[@class='n-statistics']/div[2]").get_attribute("title")

            fans = int(''.join(fans.split(',')))
            thumbs = int(''.join(thumbs[12:].split(',')))
            views = int(''.join(views[11:].split(',')))

            if fans!=0 and thumbs!=0 and views!=0:
                break
        except Exception:
            pass

    print(f'fans:{fans}')
    print(f'thumbs:{thumbs}')
    print(f'views:{views}')

    #将观看人数及其时间加入列表
    timeArray = time.localtime(t_start)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

    return [otherStyleTime,fans,thumbs,views]

def WriteExcel(data):
    owb = xlrd.open_workbook(rf'WatchData\Watch space{spid} {otherStyleTimeS}.xls')
    nwb = copy(owb)
    sheet = nwb.get_sheet(0)
    sheet.write(count, 0,data[0])
    sheet.write(count, 1,t_start)
    sheet.write(count, 2,data[1])
    sheet.write(count, 3,data[2])
    sheet.write(count, 4,data[3])
    os.remove(rf'WatchData\Watch space{spid} {otherStyleTimeS}.xls')
    nwb.save(rf'WatchData\Watch space{spid} {otherStyleTimeS}.xls')

def getFans():
    while True:
        try:
            FList = []
            for i in range(1,21):
                fan = driver.find_element_by_xpath(f"//ul[@class='relation-list']/li[{i}]/a[1]").get_attribute("href")+'\n'
                FList.append(fan)
            break
        except Exception:
            pass
    return FList

#print('Welcome! input avid please!')
spid = eval(input('Welcome! input space id please!'))
#print('How long is you want to be?(hours)')
t = eval(input('How long is you want to be?(hours)'))*3600
#print('What about the frequency?(>=30s)')
fr = int(input('What about the frequency?(>=30s)'))
#TheLine
TheLine = int(input('What will be The Line(fans count)? '))
CrossingFlag = False

timeStrat = time.time()
tS = round(timeStrat,5)
timeArrayS = time.localtime(tS)
otherStyleTimeS = str(time.strftime("%Y-%m-%d %H:%M:%S", timeArrayS)).replace(':','_')

#创建excel文件
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
#生成表格
sheet = book.add_sheet('test', cell_overwrite_ok=True)
#写入表头
sheet.write(0, 0, '时间') 
sheet.write(0, 1, '时间戳') 
sheet.write(0, 2, '粉丝数') 
sheet.write(0, 3, '累计获得赞数') 
sheet.write(0, 4, '累计播放量') 
#保存excell文件
book.save(rf'WatchData\Watch space{spid} {otherStyleTimeS}.xls')

watching_list = []
tCostList = []
#53437058
#打开浏览器driver（Edge）
driver = webdriver.Edge()

count = 1
#根据av号生成对应url
url = 'https://space.bilibili.com/'+str(spid)+'/fans/fans'
time.sleep(0.5)
#访问该url
driver.get(url)
while t > 0:
    t_start = time.time()
    Data = getData()
    if Data[1]>= TheLine and not CrossingFlag:
        print('Crossed The Line!')
        FanList = []
        FanList+= getFans()
        driver.find_element_by_xpath(f"//ul[@class='be-pager']/li[@title='2']/a").click()
        FanList+= getFans()
        driver.find_element_by_xpath(f"//ul[@class='be-pager']/li[@title='3']/a").click()
        FanList+= getFans()
        driver.find_element_by_xpath(f"//ul[@class='be-pager']/li[@title='4']/a").click()
        FanList+= getFans()
        driver.find_element_by_xpath(f"//ul[@class='be-pager']/li[@title='5']/a").click()
        FanList+= getFans()
        LogTime = str(Data[0]).replace(':','_')
        LogFile = open(rf'WatchData\LineCrossingLog {LogTime}.txt','w')
        writeList = []
        writeList+=FanList
        for i in Data:
            writeList.append(str(i)+'\n')
        LogFile.writelines(writeList)
        LogFile.close()
        CrossingFlag = True
        driver.get(url)
    watching_list.append([t_start]+Data)
    t_end = time.time()
    t_cost = t_end - t_start
    t -= int(t_cost)
    tCostList.append(t_cost)
    WriteExcel(Data)
    count +=1

    delay = fr-3
    if delay>0:
        time.sleep(delay)
    driver.refresh()

#关闭Edge
driver.close()
#输出实际平均耗时
print('Actual time consumed every watch on average: ',sum(tCostList)/len(tCostList))
#Excel写入
for i,v in enumerate(watching_list):
    print(v)
