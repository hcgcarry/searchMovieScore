from bs4 import BeautifulSoup
from urllib import request
import urllib
import chardet
import urllib.parse  
import search_name #這個script會先去抓英文名字


while (1):
	englishname=search_name.enName().replace(" ","-")
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
	search_url = "http://www.metacritic.com/movie/"+englishname.lower()
	req = urllib.request.Request(url=search_url, headers=headers)  
	
	print("search url:",search_url)
	try:
		response = request.urlopen(req)
	except:
		print("metascript網站找不到該電影")
		print("englishname")
		continue
	html = response.read()
	charset = chardet.detect(html)
	html = html.decode(str(charset["encoding"]))  # 设置抓取到的html的编码方式
	
	# 使用剖析器为html.parser
	soup = BeautifulSoup(html, 'html.parser')
	meta_score = soup.select('div.metascore_w.larger.movie.positive')[0].text
	
	user_score = soup.select('div.metascore_w.user.larger.movie.positive')[0].text
	
	
	print("meta_score:",meta_score,"user_score",user_score)
	
