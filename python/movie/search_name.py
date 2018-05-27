from bs4 import BeautifulSoup
from urllib import request
import chardet
import urllib.parse  
def enName():
	url = "https://zh.wikipedia.org/wiki/"
	movieName = input("please input what movie you want to search:\n")
	def check_contain_chinese(check_str):
		for ch in check_str:
			if '\u4e00' <= ch <= '\u9faf':
				return True
		return False
		
	if check_contain_chinese(movieName):
		url += urllib.parse.quote(movieName)
		try:
			response = request.urlopen(url)
		except:
			print("無此維基百科網頁",movieName)
		html = response.read()
		charset = chardet.detect(html)
		html = html.decode(str(charset["encoding"]))  # 设置抓取到的html的编码方式
	
		# 使用剖析器为html.parser
		soup = BeautifulSoup(html, 'html.parser')
		# 获取到每一个class=hot-article-img的a节点
		englishname=soup.select('span.LangWithName > span[lang="en"] > i')[0].text
	
		if(len(englishname)==0):print("維基百科找不到他的英文名字")
		#遍历列表，获取有效信息
	else:
		englishname=movieName		
	return englishname
	
	
	
