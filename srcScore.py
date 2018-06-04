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
    

start_time=time.time()
score=dict()


print(len(sys.argv))
#判斷是否式shell 啟動
if(len(sys.argv))==3:
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
if sys.argv[2]=='meta':

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

    score_mixed = soup.select('div.chart.mixed > div.text.oswald > div.count.fr')

    score_negative = soup.select('div.chart.negative > div.text.oswald > div.count.fr')

    tagToNum(score_positive)
    tagToNum(score_mixed)
    tagToNum(score_negative)

    meta_pro_count=score_positive[0]+score_mixed[0]+score_negative[0]
    meta_user_count=score_positive[1]+score_mixed[1]+score_negative[1]
    score['meta_pro_score']=meta_pro_score
    score['meta_user_score']=meta_user_score
    score['meta_pro_count']=meta_pro_count
    score['meta_user_score']=meta_user_count
    #metacritic收尋完畢




#print("it cost %f sec"%(end_time - start_time))
#search imdb start


if sys.argv[2]=='imdb':

    url_parems={'ref_':'nv_sr_fn','q':englishname,'s':'all'}

    search_url='https://www.imdb.com/find'
    result=requests.get(search_url,params=url_parems)


    print("search url:",search_url)


    # 使用剖析器为html.parser
    #注意result還要.text
    soup = BeautifulSoup(result.text, 'html.parser')

    imdb_select_titleAndrUrl=soup.select('tr.findResult.odd > td.result_text > a')
    imdb_select_image_tags=soup.select('tr.findResult.odd > td.primary_photo > a > img')
    imdb_select_url=[]
    imdb_select_title=[]
    imdb_select_image=[]

    for items in imdb_select_titleAndrUrl:
        imdb_select_url.append('https://www.imdb.com'+items.get("href"))
        imdb_select_title.append(items.text)
        
    for items in imdb_select_image_tags:
            imdb_select_image.append(items.get("src"))

        
    score['imdb_select_url']=imdb_select_url
    score['imdb_select_image']=imdb_select_image
    score['imdb_select_title']=imdb_select_title


    end_time=time.time()


if sys.argv[2]=='rotten':
    #收尋 rotten tomato
    search_url = "https://www.rottentomatoes.com/m/"+englishname
    req = urllib.request.Request(url=search_url, headers=headers)  
    print("search url:",search_url)
    response = request.urlopen(req)

    html = response.read()
    charset = chardet.detect(html)
    html = html.decode(str(charset["encoding"]))  # 设置抓取到的html的编码方式

    # 使用剖析器为html.parser
    soup = BeautifulSoup(html, 'html.parser')
    rotten_pro_score=soup.select("span.meter-value.superPageFontColor > span")[0].text
    rotten_user_score=soup.select("div.meter-value > span.superPageFontColor")[0].text
    rotten_user_score=re.search(r"\d+",rotten_user_score).group()
    rotten_pro_count=soup.select("div.hidden-xs > div.superPageFontColor > span")[2].text
    #user_count有問題
    rotten_user_count=soup.select("div.audience-info.hidden-xs.superPageFontColor > div")[1].text
    rotten_user_count=re.search(r"\d*,?\d+",rotten_user_count).group()

    rotten_pro_score=int(rotten_pro_score)
    rotten_user_score=int(rotten_user_score)
    rotten_pro_count=int(rotten_pro_count.replace(",",""))
    rotten_user_count=int(rotten_user_count.replace(",",""))

    score['rotten_user_score']=rotten_user_score
    score['rotten_pro_score']=rotten_pro_score
    score['rotten_user_count']=rotten_user_count
    score['rotten_pro_count']=rotten_pro_count




#json_score=json.dumps(score)
#print(json_score)

#rotten收尋完畢



print(score)
end_time=time.time()
#print("it cost %f sec"%(end_time - start_time))


