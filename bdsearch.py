
driver = webdriver.Chrome(chrome_options=chrome_options)




#driver = webdriver.Chrome()

driver.get("https://movie.douban.com/")
driver.find_element_by_id("inp-query").click()
driver.find_element_by_id("inp-query").clear()
driver.find_element_by_id("inp-query").send_keys(englishname)
driver.find_element_by_xpath(u"//input[@value='搜索']").click()

html = driver.page_source       # get html
driver.get_screenshot_as_file("./img/sreenshot1.png")


driver.close()

soup=BeautifulSoup(html,'html.parser') 
douban_result_picture=soup.select("div.item-root > a.cover-link > img.cover")

print(douban_result_picture)
douban_result_picture_url=[]

for items in douban_result_picture:
        douban_result_picture_url.append(items.get("src"))

        print(douban_result_picture_url)
        douban_result_titleAndUrl=soup.select("div.item-root > div.detail > div.title >
        a.title-text")
        print(douban_result_titleAndUrl)
        douban_result_url=[]
        douban_result_text=[]
        for items in douban_result_titleAndUrl:
                douban_result_text.append(items.text) 
                    douban_result_url.append(items.get("herf"))

                    result_list=zip(douban_result_url,douban_result_text)
                    for items in result_list:
                            print(items)

