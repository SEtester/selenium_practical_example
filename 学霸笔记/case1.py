# encoding:utf8

'''
selenium 知识点
How to verify if a button is enabled and disabled in Webdriver Python?
使用 python selenium webdriver 怎么去验证一个按钮是启用的（可以操作）？
'''

'''
用例 ：验证发送验证码成功
步骤 ：
        1、打开 饿了么 的注册页面
        2、输入 11位 大陆手机号 
        3、点击 【获取验证码】
        4、等待30秒
        5、点击 【获取验证码】
        
预期结果：
        3、【获取验证码】按钮置灰，不可点击， 友好提示语：已发送
        4、30秒后， 【获取验证码按钮】不再置灰，可点击； 
        5、【获取验证码】按钮置灰，不可点击， 友好提示语：已发送
'''

from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.implicitly_wait(10)

# 导航到 饿了么 注册页面
dr.get('https://h5.ele.me/login/#redirect=https%3A%2F%2Fwww.ele.me%2Fhome%2F')

# 定位并输入手机号
dr.find_element_by_css_selector('[type = "tel"]').send_keys('13148850558')

# 点击【获取验证码】按钮
dr.find_element_by_css_selector('.CountButton-3e-kd').click()

# 打印 定位【获取验证码】按钮 ，is_enabled()返回结果
print('is_enabled()返回结果:', dr.find_element_by_css_selector('.CountButton-3e-kd').is_enabled())

# 验证【获取验证码】按钮不可点击
assert dr.find_element_by_css_selector('.CountButton-3e-kd').is_enabled() == False
sleep(2)

# 获取 “验证码发送成功” 文本信息
actual_result = dr.find_element_by_css_selector('.CountButton-3e-kd').text
print('actual_result:', actual_result)

# 验证 【获取验证码】 文本信息 变更 【已发送】
assert '已发送' in actual_result

# 强制等待30秒
sleep(30)

# 打印 定位【获取验证码】按钮 is_enabled()返回结果
print('is_enabled()返回结果:', dr.find_element_by_css_selector('.CountButton-3e-kd').is_enabled())

# 验证 【获取验证码】按钮，已启动，可点击
assert dr.find_element_by_css_selector('.CountButton-3e-kd').is_enabled() == True
sleep(2)

# 点击【获取验证码】按钮
dr.find_element_by_css_selector('.CountButton-3e-kd').click()

# 获取 “验证码发送成功” 文本信息
actual_result_ = dr.find_element_by_css_selector('.CountButton-3e-kd').text
print('actual_result_:', actual_result)

# 验证 【获取验证码】 文本信息 变更 【已发送】
assert '已发送' in actual_result


# sleep(3)
# text =dr.find_element_by_css_selector('#registerContainer > div > div.codeSendHint').text
# assert text == '验证码发送成功'
