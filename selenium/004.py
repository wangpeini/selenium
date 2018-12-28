import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BaiDuSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
    def test_baidu_search(self):
        driver =self.driver
        driver.get("https://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("Á÷ÐÇ»¨Ô°¸ö")
        driver.find_element_by_id("kw").send_keys(Keys.ENTER)

    def tearDown(self):
        
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

