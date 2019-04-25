#!/usr/bin/pyton
import requests  #发起网页请求
import re  #使用正则表达式来匹配到图片网址
import time  #获取当前时间，用来文件命名
import os  #执行shell命令,判断文件是否存在
from bs4 import BeautifulSoup


while True:
    time = time.localtime()  #获取当前时间
    filename = 'bing_%s_%s_%s.jpg' % (time.tm_year, time.tm_mon, time.tm_mday)  #用时间构建好文件名 
    url = 'https://cn.bing.com'  #国内Bing网址
    headers = {'user-agent': 'Mozilla/5.0'}  #伪装成浏览器，降低访问失败的概率

    if os.path.exists(filename):
        time.sleep(360*60)#如果已经爬了当天的壁纸则休眠六个小时
    else:
        r = requests.get(url, headers=headers)  #get到网页
        if r.status_code == 200:   #status_code是状态码，不为200说明爬取没有正常获取到Bing首页
            html = r.text
            soup = BeautifulSoup(html,'lxml')
            imgu = soup.find_all('link',id='bgLink')
            for img in imgu:
                img = img['href']
                #print(img)
    
            imgurl = url + '/' + img
            #print(imgurl)
            img = requests.get(imgurl)
            with open('/home/spt/211/Wallpapers/%s'%filename, 'wb') as fp:
                fp.write(img.content)
        else:  #没正常获取到Bing首页，那其他操作自然不要做了，输出一段信息就好了。当然这段信息也是会被重定向到log文件的，这会在设置定时任务的时候设置
            print('OpenURLError.')
