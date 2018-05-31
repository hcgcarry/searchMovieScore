#-*- coding: UTF-8 -*- 
from bs4 import BeautifulSoup
from urllib import request
import urllib
import chardet
import urllib.parse  
import json
import sys
def check_contain_chinese(check_str):
    for ch in check_str:
        if '\u4e00' <= ch <= '\u9faf':
            return True
    return False

def search_score(search_url):
	req = urllib.request.Request(url=search_url, headers=headers)  
	
	print("search url:",search_url)
	try:
	        response = request.urlopen(req)
	except:
	        print("metacritic網站找不到該電影")
	        print("englishname")
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
	score={}
	score['meta_score_positive'] = score_positive[0].text
	score['users_score_positive'] = score_positive[1].text
	
	score_mixed = soup.select('div.chart.mixed > div.text.oswald > div.count.fr')
	score['meta_score_mixed'] = score_mixed[0].text
	score['users_score_mixed']= score_mixed[1].text
	
	score_negative = soup.select('div.chart.negative > div.text.oswald > div.count.fr')
	
	score['meta_score_negative']= score_negative[0].text
	score['users_score_negative']= score_negative[1].text
	score_json=json.dumps(score) 
	print(score_json)        
	
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



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; \
rv:23.0) Gecko/20100101 Firefox/23.0'}  
search_url = "http://www.metacritic.com/movie/"+englishname.lower()


search_score(search_url)
