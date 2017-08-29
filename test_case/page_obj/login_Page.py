from selenium.webdriver.common.action_chains import ActionChains
from test_case.models.Xpath import *
from test_case.models import functions
from test_case.models import myunit
import time

class loginCase(myunit.myTest):

    # def setUp(self):
    #     self.dr = Driver().driver

    # 登录方法
    def login(self, username, password):
        self.driver.find_element_by_xpath(username_inputbox).clear()
        self.driver.find_element_by_xpath(username_inputbox).send_keys(username)
        self.driver.find_element_by_xpath(password_inputbox).clear()
        self.driver.find_element_by_xpath(password_inputbox).send_keys(password)
        self.driver.find_element_by_xpath(authCode_loc).send_keys('T@$!0')
        self.driver.find_element_by_xpath(submit_button).click()

    # 登录失败验证消息
    def login_fail_hint(self):
        return self.driver.find_element_by_xpath(login_fail).text

    # 登录成功验证消息
    def login_success_hint(self):
        return self.driver.find_element_by_xpath(login_success).text

    # 退出验证消息
    def logout_hint(self):
        url = self.driver.current_url
        return url

    # 进入催收系统验证消息
    def collection_verify(self):
        return self.driver.find_element_by_xpath(collection_verify1).text

    # 首页frame
    def welcome_frame(self):
        return self.driver.find_element_by_xpath(welcome_frame)

    # 定义统一登录入口
    def collection_enterance(self):
        self.login('18202815282', '123456')
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(collection_icon).click()

    # 登录成功
    def test_login_success(self):
        self.login('18202815282', '123456')
        self.driver.implicitly_wait(5)
        self.assertEqual(self.login_success_hint(), 'Jason')
        functions.insert_img(self.driver, 'login_success.jpg')

    # 账号、密码为空
    def test_username_pwd_null(self):
        self.login('', '')
        self.driver.implicitly_wait(5)
        self.assertEqual(self.login_fail_hint(), '\ue623用户名不能为空')
        functions.insert_img(self.driver, 'username_pwd_null.jpg')

    # 账号为空
    def test_username_null(self):
        self.login('', '123')
        self.driver.implicitly_wait(5)
        self.assertEqual(self.login_fail_hint(), '\ue623用户名不能为空')
        functions.insert_img(self.driver, 'username_null.jpg')

    # 密码为空
    def test_pwd_null(self):
        self.login('admin', '')
        self.driver.implicitly_wait(5)
        self.assertEqual(self.login_fail_hint(), '\ue623密码不能为空')
        functions.insert_img(self.driver, 'pwd_null.jpg')

    # 账号不存在
    def test_username_inexistent(self):
        self.login('123', '123')
        self.driver.implicitly_wait(5)
        self.assertEqual(self.login_fail_hint(), '\ue623账号或密码错误')
        functions.insert_img(self.driver, 'username_inexistent.jpg')

    # 密码错误
    def test_pwd_error(self):
        self.login('admin', '1234')
        self.driver.implicitly_wait(5)
        self.assertEqual(self.login_fail_hint(), '\ue623账号或密码错误')
        functions.insert_img(self.driver, 'pwd_error.jpg')

    # 进入催收系统
    def test_collection_verify(self):
        self.login('18202815282', '123456')
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(collection_icon).click()
        time.sleep(2)
        login_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != login_windows:
                self.driver.switch_to_window(handle)
                self.driver.implicitly_wait(20)
                self.driver.switch_to_frame(self.welcome_frame())
                self.assertEqual(self.collection_verify(), '欢迎使用风控邦催收管理系统！！！')

    # 退出登录
    def test_logout(self):
        self.login('18202815282', '123456')
        time.sleep(2)
        move_mouse = self.driver.find_element_by_xpath(logout_icon)
        ActionChains(self.driver).move_to_element(move_mouse).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath(logout_button).click()
        self.assertEqual(self.logout_hint(), 'https://login.fengkongbang.cn/justitia/toLogin.htm')
        functions.insert_img(self.driver, 'logout_success.jpg')
