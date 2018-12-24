from selenium import webdriver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("hello")
driver.find_elements_by_css_selector('span[class = "soutu-btn"] ').click()
driver.find_elements_by_css_selector('input[type = "file"]').send_keys("")

driver.maximize_window()
driver.quit()
 