import unittest
from selenium import webdriver
from time import sleep
"""
�����˻�:
�û�����testuser01  
���룺123456
"""
class LoginCase(unittest.TestCase):
  
     def setUp(self):
         self.dr = webdriver.Chrome()
         self.dr.maximize_window()
  
     #�����¼����
     def login(self, username, password):
         self.dr.get('http://39.107.96.138:3000/')  #cnblog��¼ҳ��
         self.dr.find_element_by_id('input1').send_keys(username)
         self.dr.find_element_by_id('input2').send_keys(password)
         self.dr.find_element_by_id('signin').click()
  
     def test_login_success(self):
         '''�û�����������ȷ'''
         self.login('kemi_xxx', 'kemi_xxxx') #��ȷ�û���������
         sleep(3)
         link = self.dr.find_element_by_id('lnk_current_user')
         self.assertTrue('�������' in link.text)   #��assertTrue(x)����������  bool(x) is True ��¼�ɹ����û��ǳ���lnk_current_user��
         self.dr.get_screenshot_as_file("D:\cnblogtest\\login_success.jpg")  #��ͼ  ���Զ����ͼ��ı���λ�ú�ͼƬ����
  
     def test_login_pwd_error(self):
         '''�û�����ȷ�����벻��ȷ'''
         self.login('kemi_xxx', 'kemi')  #��ȷ�û�������������
         sleep(2)
         error_message = self.dr.find_element_by_id('tip_btn').text
         self.assertIn('�û������������', error_message)  #��assertIn(a,b)���������� a in b  '�û������������'��error_message��
         self.dr.get_screenshot_as_file("D:\cnblogtest\\login_pwd_error.jpg")
  
     def test_login_pwd_null(self):
         '''�û�����ȷ������Ϊ��'''
         self.login('kemi_xxx', '')  #����Ϊ��
         error_message = self.dr.find_element_by_id('tip_input2').text
         self.assertEqual(error_message,'����������')  #��assertEqual(a,b)����������  a == b  �������������error_message
         self.dr.get_screenshot_as_file("D:\cnblogtest\\login_pwd_null.jpg")
  
     def test_login_user_error(self):
         '''�û�������������ȷ'''
         self.login('kemixing', 'kemi_xxx')  #������ȷ���û�������
         sleep(2)
         error_message = self.dr.find_element_by_id('tip_btn').text
         self.assertIn('���û�������', error_message)  #��assertIn(a,b)���������� a in b
         self.dr.get_screenshot_as_file("D:\cnblogtest\\login_user_error.jpg")
  
     def test_login_user_null(self):
         '''�û���Ϊ�ա�������ȷ'''
         self.login('', 'kemi_xxx')  #�û���Ϊ�գ�������ȷ
         error_message = self.dr.find_element_by_id('tip_input1').text
         self.assertEqual(error_message,'�������¼�û���')  #��assertEqual(a,b)����������  a == b
         self.dr.get_screenshot_as_file("D:\cnblogtest\\login_user_null.jpg")
 
    def tearDown(self):
      sleep(2)
         print('�Զ�������ϣ�')
       self.dr.quit()

if __name__ == '__main__':
    unittest.main()