from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print(driver.title)#��ȡ��ҳ����
assert "�ٶ�" in driver.title  #�����ж�assert
driver.find_element_by_id("kw").send_keys("���ǻ�԰")

driver.find_element_by_id("su").click()
l = driver.find_element_by_id("content_left").text��ȡ�ı�
print(l)
assert "���ǻ�԰" in l
