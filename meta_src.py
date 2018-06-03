#-*- coding: UTF-8 -*- 
from bs4 import BeautifulSoup
from urllib import request
import urllib
import re
import requests
import chardet
import urllib.parse  
import json
import time
import sys
def tagToNum(arr):
    for index, items in enumerate(arr):
        arr[index]=int(items.text.replace(",",""))

def check_contain_chinese(check_str):
    for ch in check_str:
        if '\u4e00' <= ch <= '\u9faf':
            return True
    return False
def add_score(dic,key_one,key_two,value):
    keys=dic.keys()
    if key_one in keys:
        score[key_one].update({key_two:value})
    else:
        score.update({key_one:{key_two:value}})
    

start_time=time.time()


#判斷是否式shell 啟動
if(len(sys.argv))==2:
    name_input=sys.argv[1] 
else:
    name_input=input("please input what movie you want to search ,better input english:\n")

#判斷輸入的是否式中文名字
check_if_ch=check_contain_chinese(name_input)
if check_if_ch == True:
    import search_name 
    englishname=search_name.enName(name_input)
else:
    englishname=name_input

englishname=englishname.lower()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; \
rv:23.0) Gecko/20100101 Firefox/23.0'}  


#收尋metacritic
search_url = "http://www.metacritic.com/movie/"+englishname



req = urllib.request.Request(url=search_url, headers=headers)  

print("search url:",search_url)
try:
    response = request.urlopen(req)
except:
    print("metacritic網站找不到該電影")

html = response.read()
charset = chardet.detect(html)
html = html.decode(str(charset["encoding"]))  # 设置抓取到的html的编码方式

# 使用剖析器为html.parser
soup = BeautifulSoup(html, 'html.parser')
#總評論分數
meta_pro_score = int(float(soup.select('div.metascore_w.larger.movie.positive')[0].text))
meta_user_score= int(float(soup.select('div.metascore_w.user.larger.movie.positive')[0].text)*10)

#擷取精準的評論number
score_positive = soup.select('div.chart.positive > div.text.oswald > div.count.fr')
score=dict()

score_mixed = soup.select('div.chart.mixed > div.text.oswald > div.count.fr')

score_negative = soup.select('div.chart.negative > div.text.oswald > div.count.fr')

tagToNum(score_positive)
tagToNum(score_mixed)
tagToNum(score_negative)

meta_pro_count=score_positive[0]+score_mixed[0]+score_negative[0]
meta_user_count=score_positive[1]+score_mixed[1]+score_negative[1]
add_score(score,'metacritic','meta_pro_score',meta_pro_score)
add_score(score,'metacritic','meta_user_score',meta_user_score)
add_score(score,'metacritic','meta_pro_count',meta_pro_count)
add_score(score,'metacritic','meta_user_count',meta_user_count)
#metacritic收尋完畢



print(score)

end_time=time.time()
#print("it cost %f sec"%(end_time - start_time))

