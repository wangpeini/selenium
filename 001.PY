from selenium import webdriver
driver=webdriver.Chrome() 
driver.maximize_window()
#driver.implicitly_wait(8)
driver.get("https://www.baidu.com") 
#driver.find_element_by_id("kw").send_keys("流星花园")
#driver.find_element_by_class_name("wd").send_keys("流星花园")
#driver.find_element_by_name("wd").send_keys("流星花园")
driver.find_element_by_css_selector('span[class="soutu-btn"]').click()
driver.find_element_by_css_selector('input[type="file"]').send_keys("C://Users//Public//Pictures//Sample Pictures//1.jpg")
#driver.quit