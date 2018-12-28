from selenium import webdriver
from time import  sleep
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element_by_link_text("设置").click()
driver.find_element_by_link_text("高级搜索").click()
#driver.find_element_by_id("kw").send_keys("流星花园")
#driver.find_element_by_link_text("新闻").click()  #超链接匹配
#driver.find_element_by_partial_link_text("新").click#模糊匹配超链接
sleep(3)
list = driver.find_elements_by_tag_name("input")#返回的是列表对象
for i in list:

    if  i.get_attribute("size")=="35":
        i.send_keys("wang")