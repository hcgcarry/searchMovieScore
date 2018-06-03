from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://morvanzhou.github.io/tutorials/data-manipulation/scraping/5-01-selenium/")
driver.find_element_by_link_text(u"莫烦Python").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"Python基础 ▾").click()
driver.find_element_by_link_text(u"多线程 threading").click()
driver.find_element_by_link_text(u"1.1 什么是多线程 Threading").click()

html = driver.page_source       # get html
print(html)
driver.get_screenshot_as_file("./img/sreenshot1.png")
driver.close()


