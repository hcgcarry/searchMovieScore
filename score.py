#-*- coding: UTF-8 -*- 
from bs4 import BeautifulSoup
from urllib import request
import urllib
import re
import requests
import chardet
import urllib.parse  
import json
import sys
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
meta_score = soup.select('div.metascore_w.larger.movie.positive')[0].text
user_score = soup.select('div.metascore_w.user.larger.movie.positive')[0].text

#擷取精準的評論number
score_positive = soup.select('div.chart.positive > div.text.oswald > div.count.fr')
score=dict()
add_score(score,'metacritic','meta_score_positive',score_positive[0].text)
add_score(score,'metacritic','user_score_positive',score_positive[1].text)

score_mixed = soup.select('div.chart.mixed > div.text.oswald > div.count.fr')
add_score(score,'metacritic','meta_score_mixed',score_mixed[0].text)
add_score(score,'metacritic','user_score_mixed',score_mixed[1].text)

score_negative = soup.select('div.chart.negative > div.text.oswald > div.count.fr')

add_score(score,'metacritic','meta_score_negative',score_negative[0].text)
add_score(score,'metacritic','user_score_negative',score_negative[1].text)
print(score)
score_json=json.dumps(score) 
print(score_json)        
#metacritic收尋完畢



#收尋 rotten tomato
search_url = "https://www.rottentomatoes.com/m/"+englishname
req = urllib.request.Request(url=search_url, headers=headers)  
print("search url:",search_url)
try:
    response = request.urlopen(req)
except:
    print("rotten網站找不到該電影")

html = response.read()
charset = chardet.detect(html)
html = html.decode(str(charset["encoding"]))  # 设置抓取到的html的编码方式

# 使用剖析器为html.parser
soup = BeautifulSoup(html, 'html.parser')
rotten_meta_score=soup.select("span.meter-value.superPageFontColor > span")[0].text
rotten_user_score=soup.select("div.meter-value > span.superPageFontColor")[0].text
rotten_user_score=re.search(r"\d+",rotten_user_score).group()
rotten_meta_count=soup.select("div.hidden-xs > div.superPageFontColor > span")[2].text
#user_count有問題
rotten_user_count=soup.select("div.audience-info.hidden-xs.superPageFontColor > div")[1].text
rotten_user_count=re.search(r"\d*,?\d+",rotten_user_count).group()


print("rotten_meta_count::",rotten_meta_count,"\nrotten_meta_score::",rotten_meta_score,"\nrotten_user_count::",\
        rotten_user_count,"\nrotten_user_score::",rotten_user_score)

#rotten收尋完畢


search_url="https://movie.douban.com/subject_search"

my_parmas={'search_text':englishname}
try:
    response=requests.get(search_url,params=my_parmas)
except:
    print("豆瓣網站找不到該電影")

if response.status_code==requests.codes.ok:
    soup=BeautifulSoup(html,'html.parser')
    #print(soup.prettify())
    douban_result_picture=soup.select("div.item-root > a.cover-link > img.cover")
    print(douban_result_picture)
    douban_result_titleAndUrl=soup.select("div.item-root > div.detail > div.title >\
            a.title-text")[0].text
    print(douban_result_titleAndUrl)
    douban_result_text=[]
    douban_result_url=[]
    douban_result_text=[]
    for items in douban_result_titleAndUrl:
        douban_result_text.append(items.text)
        douban_result_url.append(items.get("herf"))

    result_list=zip(douban_result_url,douban_result_text)
    print(result_list)
