from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print(driver.title)#获取网页标题
assert "百度" in driver.title  #增加判断assert
driver.find_element_by_id("kw").send_keys("流星花园")

driver.find_element_by_id("su").click()
l = driver.find_element_by_id("content_left").text获取文本
print(l)
assert "流星花园" in l
