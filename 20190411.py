from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import json
import random
from fake_useragent import UserAgent 
import requests
from bs4 import BeautifulSoup

url = 'https://www.juzimi.com'

def cookie_list():
    cookielist = []
    for num in range(1,4):
        num = str(num)
        with open('juzicookie'+num+'.json','r',encoding='utf-8') as f:
            listCookies=json.loads(f.read())
        cookie = [item["name"] + "=" + item["value"] for item in listCookies]
        cookiestr = '; '.join(item for item in cookie)
        cookielist.append(cookiestr)

    
    return cookielist
	
def get_header():
    cookiestr = cookie_list()
    ua = UserAgent()
    header = {
        'Connection': 'keep-alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cookie': random.choice(cookiestr),
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':ua.random
    }
    return header


def get_pages(keyword):
    pro = ['211.159.171.58:80','163.204.245.64:9999','115.218.218.15:9000','123.55.39.54:53281']
    headers = get_header()
    RealUrl = url + '/search/node/' + keyword + '%20type:sentence'
    html = requests.get(url=RealUrl,proxies={'http':random.choice(pro)},headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    pages = soup.find_all('li',class_ = 'pager-last')
    pages = int(pages[0].text)
    time.sleep(3)
	
    return pages

def urllist(keyword):
    urllist = set()
    pages = get_pages(keyword)	
    for page in range(pages):
        RealUrl = url + '/search/node/' + keyword + '%20type%3Asentence?page=' + format(page)
        urllist.add(RealUrl)
    return urllist

	
	
if __name__ == '__main__':

    headers = urllist('李白')
    print(headers)
