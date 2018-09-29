#encoding:utf8


from selenium import webdriver
from time import sleep
import unittest

class SendMsgCase(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.get('https://h5.ele.me/login/#redirect=https%3A%2F%2Fwww.ele.me%2Fhome%2F')
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)

    def by_css(self,css):
        return self.dr.find_element_by_css_selector(css)

    #  手机号码输入框定位
    def mobile_phone_input_box(self):
        return self.by_css('[type = "tel"]')

    #  【免费获取验证码】按钮定位
    def send_msg_button(self):
        return self.by_css('.CountButton-3e-kd')

    #   获取 发送验证码成功 文本信息
    def send_msg_successful_text(self):
        return self.by_css('#registerContainer > div > div.codeSendHint').text

    #   发送验证码
    def send_msg(self,mobile_phone):
        self.mobile_phone_input_box().send_keys(mobile_phone)
        self.send_msg_button().click()

    #   测试用例
    def test_send_msg(self):
        self.send_msg('0000000000')
        sleep(2)
        #   验证【免费获取验证码】按钮 被禁用
        # print(self.send_msg_button().is_enabled())
        self.assertFalse(self.send_msg_button().is_enabled())
        expected_result = '已发送'
        actual_result = self.send_msg_button().text
        # print(actual_result)
        self.assertTrue(expected_result in actual_result)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()

# dr = webdriver.Chrome()
# dr.implicitly_wait(10)
# dr.get('https://h5.ele.me/login/#redirect=https%3A%2F%2Fwww.ele.me%2Fhome%2F')
# dr.find_element_by_css_selector('#reMobileNo').send_keys('00000000000')
# # 点击【免费获取验证码】按钮
# dr.find_element_by_css_selector('#getReAuthCode').click()
# # 验证【免费获取验证码】按钮不可点击
# assert dr.find_element_by_css_selector('#getReAuthCode').is_enabled() == False
# # 获取 “验证码发送成功” 文本信息
# text = dr.find_element_by_css_selector('#registerContainer > div > div.codeSendHint').text
