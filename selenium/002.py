from selenium import webdriver
from time import  sleep
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element_by_link_text("����").click()
driver.find_element_by_link_text("�߼�����").click()
#driver.find_element_by_id("kw").send_keys("���ǻ�԰")
#driver.find_element_by_link_text("����").click()  #������ƥ��
#driver.find_element_by_partial_link_text("��").click#ģ��ƥ�䳬����
sleep(3)
list = driver.find_elements_by_tag_name("input")#���ص����б����
for i in list:

    if  i.get_attribute("size")=="35":
        i.send_keys("wang")