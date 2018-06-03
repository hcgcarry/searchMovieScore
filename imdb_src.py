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
    
score=dict()

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
    

add_score(score,'imdb','imdb_select_url',imdb_select_url)
add_score(score,'imdb','imdb_select_title',imdb_select_title)
add_score(score,'imdb','imdb_select_image',imdb_select_image)

print(score)

end_time=time.time()
#print("it cost %f sec"%(end_time - start_time))

