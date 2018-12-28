from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.find_element_by_css_selector('span[class="soutu-btn"]').click()
driver.find_element_by_css_selector('input[type="file"]').send_keys("C://Users//Public//Pictures//Sample Pictures//1.jpg")