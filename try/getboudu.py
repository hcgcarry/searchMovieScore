from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://movie.douban.com/")
driver.find_element_by_id("inp-query").click()
driver.find_element_by_id("inp-query").clear()
driver.find_element_by_id("inp-query").send_keys("inception")
driver.find_element_by_xpath(u"//input[@value='搜索']").click()

html = driver.page_source       # get html
print(html)
driver.get_screenshot_as_file("./img/sreenshot1.png")
driver.close()

