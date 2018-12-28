import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
class BaiDuSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_baidu_search(self):
        driver = self.driver
        driver.get("https://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("皇帝的新装")
        driver.find_element_by_id("kw").send_keys(Keys.ENTER)
    def test_bing_search(self):
        driver =self.driver  
        driver.get("https://www.bing.com")
        driver.find_element_by_id("sb_form_q").send_keys("皇帝的新装")
        driver.find_element_by_id("sb_form_q").send_keys(Keys.ENTER)

    def tearDown(self):
        sleep(4)
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()